using ComitatoFeste.Api.Filters;
using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ComitatoFeste.Api.Controllers;

[ApiController]
[Route("api/links")]
public sealed class LinksController : ControllerBase
{
    private readonly ComitatoFesteDbContext _db;
    private readonly LinkPreviewService _previews;

    public LinksController(ComitatoFesteDbContext db, LinkPreviewService previews)
    {
        _db = db;
        _previews = previews;
    }

    /// <summary>
    /// Anteprima OpenGraph (titolo, descrizione, immagine, sito) di un link.
    /// Restituisce l'anteprima solo se l'<c>url</c> compare in un <c>DigestPoint.Text</c>:
    /// così l'endpoint non è utilizzabile come proxy di fetch verso URL arbitrari.
    /// <c>204</c> se non c'è un'anteprima ricavabile, <c>404</c> se l'URL non è tra i punti.
    /// </summary>
    [HttpGet("preview")]
    [TokenAuth]
    public async Task<IActionResult> GetPreview([FromQuery] string? url, CancellationToken ct)
    {
        if (string.IsNullOrWhiteSpace(url)
            || !Uri.TryCreate(url, UriKind.Absolute, out var uri)
            || (uri.Scheme != Uri.UriSchemeHttp && uri.Scheme != Uri.UriSchemeHttps))
            return BadRequest("Parametro 'url' non valido: richiesto un URL http/https assoluto.");

        var known = await _db.DigestPoints.AnyAsync(d => d.Text.Contains(url), ct);
        if (!known)
            return NotFound("URL non presente in nessun punto del digest.");

        var preview = await _previews.GetAsync(url, ct);
        return preview is null ? NoContent() : Ok(preview);
    }
}
