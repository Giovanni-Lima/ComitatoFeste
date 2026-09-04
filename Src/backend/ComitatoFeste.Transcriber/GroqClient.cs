using System.Net;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace ComitatoFeste.Transcriber;

/// <summary>
/// Client minimale per le due API Groq usate dal transcriber: Whisper (audio → testo)
/// e chat completion (testo → classificazione). Ritenta in automatico su 429/5xx con backoff.
/// </summary>
public sealed class GroqClient
{
    // Coppie di modelli intercambiabili per il tier gratuito Groq. Al primo HTTP 429 su un
    // modello si passa al suo backup e ci si resta per il resto del run: il 429 su Groq è
    // quasi sempre quota (al minuto o giornaliera) esaurita per QUEL modello, e i contatori
    // sono separati per modello, quindi il backup di solito ha ancora budget.
    //   Whisper: v3 (default, migliore su dialetto marchigiano/abruzzese e audio WhatsApp
    //            rumoroso) -> v3-turbo (backup, più veloce, un filo meno accurato).
    //   Classificatore: gpt-oss-120b (default, meno confusione rumore/info, ma rispetta male
    //            response_format json_object: vedi ParseClassification) -> gpt-oss-20b (backup,
    //            stessi limiti free 1.000 req/g · 200k token/g · 30/min · 8.000 token/min ma
    //            bucket separato). I llama-3.x sono deprecati (giu 2026).
    // Verifica su https://console.groq.com/docs/models che i nomi siano ancora correnti.
    private static readonly string[] WhisperModels    = { "whisper-large-v3", "whisper-large-v3-turbo" };
    private static readonly string[] ClassifierModels = { "openai/gpt-oss-120b", "openai/gpt-oss-20b" };

    private int _whisperIdx;
    private int _classifierIdx;
    private string WhisperModel => WhisperModels[_whisperIdx];
    private string ClassifierModel => ClassifierModels[_classifierIdx];

    /// <summary>Modelli attualmente in uso (cambiano se scatta il fallback su 429).</summary>
    public string CurrentWhisperModel => WhisperModel;
    public string CurrentClassifierModel => ClassifierModel;

    /// <summary>Passa al backup della coppia (una volta sola). Restituisce il nuovo nome, o null se già sul backup.</summary>
    private string? FallbackWhisper() =>
        _whisperIdx + 1 < WhisperModels.Length ? WhisperModels[++_whisperIdx] : null;

    private string? FallbackClassifier()
    {
        if (_classifierIdx + 1 >= ClassifierModels.Length)
            return null;
        _classifierTokenLog.Clear();   // il nuovo modello ha un suo budget TPM: log da zero
        return ClassifierModels[++_classifierIdx];
    }

    /// <summary>Quante volte richiedere la classificazione se torna una risposta non valida.</summary>
    private const int ClassifyAttempts = 2;

    // Freno adattivo per il TPM del classificatore (gpt-oss-20b free tier = 8.000 token/min).
    // Dopo ogni chiamata registriamo i token consumati (campo `usage` della risposta); prima
    // della successiva aspettiamo che la somma sugli ultimi 60 s rientri sotto la soglia.
    // NB: i token serviti da cache contano comunque ai fini del rate limit, quindi il prompt
    // lungo pesa a ogni chiamata anche se identico.
    private const int ClassifierTpmSoftLimit = 6500;
    private readonly Queue<(DateTime At, int Tokens)> _classifierTokenLog = new();

    private const string TranscriptionsUrl = "https://api.groq.com/openai/v1/audio/transcriptions";
    private const string ChatCompletionsUrl = "https://api.groq.com/openai/v1/chat/completions";

    private static readonly string[] AllowedTypes = { "decisione", "domanda", "info", "media", "rumore" };

    private readonly HttpClient _http;
    private readonly int _maxRetries;

    public GroqClient(HttpClient http, string apiKey, int maxRetries = 3)
    {
        _http = http;
        _http.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", apiKey);
        _maxRetries = maxRetries;
    }

    /// <summary>Trascrive un vocale con Groq Whisper. Restituisce stringa vuota se non c'è parlato riconoscibile.</summary>
    public async Task<string> TranscribeAsync(byte[] audio, string fileName, string? contentType, CancellationToken ct = default)
    {
        // I vocali WhatsApp (.opus) sono in realtà Ogg/Opus: Groq elenca "ogg" tra i formati
        // supportati, non ".opus" esplicitamente, quindi normalizzo l'estensione inviata.
        var sendName = Path.GetExtension(fileName).Equals(".opus", StringComparison.OrdinalIgnoreCase)
            ? Path.ChangeExtension(fileName, ".ogg")
            : fileName;

        var body = await SendWithRetryAsync(() =>
        {
            var form = new MultipartFormDataContent();
            var file = new ByteArrayContent(audio);
            file.Headers.ContentType = new MediaTypeHeaderValue(contentType ?? "application/octet-stream");
            form.Add(file, "file", sendName);
            form.Add(new StringContent(WhisperModel), "model");   // letto ad ogni tentativo
            form.Add(new StringContent("it"), "language");
            form.Add(new StringContent("json"), "response_format");
            return new HttpRequestMessage(HttpMethod.Post, TranscriptionsUrl) { Content = form };
        }, "Whisper", FallbackWhisper, ct);

        using var doc = JsonDocument.Parse(body);
        return doc.RootElement.TryGetProperty("text", out var t) ? (t.GetString() ?? "").Trim() : "";
    }

