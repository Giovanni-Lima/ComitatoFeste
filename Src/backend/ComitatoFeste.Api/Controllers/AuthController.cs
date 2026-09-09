using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
using ComitatoFeste.Domain;
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
    public sealed record LoginResponse(string Token, string Username, int MemberId, string DisplayName, string Role);

    /// <summary>Il frontend lo chiama all'avvio: se <c>enabled</c> è false salta la schermata di login.</summary>
    [HttpGet("status")]
    public IActionResult Status() => Ok(new { enabled = _auth.Enabled });

    /// <summary>
    /// Login: lo username deve corrispondere a un membro (forma <c>iniziale.cognome</c>). Due
    /// passphrase condivise: quella lettore vale per chiunque (token Lettore); quella admin eleva
    /// a token Amministratore ma solo se il membro ha già quel ruolo a DB — un lettore che la
    /// indovina resta comunque fuori. Restituisce un token da rimandare come Bearer.
    /// </summary>
    [HttpPost("login")]
    public async Task<IActionResult> Login([FromBody] LoginRequest req, CancellationToken ct)
    {
        var username = (req.Username ?? string.Empty).Trim().ToLowerInvariant();
        if (username.Length == 0)
            return BadRequest("Username mancante.");

        var members = await _db.Members
            .Where(m => m.DisplayName != "Sistema")
            .Select(m => new { m.Id, m.DisplayName, m.Role })
            .ToListAsync(ct);

        var match = members.FirstOrDefault(m =>
            string.Equals(AuthService.NormalizeUsername(m.DisplayName), username, StringComparison.Ordinal));

        if (match is null)
            return Unauthorized("Credenziali non valide.");

        MemberRole role;
        if (_auth.AdminPasswordOk(req.Password))
        {
            if (match.Role != MemberRole.Amministratore)
                return Unauthorized("Credenziali non valide.");
            role = MemberRole.Amministratore;
        }
        else if (_auth.ReaderPasswordOk(req.Password))
        {
            role = MemberRole.Lettore;
        }
        else
        {
            return Unauthorized("Credenziali non valide.");
        }

        var roleName = role.ToString().ToLowerInvariant();
        return Ok(new LoginResponse(_auth.IssueToken(username, role), username, match.Id, match.DisplayName, roleName));
    }
}
