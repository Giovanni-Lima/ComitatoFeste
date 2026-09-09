using ComitatoFeste.Api.Services;
using ComitatoFeste.Domain;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;

namespace ComitatoFeste.Api.Filters;

/// <summary>
/// Richiede un token valido nell'header <c>Authorization: Bearer</c> (vedi <see cref="AuthService"/>).
/// Se il login è disattivato (<see cref="AuthService.Enabled"/> false) lascia passare tutto.
/// Con <paramref name="requiredRole"/> valorizzato, richiede anche che il ruolo del token sia
/// almeno quello indicato (oggi nessun endpoint lo usa: pronto per future funzionalità admin-only).
/// </summary>
public sealed class TokenAuthAttribute : Attribute, IAsyncAuthorizationFilter
{
    private readonly MemberRole? _requiredRole;

    public TokenAuthAttribute()
    {
    }

    public TokenAuthAttribute(MemberRole requiredRole)
    {
        _requiredRole = requiredRole;
    }

    public Task OnAuthorizationAsync(AuthorizationFilterContext context)
    {
        var auth = context.HttpContext.RequestServices.GetRequiredService<AuthService>();
        if (!auth.Enabled)
            return Task.CompletedTask;

        var header = context.HttpContext.Request.Headers.Authorization.ToString();
        var token = header.StartsWith("Bearer ", StringComparison.OrdinalIgnoreCase)
            ? header["Bearer ".Length..].Trim()
            : null;

        var principal = auth.ValidatePrincipal(token);
        if (principal is null)
        {
            context.Result = new UnauthorizedObjectResult("Autenticazione richiesta.");
            return Task.CompletedTask;
        }

        if (_requiredRole is { } required && principal.Role < required)
            context.Result = new ObjectResult("Permessi insufficienti.") { StatusCode = StatusCodes.Status403Forbidden };

        return Task.CompletedTask;
    }
}
