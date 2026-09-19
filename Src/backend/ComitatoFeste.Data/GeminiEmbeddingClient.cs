using System.Net;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using ComitatoFeste.Data.Configurations;

namespace ComitatoFeste.Data;

/// <summary>
/// Client minimale per gli embedding di Gemini (<c>gemini-embedding-2</c>), condiviso da
/// <c>ComitatoFeste.Embedder</c> (indicizza i punti) e dall'API (embedda le domande): i due lati
/// DEVONO usare lo stesso modello, la stessa dimensione e i formati di input asimmetrici qui sotto,
/// altrimenti i vettori non sono confrontabili — per questo stanno insieme.
/// Ritenta su HTTP 429/5xx con backoff.
/// </summary>
/// <remarks>
/// Verificato sulla documentazione e con chiamate reali (set 2026): il modello tronca a
/// <c>output_dimensionality</c> (MRL) e restituisce già vettori normalizzati; il "tipo di task"
/// non è un parametro ma un prefisso nel testo (<c>gemini-embedding-001</c>, con <c>task_type</c>,
/// è il modello precedente e ha regole diverse). Free tier gratuito; i dati inviati servono a
/// Google per migliorare i prodotti (il gruppo ha dato l'ok).
/// </remarks>
public sealed class GeminiEmbeddingClient
{
    public const string Model = "gemini-embedding-2";

    /// <summary>Dimensione dei vettori: la stessa della colonna <c>vector(N)</c> a DB.</summary>
    public const int Dimensions = DigestPointEmbeddingConfiguration.Dimensions;

    private const string BaseUrl = "https://generativelanguage.googleapis.com/v1beta/models/" + Model;
    private const int MaxAttempts = 6;

    private readonly HttpClient _http;
    private readonly string _apiKey;

    public GeminiEmbeddingClient(HttpClient http, string apiKey)
    {
        _http = http;
        _apiKey = apiKey;
    }

    /// <summary>
    /// Testo da indicizzare per un punto, nel formato "documento" del modello (senza titolo).
    /// Il prefisso con l'autore aiuta le domande del tipo "cosa ha proposto Antonio".
    /// </summary>
    public static string DocumentInput(string author, string text) =>
        $"title: none | text: {author}: {text}";

    /// <summary>Testo di una domanda dell'utente, nel formato "query" (ricerca asimmetrica).</summary>
    public static string QueryInput(string question) =>
        $"task: search result | query: {question}";

    /// <summary>SHA-256 esadecimale (minuscolo) dell'input: finisce in <c>InputSha256</c>.</summary>
    public static string Hash(string input) =>
        Convert.ToHexString(SHA256.HashData(Encoding.UTF8.GetBytes(input))).ToLowerInvariant();

    /// <summary>Embedda più testi già formattati (vedi <see cref="DocumentInput"/>) in una sola richiesta.</summary>
    public async Task<float[][]> EmbedBatchAsync(IReadOnlyList<string> inputs, CancellationToken ct)
    {
        if (inputs.Count == 0)
            return Array.Empty<float[]>();

        var payload = new
        {
            requests = inputs.Select(t => new
            {
                model = $"models/{Model}",
                content = new { parts = new[] { new { text = t } } },
                output_dimensionality = Dimensions,
            }).ToArray(),
        };

        using var doc = await PostAsync($"{BaseUrl}:batchEmbedContents", payload, ct);
        var items = doc.RootElement.GetProperty("embeddings");
        if (items.GetArrayLength() != inputs.Count)
            throw new InvalidOperationException(
                $"Gemini ha restituito {items.GetArrayLength()} embedding per {inputs.Count} testi.");

        return items.EnumerateArray().Select(e => ReadValues(e)).ToArray();
    }

    /// <summary>Embedda una domanda (formato "query"): una sola richiesta.</summary>
    public async Task<float[]> EmbedQueryAsync(string question, CancellationToken ct)
    {
        var payload = new
        {
            content = new { parts = new[] { new { text = QueryInput(question) } } },
            output_dimensionality = Dimensions,
        };

        using var doc = await PostAsync($"{BaseUrl}:embedContent", payload, ct);
        return ReadValues(doc.RootElement.GetProperty("embedding"));
    }

    private static float[] ReadValues(JsonElement embedding)
    {
        var values = embedding.GetProperty("values").EnumerateArray().Select(v => v.GetSingle()).ToArray();
        if (values.Length != Dimensions)
            throw new InvalidOperationException($"Attesi {Dimensions} valori, ricevuti {values.Length}.");

        // Il modello li restituisce già normalizzati; rinormalizzo solo se non lo fossero, perché
        // la distanza coseno di pgvector si aspetta vettori confrontabili.
        var norm = MathF.Sqrt(values.Sum(x => x * x));
        if (norm > 0 && MathF.Abs(norm - 1f) > 1e-3f)
            for (var i = 0; i < values.Length; i++)
                values[i] /= norm;

        return values;
    }

    private async Task<JsonDocument> PostAsync(string url, object payload, CancellationToken ct)
    {
        var json = JsonSerializer.Serialize(payload);

        for (var attempt = 1; ; attempt++)
        {
            using var req = new HttpRequestMessage(HttpMethod.Post, url)
            {
                Content = new StringContent(json, Encoding.UTF8, "application/json"),
            };
            // La chiave viaggia nell'header, mai nell'URL: così non finisce nei log/eccezioni.
            req.Headers.Add("x-goog-api-key", _apiKey);

            using var resp = await _http.SendAsync(req, ct);
            var body = await resp.Content.ReadAsStringAsync(ct);

            if (resp.IsSuccessStatusCode)
                return JsonDocument.Parse(body);

            var retryable = resp.StatusCode == HttpStatusCode.TooManyRequests || (int)resp.StatusCode >= 500;
            if (!retryable || attempt >= MaxAttempts)
                throw new InvalidOperationException(
                    $"Gemini HTTP {(int)resp.StatusCode}: {body[..Math.Min(300, body.Length)]}");

            var wait = resp.Headers.RetryAfter?.Delta
                       ?? TimeSpan.FromSeconds(Math.Min(60, 5 * Math.Pow(2, attempt - 1)));
            await Task.Delay(wait, ct);
        }
    }
}
