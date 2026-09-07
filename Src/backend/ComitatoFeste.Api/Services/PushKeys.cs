namespace ComitatoFeste.Api.Services;

/// <summary>
/// Chiavi VAPID per il Web Push. Da env <c>COMITATOFESTE_VAPID_PUBLIC</c> / <c>_PRIVATE</c> /
/// <c>_SUBJECT</c>, con fallback su config (<c>Vapid:Public</c> / <c>Vapid:Private</c> /
/// <c>Vapid:Subject</c>). La pubblica è servita al frontend da <c>GET /api/push/key</c>
/// (il file statico non può contenerla: cambiarla richiederebbe un redeploy); la privata
/// resta solo lato server. Senza <see cref="IsConfigured"/> le notifiche push sono disattivate.
/// </summary>
public sealed class PushKeys
{
    public PushKeys(IConfiguration config)
    {
        PublicKey = Read("COMITATOFESTE_VAPID_PUBLIC") ?? Trimmed(config["Vapid:Public"]);
        PrivateKey = Read("COMITATOFESTE_VAPID_PRIVATE") ?? Trimmed(config["Vapid:Private"]);
        Subject = Read("COMITATOFESTE_VAPID_SUBJECT")
                  ?? Trimmed(config["Vapid:Subject"])
                  ?? "mailto:giovannilima800@gmail.com";
    }

    public string? PublicKey { get; }
    public string? PrivateKey { get; }

    /// <summary>Identità del mittente richiesta dallo spec VAPID (<c>mailto:</c> o URL).</summary>
    public string Subject { get; }

    /// <summary>Entrambe le chiavi presenti: si può inviare (e servire la pubblica).</summary>
    public bool IsConfigured => !string.IsNullOrWhiteSpace(PublicKey) && !string.IsNullOrWhiteSpace(PrivateKey);

    private static string? Read(string envName) => Trimmed(Environment.GetEnvironmentVariable(envName));

    private static string? Trimmed(string? value) => string.IsNullOrWhiteSpace(value) ? null : value.Trim();
}
