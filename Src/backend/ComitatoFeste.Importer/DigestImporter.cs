using System.Globalization;
using System.Security.Cryptography;
using System.Text.Json;
using ComitatoFeste.Data;
using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;

namespace ComitatoFeste.Importer;

/// <summary>
/// Legge i file <c>digest_&lt;data&gt;.json</c> dalla cartella Export e li persiste:
/// get-or-create <see cref="Group"/> e <see cref="Member"/>, un <see cref="IngestionRun"/> per file,
/// un <see cref="DigestPoint"/> per entry, con <see cref="MediaAsset"/>+<see cref="MediaBlob"/> se c'è un file.
/// Dedup a più livelli, così un reimport di una giornata non ancora "chiusa" resta idempotente:
/// <list type="bullet">
///   <item>identità media: entry con un <c>file</c> già presente nella finestra per lo stesso autore →
///     è lo stesso messaggio anche se il Transcriber ne ha riscritto il <c>Text</c>;</item>
///   <item>esatto sul vincolo (GroupId, MemberId, OccurredAt, Text) contro i rerun letterali;</item>
///   <item>fuzzy pg_trgm su <c>Text</c> per le riformulazioni tra run diversi.</item>
/// </list>
/// </summary>
public sealed class DigestImporter
{
    private static readonly JsonSerializerOptions JsonOptions = new() { PropertyNameCaseInsensitive = true };

    private static readonly HashSet<string> ImageExtensions =
        new(StringComparer.OrdinalIgnoreCase) { ".jpg", ".jpeg", ".png", ".webp", ".gif" };

    private readonly ComitatoFesteDbContext _db;
    private readonly string _exportRoot;
    private readonly ImportOptions _options;
    private readonly IBlobStore? _store;

    /// <param name="store">Object storage R2 per i byte dei file; <c>null</c> = restano in Postgres.</param>
    public DigestImporter(ComitatoFesteDbContext db, string exportRoot, ImportOptions? options = null, IBlobStore? store = null)
    {
        _db = db;
        _exportRoot = exportRoot;
        _options = options ?? new ImportOptions();
        _store = store;
    }

    /// <summary>
    /// Sposta su R2 i byte dei blob appena inseriti e azzera <c>Content</c> a DB. Eseguito
    /// **dopo** il salvataggio perché la chiave contiene l'id del <see cref="MediaAsset"/>. Se
    /// l'upload fallisce (o il processo muore a metà) i byte restano in Postgres, che è il
    /// fallback: nulla si perde, e verranno spostati da un successivo run di backfill.
    /// </summary>
    private async Task OffloadBlobsAsync(IReadOnlyList<MediaBlob> blobs, ImportResult result, CancellationToken ct)
    {
        if (_store is null || blobs.Count == 0) return;

        var moved = 0;
        foreach (var blob in blobs)
        {
            if (blob.Content is null || blob.Sha256 is null) continue;
            try
            {
                await _store.PutAsync(BlobKeys.Media(blob.MediaAssetId, blob.Sha256), blob.Content, blob.ContentType, ct);
                blob.Content = null;
                moved++;
            }
            catch (Exception ex) when (!ct.IsCancellationRequested)
            {
                result.Warnings.Add($"upload R2 fallito per media {blob.MediaAssetId} (resta in DB): {ex.Message}");
            }
        }
        if (moved > 0) await _db.SaveChangesAsync(ct);
    }

    /// <summary>Importa tutti i <c>digest_*.json</c> presenti nella cartella Export, in ordine di nome.</summary>
    public async Task<List<ImportResult>> ImportAllAsync(string groupName, CancellationToken ct = default)
    {
        var files = Directory.EnumerateFiles(_exportRoot, "digest_*.json")
            .OrderBy(f => f, StringComparer.Ordinal)
            .ToList();

        var results = new List<ImportResult>();
        foreach (var file in files)
            results.Add(await ImportFileAsync(file, groupName, ct));

        return results;
    }

