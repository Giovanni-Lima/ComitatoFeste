namespace ComitatoFeste.Domain;

/// <summary>
/// Embedding semantico di un <see cref="DigestPoint"/> (relazione 1:1), per l'assistente AI
/// (ricerca dei punti più vicini a una domanda, vedi pgvector). Tenuto in tabella separata
/// come i blob: la timeline non trascina 768 float per riga. Calcolato dopo il Transcriber,
/// perché il testo dei vocali viene riscritto dopo l'import.
/// </summary>
public class DigestPointEmbedding
{
    /// <summary>PK e FK insieme: un solo embedding per punto.</summary>
    public int DigestPointId { get; set; }
    public DigestPoint DigestPoint { get; set; } = null!;

    /// <summary>Vettore normalizzato (768 dimensioni). Nel DB è <c>vector(768)</c>.</summary>
    public float[] Embedding { get; set; } = Array.Empty<float>();

    /// <summary>Modello che l'ha prodotto: se cambia, gli embedding vanno ricalcolati tutti.</summary>
    public string Model { get; set; } = null!;

    /// <summary>
    /// SHA-256 esadecimale del testo effettivamente embeddato (prefisso autore incluso). Se il
    /// testo del punto o il formato di input cambiano, l'hash non fa più match e l'Embedder
    /// ricalcola solo quella riga.
    /// </summary>
    public string InputSha256 { get; set; } = null!;

    public DateTimeOffset EmbeddedAt { get; set; }
}
