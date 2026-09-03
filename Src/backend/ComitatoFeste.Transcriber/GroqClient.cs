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
    // Modelli scelti per il tier gratuito Groq (limiti indicativi 2026, quelli reali sono su
    // https://console.groq.com/settings/limits):
    //   whisper-large-v3   : 2.000 richieste/g, 20/min, 7.200 s audio/ora. Preferito al -turbo
    //     (stessi limiti free) perché su italiano + dialetto marchigiano/abruzzese e audio
    //     WhatsApp rumoroso il decoder pieno sbaglia meno; la velocità di turbo qui non serve,
    //     il ritmo lo detta comunque --delay-ms.
    //   openai/gpt-oss-120b : 1.000 richieste/g, 200k token/g, 30/min, 8.000 token/min —
    //     stessi identici limiti free di gpt-oss-20b ma contatore RPD/TPD SEPARATO per modello,
    //     e classificazione più accurata (meno confusione rumore/info). Rimpiazzo Groq dei
    //     llama-3.x (deprecati giu 2026). Rispetta male response_format json_object: vedi
    //     ParseClassification. Ogni risposta è un po' più pesante del 20b → il freno TPM
    //     adattivo qui sotto serve davvero.
    // Verifica su https://console.groq.com/docs/models che i nomi siano ancora correnti.
    private const string WhisperModel = "whisper-large-v3";
    private const string ClassifierModel = "openai/gpt-oss-120b";

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
            form.Add(new StringContent(WhisperModel), "model");
            form.Add(new StringContent("it"), "language");
            form.Add(new StringContent("json"), "response_format");
            return new HttpRequestMessage(HttpMethod.Post, TranscriptionsUrl) { Content = form };
        }, "Whisper", ct);

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

        var payload = new
        {
            model = ClassifierModel,
            temperature = 0,
            // gpt-oss è un modello "reasoning": senza questo emette una lunga catena di
            // ragionamento che gonfia i token/minuto ~10x (il classificatore serve solo una
            // riga di JSON). "low" tiene il grosso; il cap è solo una rete di sicurezza contro
            // le derive — se fosse troppo stretto troncherebbe il JSON prima che venga emesso.
            reasoning_effort = "low",
            max_completion_tokens = 512,
            response_format = new { type = "json_object" },
            messages = new[] { new { role = "user", content = prompt } },
        };

        var json = JsonSerializer.Serialize(payload);

        // gpt-oss ogni tanto risponde con JSON malformato / incorniciato / troncato: ri-chiediamo
        // fino a ClassifyAttempts volte prima di rassegnarci a un esito "incerto".
        Classification last = new("media", null, Uncertain: true);
        for (var attempt = 1; attempt <= ClassifyAttempts; attempt++)
        {
            await WaitForClassifierTokenBudgetAsync(ct);

            var body = await SendWithRetryAsync(() => new HttpRequestMessage(HttpMethod.Post, ChatCompletionsUrl)
            {
                Content = new StringContent(json, Encoding.UTF8, "application/json"),
            }, "classificazione", ct);

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

    private async Task<string> SendWithRetryAsync(Func<HttpRequestMessage> build, string label, CancellationToken ct)
    {
        for (var attempt = 1; ; attempt++)
        {
            using var req = build();
            using var resp = await _http.SendAsync(req, ct);
            var body = await resp.Content.ReadAsStringAsync(ct);

            if (resp.IsSuccessStatusCode)
                return body;

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
