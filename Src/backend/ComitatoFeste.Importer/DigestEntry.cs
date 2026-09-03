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
}
