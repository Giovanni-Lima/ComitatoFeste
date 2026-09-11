using System.Text;
using ComitatoFeste.Api.Contracts;
using ComitatoFeste.Api.Filters;
using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
using ComitatoFeste.Domain;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Net.Http.Headers;

namespace ComitatoFeste.Api.Controllers;

[ApiController]
[Route("api/digestpoints")]
public sealed class DigestPointsController : ControllerBase
{
    private readonly ComitatoFesteDbContext _db;
    private readonly GroqRecapClient _groq;
    private readonly ImageThumbnailer _thumbs;

    public DigestPointsController(ComitatoFesteDbContext db, GroqRecapClient groq, ImageThumbnailer thumbs)
    {
        _db = db;
        _groq = groq;
        _thumbs = thumbs;
    }

    /// <summary>
    /// Punti di digest in ordine cronologico (fuso Europe/Rome).
    /// Con <c>date</c> (yyyy-MM-dd) restituisce solo quella giornata; con <c>from</c>/<c>to</c>
    /// (entrambi opzionali e inclusivi) un range di giorni — usato dal frontend per caricare
    /// l'Agenda un mese alla volta invece di tutto lo storico. Senza nessuno dei tre, tutti i
    /// giorni (nessun limite: uso interno/di servizio, il frontend non lo fa più per l'Agenda).
    /// <c>important=true</c> restituisce solo i punti flaggati (storico completo, a prescindere
    /// da date/from/to: sono pochi anche su base annua, è la query della vista Importanti).
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
        [FromQuery] DateOnly? from,
        [FromQuery] DateOnly? to,
        [FromQuery] string? author,
        [FromQuery] string? type,
        [FromQuery] bool important,
        CancellationToken ct)
    {
        DigestPointType? typeFilter = null;
        if (!string.IsNullOrWhiteSpace(type))
        {
            if (!Enum.TryParse<DigestPointType>(type, ignoreCase: true, out var parsed))
                return BadRequest($"Valore 'type' non valido: '{type}'. Ammessi: decisione, proposta, domanda, media, info, rumore.");
            typeFilter = parsed;
        }

        if (from is not null && to is not null && from > to)
            return BadRequest("'from' non può essere successivo a 'to'.");

        var query = _db.DigestPoints.AsQueryable();

        if (date is not null)
        {
            var (startUtc, endUtc) = RomeTime.DayRangeUtc(date.Value);
            query = query.Where(d => d.OccurredAt >= startUtc && d.OccurredAt < endUtc);
        }
        else
        {
            if (from is not null)
            {
                var (startUtc, _) = RomeTime.DayRangeUtc(from.Value);
                query = query.Where(d => d.OccurredAt >= startUtc);
            }
            if (to is not null)
            {
                var (_, endUtc) = RomeTime.DayRangeUtc(to.Value);
                query = query.Where(d => d.OccurredAt < endUtc);
            }
        }

        if (important)
            query = query.Where(d => d.IsImportant);

        query = query
            .Where(d => author == null || d.Member.DisplayName == author)
            .Where(d => typeFilter == null ? d.Type != DigestPointType.Rumore : d.Type == typeFilter)
            // Vista di default: nasconde i vocali non ancora digeriti — audio senza
            // TranscribedAt (mai trascritti, oppure trascritti ma con classificazione incerta).
            .Where(d => typeFilter != null
                        || d.MediaAsset == null
                        || d.MediaAsset.MediaType != MediaType.Audio
                        || d.MediaAsset.TranscribedAt != null);

        return Ok(await ProjectToDtoAsync(query, ct));
    }

    /// <summary>
    /// Primo/ultimo giorno (fuso Europe/Rome) con almeno un punto nella vista "pulita" (vedi
    /// <see cref="GetByDay"/>). Il frontend lo interroga una volta all'avvio per scegliere il
    /// mese di default dell'Agenda (quello di <c>Latest</c>, non necessariamente il mese
    /// solare corrente — così un mese ancora senza punti non appare vuoto) e per sapere quando
    /// nascondere "carica mese precedente" (una volta raggiunto <c>Earliest</c>).
    /// </summary>
    [HttpGet("bounds")]
    [TokenAuth]
    public async Task<ActionResult<DigestPointsBoundsDto>> GetBounds(CancellationToken ct)
    {
        var query = CleanViewQuery();

        if (!await query.AnyAsync(ct))
            return Ok(new DigestPointsBoundsDto());

        var minUtc = await query.MinAsync(d => d.OccurredAt, ct);
        var maxUtc = await query.MaxAsync(d => d.OccurredAt, ct);

        return Ok(new DigestPointsBoundsDto
        {
            Earliest = DateOnly.FromDateTime(TimeZoneInfo.ConvertTime(minUtc, RomeTime.Zone).DateTime),
            Latest = DateOnly.FromDateTime(TimeZoneInfo.ConvertTime(maxUtc, RomeTime.Zone).DateTime),
        });
    }

    /// <summary>
    /// Tutti i punti con un media scaricabile che non sia audio (foto/video/documento — i
    /// vocali si ascoltano inline in Agenda, non compaiono nella griglia Media). Storico
    /// completo, a prescindere da date: è la query dedicata della vista Media, separata da
    /// quella (paginata per mese) dell'Agenda perché la galleria deve restare sfogliabile per
    /// intero anche quando l'Agenda carica solo il mese corrente.
    /// </summary>
    [HttpGet("media")]
    [TokenAuth]
    public async Task<ActionResult<IReadOnlyList<DigestPointDto>>> GetMediaItems(CancellationToken ct)
    {
        var query = _db.DigestPoints
            .Where(d => d.MediaAsset != null
                        && d.MediaAsset.Blob != null
                        && d.MediaAsset.MediaType != MediaType.Audio);

        return Ok(await ProjectToDtoAsync(query, ct));
    }

    /// <summary>Punti della vista "pulita": niente rumore, niente audio non ancora digerito.</summary>
    private IQueryable<DigestPoint> CleanViewQuery() =>
        _db.DigestPoints
            .Where(d => d.Type != DigestPointType.Rumore)
            .Where(d => d.MediaAsset == null
                        || d.MediaAsset.MediaType != MediaType.Audio
                        || d.MediaAsset.TranscribedAt != null);

    /// <summary>Proiezione comune a <see cref="GetByDay"/> e <see cref="GetMediaItems"/>: righe
    /// piatte dal DB (niente <c>Url.Action</c>, non traducibile in SQL), poi mappate a
    /// <see cref="DigestPointDto"/> in memoria.</summary>
    private async Task<List<DigestPointDto>> ProjectToDtoAsync(IQueryable<DigestPoint> query, CancellationToken ct)
    {
        var rows = await query
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
                d.IsImportant,
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

        return rows.Select(r => new DigestPointDto
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
            IsImportant = r.IsImportant,
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
    }

    /// <summary>Evidenzia/rimuove un punto come importante. Riservato agli amministratori.</summary>
    [HttpPut("{id:int}/important")]
    [TokenAuth(MemberRole.Amministratore)]
    public async Task<IActionResult> SetImportant(int id, [FromBody] SetImportantRequest req, CancellationToken ct)
    {
        var point = await _db.DigestPoints.FindAsync(new object[] { id }, ct);
        if (point is null)
            return NotFound();

        point.IsImportant = req.Important;
        await _db.SaveChangesAsync(ct);

        return Ok(new { id = point.Id, important = point.IsImportant });
    }

    /// <summary>
    /// Elimina un punto. Riservato agli amministratori. Il <see cref="MediaAsset"/> collegato
    /// (e il suo <see cref="MediaBlob"/>) sono cancellati a cascata a DB (vedi
    /// <c>DigestPointConfiguration</c>); <c>ImageThumbnails</c> non ha FK e va ripulita a mano
    /// per non lasciare thumbnail orfane. Invalida anche l'eventuale verbale già generato per
    /// quel giorno, così la prossima richiesta lo rigenera senza il punto cancellato.
    /// </summary>
    [HttpDelete("{id:int}")]
    [TokenAuth(MemberRole.Amministratore)]
    public async Task<IActionResult> Delete(int id, CancellationToken ct)
    {
        var point = await _db.DigestPoints
            .Where(d => d.Id == id)
            .Select(d => new
            {
                d.GroupId,
                d.OccurredAt,
                MediaAssetId = d.MediaAsset == null ? (int?)null : d.MediaAsset.Id,
            })
            .FirstOrDefaultAsync(ct);

        if (point is null)
            return NotFound();

        if (point.MediaAssetId is int mediaAssetId)
            await _db.ImageThumbnails
                .Where(t => t.Kind == "media" && t.SourceId == mediaAssetId)
                .ExecuteDeleteAsync(ct);

        var day = DateOnly.FromDateTime(TimeZoneInfo.ConvertTime(point.OccurredAt, RomeTime.Zone).DateTime);
        await _db.Verbali
            .Where(v => v.GroupId == point.GroupId && v.Date == day)
            .ExecuteDeleteAsync(ct);

        await _db.DigestPoints.Where(d => d.Id == id).ExecuteDeleteAsync(ct);

        return NoContent();
    }

    /// <summary>
    /// Contenuto binario di un media (immagine/audio/documento), servito inline.
    /// Con <c>?w=192|480|960</c> su un'immagine restituisce un thumbnail WebP di quella
    /// larghezza (vedi <see cref="ImageThumbnailer"/>); ogni altro valore o tipo → originale.
    /// </summary>
    [HttpGet("media/{mediaId:int}/content")]
    public async Task<IActionResult> GetMediaContent(int mediaId, [FromQuery] int? w, CancellationToken ct)
    {
        // Il contenuto di un mediaId non cambia mai (l'Importer non riscrive i blob, il
        // Transcriber tocca solo il Text): cache lunga + immutable, così il browser non
        // ri-richiede nemmeno. L'ETag (SHA-256) lascia gestire a ASP.NET i 304.
        Response.Headers.CacheControl = "public, max-age=31536000, immutable";

        // Percorso thumbnail: prima solo i metadati (tipo + SHA); il blob grande si scarica
        // solo se il thumbnail non è già in ImageThumbnails.
        if (w is int width && ImageThumbnailer.IsAllowedWidth(width))
        {
            var meta = await _db.MediaBlobs
                .Where(b => b.MediaAssetId == mediaId)
                .Select(b => new { b.ContentType, b.Sha256 })
                .FirstOrDefaultAsync(ct);

            if (meta is null)
                return NotFound();

            if (meta.Sha256 is not null
                && (meta.ContentType ?? "").StartsWith("image/", StringComparison.OrdinalIgnoreCase))
            {
                var thumb = await _thumbs.GetWebpAsync("media", mediaId, width, meta.Sha256,
                    () => _db.MediaBlobs.Where(b => b.MediaAssetId == mediaId).Select(b => b.Content).FirstAsync(ct),
                    ct);
                if (thumb is not null)
                    return File(thumb, "image/webp", lastModified: null,
                        entityTag: new EntityTagHeaderValue($"\"{meta.Sha256}-w{width}\""));
                // non immagine decodificabile: ripiega sull'originale sotto
            }
        }

        var blob = await _db.MediaBlobs
            .Where(b => b.MediaAssetId == mediaId)
            .Select(b => new { b.Content, b.ContentType, b.Sha256 })
            .FirstOrDefaultAsync(ct);

        if (blob is null)
            return NotFound();

        var contentType = string.IsNullOrWhiteSpace(blob.ContentType) ? "application/octet-stream" : blob.ContentType;
        var etag = new EntityTagHeaderValue($"\"{blob.Sha256}\"");
        return File(blob.Content, contentType, lastModified: null, entityTag: etag, enableRangeProcessing: true);
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
