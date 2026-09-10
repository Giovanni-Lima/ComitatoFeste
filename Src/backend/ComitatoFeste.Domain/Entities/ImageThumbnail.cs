namespace ComitatoFeste.Domain;

/// <summary>
/// Versione WebP ridimensionata di un'immagine servita dagli endpoint blob — la foto di un
/// <see cref="MediaAsset"/> (<c>Kind = "media"</c>, <c>SourceId</c> = <see cref="MediaAsset.Id"/>)
/// o la foto profilo di un <see cref="Member"/> (<c>Kind = "memberphoto"</c>, <c>SourceId</c> =
/// <see cref="Member.Id"/>). Generata una volta e persistita, così sopravvive ai restart del
/// container (piano free di Render): senza, ogni cold start costringeva a rigenerare tutti i
/// thumbnail su richiesta. Una riga per <c>(Kind, SourceId, Width)</c>.
///
/// Niente FK: le sorgenti non vengono mai cancellate singolarmente (i <see cref="MediaAsset"/>
/// solo a cascata di un <see cref="IngestionRun"/>, i <see cref="Member"/> mai), quindi
/// un'eventuale riga orfana è solo peso morto, non un problema di integrità.
/// </summary>
public class ImageThumbnail
{
    public int Id { get; set; }

    /// <summary>"media" oppure "memberphoto".</summary>
    public string Kind { get; set; } = null!;

    public int SourceId { get; set; }

    /// <summary>Larghezza del thumbnail in px.</summary>
    public int Width { get; set; }

    /// <summary>
    /// SHA-256 esadecimale della sorgente al momento della generazione. Se la sorgente cambia
    /// (foto profilo ricaricata dall'Importer) questa riga non fa più match e se ne genera una
    /// nuova; la vecchia resta come peso morto finché non la si ripulisce.
    /// </summary>
    public string SourceSha256 { get; set; } = null!;

    /// <summary>Byte del WebP ridimensionato.</summary>
    public byte[] Content { get; set; } = Array.Empty<byte>();

    public string ContentType { get; set; } = "image/webp";

    public DateTimeOffset CreatedAt { get; set; }
}
