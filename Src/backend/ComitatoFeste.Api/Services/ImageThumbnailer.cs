using Microsoft.Extensions.Caching.Memory;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Processing;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Genera al volo versioni WebP ridimensionate delle immagini servite dagli endpoint blob
/// (foto profilo e media), con cache in memoria. Serve a non mandare il file originale
/// (foto profilo ~73 KB medi, foto condivise ~175 KB) dove il frontend lo mostra piccolo
/// — avatar, griglia della vista Media. Vedi CLAUDE.md "Prossimi passi noti" punto 5c.
///
/// Storage: <see cref="IMemoryCache"/> — semplice, si perde a ogni restart del container
/// (frequente sul piano free) e si rigenera su richiesta. Se in futuro serve persistenza,
/// il candidato è una tabella <c>MediaThumbnails</c> 1:1 come <c>MediaBlobs</c>: cambia
/// solo l'implementazione di questo servizio, non i controller.
/// </summary>
public sealed class ImageThumbnailer
{
    /// <summary>Larghezze ammesse (il resto → nessun thumbnail, si serve l'originale).
    /// Tenerle poche limita le voci di cache per immagine. Valori pensati retina:
    /// 192 = avatar, 480 = tile griglia Media, 960 = foto inline nelle card.</summary>
    private static readonly int[] AllowedWidths = { 192, 480, 960 };

    private readonly IMemoryCache _cache;
    // Serializza il lavoro pesante: ImageSharp tiene l'immagine decompressa in RAM
    // (una JPEG da 600 KB può essere decine di MB) e il free tier ha 512 MB.
    private readonly SemaphoreSlim _gate = new(2, 2);

    public ImageThumbnailer(IMemoryCache cache) => _cache = cache;

    public static bool IsAllowedWidth(int w) => Array.IndexOf(AllowedWidths, w) >= 0;

    /// <summary>
    /// WebP di <paramref name="original"/> ridotto a <paramref name="width"/> px di larghezza
    /// (mai ingrandito), con caching per <paramref name="cacheKey"/>. <c>null</c> se i byte non
    /// sono un'immagine decodificabile (il chiamante ripiega sull'originale).
    /// </summary>
    public async Task<byte[]?> GetWebpAsync(string cacheKey, byte[] original, int width, CancellationToken ct)
    {
        if (_cache.TryGetValue(cacheKey, out byte[]? cached)) return cached;

        await _gate.WaitAsync(ct);
        try
        {
            if (_cache.TryGetValue(cacheKey, out cached)) return cached;   // ricontrolla dopo il gate

            byte[] webp;
            try
            {
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

            // ~100 immagini × 3 larghezze × ~30 KB ≈ pochi MB; la sliding expiration
            // evita crescita illimitata nel tempo. Niente Size: il MemoryCache di
            // AddMemoryCache() non ha SizeLimit.
            _cache.Set(cacheKey, webp, new MemoryCacheEntryOptions
            {
                SlidingExpiration = TimeSpan.FromHours(24),
            });
            return webp;
        }
        finally
        {
            _gate.Release();
        }
    }
}
