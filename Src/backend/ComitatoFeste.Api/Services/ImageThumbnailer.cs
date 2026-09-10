using ComitatoFeste.Data;
using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Processing;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Genera versioni WebP ridimensionate delle immagini servite dagli endpoint blob (foto
/// profilo e media) e le **persiste** in <c>ImageThumbnails</c>: così ogni <c>(sorgente,
/// larghezza)</c> si ridimensiona una volta sola nella vita e le richieste "calde" leggono
/// una riga piccola dal DB senza toccare ImageSharp né il blob originale. Vedi CLAUDE.md
/// "Prossimi passi noti" punto 5c.
///
/// Servizio **scoped** (usa il <see cref="ComitatoFesteDbContext"/> della richiesta); il
/// freno alla concorrenza è statico perché limita una risorsa globale — la RAM: ImageSharp
/// tiene l'immagine decompressa in memoria (una JPEG da 600 KB può essere decine di MB) e il
/// free tier ha 512 MB.
/// </summary>
public sealed class ImageThumbnailer
{
    /// <summary>Larghezze ammesse (il resto → nessun thumbnail, si serve l'originale). Poche
    /// per limitare le righe per immagine. Pensate retina: 192 avatar, 480 tile griglia
    /// Media, 960 foto inline nelle card.</summary>
    private static readonly int[] AllowedWidths = { 192, 480, 960 };

    private static readonly SemaphoreSlim Gate = new(2, 2);

    private readonly ComitatoFesteDbContext _db;

    public ImageThumbnailer(ComitatoFesteDbContext db) => _db = db;

    public static bool IsAllowedWidth(int w) => Array.IndexOf(AllowedWidths, w) >= 0;

    /// <summary>
    /// WebP di larghezza <paramref name="width"/> (mai ingrandito) per la sorgente
    /// <paramref name="kind"/>/<paramref name="sourceId"/>. Se esiste già in
    /// <c>ImageThumbnails</c> per lo stesso <paramref name="sourceSha256"/> lo restituisce
    /// senza altro lavoro; altrimenti chiama <paramref name="loadOriginal"/> (che scarica il
    /// blob grande), genera, salva e restituisce. <c>null</c> se i byte non sono un'immagine
    /// decodificabile (il chiamante ripiega sull'originale).
    /// </summary>
    public async Task<byte[]?> GetWebpAsync(
        string kind, int sourceId, int width, string sourceSha256,
        Func<Task<byte[]>> loadOriginal, CancellationToken ct)
    {
        var hit = await FindAsync(kind, sourceId, width, sourceSha256, ct);
        if (hit is not null) return hit;

        await Gate.WaitAsync(ct);
        try
        {
            hit = await FindAsync(kind, sourceId, width, sourceSha256, ct);   // un'altra richiesta può averlo appena inserito
            if (hit is not null) return hit;

            byte[] webp;
            try
            {
                var original = await loadOriginal();
                using var image = Image.Load(original);
                var target = Math.Min(width, image.Width);
                image.Mutate(x => x.Resize(new ResizeOptions
                {
                    Size = new Size(target, 0),   // altezza 0 = proporzionale
                    Mode = ResizeMode.Max,
                }));
                using var ms = new MemoryStream();
                await image.SaveAsWebpAsync(ms, ct);
                webp = ms.ToArray();
            }
            catch (Exception) when (!ct.IsCancellationRequested)
            {
                return null;   // formato non supportato / immagine corrotta
            }

            _db.ImageThumbnails.Add(new ImageThumbnail
            {
                Kind = kind,
                SourceId = sourceId,
                Width = width,
                SourceSha256 = sourceSha256,
                Content = webp,
                ContentType = "image/webp",
                CreatedAt = DateTimeOffset.UtcNow,
            });
            try
            {
                await _db.SaveChangesAsync(ct);
            }
            catch (DbUpdateException)
            {
                // Corsa: un'altra richiesta ha inserito la stessa (Kind, SourceId, Width).
                // I byte sono equivalenti: si scarta la Add e si restituisce quanto generato.
                _db.ChangeTracker.Clear();
            }
            return webp;
        }
        finally
        {
            Gate.Release();
        }
    }

    private Task<byte[]?> FindAsync(string kind, int sourceId, int width, string sha, CancellationToken ct) =>
        _db.ImageThumbnails.AsNoTracking()
            .Where(t => t.Kind == kind && t.SourceId == sourceId && t.Width == width && t.SourceSha256 == sha)
            .Select(t => (byte[]?)t.Content)
            .FirstOrDefaultAsync(ct);
}
