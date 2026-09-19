using System.Globalization;
using ComitatoFeste.Data;
using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;

const string DefaultGroup = "Comitato feste 87";
const string DefaultConnection = "Host=localhost;Port=5432;Database=postgres;Username=postgres;Password=postgres";

// --- parsing argomenti -----------------------------------------------------
var groupName = DefaultGroup;
var batchSize = 50;     // testi per richiesta a Gemini
// Pausa tra un batch e il successivo: i limiti del free tier per gli embedding non sono
// pubblicati (li mostra solo AI Studio), il retry su 429 assorbe gli sforamenti.
var delayMs = 500;
var limit = 0;          // 0 = nessun limite
var dryRun = false;
string? search = null;  // se valorizzato: non scrive nulla, stampa i punti più vicini alla domanda
var top = 10;

for (var i = 0; i < args.Length; i++)
{
    switch (args[i])
    {
        case "--group" when i + 1 < args.Length:
            groupName = args[++i];
            break;
        case "--batch-size" when i + 1 < args.Length:
            batchSize = int.Parse(args[++i], CultureInfo.InvariantCulture);
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
        case "--search" when i + 1 < args.Length:
            search = args[++i];
            break;
        case "--top" when i + 1 < args.Length:
            top = int.Parse(args[++i], CultureInfo.InvariantCulture);
            break;
        case "--help" or "-h":
            Console.WriteLine("uso: ComitatoFeste.Embedder [opzioni]");
            Console.WriteLine("  (senza opzioni)       embedda i punti nuovi o cambiati (idempotente: serve anche da backfill)");
            Console.WriteLine("  --group <nome>        gruppo WhatsApp (default: \"Comitato feste 87\")");
            Console.WriteLine("  --batch-size <n>      testi per richiesta a Gemini (default: 50)");
            Console.WriteLine("  --delay-ms <n>        pausa tra un batch e il successivo (default: 500)");
            Console.WriteLine("  --limit <n>           elabora al massimo n punti (default: tutti)");
            Console.WriteLine("  --dry-run             conta i punti da embeddare ma non chiama Gemini né scrive");
            Console.WriteLine("  --search \"<domanda>\"  non scrive nulla: stampa i punti semanticamente più vicini");
            Console.WriteLine("  --top <n>             quanti risultati con --search (default: 10)");
            return 0;
        default:
            Console.Error.WriteLine($"argomento non riconosciuto: {args[i]} (usa --help)");
            return 2;
    }
}

if (batchSize < 1)
{
    Console.Error.WriteLine("--batch-size deve essere almeno 1.");
    return 2;
}

// Chiave Gemini: prima l'env GEMINI_API_KEY, poi gemini.key.txt (in .gitignore) cercato
// risalendo dalla cartella corrente / dell'eseguibile fino alla radice del repo.
// In --dry-run non serve: non si chiama Gemini.
var geminiKey = GeminiKey.Resolve();
if (string.IsNullOrWhiteSpace(geminiKey) && !dryRun)
{
    Console.Error.WriteLine("chiave Gemini assente: imposta l'env GEMINI_API_KEY oppure crea gemini.key.txt nella radice del repo.");
    return 2;
}

var connection = Environment.GetEnvironmentVariable("COMITATOFESTE_CONNECTION") ?? DefaultConnection;
var options = new DbContextOptionsBuilder<ComitatoFesteDbContext>().UseComitatoFesteNpgsql(connection).Options;
await using var db = new ComitatoFesteDbContext(options);

if (!await db.Database.CanConnectAsync())
{
    Console.Error.WriteLine("impossibile connettersi al database (controlla COMITATOFESTE_CONNECTION).");
    return 3;
}
if ((await db.Database.GetPendingMigrationsAsync()).Any())
{
    Console.Error.WriteLine("il database ha migration non applicate: esegui 'dotnet ef database update'.");
    return 4;
}

// Ctrl+C interrompe in modo pulito dopo il batch in corso (il lavoro già salvato resta).
using var cts = new CancellationTokenSource();
Console.CancelKeyPress += (_, e) => { e.Cancel = true; cts.Cancel(); };

using var http = new HttpClient { Timeout = TimeSpan.FromMinutes(2) };

// --- modalità --search: prova del retrieval, non scrive nulla --------------
if (search is not null)
{
    var gemini = new GeminiEmbeddingClient(http, geminiKey!);
    var q = new Pgvector.Vector(await gemini.EmbedQueryAsync(search, cts.Token));

    // Distanza coseno di pgvector (<=>): 0 = identici, 2 = opposti. Stessi criteri della vista
    // "pulita": nessuna riga di rumore/vocale non digerito ha un embedding, ma un punto può
    // essere diventato rumore dopo essere stato embeddato, quindi si ricontrolla qui.
    var rows = await db.Database.SqlQuery<SearchRow>($"""
        SELECT p."OccurredAt" AS "OccurredAt", m."DisplayName" AS "Author", p."Type" AS "Type",
               p."Text" AS "Text", (e."Embedding" <=> {q}) AS "Distance"
        FROM "DigestPointEmbeddings" e
        JOIN "DigestPoints" p ON p."Id" = e."DigestPointId"
        JOIN "Members" m ON m."Id" = p."MemberId"
        JOIN "Groups" g ON g."Id" = p."GroupId"
        WHERE g."Name" = {groupName} AND p."Type" <> 'rumore'
        ORDER BY e."Embedding" <=> {q}
        LIMIT {top}
        """).ToListAsync(cts.Token);

    Console.WriteLine($"domanda: {search}");
    Console.WriteLine($"{rows.Count} risultati (distanza coseno, più bassa = più vicino):");
    foreach (var r in rows)
    {
        var local = TimeZoneInfo.ConvertTime(r.OccurredAt, RomeTime.Zone);
        Console.WriteLine($"  {r.Distance:0.000}  {local:MM-dd HH:mm}  {r.Author} [{r.Type}] {r.Text}");
    }
    return 0;
}

