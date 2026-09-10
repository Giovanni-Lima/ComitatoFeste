using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Net.Http.Headers;

namespace ComitatoFeste.Api.Controllers;

[ApiController]
[Route("api/members")]
public sealed class MembersController : ControllerBase
{
    private readonly ComitatoFesteDbContext _db;
    private readonly ImageThumbnailer _thumbs;

    public MembersController(ComitatoFesteDbContext db, ImageThumbnailer thumbs)
    {
        _db = db;
        _thumbs = thumbs;
    }

    /// <summary>
    /// Foto profilo di un membro, servita inline. Con <c>?w=192|480|960</c> restituisce un
    /// thumbnail WebP di quella larghezza; ogni altro valore → foto originale.
    /// </summary>
    [HttpGet("{memberId:int}/photo")]
    public async Task<IActionResult> GetPhoto(int memberId, [FromQuery] int? w, CancellationToken ct)
    {
        // La foto può cambiare (l'Importer la riscrive se cambia lo SHA): niente "immutable",
        // ma l'ETag = SHA-256 fa sì che un cambio invalidi la cache e nel frattempo i 304
        // evitino di ritrasferire i byte.
        Response.Headers.CacheControl = "public, max-age=86400";

        if (w is int width && ImageThumbnailer.IsAllowedWidth(width))
        {
            var meta = await _db.MemberProfilePhotos
                .Where(p => p.MemberId == memberId)
                .Select(p => new { p.ContentType, p.Sha256 })
                .FirstOrDefaultAsync(ct);

            if (meta is null)
                return NotFound();

            if (meta.Sha256 is not null
                && (meta.ContentType ?? "").StartsWith("image/", StringComparison.OrdinalIgnoreCase))
            {
                var thumb = await _thumbs.GetWebpAsync("memberphoto", memberId, width, meta.Sha256,
                    () => _db.MemberProfilePhotos.Where(p => p.MemberId == memberId).Select(p => p.Content).FirstAsync(ct),
                    ct);
                if (thumb is not null)
                    return File(thumb, "image/webp", lastModified: null,
                        entityTag: new EntityTagHeaderValue($"\"{meta.Sha256}-w{width}\""));
            }
        }

        var photo = await _db.MemberProfilePhotos
            .Where(p => p.MemberId == memberId)
            .Select(p => new { p.Content, p.ContentType, p.Sha256 })
            .FirstOrDefaultAsync(ct);

        if (photo is null)
            return NotFound();

        var contentType = string.IsNullOrWhiteSpace(photo.ContentType) ? "application/octet-stream" : photo.ContentType;
        var etag = new EntityTagHeaderValue($"\"{photo.Sha256}\"");
        return File(photo.Content, contentType, lastModified: null, entityTag: etag);
    }
}
