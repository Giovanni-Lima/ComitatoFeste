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

    public MembersController(ComitatoFesteDbContext db) => _db = db;

    /// <summary>Foto profilo di un membro, servita inline.</summary>
    [HttpGet("{memberId:int}/photo")]
    public async Task<IActionResult> GetPhoto(int memberId, CancellationToken ct)
    {
        var photo = await _db.MemberProfilePhotos
            .Where(p => p.MemberId == memberId)
            .Select(p => new { p.Content, p.ContentType, p.Sha256 })
            .FirstOrDefaultAsync(ct);

        if (photo is null)
            return NotFound();

        var contentType = string.IsNullOrWhiteSpace(photo.ContentType) ? "application/octet-stream" : photo.ContentType;
        // La foto può cambiare (l'Importer la riscrive se cambia lo SHA): niente "immutable",
        // ma l'ETag = SHA-256 fa sì che un cambio invalidi la cache e nel frattempo i 304
        // evitino di ritrasferire i byte.
        Response.Headers.CacheControl = "public, max-age=86400";
        var etag = new EntityTagHeaderValue($"\"{photo.Sha256}\"");
        return File(photo.Content, contentType, lastModified: null, entityTag: etag);
    }
}
