namespace ComitatoFeste.Api.Contracts;

/// <summary>
/// Range di date (fuso Roma) coperto dai punti della vista "pulita" (niente rumore, niente
/// audio non ancora digerito). Il frontend lo usa per scegliere il mese di default dell'Agenda
/// (il mese di <see cref="Latest"/>, non necessariamente quello di oggi) e per sapere quando
/// nascondere il bottone "carica mese precedente" (quando si è già arrivati a <see cref="Earliest"/>).
/// </summary>
public sealed record DigestPointsBoundsDto
{
    public DateOnly? Earliest { get; init; }
    public DateOnly? Latest { get; init; }
}
