namespace ComitatoFeste.Domain;

/// <summary>
/// Una esecuzione della pipeline di ingestion su una finestra temporale della chat.
/// I <see cref="DigestPoint"/> referenziano il run che li ha prodotti: cancellare un run
/// cancella a cascata i suoi punti, così un rerun su una finestra sovrapposta è annullabile come unità.
/// </summary>
public class IngestionRun
{
    public int Id { get; set; }

    public int GroupId { get; set; }
    public Group Group { get; set; } = null!;

    /// <summary>Inizio della finestra temporale coperta dal run (timestamptz).</summary>
    public DateTimeOffset WindowStart { get; set; }

    /// <summary>Fine della finestra temporale coperta dal run (timestamptz).</summary>
    public DateTimeOffset WindowEnd { get; set; }

    public DateTimeOffset StartedAt { get; set; }
    public DateTimeOffset? CompletedAt { get; set; }

    /// <summary>File JSON sorgente prodotto dalla pipeline, es. "digest_2026-09-01.json".</summary>
    public string? SourceFile { get; set; }

    public string? Notes { get; set; }

    public ICollection<DigestPoint> DigestPoints { get; set; } = new List<DigestPoint>();
}
