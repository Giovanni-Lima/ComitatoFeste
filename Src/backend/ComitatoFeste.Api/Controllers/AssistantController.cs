using ComitatoFeste.Api.Contracts;
using ComitatoFeste.Api.Filters;
using ComitatoFeste.Api.Services;
using Microsoft.AspNetCore.Mvc;

namespace ComitatoFeste.Api.Controllers;

/// <summary>
/// Assistente AI: risponde a domande in linguaggio naturale sui punti del digest (RAG: embedding
/// Gemini + pgvector per il retrieval, Groq per la risposta). Vedi <see cref="AssistantService"/>.
/// </summary>
[ApiController]
[Route("api/assistant")]
[TokenAuth]
public sealed class AssistantController : ControllerBase
{
    private readonly AssistantService _assistant;
    private readonly AssistantLimiter _limiter;
    private readonly AuthService _auth;

    public AssistantController(AssistantService assistant, AssistantLimiter limiter, AuthService auth)
    {
        _assistant = assistant;
        _limiter = limiter;
        _auth = auth;
    }

    /// <summary>
    /// Risponde a una domanda usando i punti del digest più pertinenti. Con <c>from</c>/<c>to</c>
    /// (giorni inclusivi, yyyy-MM-dd) restringe la ricerca a un intervallo. Limiti: per utente
    /// all'ora e totali al giorno (la quota gratuita di Groq/Gemini è condivisa) → 429 con
    /// <c>Retry-After</c>. 503 se i servizi esterni sono saturi o non configurati.
    /// </summary>
    [HttpPost("ask")]
    [ProducesResponseType(typeof(AssistantAnswerDto), StatusCodes.Status200OK)]
    public async Task<IActionResult> Ask([FromBody] AskRequest request, CancellationToken ct)
    {
        var question = request.Question?.Trim();
        if (string.IsNullOrEmpty(question))
            return BadRequest("Scrivi una domanda.");
        if (question.Length > AssistantService.MaxQuestionLength)
            return BadRequest($"La domanda è troppo lunga (massimo {AssistantService.MaxQuestionLength} caratteri).");
        if (request.From is { } from && request.To is { } to && from > to)
            return BadRequest("'from' non può essere successivo a 'to'.");

        if (!_assistant.IsConfigured)
            return StatusCode(StatusCodes.Status503ServiceUnavailable,
                "Assistente non configurato: servono GEMINI_API_KEY e GROQ_API_KEY sull'API.");

        var user = CurrentUsername();
        var ticket = _limiter.TryAcquire(user, out var denial);
        if (ticket is null)
        {
            Response.Headers.RetryAfter = ((int)Math.Ceiling(denial.RetryAfter.TotalSeconds)).ToString();
            return StatusCode(StatusCodes.Status429TooManyRequests, denial.Message);
        }

        // Se la domanda non arriva a buon fine (servizio esterno saturo, richiesta annullata) il
        // biglietto viene restituito: l'utente non paga un errore che non è suo.
        var succeeded = false;
        try
        {
            using var slot = await _limiter.WaitSlotAsync(TimeSpan.FromSeconds(20), ct);
            if (slot is null)
            {
                Response.Headers.RetryAfter = "15";
                return StatusCode(StatusCodes.Status503ServiceUnavailable,
                    "L'assistente è occupato con altre domande: riprova tra qualche secondo.");
            }

            var answer = await _assistant.AskAsync(question, request.From, request.To, ct);
            succeeded = true;
            return Ok(answer);
        }
        catch (AssistantException ex)
        {
            return StatusCode(ex.StatusCode, ex.Message);
        }
        finally
        {
            if (!succeeded)
                _limiter.Refund(user, ticket.Value);
        }
    }

    /// <summary>Username del token (per il limite per utente); con il login disattivato (locale) un bucket unico.</summary>
    private string CurrentUsername()
    {
        var header = Request.Headers.Authorization.ToString();
        var token = header.StartsWith("Bearer ", StringComparison.OrdinalIgnoreCase)
            ? header["Bearer ".Length..].Trim()
            : null;
        return _auth.ValidatePrincipal(token)?.Username ?? "anonimo";
    }
}
