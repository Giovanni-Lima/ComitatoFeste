using System.Text;
using ComitatoFeste.Api.Contracts;
using ComitatoFeste.Api.Filters;
using ComitatoFeste.Api.Services;
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
    private readonly GroqRecapClient _groq;

    public DigestPointsController(ComitatoFesteDbContext db, GroqRecapClient groq)
    {
        _db = db;
        _groq = groq;
    }

    /// <summary>
    /// Punti di digest in ordine cronologico (fuso Europe/Rome).
    /// Con <c>date</c> (yyyy-MM-dd) restituisce solo quella giornata; senza, tutti i giorni
    /// (non paginato — il volume atteso è piccolo, il frontend li raggruppa per data).
    /// Filtri opzionali per autore (<c>DisplayName</c> esatto) e tipo.
    /// Senza filtro esplicito su 'type' la vista è "pulita": esclude i punti "rumore" e i
    /// vocali non ancora digeriti dal Transcriber (audio senza <c>TranscribedAt</c> — sia i
    /// pendenti sia quelli con classificazione ancora incerta). Un filtro <c>type=</c>
    /// esplicito mostra invece tutto ciò che corrisponde, inclusi quei vocali.
    /// </summary>
    [HttpGet]
    [TokenAuth]
    public async Task<ActionResult<IReadOnlyList<DigestPointDto>>> GetByDay(
        [FromQuery] DateOnly? date,
        [FromQuery] string? author,
        [FromQuery] string? type,
        CancellationToken ct)
    {
        DigestPointType? typeFilter = null;
        if (!string.IsNullOrWhiteSpace(type))
        {
            if (!Enum.TryParse<DigestPointType>(type, ignoreCase: true, out var parsed))
                return BadRequest($"Valore 'type' non valido: '{type}'. Ammessi: decisione, domanda, media, info, rumore.");
            typeFilter = parsed;
        }

        var query = _db.DigestPoints.AsQueryable();

        if (date is not null)
        {
            var (startUtc, endUtc) = RomeTime.DayRangeUtc(date.Value);
            query = query.Where(d => d.OccurredAt >= startUtc && d.OccurredAt < endUtc);
        }

        var rows = await query
            .Where(d => author == null || d.Member.DisplayName == author)
            .Where(d => typeFilter == null ? d.Type != DigestPointType.Rumore : d.Type == typeFilter)
            // Vista di default: nasconde i vocali non ancora digeriti — audio senza
            // TranscribedAt (mai trascritti, oppure trascritti ma con classificazione incerta).
            .Where(d => typeFilter != null
                        || d.MediaAsset == null
                        || d.MediaAsset.MediaType != MediaType.Audio
                        || d.MediaAsset.TranscribedAt != null)
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

    /// <summary>
    /// Verbale in prosa della giornata, scaricato come file: <b>PDF</b> di default,
    /// <c>format=md</c> per il Markdown grezzo. Il testo è generato da Groq alla prima
    /// richiesta e messo in cache nella tabella <c>Verbali</c> (il PDF è reso al volo dal
    /// Markdown salvato, senza nuove chiamate); <c>refresh=true</c> rigenera il testo.
    /// </summary>
    [HttpGet("recap")]
    [TokenAuth]
    public async Task<IActionResult> GetDailyRecap(
        [FromQuery] DateOnly? date,
        [FromQuery] bool refresh,
        [FromQuery] string? format,
        CancellationToken ct)
    {
        if (date is null)
            return BadRequest("Parametro 'date' obbligatorio (formato yyyy-MM-dd).");

        var day = date.Value;
        var (startUtc, endUtc) = RomeTime.DayRangeUtc(day);

        // Stessi criteri della vista "pulita": niente rumore, niente audio non ancora digerito.
        var points = await _db.DigestPoints
            .Where(d => d.OccurredAt >= startUtc && d.OccurredAt < endUtc)
            .Where(d => d.Type != DigestPointType.Rumore)
            .Where(d => d.MediaAsset == null
                        || d.MediaAsset.MediaType != MediaType.Audio
                        || d.MediaAsset.TranscribedAt != null)
            .OrderBy(d => d.OccurredAt).ThenBy(d => d.Id)
            .Select(d => new
            {
                d.GroupId,
                GroupName = d.Group.Name,
                d.OccurredAt,
                Author = d.Member.DisplayName,
                d.Type,
                d.Text,
            })
            .ToListAsync(ct);

        if (points.Count == 0)
            return NotFound($"Nessun punto per il {day:dd/MM/yyyy}: verbale non generabile.");

        var groupId = points[0].GroupId;
        var groupName = points[0].GroupName;

        var existing = await _db.Verbali
            .FirstOrDefaultAsync(v => v.GroupId == groupId && v.Date == day, ct);

        if (existing is not null && !refresh)
            return RecapResponse(existing.Content, day, groupName, format);

        if (!_groq.IsConfigured)
            return StatusCode(StatusCodes.Status503ServiceUnavailable,
                "GROQ_API_KEY non configurata sull'API: impossibile generare il verbale.");

        var block = string.Join('\n', points.Select(p =>
        {
            var rome = TimeZoneInfo.ConvertTime(p.OccurredAt, RomeTime.Zone);
            return $"- {rome:HH:mm} · {p.Author} · {p.Type.ToString().ToLowerInvariant()}: {p.Text}";
        }));

        string content;
        try
        {
            content = await _groq.WriteRecapAsync(groupName, day, block, ct);
        }
        catch (Exception ex)
        {
            return StatusCode(StatusCodes.Status502BadGateway, $"Groq non ha prodotto il verbale: {ex.Message}");
        }

        if (string.IsNullOrWhiteSpace(content))
            return StatusCode(StatusCodes.Status502BadGateway, "Groq ha restituito un verbale vuoto.");

        if (existing is null)
            _db.Verbali.Add(new Verbale
            {
                GroupId = groupId,
                Date = day,
                Content = content,
                Model = _groq.ModelName,
                PointCount = points.Count,
                GeneratedAt = DateTimeOffset.UtcNow,
            });
        else
        {
            existing.Content = content;
            existing.Model = _groq.ModelName;
            existing.PointCount = points.Count;
            existing.GeneratedAt = DateTimeOffset.UtcNow;
        }

        try
        {
            await _db.SaveChangesAsync(ct);
        }
        catch (DbUpdateException) when (existing is null)
        {
            // Race sulla prima generazione: un'altra richiesta ha già inserito il verbale.
            var raced = await _db.Verbali
                .FirstOrDefaultAsync(v => v.GroupId == groupId && v.Date == day, ct);
            if (raced is not null)
                return RecapResponse(raced.Content, day, groupName, format);
            throw;
        }

        return RecapResponse(content, day, groupName, format);
    }

    /// <summary>Restituisce il verbale come PDF (default) oppure come Markdown grezzo (<c>format=md</c>).</summary>
    private FileContentResult RecapResponse(string markdown, DateOnly day, string groupName, string? format)
    {
        if (string.Equals(format, "md", StringComparison.OrdinalIgnoreCase))
            return File(Encoding.UTF8.GetBytes(markdown), "text/markdown; charset=utf-8", $"verbale-{day:yyyy-MM-dd}.md");

        var pdf = VerbalePdf.Render(groupName, day, markdown);
        return File(pdf, "application/pdf", $"verbale-{day:yyyy-MM-dd}.pdf");
    }
}
