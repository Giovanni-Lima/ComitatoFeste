using System.Net;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Client minimale per la chat completion di Groq, usato solo per generare il verbale
/// giornaliero. Ritenta su 429/5xx con backoff. Il Transcriber ha un suo <c>GroqClient</c>
/// più ricco (Whisper + throttle TPM); non è condiviso qui di proposito — se servisse un
/// terzo consumatore si estrae un progetto comune.
/// </summary>
public sealed class GroqRecapClient
{
    private const string Model = "openai/gpt-oss-120b";
    private const string Url = "https://api.groq.com/openai/v1/chat/completions";

    private readonly HttpClient _http;
    private readonly string? _apiKey;

    public GroqRecapClient(HttpClient http, IConfiguration config)
    {
        _http = http;
        _apiKey = config["GROQ_API_KEY"] ?? config["Groq:ApiKey"];
    }

    /// <summary>La chiave Groq è disponibile (env <c>GROQ_API_KEY</c> o config <c>Groq:ApiKey</c>).</summary>
    public bool IsConfigured => !string.IsNullOrWhiteSpace(_apiKey);

    public string ModelName => Model;

    /// <summary>Produce il verbale in Markdown a partire dall'elenco testuale dei punti del giorno.</summary>
    public async Task<string> WriteRecapAsync(string groupName, DateOnly date, string pointsBlock, CancellationToken ct)
    {
        var system = $$"""
            Sei il segretario del comitato feste "{{groupName}}". Ricevi i punti salienti estratti
            dalla chat WhatsApp del gruppo per una singola giornata. Scrivi un verbale sintetico in
            italiano, in prosa scorrevole, con queste sezioni Markdown (ometti quelle senza contenuto):

            ## Decisioni
            ## Domande aperte
            ## Informazioni

            Regole: attieniti ai punti forniti, non inventare nulla, non elencare i file multimediali,
            niente preamboli o chiuse. Attribuisci le affermazioni alle persone quando è utile.
            """;

        var user = $"Giornata: {date:dd/MM/yyyy}\n\nPunti (orario · autore · tipo: testo):\n{pointsBlock}";

        var payload = new
        {
            model = Model,
            temperature = 0.2,
            reasoning_effort = "low",
            max_completion_tokens = 2000,
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
                var content = doc.RootElement.GetProperty("choices")[0]
                    .GetProperty("message").GetProperty("content").GetString();
                return (content ?? string.Empty).Trim();
            }

            var retryable = resp.StatusCode == HttpStatusCode.TooManyRequests || (int)resp.StatusCode >= 500;
            if (!retryable || attempt > 3)
                throw new InvalidOperationException(
                    $"Groq HTTP {(int)resp.StatusCode}: {body[..Math.Min(300, body.Length)]}");

            var wait = resp.Headers.RetryAfter?.Delta ?? TimeSpan.FromSeconds(Math.Min(20, 2 * attempt));
            await Task.Delay(wait, ct);
        }
    }
}
