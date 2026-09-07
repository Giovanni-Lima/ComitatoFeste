using System.Net.Http.Json;

namespace ComitatoFeste.Data;

/// <summary>
/// Notifica push a fine run della pipeline: <c>POST {COMITATOFESTE_HOOK_URL}/api/push/broadcast</c>
/// con header <c>X-Hook-Secret</c> (= <c>COMITATOFESTE_HOOK_SECRET</c>). Best-effort:
/// se le due env non ci sono, o la chiamata fallisce/va in timeout, si logga e basta —
/// il run della pipeline non deve fallire per una notifica.
/// </summary>
public static class PushHook
{
    private static readonly HttpClient Http = new() { Timeout = TimeSpan.FromSeconds(6) };

    public static async Task NotifyAsync(string title, string body, string? url = null, string? tag = null)
    {
        var baseUrl = Environment.GetEnvironmentVariable("COMITATOFESTE_HOOK_URL")?.Trim().TrimEnd('/');
        var secret = Environment.GetEnvironmentVariable("COMITATOFESTE_HOOK_SECRET");

        if (string.IsNullOrWhiteSpace(baseUrl) || string.IsNullOrWhiteSpace(secret))
        {
            Console.WriteLine("notifiche push: COMITATOFESTE_HOOK_URL / _SECRET non impostati — salto.");
            return;
        }

        try
        {
            using var req = new HttpRequestMessage(HttpMethod.Post, $"{baseUrl}/api/push/broadcast")
            {
                Content = JsonContent.Create(new { title, body, url, tag }),
            };
            req.Headers.Add("X-Hook-Secret", secret);

            using var res = await Http.SendAsync(req);
            var payload = (await res.Content.ReadAsStringAsync()).Trim();
            Console.WriteLine(res.IsSuccessStatusCode
                ? $"notifica push inviata: {payload}"
                : $"notifica push non riuscita: HTTP {(int)res.StatusCode} {payload}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"notifica push non inviata: {ex.Message}");
        }
    }
}
