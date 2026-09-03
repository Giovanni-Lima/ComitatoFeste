namespace ComitatoFeste.Domain;

/// <summary>
/// Foto profilo di un <see cref="Member"/> (relazione 1:1). I byte stanno in tabella separata,
/// come per <see cref="MediaBlob"/>, per non appesantire le query sui membri.
/// </summary>
public class MemberProfilePhoto
{
    public int Id { get; set; }

    public int MemberId { get; set; }
    public Member Member { get; set; } = null!;

    /// <summary>Contenuto dell'immagine (da <c>Export/profili/&lt;Nome&gt;.jpg</c>).</summary>
    public byte[] Content { get; set; } = Array.Empty<byte>();

    /// <summary>MIME type, es. "image/jpeg".</summary>
    public string ContentType { get; set; } = null!;

    /// <summary>SHA-256 esadecimale del contenuto, per aggiornare la foto solo quando cambia.</summary>
    public string? Sha256 { get; set; }
}
