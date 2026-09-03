namespace ComitatoFeste.Domain;

/// <summary>
/// Il file scaricato dietro un <see cref="DigestPoint"/> di tipo media (relazione 1:1),
/// con i metadati di trascrizione per l'audio.
/// </summary>
public class MediaAsset
{
    public int Id { get; set; }

    public int DigestPointId { get; set; }
    public DigestPoint DigestPoint { get; set; } = null!;

    public MediaType MediaType { get; set; }

    /// <summary>Nome file rinominato dalla pipeline: <c>HHMM_Autore_breve-descrizione.ext</c>.</summary>
    public string FileName { get; set; } = null!;

    /// <summary>Percorso relativo di archiviazione, es. "2026-09-01/2211_Elvis_vocale-reazione.ogg".</summary>
    public string? StoragePath { get; set; }

    public long? SizeBytes { get; set; }

    /// <summary>
    /// Testo della trascrizione (catturata da WhatsApp o prodotta da Groq Whisper).
    /// <c>null</c> = vocale non ancora trascritto.
    /// </summary>
    public string? TranscriptionText { get; set; }

    public DateTimeOffset? TranscribedAt { get; set; }

    /// <summary>Contenuto binario del file (relazione 1:1). Null finché i byte non vengono caricati.</summary>
    public MediaBlob? Blob { get; set; }
}
