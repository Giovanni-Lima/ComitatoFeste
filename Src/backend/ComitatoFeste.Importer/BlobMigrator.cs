using System.Security.Cryptography;
using ComitatoFeste.Data;
using Microsoft.EntityFrameworkCore;

namespace ComitatoFeste.Importer;

/// <summary>
/// Backfill una tantum: sposta su R2 i byte già presenti in Postgres (<c>MediaBlobs</c>,
/// <c>MemberProfilePhotos</c>, <c>ImageThumbnails</c>). Idempotente e in due fasi:
/// <list type="number">
///   <item>senza <c>clearDb</c>: carica ciò che manca su R2 e verifica che l'oggetto esista;
///     il DB non viene modificato, quindi resta il fallback;</item>
///   <item>con <c>clearDb</c>: per ogni riga con i byte ancora a DB verifica che l'oggetto sia su R2
///     (<c>ExistsAsync</c>, dopo l'eventuale upload) e solo allora azzera <c>Content</c>.</item>
/// </list>
/// Una riga alla volta (i blob arrivano a qualche MB): memoria bassa e ripartenza gratuita.
/// Nota: azzerare <c>Content</c> non restituisce subito spazio su disco — vedi docs/DEPLOY.md.
/// </summary>
public sealed class BlobMigrator
{
    private readonly ComitatoFesteDbContext _db;
    private readonly IBlobStore _store;
    private readonly bool _clearDb;
    private readonly bool _dryRun;

    public int Uploaded, AlreadyThere, Cleared, Failed;
    public long BytesCleared;

    public BlobMigrator(ComitatoFesteDbContext db, IBlobStore store, bool clearDb, bool dryRun)
    {
        _db = db;
        _store = store;
        _clearDb = clearDb;
        _dryRun = dryRun;
    }

    public async Task RunAsync(CancellationToken ct)
    {
        await MigrateMediaAsync(ct);
        await MigratePhotosAsync(ct);
        await MigrateThumbnailsAsync(ct);
    }

    private async Task MigrateMediaAsync(CancellationToken ct)
    {
        var ids = await _db.MediaBlobs.Where(b => b.Content != null).OrderBy(b => b.Id).Select(b => b.Id).ToListAsync(ct);
        Console.WriteLine($"MediaBlobs con byte a DB: {ids.Count}");
        foreach (var id in ids)
        {
            if (ct.IsCancellationRequested) return;
            var b = await _db.MediaBlobs.FirstAsync(x => x.Id == id, ct);
            if (b.Content is null) continue;
            b.Sha256 ??= Sha(b.Content);
            await SyncAsync($"media #{b.MediaAssetId}", BlobKeys.Media(b.MediaAssetId, b.Sha256), b.Content, b.ContentType,
                () => b.Content = null, ct);
            _db.ChangeTracker.Clear();
        }
    }

    private async Task MigratePhotosAsync(CancellationToken ct)
    {
        var ids = await _db.MemberProfilePhotos.Where(p => p.Content != null).OrderBy(p => p.Id).Select(p => p.Id).ToListAsync(ct);
        Console.WriteLine($"MemberProfilePhotos con byte a DB: {ids.Count}");
        foreach (var id in ids)
        {
            if (ct.IsCancellationRequested) return;
            var p = await _db.MemberProfilePhotos.FirstAsync(x => x.Id == id, ct);
            if (p.Content is null) continue;
            p.Sha256 ??= Sha(p.Content);
            await SyncAsync($"foto membro #{p.MemberId}", BlobKeys.MemberPhoto(p.MemberId, p.Sha256), p.Content, p.ContentType,
                () => p.Content = null, ct);
            _db.ChangeTracker.Clear();
        }
    }

    private async Task MigrateThumbnailsAsync(CancellationToken ct)
    {
        var ids = await _db.ImageThumbnails.Where(t => t.Content != null).OrderBy(t => t.Id).Select(t => t.Id).ToListAsync(ct);
        Console.WriteLine($"ImageThumbnails con byte a DB: {ids.Count}");
        foreach (var id in ids)
        {
            if (ct.IsCancellationRequested) return;
            var t = await _db.ImageThumbnails.FirstAsync(x => x.Id == id, ct);
            if (t.Content is null) continue;
            await SyncAsync($"thumb {t.Kind} #{t.SourceId} w{t.Width}",
                BlobKeys.Thumbnail(t.Kind, t.SourceId, t.Width, t.SourceSha256), t.Content, t.ContentType,
                () => t.Content = null, ct);
            _db.ChangeTracker.Clear();
        }
    }

    /// <summary>Garantisce l'oggetto su R2 e, con <c>clearDb</c>, azzera i byte a DB dopo averne verificato l'esistenza.</summary>
    private async Task SyncAsync(string label, string key, byte[] content, string contentType, Action clear, CancellationToken ct)
    {
        try
        {
            var exists = await _store.ExistsAsync(key, ct);
            if (exists)
                AlreadyThere++;
            else if (_dryRun)
                Console.WriteLine($"  [dry-run] caricherei {label} ({content.Length:N0} B)");
            else
            {
                await _store.PutAsync(key, content, contentType, ct);
                if (!await _store.ExistsAsync(key, ct))
                    throw new InvalidOperationException("l'oggetto non risulta su R2 dopo l'upload");
                Uploaded++;
                exists = true;
            }

            if (_clearDb && exists && !_dryRun)
            {
                var size = content.LongLength;
                clear();
                await _db.SaveChangesAsync(ct);
                Cleared++;
                BytesCleared += size;
            }
        }
        catch (Exception ex) when (!ct.IsCancellationRequested)
        {
            Failed++;
            Console.WriteLine($"  ERRORE {label}: {ex.Message}");
        }
    }

    private static string Sha(byte[] bytes) => Convert.ToHexString(SHA256.HashData(bytes)).ToLowerInvariant();
}
