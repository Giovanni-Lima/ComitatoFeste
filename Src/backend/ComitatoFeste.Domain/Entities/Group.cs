namespace ComitatoFeste.Domain;

/// <summary>Un gruppo WhatsApp monitorato (es. "Comitato feste 87").</summary>
public class Group
{
    public int Id { get; set; }

    /// <summary>Nome del gruppo come mostrato da WhatsApp. Unico.</summary>
    public string Name { get; set; } = null!;

    public DateTimeOffset CreatedAt { get; set; }

    public ICollection<Member> Members { get; set; } = new List<Member>();
    public ICollection<IngestionRun> IngestionRuns { get; set; } = new List<IngestionRun>();
    public ICollection<DigestPoint> DigestPoints { get; set; } = new List<DigestPoint>();
    public ICollection<Verbale> Verbali { get; set; } = new List<Verbale>();
}