    /// <summary>Classifica una trascrizione in decisione/domanda/info/media/rumore, con sintesi in una frase.</summary>
    public async Task<Classification> ClassifyAsync(string groupName, string author, string transcript, CancellationToken ct = default)
    {
        if (string.IsNullOrWhiteSpace(transcript))
            return new Classification("rumore", null);

        var prompt = $$"""
            Sei un assistente che analizza il vocale trascritto di una chat WhatsApp del comitato
            feste "{{groupName}}". Autore: {{author}}. Trascrizione (può contenere dialetto
            marchigiano/abruzzese, a tratti imprecisa):

            "{{transcript}}"

            PRIMA valuta: questo vocale contiene qualcosa di concretamente utile per ORGANIZZARE
            gli eventi del comitato (una decisione, una proposta operativa, una domanda operativa,
            un fatto verificabile)? Se NO — è una battuta, un commento personale, un'esitazione,
            una conferma, un saluto, un frammento di conversazione senza contesto — allora è
            "rumore". Nel dubbio fra "rumore" e altro, scegli "rumore".

            Se invece ha sostanza, scegli:
            - "decisione": una decisione presa, o una proposta operativa rivolta al gruppo, anche
              abbozzata ("potremmo...", "io farei...", "proviamo a...", "bisognerebbe...")
            - "domanda": una domanda aperta rivolta al gruppo che attende una risposta
            - "info": condivide un FATTO concreto e verificabile utile al comitato — una data, un
              luogo, un numero, un preventivo, un contatto, lo stato di un compito. Un'opinione o
              un commento generico NON è "info".
            - "media": contenuto chiaramente sostanzioso che non rientra in decisione/domanda/info

            Esempi:
            "Vabbè, dopo a casa mi va bene, lo sto a dire." -> {"type":"rumore","summary":""}
            "Secondo me la festa è andata bene dai." -> {"type":"rumore","summary":""}
            "Il preventivo del service è 800 euro." -> {"type":"info","summary":"Informa che il preventivo del service è di 800 euro."}
            "Facciamo la riunione giovedì alle 21?" -> {"type":"domanda","summary":"Chiede se fissare la riunione giovedì alle 21."}
            "Io direi di puntare sugli sponsor per il cantante." -> {"type":"decisione","summary":"Propone di puntare sugli sponsor per finanziare il cantante."}

            Rispondi SOLO con un oggetto JSON, senza altro testo, in questo formato esatto:
            {"type": "<categoria>", "summary": "<una frase in italiano, in terza persona, stile
            'Propone di...' / 'Chiede se...' / 'Informa che...'; stringa vuota se type è 'rumore'>"}
            """;

        // Payload ricostruito ad ogni chiamata: `ClassifierModel` può cambiare se scatta il
        // fallback su 429. `reasoning_effort = "low"` perché gpt-oss senza freno emette una
        // lunga catena di ragionamento che gonfia i token/minuto ~10x (qui serve una riga di
        // JSON); `max_completion_tokens` è solo una rete contro le derive, non deve troncare.
        HttpRequestMessage BuildClassifyRequest() => new(HttpMethod.Post, ChatCompletionsUrl)
        {
            Content = new StringContent(JsonSerializer.Serialize(new
            {
                model = ClassifierModel,
                temperature = 0,
                reasoning_effort = "low",
                max_completion_tokens = 512,
                response_format = new { type = "json_object" },
                messages = new[] { new { role = "user", content = prompt } },
            }), Encoding.UTF8, "application/json"),
        };

        // gpt-oss ogni tanto risponde con JSON malformato / incorniciato / troncato: ri-chiediamo
        // fino a ClassifyAttempts volte prima di rassegnarci a un esito "incerto".
        Classification last = new("media", null, Uncertain: true);
        for (var attempt = 1; attempt <= ClassifyAttempts; attempt++)
        {
            await WaitForClassifierTokenBudgetAsync(ct);

            var body = await SendWithRetryAsync(BuildClassifyRequest, "classificazione", FallbackClassifier, ct);

            RecordClassifierTokens(body);

            last = ParseClassification(body);
            if (!last.Uncertain)
                return last;
        }

        return last;
    }

    /// <summary>Aspetta finché i token del classificatore usati negli ultimi 60 s non rientrano sotto la soglia TPM.</summary>
    private async Task WaitForClassifierTokenBudgetAsync(CancellationToken ct)
    {
        while (true)
        {
            var now = DateTime.UtcNow;
            while (_classifierTokenLog.Count > 0 && now - _classifierTokenLog.Peek().At >= TimeSpan.FromSeconds(60))
                _classifierTokenLog.Dequeue();

            var used = 0;
            foreach (var e in _classifierTokenLog)
                used += e.Tokens;

            if (used < ClassifierTpmSoftLimit || _classifierTokenLog.Count == 0)
                return;

            var wait = TimeSpan.FromSeconds(60) - (now - _classifierTokenLog.Peek().At);
            if (wait <= TimeSpan.Zero)
                return;

            Console.Write($"[TPM {used}/{ClassifierTpmSoftLimit}, pausa {wait.TotalSeconds:0}s] ");
            await Task.Delay(wait, ct);
        }
    }

