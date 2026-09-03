namespace ComitatoFeste.Domain;

/// <summary>
/// Un punto significativo estratto dalla chat: corrisponde a una entry del JSON di ingestion
/// (<c>{date, time, author, type, text, file}</c>).
/// </summary>
/// <remarks>
/// Dedup a due livelli (vedi docs/CONTEXT.md):
/// <list type="bullet">
///   <item>vincolo UNIQUE hard su (GroupId, MemberId, OccurredAt, Text) contro i rerun letterali;</item>
///   <item>indice GIN pg_trgm su Text per il fuzzy match applicativo sulle riformulazioni tra run diversi.</item>
/// </list>
/// </remarks>
public class DigestPoint
{
    public int Id { get; set; }

    public int IngestionRunId { get; set; }
    public IngestionRun IngestionRun { get; set; } = null!;

    public int GroupId { get; set; }
    public Group Group { get; set; } = null!;

    public int MemberId { get; set; }
    public Member Member { get; set; } = null!;

    /// <summary>Istante del messaggio in chat, da <c>date</c> + <c>time</c> del JSON (timestamptz).</summary>
    public DateTimeOffset OccurredAt { get; set; }

    public DigestPointType Type { get; set; }

    /// <summary>Testo del punto di digest (la sintesi prodotta dalla pipeline).</summary>
    public string Text { get; set; } = null!;

    /// <summary>File scaricato collegato, presente solo per alcuni punti di tipo media (relazione 1:1).</summary>
    public MediaAsset? MediaAsset { get; set; }
}
