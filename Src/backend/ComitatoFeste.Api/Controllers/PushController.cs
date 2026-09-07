using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using ComitatoFeste.Api.Contracts;
using ComitatoFeste.Api.Filters;
using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
using ComitatoFeste.Domain;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ComitatoFeste.Api.Controllers;

[ApiController]
[Route("api/push")]
public sealed class PushController : ControllerBase
{
    private readonly ComitatoFesteDbContext _db;
    private readonly AuthService _auth;
    private readonly PushKeys _keys;
    private readonly PushSender _sender;
    private readonly string? _hookSecret;

    public PushController(ComitatoFesteDbContext db, AuthService auth, PushKeys keys, PushSender sender, IConfiguration config)
    {
        _db = db;
        _auth = auth;
        _keys = keys;
        _sender = sender;
        var secret = Environment.GetEnvironmentVariable("COMITATOFESTE_HOOK_SECRET") ?? config["Push:HookSecret"];
        _hookSecret = string.IsNullOrWhiteSpace(secret) ? null : secret;
    }

    /// <summary>
    /// Chiave pubblica VAPID, che il frontend passa a <c>pushManager.subscribe</c>.
    /// 503 se le chiavi non sono configurate sull'API (il frontend nasconde il bottone 🔔).
    /// </summary>
    [HttpGet("key")]
    public IActionResult GetKey() =>
        _keys.IsConfigured
            ? Ok(new PushKeyResponse(_keys.PublicKey!))
            : StatusCode(StatusCodes.Status503ServiceUnavailable, "VAPID non configurato sull'API.");

    /// <summary>
    /// Registra o aggiorna la subscription Web Push del browser corrente. Body = l'oggetto
    /// di <c>PushSubscription.toJSON()</c>. Upsert sull'<c>Endpoint</c> (una re-subscribe dallo
    /// stesso browser aggiorna la riga); <c>MemberId</c> risolto dal token, se il login è attivo.
    /// </summary>
    [HttpPost("subscribe")]
    [TokenAuth]
    public async Task<IActionResult> Subscribe([FromBody] PushSubscribeRequest req, CancellationToken ct)
    {
        if (string.IsNullOrWhiteSpace(req.Endpoint)
            || req.Keys is null
            || string.IsNullOrWhiteSpace(req.Keys.P256dh)
            || string.IsNullOrWhiteSpace(req.Keys.Auth))
            return BadRequest("Subscription incompleta: servono endpoint e keys.p256dh/auth.");

        var memberId = await ResolveMemberIdAsync(ct);

        var ua = Request.Headers.UserAgent.ToString();
        if (ua.Length > 400) ua = ua[..400];
        if (string.IsNullOrWhiteSpace(ua)) ua = null;

        var existing = await _db.PushSubscriptions.FirstOrDefaultAsync(s => s.Endpoint == req.Endpoint, ct);
        if (existing is null)
        {
            _db.PushSubscriptions.Add(new PushSubscription
            {
                Endpoint = req.Endpoint!,
                P256dh = req.Keys.P256dh!,
                Auth = req.Keys.Auth!,
                MemberId = memberId,
                UserAgent = ua,
            });
        }
        else
        {
            existing.P256dh = req.Keys.P256dh!;
            existing.Auth = req.Keys.Auth!;
            existing.MemberId = memberId ?? existing.MemberId;   // non perdere l'associazione se il token manca
            if (ua is not null) existing.UserAgent = ua;
        }

        await _db.SaveChangesAsync(ct);
        return NoContent();
    }

    /// <summary>Rimuove la subscription con quell'<c>Endpoint</c> (idempotente: 204 anche se non c'era).</summary>
    [HttpPost("unsubscribe")]
    [TokenAuth]
    public async Task<IActionResult> Unsubscribe([FromBody] PushUnsubscribeRequest req, CancellationToken ct)
    {
        if (string.IsNullOrWhiteSpace(req.Endpoint))
            return BadRequest("Endpoint mancante.");

        await _db.PushSubscriptions.Where(s => s.Endpoint == req.Endpoint).ExecuteDeleteAsync(ct);
        return NoContent();
    }