    private void RecordClassifierTokens(string body)
    {
        try
        {
            using var d = JsonDocument.Parse(body);
            if (d.RootElement.TryGetProperty("usage", out var u) && u.TryGetProperty("total_tokens", out var t))
                _classifierTokenLog.Enqueue((DateTime.UtcNow, t.GetInt32()));
        }
        catch (JsonException)
        {
            // risposta senza `usage`: non possiamo contabilizzare, pazienza
        }
    }

    /// <summary>Estrae la classificazione dalla risposta chat di Groq; marca <c>Uncertain</c> se il JSON non è utilizzabile.</summary>
    private static Classification ParseClassification(string body)
    {
        using var doc = JsonDocument.Parse(body);
        var choice = doc.RootElement.GetProperty("choices")[0];
        var finishReason = choice.TryGetProperty("finish_reason", out var fr) ? fr.GetString() : null;
        var content = choice.GetProperty("message").GetProperty("content").GetString() ?? "";

        // Risposta troncata prima del JSON: classificazione non attendibile.
        if (finishReason == "length")
            return new Classification("media", null, Uncertain: true);

        try
        {
            // gpt-oss tende a incorniciare il JSON in ```json ... ``` o ad anteporre testo
            // anche con response_format json_object: isoliamo l'oggetto { ... } prima di parsare.
            using var inner = JsonDocument.Parse(ExtractJsonObject(content));
            var type = inner.RootElement.TryGetProperty("type", out var tp) ? tp.GetString() : null;
            var summary = inner.RootElement.TryGetProperty("summary", out var s) ? s.GetString() : null;
            if (string.IsNullOrWhiteSpace(summary))
                summary = null;

            // type mancante o fuori dalle categorie: il modello non ha rispettato lo schema.
            if (type is null || Array.IndexOf(AllowedTypes, type) < 0)
                return new Classification("media", summary, Uncertain: true);

            return new Classification(type, summary);
        }
        catch (JsonException)
        {
            // La risposta non è JSON valido: non è rumore, ma non sappiamo altro.
            return new Classification("media", null, Uncertain: true);
        }
    }

    /// <param name="fallback">
    /// Invocato su HTTP 429: se restituisce un nome di modello (backup della coppia) si ripete
    /// subito la richiesta con quello e i tentativi ripartono da capo; se restituisce null
    /// (già sul backup) si prosegue col normale retry/backoff.
    /// </param>
    private async Task<string> SendWithRetryAsync(Func<HttpRequestMessage> build, string label, Func<string?> fallback, CancellationToken ct)
    {
        for (var attempt = 1; ; attempt++)
        {
            using var req = build();
            using var resp = await _http.SendAsync(req, ct);
            var body = await resp.Content.ReadAsStringAsync(ct);

            if (resp.IsSuccessStatusCode)
                return body;

            if (resp.StatusCode == HttpStatusCode.TooManyRequests && fallback() is { } backup)
            {
                Console.Write($"[429 {label}: passo al modello di backup {backup}] ");
                attempt = 0;   // il backup riparte con i tentativi pieni
                continue;
            }

            var retryable = resp.StatusCode == HttpStatusCode.TooManyRequests || (int)resp.StatusCode >= 500;
            if (!retryable || attempt > _maxRetries)
                throw new InvalidOperationException($"Groq {label} HTTP {(int)resp.StatusCode}: {Truncate(body, 300)}");

            var wait = resp.Headers.RetryAfter?.Delta ?? TimeSpan.FromSeconds(Math.Min(30, 2 * attempt));
            Console.Write($"[HTTP {(int)resp.StatusCode}, ritento tra {wait.TotalSeconds:0}s] ");
            await Task.Delay(wait, ct);
        }
    }

    internal static string Truncate(string s, int n) => s.Length <= n ? s : s[..n] + "…";

    /// <summary>Estrae il primo oggetto JSON <c>{ ... }</c> da una risposta che può avere fence markdown o testo intorno.</summary>
    internal static string ExtractJsonObject(string s)
    {
        var start = s.IndexOf('{');
        var end = s.LastIndexOf('}');
        return start >= 0 && end > start ? s[start..(end + 1)] : s;
    }
}

/// <summary>Esito della classificazione di un vocale trascritto.</summary>
/// <param name="Type">Una fra: decisione, domanda, info, media, rumore.</param>
/// <param name="Summary">Sintesi in una frase; <c>null</c> per "rumore" o se assente.</param>
/// <param name="Uncertain">
/// <c>true</c> quando "media" è un ripiego perché la risposta del modello non era valida
/// (JSON malformato, troncato, o <c>type</c> fuori dalle categorie), non una vera classificazione.
/// </param>
public sealed record Classification(string Type, string? Summary, bool Uncertain = false);
