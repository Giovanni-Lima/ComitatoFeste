namespace ComitatoFeste.Domain;

/// <summary>
/// Verbale in prosa di una giornata, generato una tantum da un LLM (Groq) a partire dai
/// <see cref="DigestPoint"/> di quel giorno e messo in cache: alla prima richiesta viene
/// prodotto e salvato, dalle successive viene servito così com'è (nessuna nuova chiamata,
/// a meno di una rigenerazione esplicita).
/// </summary>
public class Verbale
{
    public int Id { get; set; }

    public int GroupId { get; set; }
    public Group Group { get; set; } = null!;

    /// <summary>Giorno coperto (fuso Europe/Rome). Unico per gruppo.</summary>
    public DateOnly Date { get; set; }

    /// <summary>Testo del verbale in Markdown.</summary>
    public string Content { get; set; } = null!;

    /// <summary>Modello LLM che l'ha prodotto (tracciabilità), es. "openai/gpt-oss-120b".</summary>
    public string Model { get; set; } = null!;

    /// <summary>Quanti <see cref="DigestPoint"/> riassumeva al momento della generazione.</summary>
    public int PointCount { get; set; }

    public DateTimeOffset GeneratedAt { get; set; }
}
