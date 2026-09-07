using System.Net;
using ComitatoFeste.Data;
using Microsoft.EntityFrameworkCore;
using WebPush;
using LibSubscription = WebPush.PushSubscription;
using DbSubscription = ComitatoFeste.Domain.PushSubscription;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Invia notifiche Web Push firmate VAPID alle subscription salvate (<see cref="PushKeys"/> per
/// le chiavi). Le subscription che il push service segnala come non più valide — HTTP
/// <b>404/410</b> — vengono cancellate ("prune"); gli altri errori sono loggati e non fermano il
/// giro. L'<see cref="WebPushClient"/> riusa un unico <see cref="HttpClient"/> (typed client).
/// </summary>
public sealed class PushSender
{
    private readonly ComitatoFesteDbContext _db;
    private readonly PushKeys _keys;
    private readonly ILogger<PushSender> _log;
    private readonly WebPushClient _client;

    public PushSender(HttpClient http, ComitatoFesteDbContext db, PushKeys keys, ILogger<PushSender> log)
    {
        _db = db;
        _keys = keys;
        _log = log;
        _client = new WebPushClient(http);
    }

    /// <summary>Chiavi VAPID presenti: si può inviare.</summary>
    public bool IsConfigured => _keys.IsConfigured;

    /// <summary>Invia lo stesso payload a tutte le subscription. Ritorna (inviate con successo, potate).</summary>
    public Task<(int Sent, int Pruned)> BroadcastAsync(string payloadJson, CancellationToken ct) =>
        SendAsync(_db.PushSubscriptions, payloadJson, ct);

    /// <summary>Invia alle sole subscription di un membro (usato dalla notifica di prova).</summary>
    public Task<(int Sent, int Pruned)> SendToMemberAsync(int memberId, string payloadJson, CancellationToken ct) =>
        SendAsync(_db.PushSubscriptions.Where(s => s.MemberId == memberId), payloadJson, ct);

    private async Task<(int Sent, int Pruned)> SendAsync(
        IQueryable<DbSubscription> query, string payloadJson, CancellationToken ct)
    {
        if (!IsConfigured)
            return (0, 0);

        var subs = await query.ToListAsync(ct);
        if (subs.Count == 0)
            return (0, 0);

        var vapid = new VapidDetails(_keys.Subject, _keys.PublicKey, _keys.PrivateKey);
        var sent = 0;
        var stale = new List<DbSubscription>();

        foreach (var s in subs)
        {
            ct.ThrowIfCancellationRequested();
            try
            {
                await _client.SendNotificationAsync(
                    new LibSubscription(s.Endpoint, s.P256dh, s.Auth), payloadJson, vapid);
                s.LastNotifiedAt = DateTimeOffset.UtcNow;
                sent++;
            }
            catch (WebPushException ex) when (
                ex.StatusCode is HttpStatusCode.NotFound or HttpStatusCode.Gone)
            {
                stale.Add(s);   // subscription non più valida: da cancellare
            }
            catch (Exception ex)
            {
                _log.LogWarning(ex, "Push verso {Endpoint} fallito", Trunc(s.Endpoint));
            }
        }

        if (stale.Count > 0)
            _db.PushSubscriptions.RemoveRange(stale);
        if (sent > 0 || stale.Count > 0)
            await _db.SaveChangesAsync(ct);

        return (sent, stale.Count);
    }

    private static string Trunc(string s) => s.Length <= 80 ? s : s[..80] + "…";
}
