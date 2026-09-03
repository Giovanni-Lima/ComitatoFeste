using ComitatoFeste.Api.Services;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;

namespace ComitatoFeste.Api.Filters;

/// <summary>
/// Richiede un token valido nell'header <c>Authorization: Bearer</c> (vedi <see cref="AuthService"/>).
/// Se il login è disattivato (<see cref="AuthService.Enabled"/> false) lascia passare tutto.
/// </summary>
public sealed class TokenAuthAttribute : Attribute, IAsyncAuthorizationFilter
{
    public Task OnAuthorizationAsync(AuthorizationFilterContext context)
    {
        var auth = context.HttpContext.RequestServices.GetRequiredService<AuthService>();
        if (!auth.Enabled)
            return Task.CompletedTask;

        var header = context.HttpContext.Request.Headers.Authorization.ToString();
        var token = header.StartsWith("Bearer ", StringComparison.OrdinalIgnoreCase)
            ? header["Bearer ".Length..].Trim()
            : null;

        if (auth.ValidateToken(token) is null)
            context.Result = new UnauthorizedObjectResult("Autenticazione richiesta.");

        return Task.CompletedTask;
    }
}
