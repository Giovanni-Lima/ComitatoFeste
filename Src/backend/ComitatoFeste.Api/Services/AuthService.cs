using System.Globalization;
using System.Security.Cryptography;
using System.Text;
using ComitatoFeste.Domain;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Login "casereccio": username = <c>iniziale.cognome</c> di un membro (derivato dal
/// <see cref="Domain.Member.DisplayName"/>). Due passphrase condivise: quella lettore (storica)
/// funziona per chiunque; quella admin eleva a token Amministratore, ma solo per un membro che ha
/// già <see cref="MemberRole.Amministratore"/> a DB (vedi <see cref="AuthController.Login"/>). Al
/// successo emette un token firmato HMAC (<c>username|ruolo|scadenza</c>) che il frontend rimanda
/// nell'header <c>Authorization: Bearer</c>. Non è sicurezza vera: tiene fuori chi capita per sbaglio.
/// </summary>
public sealed class AuthService
{
    private static readonly TimeSpan TokenLifetime = TimeSpan.FromDays(30);

    private readonly string? _readerPassword;
    private readonly string? _adminPassword;
    private readonly byte[] _secret;

    public AuthService(IConfiguration config)
    {
        _readerPassword = Normalize(Environment.GetEnvironmentVariable("COMITATOFESTE_AUTH_PASSWORD")
                                     ?? config["Auth:Password"]);
        _adminPassword = Normalize(Environment.GetEnvironmentVariable("COMITATOFESTE_AUTH_PASSWORD_ADMIN")
                                    ?? config["Auth:PasswordAdmin"]);

        // Segreto per firmare i token: da config se c'è, altrimenti effimero (i token
        // scadono a ogni riavvio dell'API — accettabile per l'uso previsto).
        var configured = Environment.GetEnvironmentVariable("COMITATOFESTE_AUTH_SECRET")
                         ?? config["Auth:Secret"];
        _secret = string.IsNullOrWhiteSpace(configured)
            ? RandomNumberGenerator.GetBytes(32)
            : Encoding.UTF8.GetBytes(configured);
    }

    private static string? Normalize(string? s) => string.IsNullOrWhiteSpace(s) ? null : s;

    /// <summary>Se <c>false</c> il login è disattivato: l'API è aperta e il frontend salta la schermata.</summary>
    public bool Enabled => _readerPassword is not null;

    /// <summary>Password lettore corretta (o login disattivato).</summary>
    public bool ReaderPasswordOk(string? password) =>
        !Enabled || string.Equals(password, _readerPassword, StringComparison.Ordinal);

    /// <summary>Password admin corretta. <c>false</c> se non configurata (nessuno può elevare via password).</summary>
    public bool AdminPasswordOk(string? password) =>
        _adminPassword is not null && string.Equals(password, _adminPassword, StringComparison.Ordinal);

    /// <summary><c>"Giovanni Lima"</c> → <c>"g.lima"</c>; spazi, apostrofi e accenti rimossi.</summary>
    public static string NormalizeUsername(string displayName)
    {
        var parts = displayName.Trim().Split(' ', StringSplitOptions.RemoveEmptyEntries);
        if (parts.Length == 0)
            return string.Empty;

        var initial = Strip(parts[0])[..1];
        var surname = Strip(string.Concat(parts[1..]));
        return $"{initial}.{surname}".ToLowerInvariant();
    }

    private static string Strip(string s)
    {
        var sb = new StringBuilder(s.Length);
        foreach (var c in s.Normalize(NormalizationForm.FormD))
        {
            if (CharUnicodeInfo.GetUnicodeCategory(c) == UnicodeCategory.NonSpacingMark)
                continue;
            if (char.IsLetterOrDigit(c))
                sb.Append(c);
        }
        return sb.ToString();
    }

    /// <summary>Username + ruolo estratti da un token valido (vedi <see cref="ValidatePrincipal"/>).</summary>
    public sealed record Principal(string Username, MemberRole Role);

    public string IssueToken(string username, MemberRole role)
    {
        var exp = DateTimeOffset.UtcNow.Add(TokenLifetime).ToUnixTimeSeconds();
        var payload = $"{username}|{role.ToString().ToLowerInvariant()}|{exp}";
        return $"{B64(Encoding.UTF8.GetBytes(payload))}.{B64(Sign(payload))}";
    }

    /// <summary>Restituisce lo username se il token è valido e non scaduto, altrimenti <c>null</c>.</summary>
    public string? ValidateToken(string? token) => ValidatePrincipal(token)?.Username;

    /// <summary>Restituisce username + ruolo se il token è valido e non scaduto, altrimenti <c>null</c>.</summary>
    public Principal? ValidatePrincipal(string? token)
    {
        if (string.IsNullOrWhiteSpace(token))
            return null;

        var dot = token.IndexOf('.');
        if (dot <= 0 || dot == token.Length - 1)
            return null;

        try
        {
            var payload = Encoding.UTF8.GetString(UnB64(token[..dot]));
            var sig = UnB64(token[(dot + 1)..]);
            if (!CryptographicOperations.FixedTimeEquals(sig, Sign(payload)))
                return null;

            var parts = payload.Split('|');
            if (parts.Length != 3)
                return null;

            var exp = long.Parse(parts[2], CultureInfo.InvariantCulture);
            if (DateTimeOffset.FromUnixTimeSeconds(exp) < DateTimeOffset.UtcNow)
                return null;

            if (!Enum.TryParse<MemberRole>(parts[1], true, out var role))
                return null;

            return new Principal(parts[0], role);
        }
        catch (Exception ex) when (ex is FormatException or ArgumentException)
        {
            return null;
        }
    }

    private byte[] Sign(string payload)
    {
        using var hmac = new HMACSHA256(_secret);
        return hmac.ComputeHash(Encoding.UTF8.GetBytes(payload));
    }

    private static string B64(byte[] b) => Convert.ToBase64String(b).TrimEnd('=').Replace('+', '-').Replace('/', '_');

    private static byte[] UnB64(string s)
    {
        var t = s.Replace('-', '+').Replace('_', '/');
        return Convert.FromBase64String(t.PadRight((t.Length + 3) / 4 * 4, '='));
    }
}
