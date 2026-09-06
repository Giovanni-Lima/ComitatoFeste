using ComitatoFeste.Data;
using ComitatoFeste.Importer;
using Microsoft.EntityFrameworkCore;

const string DefaultGroup = "Comitato feste 87";
const string DefaultExportRoot = @"C:\ComitatoFeste\Export";
const string DefaultConnection = "Host=localhost;Port=5432;Database=postgres;Username=postgres;Password=postgres";

// --- parsing argomenti -------------------------------------------------------
string? target = null;          // file .json specifico oppure data yyyy-MM-dd
var groupName = DefaultGroup;
var exportRoot = DefaultExportRoot;
var fuzzy = true;
var fuzzyThreshold = 0.6;
var fuzzyWindowMin = 2.0;
var photosOnly = false;

for (var i = 0; i < args.Length; i++)
{
    switch (args[i])
    {
        case "--group" when i + 1 < args.Length:
            groupName = args[++i];
            break;
        case "--export-root" when i + 1 < args.Length:
            exportRoot = args[++i];
            break;
        case "--no-fuzzy":
            fuzzy = false;
            break;
        case "--photos-only":
            photosOnly = true;
            break;
        case "--fuzzy-threshold" when i + 1 < args.Length:
            fuzzyThreshold = double.Parse(args[++i], System.Globalization.CultureInfo.InvariantCulture);
            break;
        case "--fuzzy-window-min" when i + 1 < args.Length:
            fuzzyWindowMin = double.Parse(args[++i], System.Globalization.CultureInfo.InvariantCulture);
            break;
        case "--help" or "-h":
            Console.WriteLine("uso: ComitatoFeste.Importer [<file.json | yyyy-MM-dd>] [opzioni]");
            Console.WriteLine("  --group <nome>            gruppo WhatsApp (default: \"Comitato feste 87\")");
            Console.WriteLine("  --export-root <dir>      cartella Export (default: C:\\ComitatoFeste\\Export)");
            Console.WriteLine("  --no-fuzzy               disattiva il dedup fuzzy pg_trgm");
            Console.WriteLine("  --fuzzy-threshold <0..1> soglia similarity() (default: 0.6)");
            Console.WriteLine("  --fuzzy-window-min <n>   finestra ± minuti per il confronto (default: 2)");
            Console.WriteLine("  --photos-only            salta l'import dei digest, sincronizza solo Export/profili/");
            Console.WriteLine("  nota: un reimport della stessa giornata è idempotente (media dedup per nome");
            Console.WriteLine("        file, testo per match esatto/fuzzy). Resta a rischio solo un punto di");
            Console.WriteLine("        solo testo riformulato sotto la soglia fuzzy tra un import e l'altro.");
            Console.WriteLine("  senza target importa tutti i digest_*.json della cartella Export.");
            return 0;
        default:
            target ??= args[i];
            break;
    }
}

if (!Directory.Exists(exportRoot))
{
    Console.Error.WriteLine($"cartella Export non trovata: {exportRoot}");
    return 2;
}

var connection = Environment.GetEnvironmentVariable("COMITATOFESTE_CONNECTION") ?? DefaultConnection;
var options = new DbContextOptionsBuilder<ComitatoFesteDbContext>()
    .UseNpgsql(connection)
    .Options;

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

var importer = new DigestImporter(db, exportRoot, new ImportOptions
{
    FuzzyDedup = fuzzy,
    FuzzyThreshold = fuzzyThreshold,
    FuzzyWindow = TimeSpan.FromMinutes(fuzzyWindowMin),
});

// --- import digest (saltato con --photos-only) ----------------------------
if (!photosOnly)
{
// --- risoluzione del target ------------------------------------------------
List<string> files;
if (target is null)
{
    files = Directory.EnumerateFiles(exportRoot, "digest_*.json").OrderBy(f => f, StringComparer.Ordinal).ToList();
}
else if (File.Exists(target))
{
    files = new List<string> { target };
}
else if (File.Exists(Path.Combine(exportRoot, target)))
{
    files = new List<string> { Path.Combine(exportRoot, target) };
}
else
{
    var byDate = Path.Combine(exportRoot, $"digest_{target}.json");
    if (!File.Exists(byDate))
    {
        Console.Error.WriteLine($"target non trovato: '{target}' (né file, né digest_{target}.json)");
        return 2;
    }
    files = new List<string> { byDate };
}

if (files.Count == 0)
{
    Console.WriteLine("nessun file digest_*.json da importare.");
    return 0;
}

// --- import ---------------------------------------------------------------
Console.WriteLine(fuzzy
    ? $"dedup fuzzy: ON (soglia {fuzzyThreshold:0.00}, finestra ±{fuzzyWindowMin:0.#} min)"
    : "dedup fuzzy: OFF");

int totInserted = 0, totDup = 0, totFuzzy = 0, totMediaDup = 0, totMedia = 0, totMissing = 0, totMembers = 0;

foreach (var file in files)
{
    var r = await importer.ImportFileAsync(file, groupName);

    var runLabel = r.RunId == 0 ? "(nessun nuovo punto, run non creato)" : $"IngestionRun #{r.RunId}";
    Console.WriteLine($"\n{r.SourceFile}  ->  {runLabel}");
    Console.WriteLine($"  entry lette .......... {r.EntriesRead}");
    Console.WriteLine($"  punti inseriti ....... {r.PointsInserted}");
    Console.WriteLine($"  duplicati esatti ..... {r.DuplicatesSkipped}");
    Console.WriteLine($"  duplicati fuzzy ...... {r.FuzzyDuplicatesSkipped}");
    Console.WriteLine($"  duplicati media ...... {r.MediaDuplicatesSkipped}");
    Console.WriteLine($"  membri creati ........ {r.MembersCreated}");
    Console.WriteLine($"  media salvati ........ {r.MediaStored}");
    Console.WriteLine($"  media mancanti ....... {r.MediaFilesMissing}");
    foreach (var w in r.Warnings)
        Console.WriteLine($"  ! {w}");

    totInserted += r.PointsInserted;
    totDup += r.DuplicatesSkipped;
    totFuzzy += r.FuzzyDuplicatesSkipped;
    totMediaDup += r.MediaDuplicatesSkipped;
    totMedia += r.MediaStored;
    totMissing += r.MediaFilesMissing;
    totMembers += r.MembersCreated;
}

Console.WriteLine($"\n== totale: {files.Count} file, {totInserted} punti, " +
                  $"{totDup} dup esatti, {totFuzzy} dup fuzzy, {totMediaDup} dup media, " +
                  $"{totMembers} membri, {totMedia} media ({totMissing} mancanti) ==");
}

// --- foto profilo ------------------------------------------------------------
var photos = await importer.ImportProfilePhotosAsync(groupName);
Console.WriteLine($"\nfoto profilo (Export/profili/):");
Console.WriteLine($"  aggiunte ............. {photos.Added}");
Console.WriteLine($"  aggiornate .......... {photos.Updated}");
Console.WriteLine($"  invariate ........... {photos.Unchanged}");
if (photos.MembersWithoutPhoto.Count > 0)
    Console.WriteLine($"  membri senza foto ... {string.Join(", ", photos.MembersWithoutPhoto)}");
if (photos.UnmatchedFiles.Count > 0)
    Console.WriteLine($"  file senza membro ... {string.Join(", ", photos.UnmatchedFiles)}");
foreach (var w in photos.Warnings)
    Console.WriteLine($"  ! {w}");

return 0;