    /// <summary>
    /// Invia una notifica a <b>tutte</b> le subscription. Chiamato dalla pipeline locale
    /// (Importer/Transcriber) a fine run: autenticazione con header <c>X-Hook-Secret</c>
    /// (<c>COMITATOFESTE_HOOK_SECRET</c>), <b>non</b> il token utente. Pota le subscription
    /// non più valide. → <c>{ sent, pruned }</c>.
    /// </summary>
    [HttpPost("broadcast")]
    public async Task<IActionResult> Broadcast([FromBody] PushBroadcastRequest req, CancellationToken ct)
    {
        if (_hookSecret is null)
            return StatusCode(StatusCodes.Status503ServiceUnavailable, "COMITATOFESTE_HOOK_SECRET non configurato sull'API.");

        var provided = Request.Headers["X-Hook-Secret"].ToString();
        if (!CryptographicOperations.FixedTimeEquals(
                Encoding.UTF8.GetBytes(provided), Encoding.UTF8.GetBytes(_hookSecret)))
            return Unauthorized("X-Hook-Secret non valido.");

        if (string.IsNullOrWhiteSpace(req.Title) || string.IsNullOrWhiteSpace(req.Body))
            return BadRequest("title e body sono obbligatori.");

        if (!_sender.IsConfigured)
            return StatusCode(StatusCodes.Status503ServiceUnavailable, "VAPID non configurato: impossibile inviare.");

        var (sent, pruned) = await _sender.BroadcastAsync(
            BuildPayload(req.Title!, req.Body!, req.Url, req.Tag), ct);
        return Ok(new PushSendResult(sent, pruned));
    }

    /// <summary>Manda una notifica di prova alle sole subscription del membro loggato.</summary>
    [HttpPost("test")]
    [TokenAuth]
    public async Task<IActionResult> Test(CancellationToken ct)
    {
        if (!_sender.IsConfigured)
            return StatusCode(StatusCodes.Status503ServiceUnavailable, "VAPID non configurato sull'API.");

        var memberId = await ResolveMemberIdAsync(ct);
        if (memberId is null)
            return BadRequest("Nessun membro associato al token: attiva prima le notifiche.");

        var (sent, pruned) = await _sender.SendToMemberAsync(
            memberId.Value, BuildPayload("Comitato feste 87", "Notifica di prova ✅", "/", "test"), ct);

        return sent == 0 && pruned == 0
            ? NotFound("Nessuna subscription per questo membro.")
            : Ok(new PushSendResult(sent, pruned));
    }

    private static string BuildPayload(string title, string body, string? url, string? tag) =>
        JsonSerializer.Serialize(new
        {
            title,
            body,
            url = string.IsNullOrWhiteSpace(url) ? "/" : url,
            tag = string.IsNullOrWhiteSpace(tag) ? "digest" : tag,
        });

    /// <summary>
    /// Ricava il <c>MemberId</c> dal token Bearer (stesso schema di <see cref="AuthController"/>):
    /// <c>null</c> se il login è disattivato, il token manca/è scaduto, o lo username non
    /// corrisponde a nessun membro.
    /// </summary>
    private async Task<int?> ResolveMemberIdAsync(CancellationToken ct)
    {
        if (!_auth.Enabled)
            return null;

        var header = Request.Headers.Authorization.ToString();
        var token = header.StartsWith("Bearer ", StringComparison.OrdinalIgnoreCase)
            ? header["Bearer ".Length..].Trim()
            : null;

        var username = _auth.ValidateToken(token);
        if (string.IsNullOrEmpty(username))
            return null;

        var members = await _db.Members
            .Where(m => m.DisplayName != "Sistema")
            .Select(m => new { m.Id, m.DisplayName })
            .ToListAsync(ct);

        return members
            .FirstOrDefault(m => string.Equals(
                AuthService.NormalizeUsername(m.DisplayName), username, StringComparison.Ordinal))
            ?.Id;
    }
}
