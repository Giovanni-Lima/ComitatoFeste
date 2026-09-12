using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
using ComitatoFeste.Domain;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;
using Microsoft.EntityFrameworkCore;

namespace ComitatoFeste.Api.Filters;

/// <summary>
/// Richiede un token valido nell'header <c>Authorization: Bearer</c> (vedi <see cref="AuthService"/>).
/// Se il login è disattivato (<see cref="AuthService.Enabled"/> false) lascia passare tutto.
/// Con <paramref name="requiredRole"/> valorizzato, richiede anche che il ruolo del token sia
/// almeno quello indicato (oggi nessun endpoint lo usa: pronto per future funzionalità admin-only).
/// </summary>
public sealed class TokenAuthAttribute : Attribute, IAsyncAuthorizationFilter
{
    // Sotto questa soglia non riscrive LastSeenAt: un membro che usa l'app normalmente
    // farebbe altrimenti una scrittura a ogni richiesta (lista digestpoints, toggle
    // importante, ecc.). Nessun endpoint/UI espone questo dato: solo query dirette al DB.
    private static readonly TimeSpan LastSeenThrottle = TimeSpan.FromHours(12);

    private readonly MemberRole? _requiredRole;

    public TokenAuthAttribute()
    {
    }

    public TokenAuthAttribute(MemberRole requiredRole)
    {
        _requiredRole = requiredRole;
    }

    public async Task OnAuthorizationAsync(AuthorizationFilterContext context)
    {
        var auth = context.HttpContext.RequestServices.GetRequiredService<AuthService>();
        if (!auth.Enabled)
            return;

        var header = context.HttpContext.Request.Headers.Authorization.ToString();
        var token = header.StartsWith("Bearer ", StringComparison.OrdinalIgnoreCase)
            ? header["Bearer ".Length..].Trim()
            : null;

        var principal = auth.ValidatePrincipal(token);
        if (principal is null)
        {
            context.Result = new UnauthorizedObjectResult("Autenticazione richiesta.");
            return;
        }

        if (_requiredRole is { } required && principal.Role < required)
        {
            context.Result = new ObjectResult("Permessi insufficienti.") { StatusCode = StatusCodes.Status403Forbidden };
            return;
        }

        await UpdateLastSeenAsync(context, principal.Username);
    }

    private static async Task UpdateLastSeenAsync(AuthorizationFilterContext context, string username)
    {
        var db = context.HttpContext.RequestServices.GetRequiredService<ComitatoFesteDbContext>();
        var ct = context.HttpContext.RequestAborted;

        var members = await db.Members
            .Select(m => new { m.Id, m.DisplayName, m.LastSeenAt })
            .ToListAsync(ct);
        var match = members.FirstOrDefault(m =>
            string.Equals(AuthService.NormalizeUsername(m.DisplayName), username, StringComparison.Ordinal));

        if (match is null)
            return;

        var stale = match.LastSeenAt is null || match.LastSeenAt < DateTimeOffset.UtcNow - LastSeenThrottle;
        if (!stale)
            return;

        await db.Members
            .Where(m => m.Id == match.Id)
            .ExecuteUpdateAsync(s => s.SetProperty(m => m.LastSeenAt, DateTimeOffset.UtcNow), ct);
    }
}
