using System.Net;
using System.Text;
using System.Text.Json;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Client minimale per la generazione di testo di Gemini (<c>generateContent</c>), usato
/// dall'assistente AI come modello di risposta principale (Groq resta come ultimo ripiego).
/// Senza retry: per una domanda interattiva è meglio passare subito al modello successivo della
/// catena che far aspettare l'utente. Stessa chiave degli embedding (<c>GeminiKey</c>).
/// </summary>
public sealed class GeminiChatClient
{
    private readonly HttpClient _http;
    private readonly string _apiKey;

    public GeminiChatClient(HttpClient http, string apiKey)
    {
        _http = http;
        _apiKey = apiKey;
    }

    /// <summary>
    /// Genera la risposta con il modello <paramref name="model"/> (es. <c>gemini-3.5-flash-lite</c>).
    /// Solleva <see cref="GeminiBusyException"/> su 429/5xx (quota o servizio saturo) e
    /// <see cref="InvalidOperationException"/> per gli altri errori (risposta vuota, bloccata,
    /// troncata): in entrambi i casi il chiamante può ripiegare sul modello successivo.
    /// </summary>
    public async Task<string> GenerateAsync(
        string model, string system, string user, int maxOutputTokens, CancellationToken ct)
    {
        var payload = new
        {
            systemInstruction = new { parts = new[] { new { text = system } } },
            contents = new[] { new { role = "user", parts = new[] { new { text = user } } } },
            generationConfig = new { maxOutputTokens, temperature = 0.2 },
        };

        using var req = new HttpRequestMessage(
            HttpMethod.Post,
            $"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent")
        {
            Content = new StringContent(JsonSerializer.Serialize(payload), Encoding.UTF8, "application/json"),
        };
        // La chiave viaggia nell'header, mai nell'URL: così non finisce nei log/eccezioni.
        req.Headers.Add("x-goog-api-key", _apiKey);

        HttpResponseMessage resp;
        try
        {
            resp = await _http.SendAsync(req, ct);
        }
        catch (TaskCanceledException) when (!ct.IsCancellationRequested)
        {
            throw new GeminiBusyException($"Gemini {model}: timeout");
        }

        using (resp)
        {
            var body = await resp.Content.ReadAsStringAsync(ct);
            if (!resp.IsSuccessStatusCode)
            {
                var message = $"Gemini {model} HTTP {(int)resp.StatusCode}: {body[..Math.Min(300, body.Length)]}";
                if (resp.StatusCode == HttpStatusCode.TooManyRequests || (int)resp.StatusCode >= 500)
                    throw new GeminiBusyException(message);
                throw new InvalidOperationException(message);
            }

            using var doc = JsonDocument.Parse(body);
            var root = doc.RootElement;

            if (!root.TryGetProperty("candidates", out var candidates) || candidates.GetArrayLength() == 0)
            {
                var reason = root.TryGetProperty("promptFeedback", out var fb) && fb.TryGetProperty("blockReason", out var br)
                    ? br.GetString()
                    : "nessun candidato";
                throw new InvalidOperationException($"Gemini {model}: risposta assente ({reason}).");
            }

            var candidate = candidates[0];
            var text = candidate.TryGetProperty("content", out var content) && content.TryGetProperty("parts", out var parts)
                ? string.Concat(parts.EnumerateArray()
                    .Where(p => p.TryGetProperty("text", out _) && !(p.TryGetProperty("thought", out var t) && t.ValueKind == JsonValueKind.True))
                    .Select(p => p.GetProperty("text").GetString()))
                : string.Empty;

            var finish = candidate.TryGetProperty("finishReason", out var fr) ? fr.GetString() : null;
            if (finish == "MAX_TOKENS")
                throw new InvalidOperationException($"Gemini {model}: risposta troncata (max token raggiunto).");
            if (string.IsNullOrWhiteSpace(text))
                throw new InvalidOperationException($"Gemini {model}: risposta vuota (finishReason={finish}).");

            return text;
        }
    }
}

/// <summary>Gemini saturo (429, 5xx o timeout): si può ripiegare sul modello successivo.</summary>
public sealed class GeminiBusyException : InvalidOperationException
{
    public GeminiBusyException(string message) : base(message)
    {
    }
}