    /// <summary>
    /// Sincronizza le foto profilo dei membri del gruppo da <c>Export/profili/&lt;Nome&gt;.jpg</c>
    /// (gli spazi del <c>DisplayName</c> diventano trattini nel nome file, confronto case-insensitive).
    /// Idempotente: aggiorna una foto solo se il contenuto è cambiato (SHA-256). Da chiamare dopo l'import dei digest.
    /// </summary>
    public async Task<ProfilePhotoImportResult> ImportProfilePhotosAsync(string groupName, CancellationToken ct = default)
    {
        var result = new ProfilePhotoImportResult();

        var dir = Path.Combine(_exportRoot, "profili");
        if (!Directory.Exists(dir))
        {
            result.Warnings.Add($"cartella non trovata: {dir}");
            return result;
        }

        // nome-file (senza estensione, trattini -> spazi) -> percorso
        var byName = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        foreach (var f in Directory.EnumerateFiles(dir))
        {
            if (!ImageExtensions.Contains(Path.GetExtension(f))) continue;
            byName[Path.GetFileNameWithoutExtension(f).Replace('-', ' ').Trim()] = f;
        }

        var group = await _db.Groups.FirstOrDefaultAsync(g => g.Name == groupName, ct);
        if (group is null)
        {
            result.Warnings.Add($"gruppo '{groupName}' non presente: importa prima i digest");
            return result;
        }

        var members = await _db.Members
            .Where(m => m.GroupId == group.Id)
            .Select(m => new { m.Id, m.DisplayName, Sha = m.ProfilePhoto == null ? null : m.ProfilePhoto.Sha256 })
            .ToListAsync(ct);

        var matched = new HashSet<string>(StringComparer.OrdinalIgnoreCase);

        foreach (var m in members)
        {
            if (!byName.TryGetValue(m.DisplayName, out var path))
            {
                result.MembersWithoutPhoto.Add(m.DisplayName);
                continue;
            }
            matched.Add(path);

            var bytes = await File.ReadAllBytesAsync(path, ct);
            var sha = Convert.ToHexString(SHA256.HashData(bytes)).ToLowerInvariant();
            if (string.Equals(m.Sha, sha, StringComparison.OrdinalIgnoreCase))
            {
                result.Unchanged++;
                continue;
            }

            var (_, mime) = MediaKind.Resolve(path);

            // Con R2 i byte vanno lì (chiave con SHA → immutabile) e a DB resta solo Content = null.
            // Se l'upload fallisce si ripiega sui byte in Postgres.
            byte[]? dbContent = bytes;
            if (_store is not null)
            {
                try
                {
                    await _store.PutAsync(BlobKeys.MemberPhoto(m.Id, sha), bytes, mime, ct);
                    dbContent = null;
                }
                catch (Exception ex) when (!ct.IsCancellationRequested)
                {
                    result.Warnings.Add($"upload R2 fallito per foto di {m.DisplayName} (resta in DB): {ex.Message}");
                }
            }

            var existing = await _db.MemberProfilePhotos.FirstOrDefaultAsync(p => p.MemberId == m.Id, ct);
            if (existing is null)
            {
                _db.MemberProfilePhotos.Add(new MemberProfilePhoto
                {
                    MemberId = m.Id,
                    Content = dbContent,
                    ContentType = mime,
                    Sha256 = sha,
                });
                result.Added++;
            }
            else
            {
                existing.Content = dbContent;
                existing.ContentType = mime;
                existing.Sha256 = sha;
                result.Updated++;
            }
        }

        foreach (var path in byName.Values)
            if (!matched.Contains(path))
                result.UnmatchedFiles.Add(Path.GetFileName(path));

        await _db.SaveChangesAsync(ct);
        return result;
    }

