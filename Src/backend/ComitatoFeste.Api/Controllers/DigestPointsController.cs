using ComitatoFeste.Api.Contracts;
using ComitatoFeste.Data;
using ComitatoFeste.Domain;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ComitatoFeste.Api.Controllers;

[ApiController]
[Route("api/digestpoints")]
public sealed class DigestPointsController : ControllerBase
{
    private readonly ComitatoFesteDbContext _db;

    public DigestPointsController(ComitatoFesteDbContext db) => _db = db;

    /// <summary>
    /// Punti di digest di una giornata (fuso Europe/Rome), in ordine cronologico.
    /// Filtri opzionali per autore (<c>DisplayName</c> esatto) e tipo.
    /// </summary>
    [HttpGet]
    public async Task<ActionResult<IReadOnlyList<DigestPointDto>>> GetByDay(
        [FromQuery] DateOnly? date,
        [FromQuery] string? author,
        [FromQuery] string? type,
        CancellationToken ct)
    {
        if (date is null)
            return BadRequest("Parametro 'date' obbligatorio (formato yyyy-MM-dd).");

        DigestPointType? typeFilter = null;
        if (!string.IsNullOrWhiteSpace(type))
        {
            if (!Enum.TryParse<DigestPointType>(type, ignoreCase: true, out var parsed))
                return BadRequest($"Valore 'type' non valido: '{type}'. Ammessi: decisione, domanda, media, info.");
            typeFilter = parsed;
        }

        var (startUtc, endUtc) = RomeTime.DayRangeUtc(date.Value);

        var rows = await _db.DigestPoints
            .Where(d => d.OccurredAt >= startUtc && d.OccurredAt < endUtc)
            .Where(d => author == null || d.Member.DisplayName == author)
            .Where(d => typeFilter == null || d.Type == typeFilter)
            .OrderBy(d => d.OccurredAt).ThenBy(d => d.Id)
            .Select(d => new
            {
                d.Id,
                d.OccurredAt,
                AuthorId = d.MemberId,
                Author = d.Member.DisplayName,
                AuthorHasPhoto = d.Member.ProfilePhoto != null,
                d.Type,
                d.Text,
                Media = d.MediaAsset == null
                    ? null
                    : new
                    {
                        d.MediaAsset.Id,
                        d.MediaAsset.MediaType,
                        d.MediaAsset.FileName,
                        d.MediaAsset.SizeBytes,
                        d.MediaAsset.TranscriptionText,
                        ContentType = d.MediaAsset.Blob == null ? null : d.MediaAsset.Blob.ContentType,
                        HasContent = d.MediaAsset.Blob != null,
                    },
            })
            .ToListAsync(ct);

        var result = rows.Select(r => new DigestPointDto
        {
            Id = r.Id,
            OccurredAt = r.OccurredAt,
            AuthorId = r.AuthorId,
            Author = r.Author,
            AuthorPhotoUrl = r.AuthorHasPhoto
                ? Url.Action("GetPhoto", "Members", new { memberId = r.AuthorId })
                : null,
            Type = r.Type.ToString().ToLowerInvariant(),
            Text = r.Text,
            Media = r.Media is null
                ? null
                : new MediaDto
                {
                    Id = r.Media.Id,
                    MediaType = r.Media.MediaType.ToString().ToLowerInvariant(),
                    FileName = r.Media.FileName,
                    SizeBytes = r.Media.SizeBytes,
                    ContentType = r.Media.ContentType,
                    HasContent = r.Media.HasContent,
                    IsTranscribed = !string.IsNullOrWhiteSpace(r.Media.TranscriptionText),
                    TranscriptionText = r.Media.TranscriptionText,
                    ContentUrl = r.Media.HasContent
                        ? Url.Action(nameof(GetMediaContent), new { mediaId = r.Media.Id })
                        : null,
                },
        }).ToList();

        return Ok(result);
    }

    /// <summary>Contenuto binario originale di un media (immagine/audio/documento), servito inline.</summary>
    [HttpGet("media/{mediaId:int}/content")]
    public async Task<IActionResult> GetMediaContent(int mediaId, CancellationToken ct)
    {
        var blob = await _db.MediaBlobs
            .Where(b => b.MediaAssetId == mediaId)
            .Select(b => new { b.Content, b.ContentType })
            .FirstOrDefaultAsync(ct);

        if (blob is null)
            return NotFound();

        var contentType = string.IsNullOrWhiteSpace(blob.ContentType) ? "application/octet-stream" : blob.ContentType;
        return File(blob.Content, contentType, enableRangeProcessing: true);
    }
}
