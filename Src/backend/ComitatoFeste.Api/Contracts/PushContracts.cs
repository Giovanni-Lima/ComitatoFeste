namespace ComitatoFeste.Api.Contracts;

/// <summary>Risposta di <c>GET /api/push/key</c>: la chiave pubblica VAPID (base64url).</summary>
public sealed record PushKeyResponse(string PublicKey);

/// <summary>
/// Corpo di <c>POST /api/push/subscribe</c>. Ha la stessa forma dell'oggetto restituito da
/// <c>PushSubscription.toJSON()</c> nel browser: <c>{ endpoint, keys: { p256dh, auth } }</c>
/// (l'eventuale <c>expirationTime</c> viene ignorato).
/// </summary>
public sealed record PushSubscribeRequest(string? Endpoint, PushSubscribeKeys? Keys);

public sealed record PushSubscribeKeys(string? P256dh, string? Auth);

/// <summary>Corpo di <c>POST /api/push/unsubscribe</c>.</summary>
public sealed record PushUnsubscribeRequest(string? Endpoint);

/// <summary>
/// Corpo di <c>POST /api/push/broadcast</c>. <c>Url</c> = pagina da aprire al tap (default
/// <c>/</c>); <c>Tag</c> = raggruppa/aggiorna notifiche con lo stesso tag (default <c>digest</c>).
/// </summary>
public sealed record PushBroadcastRequest(string? Title, string? Body, string? Url, string? Tag);

/// <summary>Esito di un invio: quante notifiche partite e quante subscription potate (404/410).</summary>
public sealed record PushSendResult(int Sent, int Pruned);