    public async Task<ImportResult> ImportFileAsync(string jsonPath, string groupName, CancellationToken ct = default)
    {
        var result = new ImportResult { SourceFile = Path.GetFileName(jsonPath) };
        var newBlobs = new List<MediaBlob>();

        await using var stream = File.OpenRead(jsonPath);
        var entries = await JsonSerializer.DeserializeAsync<List<DigestEntry>>(stream, JsonOptions, ct)
                      ?? new List<DigestEntry>();
        result.EntriesRead = entries.Count;
        if (entries.Count == 0)
        {
            result.Warnings.Add("nessuna entry nel file");
            return result;
        }

        var group = await _db.Groups.FirstOrDefaultAsync(g => g.Name == groupName, ct);
        if (group is null)
        {
            group = new Group { Name = groupName };
            _db.Groups.Add(group);
        }

        // Finestra del run: dal minimo al massimo istante delle entry (estremo superiore esclusivo di 1s).
        var occurrences = entries.Select(e => ToOccurredAt(e)).ToList();
        var windowStart = occurrences.Min();
        var windowEnd = occurrences.Max().AddSeconds(1);

        var run = new IngestionRun
        {
            Group = group,
            WindowStart = windowStart,
            WindowEnd = windowEnd,
            StartedAt = DateTimeOffset.UtcNow,
            SourceFile = result.SourceFile,
        };
        _db.IngestionRuns.Add(run);

        // Cache membri del gruppo per DisplayName.
        var members = group.Id == 0
            ? new Dictionary<string, Member>(StringComparer.Ordinal)
            : await _db.Members
                .Where(m => m.GroupId == group.Id)
                .ToDictionaryAsync(m => m.DisplayName, m => m, StringComparer.Ordinal, ct);

        // Chiavi di dedup già presenti a DB per la finestra di questo file.
        var existingKeys = new HashSet<(string Author, DateTimeOffset At, string Text)>();
        if (group.Id != 0)
        {
            var rows = await _db.DigestPoints
                .Where(d => d.GroupId == group.Id && d.OccurredAt >= windowStart && d.OccurredAt < windowEnd)
                .Select(d => new { d.Member.DisplayName, d.OccurredAt, d.Text })
                .ToListAsync(ct);
            foreach (var r in rows)
                existingKeys.Add((r.DisplayName, r.OccurredAt, r.Text));
        }

        // Identità media già a DB nella finestra: (Autore, NomeFile). Un'entry che riporta un file
        // già presente è lo stesso messaggio anche se il Transcriber ne ha nel frattempo riscritto
        // il Text (placeholder "non trascritto" -> sintesi), caso in cui il match esatto/fuzzy sul
        // Text non lo riconoscerebbe più. Il nome file è "HHMM_Autore_descrizione.ext": stabile e
        // di fatto unico nel giorno. Nota: al PRIMO import di due vocali diversi dello stesso
        // autore nello stesso minuto questo livello non basta (i file non sono ancora a DB) — a
        // tenerli distinti è il placeholder disambiguato dal generatore del digest ("... (2)"),
        // altrimenti collassano sul vincolo UNIQUE (vedi docs/CONTEXT.md, dati del 10/9/2026).
        var existingMedia = new HashSet<(string Author, string FileName)>();
        if (group.Id != 0)
        {
            var mrows = await _db.MediaAssets
                .Where(a => a.DigestPoint.GroupId == group.Id
                            && a.DigestPoint.OccurredAt >= windowStart
                            && a.DigestPoint.OccurredAt < windowEnd)
                .Select(a => new { a.DigestPoint.Member.DisplayName, a.FileName })
                .ToListAsync(ct);
            foreach (var m in mrows)
                existingMedia.Add((m.DisplayName, m.FileName));
        }

        for (var i = 0; i < entries.Count; i++)
        {
            var entry = entries[i];
            var author = entry.Author.Trim();
            var text = entry.Text.Trim();
            var occurredAt = occurrences[i];

            if (!Enum.TryParse<DigestPointType>(entry.Type, ignoreCase: true, out var type))
            {
                result.Warnings.Add($"entry #{i} scartata: type sconosciuto '{entry.Type}'");
                continue;
            }

            // Dedup livello 0 — identità del media: se il file è già nella finestra per questo
            // autore, salta. .Add restituisce false se già presente e "prenota" il file quando è
            // nuovo, così una seconda entry con lo stesso file nello stesso run non lo duplica.
            if (!string.IsNullOrWhiteSpace(entry.File)
                && !existingMedia.Add((author, entry.File)))
            {
                result.MediaDuplicatesSkipped++;
                continue;
            }

            var key = (author, occurredAt, text);
            if (!existingKeys.Add(key))
            {
                result.DuplicatesSkipped++;
                continue;
            }

            if (!members.TryGetValue(author, out var member))
            {
                member = new Member { Group = group, DisplayName = author };
                _db.Members.Add(member);
                members[author] = member;
                result.MembersCreated++;
            }

            // Dedup livello 2 — fuzzy pg_trgm: riconosce le riformulazioni tra run diversi.
            // Solo contro punti già persistiti dello stesso membro, entro la finestra temporale:
            // così due vocali diversi dello stesso autore a distanza di minuti restano distinti.
            // Escludiamo i placeholder "vocale non trascritto (m:ss)": sono testi a modello, il
            // trigram li rende tutti simili tra loro e collasserebbe vocali diversi dello stesso
            // minuto (vedi docs/CONTEXT.md, caso falsi positivi). Per quelli vale solo il match
            // esatto, o in futuro il dedup sul SHA-256 del media.
            if (_options.FuzzyDedup && group.Id != 0 && member.Id != 0 && !IsUntranscribedPlaceholder(text))
            {
                var lo = occurredAt - _options.FuzzyWindow;
                var hi = occurredAt + _options.FuzzyWindow;
                var match = await _db.DigestPoints
                    .Where(d => d.MemberId == member.Id
                                && d.OccurredAt >= lo && d.OccurredAt <= hi
                                && EF.Functions.TrigramsSimilarity(d.Text, text) >= _options.FuzzyThreshold)
                    .OrderByDescending(d => EF.Functions.TrigramsSimilarity(d.Text, text))
                    .Select(d => new { d.Id, d.Text, Score = EF.Functions.TrigramsSimilarity(d.Text, text) })
                    .FirstOrDefaultAsync(ct);

                if (match is not null)
                {
                    result.FuzzyDuplicatesSkipped++;
                    result.Warnings.Add(
                        $"fuzzy-dup ({match.Score:0.00}) entry #{i} \"{Trim(text)}\" ~ punto #{match.Id} \"{Trim(match.Text)}\"");
                    continue;
                }
            }

            var point = new DigestPoint
            {
                IngestionRun = run,
                Group = group,
                Member = member,
                OccurredAt = occurredAt,
                Type = type,
                Text = text,
            };
            _db.DigestPoints.Add(point);
            result.PointsInserted++;

            if (!string.IsNullOrWhiteSpace(entry.File))
            {
                var (mediaType, mime) = MediaKind.Resolve(entry.File);
                var relPath = $"{entry.Date}/{entry.File}";
                var fullPath = Path.Combine(_exportRoot, entry.Date, entry.File);

                var asset = new MediaAsset
                {
                    DigestPoint = point,
                    MediaType = mediaType,
                    FileName = entry.File,
                    StoragePath = relPath,
                };
                point.MediaAsset = asset;

                if (File.Exists(fullPath))
                {
                    var bytes = await File.ReadAllBytesAsync(fullPath, ct);
                    asset.SizeBytes = bytes.LongLength;
                    var newBlob = new MediaBlob
                    {
                        MediaAsset = asset,
                        Content = bytes,
                        ContentType = mime,
                        Sha256 = Convert.ToHexString(SHA256.HashData(bytes)).ToLowerInvariant(),
                    };
                    asset.Blob = newBlob;
                    newBlobs.Add(newBlob);
                    result.MediaStored++;
                }
                else
                {
                    result.MediaFilesMissing++;
                    result.Warnings.Add($"file media mancante su disco: {relPath}");
                }

                // Vocale già trascritto/classificato in curatela (vedi
                // scripts/whatsapp-digest/transcribe_new.py + DigestEntry.Transcript):
                // valorizziamo qui TranscriptionText/TranscribedAt così il Transcriber
                // (Program.cs: WHERE TranscriptionText == null || TranscribedAt == null)
                // lo esclude da solo, senza bisogno di toccarne la query. "media" resta
                // il placeholder di sempre (non ancora classificato): in quel caso non
                // tocchiamo questi campi, il Transcriber lo elabora come oggi.
                if (!string.IsNullOrWhiteSpace(entry.Transcript)
                    && !string.Equals(entry.Type, "media", StringComparison.OrdinalIgnoreCase))
                {
                    asset.TranscriptionText = entry.Transcript;
                    asset.TranscribedAt = DateTimeOffset.UtcNow;
                }
            }
        }

        if (result.PointsInserted == 0)
        {
            // Niente di nuovo (tutto già importato): non lasciamo un IngestionRun vuoto.
            _db.IngestionRuns.Remove(run);
            await _db.SaveChangesAsync(ct);
            return result;
        }

        run.CompletedAt = DateTimeOffset.UtcNow;
        await _db.SaveChangesAsync(ct);
        result.RunId = run.Id;

        await OffloadBlobsAsync(newBlobs, result, ct);
        return result;
    }

    private static string Trim(string s) => s.Length <= 60 ? s : s[..57] + "...";

    /// <summary>True se il testo è il placeholder di un media non trascritto (es. "Vocale di ..., non trascritto (0:17).").</summary>
    private static bool IsUntranscribedPlaceholder(string text) =>
        text.Contains("non trascritt", StringComparison.OrdinalIgnoreCase);

    private static DateTimeOffset ToOccurredAt(DigestEntry entry)
    {
        var date = DateOnly.ParseExact(entry.Date, "yyyy-MM-dd", CultureInfo.InvariantCulture);
        var time = TimeOnly.ParseExact(entry.Time, "HH:mm", CultureInfo.InvariantCulture);
        return RomeTime.ToInstant(date, time);
    }
}
