using System.Globalization;
using ComitatoFeste.Data;
using ComitatoFeste.Domain;
using ComitatoFeste.Transcriber;
using Microsoft.EntityFrameworkCore;

const string DefaultGroup = "Comitato feste 87";
const string DefaultConnection = "Host=localhost;Port=5432;Database=postgres;Username=postgres;Password=postgres";

// --- parsing argomenti -----------------------------------------------------
var groupName = DefaultGroup;
// Pausa tra un vocale e il successivo, per restare sotto i limiti/minuto del tier gratuito
// (whisper-large-v3 20 req/min, gpt-oss-120b 8.000 token/min). Il retry con backoff assorbe
// comunque gli sforamenti occasionali; alzalo con --delay-ms se vedi troppi 429.
var delayMs = 6000;
var limit = 0;          // 0 = nessun limite
var dryRun = false;

for (var i = 0; i < args.Length; i++)
{
    switch (args[i])
    {
        case "--group" when i + 1 < args.Length:
            groupName = args[++i];
            break;
        case "--delay-ms" when i + 1 < args.Length:
            delayMs = int.Parse(args[++i], CultureInfo.InvariantCulture);
            break;
        case "--limit" when i + 1 < args.Length:
            limit = int.Parse(args[++i], CultureInfo.InvariantCulture);
            break;
        case "--dry-run":
            dryRun = true;
            break;
        case "--help" or "-h":
            Console.WriteLine("uso: ComitatoFeste.Transcriber [opzioni]");
            Console.WriteLine("  --group <nome>   gruppo WhatsApp (default: \"Comitato feste 87\")");
            Console.WriteLine("  --delay-ms <n>   pausa tra un vocale e il successivo (default: 6000)");
            Console.WriteLine("  --limit <n>      elabora al massimo n vocali (default: tutti)");
            Console.WriteLine("  --dry-run        trascrive/classifica ma non scrive su DB");
            return 0;
        default:
            Console.Error.WriteLine($"argomento non riconosciuto: {args[i]} (usa --help)");
            return 2;
    }
}

// Chiave Groq: prima l'env GROQ_API_KEY, poi un file key.txt (in .gitignore) cercato
// risalendo dalla cartella corrente / dell'eseguibile fino alla radice del repo.
var groqKey = GroqKey.Resolve();

if (string.IsNullOrWhiteSpace(groqKey))
{
    Console.Error.WriteLine("chiave Groq assente: imposta l'env GROQ_API_KEY oppure crea C:\\ComitatoFeste\\key.txt (chiave gratuita su https://console.groq.com/keys).");
    return 2;
}

var connection = Environment.GetEnvironmentVariable("COMITATOFESTE_CONNECTION") ?? DefaultConnection;
var options = new DbContextOptionsBuilder<ComitatoFesteDbContext>().UseNpgsql(connection).Options;
await using var db = new ComitatoFesteDbContext(options);

if (!await db.Database.CanConnectAsync())
{
    Console.Error.WriteLine($"impossibile connettersi al database ({connection}).");
    return 3;
}
if ((await db.Database.GetPendingMigrationsAsync()).Any())
{
    Console.Error.WriteLine("il database ha migration non applicate: esegui 'dotnet ef database update'.");
    return 4;
}

// Ctrl+C interrompe in modo pulito dopo il vocale in corso (il lavoro già salvato resta).
using var cts = new CancellationTokenSource();
Console.CancelKeyPress += (_, e) => { e.Cancel = true; cts.Cancel(); };

using var http = new HttpClient { Timeout = TimeSpan.FromMinutes(3) };
var groq = new GroqClient(http, groqKey);

// Vocali da lavorare, in ordine cronologico: mai trascritti (TranscriptionText == null)
// oppure trascritti ma con classificazione rimasta incerta (TranscribedAt == null → in quel
// caso si ritenta SOLO la classificazione, la trascrizione è già a DB). I byte si caricano
// uno alla volta nel loop, per non tenere in RAM tutti i blob insieme.
var query = db.MediaAssets
    .Where(a => a.MediaType == MediaType.Audio && (a.TranscriptionText == null || a.TranscribedAt == null))
    .Where(a => a.DigestPoint.Group.Name == groupName)
    .OrderBy(a => a.DigestPoint.OccurredAt)
    .Select(a => new { Asset = a, a.DigestPoint, Author = a.DigestPoint.Member.DisplayName });

