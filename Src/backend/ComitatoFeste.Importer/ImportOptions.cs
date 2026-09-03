namespace ComitatoFeste.Importer;

/// <summary>Parametri di dedup dell'import.</summary>
public sealed record ImportOptions
{
    /// <summary>
    /// Se true, oltre al dedup esatto sul vincolo (Group, Member, OccurredAt, Text) prova a riconoscere
    /// le riformulazioni tra run diversi via <c>similarity()</c> pg_trgm, confrontando solo punti
    /// dello stesso membro entro <see cref="FuzzyWindow"/> dall'istante della entry.
    /// </summary>
    public bool FuzzyDedup { get; init; } = true;

    /// <summary>Soglia minima di <c>similarity()</c> (0..1) per considerare due testi lo stesso messaggio.</summary>
    public double FuzzyThreshold { get; init; } = 0.6;

    /// <summary>Distanza massima tra gli <c>OccurredAt</c> per confrontare due punti nel fuzzy match.</summary>
    public TimeSpan FuzzyWindow { get; init; } = TimeSpan.FromMinutes(2);
}
