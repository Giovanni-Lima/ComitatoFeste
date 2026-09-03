using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ComitatoFeste.Api.Controllers;

[ApiController]
[Route("api/auth")]
public sealed class AuthController : ControllerBase
{
    private readonly ComitatoFesteDbContext _db;
    private readonly AuthService _auth;

    public AuthController(ComitatoFesteDbContext db, AuthService auth)
    {
        _db = db;
        _auth = auth;
    }

    public sealed record LoginRequest(string? Username, string? Password);
    public sealed record LoginResponse(string Token, string Username, int MemberId, string DisplayName);

    /// <summary>Il frontend lo chiama all'avvio: se <c>enabled</c> è false salta la schermata di login.</summary>
    [HttpGet("status")]
    public IActionResult Status() => Ok(new { enabled = _auth.Enabled });

    /// <summary>
    /// Login: lo username deve corrispondere a un membro (forma <c>iniziale.cognome</c>) e la
    /// password alla passphrase condivisa. Restituisce un token da rimandare come Bearer.
    /// </summary>
    [HttpPost("login")]
    public async Task<IActionResult> Login([FromBody] LoginRequest req, CancellationToken ct)
    {
        var username = (req.Username ?? string.Empty).Trim().ToLowerInvariant();
        if (username.Length == 0)
            return BadRequest("Username mancante.");

        if (!_auth.PasswordOk(req.Password))
            return Unauthorized("Credenziali non valide.");

        var members = await _db.Members
            .Where(m => m.DisplayName != "Sistema")
            .Select(m => new { m.Id, m.DisplayName })
            .ToListAsync(ct);

        var match = members.FirstOrDefault(m =>
            string.Equals(AuthService.NormalizeUsername(m.DisplayName), username, StringComparison.Ordinal));

        if (match is null)
            return Unauthorized("Credenziali non valide.");

        return Ok(new LoginResponse(_auth.IssueToken(username), username, match.Id, match.DisplayName));
    }
}
