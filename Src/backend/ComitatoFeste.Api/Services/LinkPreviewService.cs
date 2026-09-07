using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Text.RegularExpressions;
using ComitatoFeste.Api.Contracts;
using Microsoft.Extensions.Caching.Memory;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Ricava l'anteprima OpenGraph di un URL (titolo / descrizione / immagine / nome sito) e la
/// tiene in cache in memoria. È pensato per i soli link che compaiono davvero in un
/// <c>DigestPoint.Text</c> — il controller lo verifica prima di chiamare qui, così l'endpoint
/// non diventa un proxy di fetch generico.
///
/// Difese contro l'SSRF (l'URL arriva da testo curato, non è del tutto fidato):
/// <list type="bullet">
///   <item>solo schemi <c>http</c>/<c>https</c> (validato nel controller);</item>
///   <item>la connessione è consentita solo verso indirizzi IP pubblici: <see cref="SafeConnectAsync"/>
///     risolve il DNS e valida l'IP ad ogni hop, redirect inclusi (impostato come
///     <c>ConnectCallback</c> del <c>SocketsHttpHandler</c> in Program.cs);</item>
///   <item>massimo 3 redirect, timeout dal typed client, corpo letto e troncato a
///     <see cref="MaxBytes"/>, solo <c>Content-Type</c> HTML.</item>
/// </list>
/// </summary>
public sealed class LinkPreviewService
{
    private const int MaxBytes = 512 * 1024;
    private static readonly TimeSpan OkTtl = TimeSpan.FromHours(12);
    private static readonly TimeSpan FailTtl = TimeSpan.FromMinutes(30);
    private static readonly TimeSpan RegexTimeout = TimeSpan.FromSeconds(2);

    private readonly HttpClient _http;
    private readonly IMemoryCache _cache;

    public LinkPreviewService(HttpClient http, IMemoryCache cache)
    {
        _http = http;
        _cache = cache;
    }

    /// <summary>
    /// Anteprima dell'URL (dalla cache se presente), oppure <c>null</c> se non è ricavabile
    /// (host non raggiungibile o non consentito, nessun meta utile, errore di rete). Anche il
    /// <c>null</c> viene messo in cache, per un tempo più breve.
    /// </summary>
    public async Task<LinkPreviewDto?> GetAsync(string url, CancellationToken ct)
    {
        if (_cache.TryGetValue(CacheKey(url), out LinkPreviewDto? cached))
            return cached;

        var preview = await FetchAsync(url, ct);
        _cache.Set(CacheKey(url), preview, preview is null ? FailTtl : OkTtl);
        return preview;
    }

    private static string CacheKey(string url) => "linkpreview::" + url;

    private async Task<LinkPreviewDto?> FetchAsync(string url, CancellationToken ct)
    {
        try
        {
            using var req = new HttpRequestMessage(HttpMethod.Get, url);
            req.Headers.UserAgent.ParseAdd("Mozilla/5.0 (compatible; ComitatoFesteBot/1.0; +link-preview)");
            req.Headers.Accept.ParseAdd("text/html,application/xhtml+xml");

            using var resp = await _http.SendAsync(req, HttpCompletionOption.ResponseHeadersRead, ct);
            if (!resp.IsSuccessStatusCode)
                return null;

            var mediaType = resp.Content.Headers.ContentType?.MediaType;
            if (mediaType is not ("text/html" or "application/xhtml+xml"))
                return null;

            var html = await ReadCappedAsync(resp.Content, ct);
            var finalUrl = resp.RequestMessage?.RequestUri ?? new Uri(url);

            var title = Meta(html, "og:title") ?? TitleTag(html);
            var description = Meta(html, "og:description") ?? MetaByAttr(html, "name", "description");
            var image = Meta(html, "og:image") ?? Meta(html, "og:image:url");
            var siteName = Meta(html, "og:site_name") ?? finalUrl.Host;

            if (title is null && description is null && image is null)
                return null;

            return new LinkPreviewDto
            {
                Url = url,
                Title = Clean(title),
                Description = Clean(description),
                Image = AbsoluteHttpUrl(image, finalUrl),
                SiteName = Clean(siteName),
            };
        }
        catch (Exception ex) when (ex is HttpRequestException
                                   or TaskCanceledException
                                   or OperationCanceledException
                                   or IOException
                                   or InvalidOperationException
                                   or UriFormatException
                                   or RegexMatchTimeoutException)
        {
            return null;
        }
    }

    private static async Task<string> ReadCappedAsync(HttpContent content, CancellationToken ct)
    {
        await using var stream = await content.ReadAsStreamAsync(ct);
        var buffer = new byte[MaxBytes];
        var read = 0;
        while (read < MaxBytes)
        {
            var n = await stream.ReadAsync(buffer.AsMemory(read, MaxBytes - read), ct);
            if (n == 0) break;
            read += n;
        }
        return Encoding.UTF8.GetString(buffer, 0, read);
    }