var pending = limit > 0
    ? await query.Take(limit).ToListAsync(cts.Token)
    : await query.ToListAsync(cts.Token);

Console.WriteLine($"{pending.Count} vocali da trascrivere{(dryRun ? " (dry-run, niente scritture)" : "")}.");

int ok = 0, uncertain = 0, skipped = 0, errors = 0;
var byType = new Dictionary<string, int>();

foreach (var row in pending)
{
    if (cts.IsCancellationRequested)
        break;

    var asset = row.Asset;
    var point = row.DigestPoint;
    var author = row.Author;
    var reused = !string.IsNullOrWhiteSpace(asset.TranscriptionText);
    Console.Write($"[{point.OccurredAt:HH:mm}] {author} ({asset.FileName}){(reused ? " [ri-classifico]" : "")} ... ");

    try
    {
        // Trascrizione già fatta in un run precedente (classificazione era incerta) → la riuso
        // e ritento solo la classificazione, senza ri-pagare Whisper.
        string transcript;
        if (reused)
        {
            transcript = asset.TranscriptionText!;
        }
        else
        {
            var blob = await db.MediaBlobs
                .Where(b => b.MediaAssetId == asset.Id)
                .Select(b => new { b.Content, b.ContentType })
                .FirstOrDefaultAsync(cts.Token);

            if (blob is null)
            {
                skipped++;
                Console.WriteLine("SALTATO (nessun contenuto binario).");
                continue;
            }

            transcript = await groq.TranscribeAsync(blob.Content, asset.FileName, blob.ContentType, cts.Token);
        }

        var classification = await groq.ClassifyAsync(groupName, author, transcript, cts.Token);

        var bucket = classification.Uncertain ? $"{classification.Type} (incerto)" : classification.Type;
        Console.WriteLine($"[{bucket}] \"{Trunc(transcript, 60)}\"");
        byType[bucket] = byType.GetValueOrDefault(bucket) + 1;

        if (classification.Uncertain)
            uncertain++;
        else
            ok++;

        if (!dryRun)
        {
            // La trascrizione la salviamo sempre: Whisper si paga una volta sola.
            asset.TranscriptionText = transcript;

            if (classification.Uncertain)
            {
                // Classificazione non attendibile: TranscribedAt resta null → il punto è
                // nascosto dalla GUI e il prossimo run ne ritenta solo la classificazione.
                asset.TranscribedAt = null;
            }
            else
            {
                asset.TranscribedAt = DateTimeOffset.UtcNow;

                if (Enum.TryParse<DigestPointType>(classification.Type, ignoreCase: true, out var newType))
                    point.Type = newType;

                point.Text = classification.Type == "rumore"
                    ? $"Vocale di {author} — rumore/reazione, non significativo."
                    : !string.IsNullOrWhiteSpace(classification.Summary)
                        ? classification.Summary!
                        : transcript;
            }

            await db.SaveChangesAsync(cts.Token);
        }
    }
    catch (OperationCanceledException)
    {
        Console.WriteLine("INTERROTTO.");
        break;
    }
    catch (Exception ex)
    {
        errors++;
        Console.WriteLine($"ERRORE: {ex.Message}");
    }

    try
    {
        await Task.Delay(delayMs, cts.Token);
    }
    catch (OperationCanceledException)
    {
        break;
    }
}

Console.WriteLine($"\n== completato: {ok} trascritti/classificati, {uncertain} incerti (non salvati, da ritentare), {skipped} saltati, {errors} errori ==");
foreach (var (t, n) in byType.OrderByDescending(kv => kv.Value))
    Console.WriteLine($"  {t}: {n}");

return errors > 0 ? 1 : 0;

static string Trunc(string s, int n) => s.Length <= n ? s : s[..n] + "…";
