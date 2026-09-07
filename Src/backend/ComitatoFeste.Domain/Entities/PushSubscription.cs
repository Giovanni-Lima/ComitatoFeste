namespace ComitatoFeste.Domain;

/// <summary>
/// Una subscription Web Push registrata dal browser di un membro (una per dispositivo/browser).
/// L'<see cref="Endpoint"/> — URL del push service — la identifica ed è UNIQUE: una nuova
/// subscribe dallo stesso browser fa upsert su quella riga. Viene cancellata su unsubscribe
/// esplicito o quando il push service risponde 404/410 a un invio (subscription non più valida).
/// </summary>
public class PushSubscription
{
    public int Id { get; set; }

    /// <summary>URL del push service (Google/Apple/Mozilla) a cui inviare la notifica. UNIQUE.</summary>
    public string Endpoint { get; set; } = null!;

    /// <summary>Chiave pubblica ECDH P-256 del client (base64url): serve a cifrare il payload.</summary>
    public string P256dh { get; set; } = null!;

    /// <summary>Secret di autenticazione del client (base64url).</summary>
    public string Auth { get; set; } = null!;

    /// <summary>
    /// Membro che ha attivato le notifiche su questo dispositivo. Null se il login era
    /// disattivato al momento della subscribe, o se il membro è stato poi rimosso
    /// (<c>ON DELETE SET NULL</c>).
    /// </summary>
    public int? MemberId { get; set; }
    public Member? Member { get; set; }

    /// <summary>User agent del browser alla subscribe, solo per debug.</summary>
    public string? UserAgent { get; set; }

    public DateTimeOffset CreatedAt { get; set; }

    /// <summary>Ultimo invio andato a buon fine verso questa subscription.</summary>
    public DateTimeOffset? LastNotifiedAt { get; set; }
}