    // --- estrazione meta tag (regex sul <head>: sufficiente allo scopo, zero dipendenze) ---

    private static string? Meta(string html, string property) =>
        MetaByAttr(html, "property", property) ?? MetaByAttr(html, "name", property);

    private static string? MetaByAttr(string html, string attr, string value)
    {
        // <meta property="og:title" content="..."> con attributi in ordine qualunque e apici ' o ".
        var tag = Regex.Match(
            html,
            $"<meta\\b[^>]*?\\b{attr}\\s*=\\s*([\"']){Regex.Escape(value)}\\1[^>]*>",
            RegexOptions.IgnoreCase | RegexOptions.Singleline,
            RegexTimeout);
        if (!tag.Success)
            return null;

        var content = Regex.Match(
            tag.Value,
            "\\bcontent\\s*=\\s*([\"'])(.*?)\\1",
            RegexOptions.IgnoreCase | RegexOptions.Singleline,
            RegexTimeout);
        return content.Success ? content.Groups[2].Value : null;
    }

    private static string? TitleTag(string html)
    {
        var m = Regex.Match(html, "<title\\b[^>]*>(.*?)</title>",
            RegexOptions.IgnoreCase | RegexOptions.Singleline, RegexTimeout);
        return m.Success ? m.Groups[1].Value : null;
    }

    private static string? Clean(string? s)
    {
        if (string.IsNullOrWhiteSpace(s))
            return null;
        s = Regex.Replace(WebUtility.HtmlDecode(s).Trim(), "\\s+", " ", RegexOptions.None, RegexTimeout);
        return s.Length > 300 ? s[..300].TrimEnd() + "…" : s;
    }

    private static string? AbsoluteHttpUrl(string? value, Uri baseUri)
    {
        if (string.IsNullOrWhiteSpace(value))
            return null;
        if (!Uri.TryCreate(baseUri, WebUtility.HtmlDecode(value).Trim(), out var abs))
            return null;
        return abs.Scheme is "http" or "https" ? abs.ToString() : null;
    }

    // --- guardia SSRF: connette solo verso IP pubblici (usata come ConnectCallback) ---

    /// <summary>
    /// <c>ConnectCallback</c> per il <c>SocketsHttpHandler</c> del typed client: risolve l'host,
    /// scarta gli indirizzi non pubblici (loopback, LAN, link-local, CGNAT, multicast…) e apre
    /// il socket solo verso i rimanenti. Viene invocata anche per ogni redirect.
    /// </summary>
    public static async ValueTask<Stream> SafeConnectAsync(SocketsHttpConnectionContext ctx, CancellationToken ct)
    {
        var host = ctx.DnsEndPoint.Host;
        var addresses = await Dns.GetHostAddressesAsync(host, ct);
        var allowed = Array.FindAll(addresses, IsPublic);
        if (allowed.Length == 0)
            throw new IOException($"host non consentito per l'anteprima link: {host}");

        var socket = new Socket(SocketType.Stream, ProtocolType.Tcp) { NoDelay = true };
        try
        {
            await socket.ConnectAsync(allowed, ctx.DnsEndPoint.Port, ct);
            return new NetworkStream(socket, ownsSocket: true);
        }
        catch
        {
            socket.Dispose();
            throw;
        }
    }

    private static bool IsPublic(IPAddress ip)
    {
        if (IPAddress.IsLoopback(ip))
            return false;

        if (ip.AddressFamily == AddressFamily.InterNetworkV6)
        {
            if (ip.IsIPv4MappedToIPv6)
                return IsPublic(ip.MapToIPv4());
            return !(ip.IsIPv6LinkLocal || ip.IsIPv6SiteLocal || ip.IsIPv6UniqueLocal || ip.IsIPv6Multicast);
        }

        var b = ip.GetAddressBytes();
        return b[0] switch
        {
            0 or 10 or 127 => false,                              // "questo host", 10/8, loopback
            100 when b[1] is >= 64 and <= 127 => false,           // CGNAT 100.64/10
            169 when b[1] == 254 => false,                        // link-local (incl. 169.254.169.254)
            172 when b[1] is >= 16 and <= 31 => false,            // 172.16/12
            192 when b[1] == 168 => false,                        // 192.168/16
            192 when b[1] == 0 && b[2] == 0 => false,             // 192.0.0/24 (IETF protocol assignments)
            198 when b[1] is 18 or 19 => false,                   // 198.18/15 (benchmarking)
            >= 224 => false,                                      // multicast + riservato
            _ => true,
        };
    }
}
