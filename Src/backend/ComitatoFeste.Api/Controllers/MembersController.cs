using ComitatoFeste.Api.Services;
using ComitatoFeste.Api.Filters;
using ComitatoFeste.Data;
using ComitatoFeste.Domain;
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
    private readonly IBlobStore? _store;
    private readonly AuthService _auth;

    public MembersController(ComitatoFesteDbContext db, ImageThumbnailer thumbs, BlobStoreHolder blobs, AuthService auth)
    {
        _auth = auth;
        _db = db;
        _thumbs = thumbs;
        _store = blobs.Store;
    }

    public sealed record MemberSeenDto(int MemberId, string DisplayName, DateTimeOffset LastSeenAt);

    /// <summary>
    /// Membri con <c>LastSeenAt</c> valorizzato, dal più recente, escluso chi sta chiedendo.
    /// Solo architetto (pagina "Dati").
    /// </summary>
    [HttpGet("seen")]
    [TokenAuth(MemberRole.Architetto)]
    public async Task<IActionResult> GetSeen(CancellationToken ct)
    {
        var header = Request.Headers.Authorization.ToString();
        var token = header.StartsWith("Bearer ", StringComparison.OrdinalIgnoreCase)
            ? header["Bearer ".Length..].Trim()
            : null;
        var me = _auth.ValidatePrincipal(token)?.Username;

        var rows = await _db.Members
            .Where(m => m.LastSeenAt != null)
            .Select(m => new { m.Id, m.DisplayName, LastSeenAt = m.LastSeenAt!.Value })
            .ToListAsync(ct);

        var list = rows
            .Where(m => me is null || !string.Equals(AuthService.NormalizeUsername(m.DisplayName), me, StringComparison.Ordinal))
            .OrderByDescending(m => m.LastSeenAt)
            .Select(m => new MemberSeenDto(m.Id, m.DisplayName, m.LastSeenAt))
            .ToList();
        return Ok(list);
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
                    async () =>
                    {
                        var db = await _db.MemberProfilePhotos.Where(p => p.MemberId == memberId).Select(p => p.Content).FirstAsync(ct);
                        return await _store.ResolveAsync(db, BlobKeys.MemberPhoto(memberId, meta.Sha256), ct)
                               ?? throw new InvalidOperationException("foto non trovata in R2");
                    },
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

        var content = await _store.ResolveAsync(photo.Content,
            photo.Sha256 is null ? null : BlobKeys.MemberPhoto(memberId, photo.Sha256), ct);
        if (content is null)
            return NotFound();

        var contentType = string.IsNullOrWhiteSpace(photo.ContentType) ? "application/octet-stream" : photo.ContentType;
        var etag = new EntityTagHeaderValue($"\"{photo.Sha256}\"");
        return File(content, contentType, lastModified: null, entityTag: etag);
    }
}
