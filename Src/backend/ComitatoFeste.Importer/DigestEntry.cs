using System.Text.Json.Serialization;

namespace ComitatoFeste.Importer;

/// <summary>
/// Una entry del file <c>digest_&lt;data&gt;.json</c> prodotto dalla pipeline di ingestion.
/// Forma: <c>{date, time, author, type, text, file}</c>.
/// </summary>
public sealed class DigestEntry
{
    [JsonPropertyName("date")]
    public string Date { get; set; } = "";

    [JsonPropertyName("time")]
    public string Time { get; set; } = "";

    [JsonPropertyName("author")]
    public string Author { get; set; } = "";

    [JsonPropertyName("type")]
    public string Type { get; set; } = "";

    [JsonPropertyName("text")]
    public string Text { get; set; } = "";

    [JsonPropertyName("file")]
    public string? File { get; set; }

    /// <summary>
    /// Trascrizione Whisper già prodotta in fase di export (vedi
    /// <c>scripts/whatsapp-digest/transcribe_new.py</c>), presente solo per i
    /// vocali. <c>null</c> per le entry generate come oggi (nessuna
    /// pre-trascrizione). Quando è valorizzato e <see cref="Type"/> non è
    /// "media" (cioè il vocale è già stato classificato in curatela, non
    /// lasciato come placeholder), <see cref="DigestImporter"/> lo scrive su
    /// <c>MediaAsset.TranscriptionText</c>/<c>TranscribedAt</c> così il
    /// Transcriber lo salta in automatico.
    /// </summary>
    [JsonPropertyName("transcript")]
    public string? Transcript { get; set; }
}
