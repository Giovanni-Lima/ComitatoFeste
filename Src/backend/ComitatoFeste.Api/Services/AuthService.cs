using System.Globalization;
using System.Security.Cryptography;
using System.Text;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Login "casereccio": username = <c>iniziale.cognome</c> di un membro (derivato dal
/// <see cref="Domain.Member.DisplayName"/>), password unica condivisa. Al successo emette un
/// token firmato HMAC (<c>username|scadenza</c>) che il frontend rimanda nell'header
/// <c>Authorization: Bearer</c>. Non è sicurezza vera: tiene fuori chi capita per sbaglio.
/// </summary>
public sealed class AuthService
{
    private static readonly TimeSpan TokenLifetime = TimeSpan.FromDays(30);

    private readonly string? _sharedPassword;
    private readonly byte[] _secret;

    public AuthService(IConfiguration config)
    {
        _sharedPassword = Environment.GetEnvironmentVariable("COMITATOFESTE_AUTH_PASSWORD")
                          ?? config["Auth:Password"];
        if (string.IsNullOrWhiteSpace(_sharedPassword))
            _sharedPassword = null;

        // Segreto per firmare i token: da config se c'è, altrimenti effimero (i token
        // scadono a ogni riavvio dell'API — accettabile per l'uso previsto).
        var configured = Environment.GetEnvironmentVariable("COMITATOFESTE_AUTH_SECRET")
                         ?? config["Auth:Secret"];
        _secret = string.IsNullOrWhiteSpace(configured)
            ? RandomNumberGenerator.GetBytes(32)
            : Encoding.UTF8.GetBytes(configured);
    }

    /// <summary>Se <c>false</c> il login è disattivato: l'API è aperta e il frontend salta la schermata.</summary>
    public bool Enabled => _sharedPassword is not null;

    /// <summary>Password corretta (o login disattivato).</summary>
    public bool PasswordOk(string? password) =>
        !Enabled || string.Equals(password, _sharedPassword, StringComparison.Ordinal);

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

    public string IssueToken(string username)
    {
        var exp = DateTimeOffset.UtcNow.Add(TokenLifetime).ToUnixTimeSeconds();
        var payload = $"{username}|{exp}";
        return $"{B64(Encoding.UTF8.GetBytes(payload))}.{B64(Sign(payload))}";
    }

    /// <summary>Restituisce lo username se il token è valido e non scaduto, altrimenti <c>null</c>.</summary>
    public string? ValidateToken(string? token)
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

            var bar = payload.LastIndexOf('|');
            if (bar <= 0)
                return null;

            var exp = long.Parse(payload[(bar + 1)..], CultureInfo.InvariantCulture);
            if (DateTimeOffset.FromUnixTimeSeconds(exp) < DateTimeOffset.UtcNow)
                return null;

            return payload[..bar];
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
