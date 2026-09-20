namespace ComitatoFeste.Api.Contracts;

/// <summary>
/// Corpo di <c>POST /api/assistant/ask</c>. <c>From</c>/<c>To</c> (inclusivi, opzionali) limitano la
/// ricerca ai punti di quell'intervallo di giorni (fuso Roma), es. "cosa si è deciso il 12?".
/// </summary>
public sealed record AskRequest(string? Question, DateOnly? From, DateOnly? To);

/// <summary>Un punto del digest su cui si basa la risposta, citato nel testo come <c>[Ref]</c>.</summary>
public sealed record AssistantSourceDto(
    int Ref, int Id, string Date, string Time, string Author, string Type, string Text);

/// <summary>
/// Risposta dell'assistente. <c>Sources</c> contiene solo i punti che il modello ha citato con
/// <c>[n]</c> (vuoto se non ne ha citati, per esempio quando non ha trovato la risposta).
/// <c>ReducedModel</c> è true se ha risposto il modello di backup più piccolo (quota del principale
/// esaurita). <c>Retrieved</c> = quanti punti sono stati passati al modello.
/// </summary>
public sealed record AssistantAnswerDto(
    string Answer, IReadOnlyList<AssistantSourceDto> Sources, string Model, bool ReducedModel, int Retrieved);
