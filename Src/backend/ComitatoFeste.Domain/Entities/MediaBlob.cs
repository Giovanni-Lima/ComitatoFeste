namespace ComitatoFeste.Domain;

/// <summary>
/// Contenuto binario di un <see cref="MediaAsset"/> (relazione 1:1), tenuto in tabella separata
/// così le query sui metadati/timeline non trascinano i byte del file.
/// </summary>
public class MediaBlob
{
    public int Id { get; set; }

    public int MediaAssetId { get; set; }
    public MediaAsset MediaAsset { get; set; } = null!;

    /// <summary>Contenuto del file scaricato dalla pipeline.</summary>
    public byte[] Content { get; set; } = Array.Empty<byte>();

    /// <summary>MIME type per servire il file, es. "audio/ogg", "image/jpeg", "application/pdf".</summary>
    public string ContentType { get; set; } = null!;

    /// <summary>SHA-256 esadecimale del contenuto, per riconoscere file identici tra rerun.</summary>
    public string? Sha256 { get; set; }
}
