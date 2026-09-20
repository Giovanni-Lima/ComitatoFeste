using System.Net;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;
using ComitatoFeste.Data;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Client minimale per la chat completion di Groq: genera il verbale giornaliero
/// (<see cref="WriteRecapAsync"/>) e risponde alle domande dell'assistente
/// (<see cref="AskAsync"/>, con fallback sul modello 20b). Ritenta su 429/5xx con backoff.
/// Il Transcriber ha un suo <c>GroqClient</c> più ricco (Whisper + throttle TPM); non è
/// condiviso qui di proposito — se servisse un terzo consumatore si estrae un progetto comune.
/// </summary>
public sealed class GroqRecapClient
{
    private const string Model = "openai/gpt-oss-120b";

    /// <summary>
    /// Backup dell'assistente: stessa famiglia, ha un contatore di quota (RPD/TPD/TPM) separato da
    /// quello del 120b, quindi di solito ha ancora budget quando il 120b è saturo. Stessa scelta
    /// del Transcriber (<c>ClassifierModels</c>).
    /// </summary>
    public const string FallbackModel = "openai/gpt-oss-20b";

    private const string Url = "https://api.groq.com/openai/v1/chat/completions";

    private readonly HttpClient _http;
    private readonly string? _apiKey;

    public GroqRecapClient(HttpClient http, IConfiguration config)
    {
        _http = http;
        // Env GROQ_API_KEY o file key.txt (vedi GroqKey), poi config Groq:ApiKey.
        _apiKey = GroqKey.Resolve() ?? config["Groq:ApiKey"];
    }

    /// <summary>La chiave Groq è disponibile (env <c>GROQ_API_KEY</c>, file <c>key.txt</c> o config <c>Groq:ApiKey</c>).</summary>
    public bool IsConfigured => !string.IsNullOrWhiteSpace(_apiKey);

    public string ModelName => Model;

    /// <summary>Produce il verbale in Markdown a partire dall'elenco testuale dei punti del giorno.</summary>
    public async Task<string> WriteRecapAsync(string groupName, DateOnly date, string pointsBlock, CancellationToken ct)
    {
        var system = $$"""
            Sei il segretario del comitato feste "{{groupName}}". Ricevi i punti salienti estratti
            dalla chat WhatsApp del gruppo per una singola giornata. Scrivi un verbale sintetico in
            italiano, con queste sezioni Markdown (ometti quelle senza contenuto):

            ## Decisioni
            ## Domande aperte
            ## Informazioni

            Regole: una riga concisa per punto (massimo ~20 parole), come elenco puntato;
            accorpa in un'unica riga i punti quasi identici o consecutivi dello stesso autore;
            attieniti ai punti forniti, non inventare nulla, non elencare i file multimediali,
            niente preamboli o chiuse. Attribuisci le affermazioni alle persone quando è utile.
            Copri TUTTI i punti, dal primo all'ultimo orario: non fermarti a metà giornata.
            """;

        var user = $"Giornata: {date:dd/MM/yyyy}\n\nPunti (orario · autore · tipo: testo):\n{pointsBlock}";

        // gpt-oss conta i token di ragionamento nel budget; 4096 basta per una giornata
        // densa (~95 punti) restando sotto il limite 8k token/min del tier gratuito.
        return await ChatAsync(
            Model, system, user, maxCompletionTokens: 4096, maxAttempts: 4,
            truncatedMessage: "Groq ha troncato il verbale (max token raggiunto): riprova o riduci i punti del giorno.",
            ct);
    }

    /// <summary>
    /// Risposta dell'assistente. Prova il 120b senza attese: se è saturo (429/5xx) passa subito al
    /// 20b, che ha un contatore di quota separato, invece di far aspettare l'utente. Restituisce
    /// anche il modello che ha risposto, per segnalare all'utente quando è il ridotto.
    /// </summary>
    public async Task<(string Content, string Model)> AskAsync(
        string system, string user, int maxCompletionTokens, CancellationToken ct)
    {
        const string truncated =
            "La risposta è stata troncata (max token raggiunto): prova con una domanda più specifica.";

        try
        {
            var content = await ChatAsync(Model, system, user, maxCompletionTokens, maxAttempts: 1, truncated, ct);
            return (content, Model);
        }
        catch (GroqBusyException)
        {
            // 429/5xx sul 120b: tocca al 20b (qualche tentativo, ha il suo contatore).
        }

        var fallback = await ChatAsync(FallbackModel, system, user, maxCompletionTokens, maxAttempts: 3, truncated, ct);
        return (fallback, FallbackModel);
    }

    private async Task<string> ChatAsync(
        string model, string system, string user, int maxCompletionTokens, int maxAttempts,
        string truncatedMessage, CancellationToken ct)
    {
        var payload = new
        {
            model,
            temperature = 0.2,
            reasoning_effort = "low",
            max_completion_tokens = maxCompletionTokens,
            messages = new[]
            {
                new { role = "system", content = system },
                new { role = "user", content = user },
            },
        };
        var json = JsonSerializer.Serialize(payload);

        for (var attempt = 1; ; attempt++)
        {
            using var req = new HttpRequestMessage(HttpMethod.Post, Url)
            {
                Content = new StringContent(json, Encoding.UTF8, "application/json"),
            };
            req.Headers.Authorization = new AuthenticationHeaderValue("Bearer", _apiKey);

            using var resp = await _http.SendAsync(req, ct);
            var body = await resp.Content.ReadAsStringAsync(ct);

            if (resp.IsSuccessStatusCode)
            {
                using var doc = JsonDocument.Parse(body);
                var choice = doc.RootElement.GetProperty("choices")[0];
                var content = choice.GetProperty("message").GetProperty("content").GetString();

                // Risposta tagliata a metà: meglio un errore (l'endpoint non la mette in cache)
                // che salvare un verbale incompleto.
                var finish = choice.TryGetProperty("finish_reason", out var fr) ? fr.GetString() : null;
                if (finish == "length")
                    throw new InvalidOperationException(truncatedMessage);

                return (content ?? string.Empty).Trim();
            }

            var message = $"Groq HTTP {(int)resp.StatusCode}: {body[..Math.Min(300, body.Length)]}";
            var retryable = resp.StatusCode == HttpStatusCode.TooManyRequests || (int)resp.StatusCode >= 500;
            if (!retryable)
                throw new InvalidOperationException(message);
            if (attempt >= maxAttempts)
                throw new GroqBusyException(message);

            var wait = resp.Headers.RetryAfter?.Delta ?? TimeSpan.FromSeconds(Math.Min(20, 2 * attempt));
            await Task.Delay(wait, ct);
        }
    }
}

/// <summary>Groq saturo (429 o 5xx) anche dopo i tentativi consentiti: chi può, ripiega sul modello di backup.</summary>
public sealed class GroqBusyException : InvalidOperationException
{
    public GroqBusyException(string message) : base(message)
    {
    }
}