// --- modalità normale: embedda i punti nuovi o cambiati ---------------------
// Stessi criteri della vista "pulita" del controller (DigestPointsController.CleanViewQuery):
// niente rumore, niente vocali non ancora digeriti dal Transcriber. Va eseguito DOPO il
// Transcriber, perché quest'ultimo riscrive il testo dei vocali.
var candidates = await (
        from p in db.DigestPoints
        where p.Group.Name == groupName
              && p.Type != DigestPointType.Rumore
              && (p.MediaAsset == null
                  || p.MediaAsset.MediaType != MediaType.Audio
                  || p.MediaAsset.TranscribedAt != null)
        join e in db.DigestPointEmbeddings on p.Id equals e.DigestPointId into g
        from e in g.DefaultIfEmpty()
        orderby p.OccurredAt, p.Id
        select new
        {
            p.Id,
            Author = p.Member.DisplayName,
            p.Text,
            EmbeddedModel = e == null ? null : e.Model,
            EmbeddedHash = e == null ? null : e.InputSha256,
        })
    .ToListAsync(cts.Token);

// Da (ri)calcolare: mai embeddati, oppure embeddati con un altro modello, oppure il cui input
// (testo o formato) è cambiato da allora — l'hash lo intercetta senza ricalcolare il resto.
var pending = candidates
    .Select(c =>
    {
        var input = GeminiEmbeddingClient.DocumentInput(c.Author, c.Text);
        return new { c.Id, Input = input, Hash = GeminiEmbeddingClient.Hash(input), c.EmbeddedModel, c.EmbeddedHash };
    })
    .Where(c => c.EmbeddedModel != GeminiEmbeddingClient.Model || c.EmbeddedHash != c.Hash)
    .ToList();

if (limit > 0)
    pending = pending.Take(limit).ToList();

Console.WriteLine($"{candidates.Count} punti nella vista pulita, {pending.Count} da embeddare{(dryRun ? " (dry-run, niente chiamate né scritture)" : "")}.");
Console.WriteLine($"modello: {GeminiEmbeddingClient.Model}, {GeminiEmbeddingClient.Dimensions} dimensioni, batch da {batchSize}.");

if (dryRun || pending.Count == 0)
    return 0;

var client = new GeminiEmbeddingClient(http, geminiKey!);
var done = 0;

try
{
    foreach (var batch in pending.Chunk(batchSize))
    {
        cts.Token.ThrowIfCancellationRequested();

        var vectors = await client.EmbedBatchAsync(batch.Select(b => b.Input).ToList(), cts.Token);

        // Upsert: le righe già presenti (modello o testo cambiati) si aggiornano, le altre si aggiungono.
        var ids = batch.Select(b => b.Id).ToList();
        var existing = await db.DigestPointEmbeddings
            .Where(e => ids.Contains(e.DigestPointId))
            .ToDictionaryAsync(e => e.DigestPointId, cts.Token);

        var now = DateTimeOffset.UtcNow;
        for (var i = 0; i < batch.Length; i++)
        {
            if (!existing.TryGetValue(batch[i].Id, out var row))
            {
                row = new DigestPointEmbedding { DigestPointId = batch[i].Id };
                db.DigestPointEmbeddings.Add(row);
            }

            row.Embedding = vectors[i];
            row.Model = GeminiEmbeddingClient.Model;
            row.InputSha256 = batch[i].Hash;
            row.EmbeddedAt = now;
        }

        await db.SaveChangesAsync(cts.Token);
        done += batch.Length;
        Console.WriteLine($"  {done}/{pending.Count}");

        if (delayMs > 0 && done < pending.Count)
            await Task.Delay(delayMs, cts.Token);
    }
}
catch (OperationCanceledException)
{
    Console.WriteLine($"interrotto: {done}/{pending.Count} salvati (i batch già scritti restano).");
    return 130;
}
catch (InvalidOperationException ex)
{
    Console.Error.WriteLine($"errore: {ex.Message}");
    Console.Error.WriteLine($"salvati {done}/{pending.Count}: rilancia per riprendere dai rimanenti.");
    return 1;
}

Console.WriteLine($"fatto: {done} punti embeddati.");
return 0;

// Riga del risultato di --search (colonne mappate per nome da SqlQuery).
internal sealed class SearchRow
{
    public DateTimeOffset OccurredAt { get; set; }
    public string Author { get; set; } = null!;
    public string Type { get; set; } = null!;
    public string Text { get; set; } = null!;
    public double Distance { get; set; }
}
