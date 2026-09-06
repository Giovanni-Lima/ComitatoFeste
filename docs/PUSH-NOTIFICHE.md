# Piano — notifiche push a fine import

Stato: **piano, non implementato**. Obiettivo: quando la pipeline locale
(`Importer` / `Transcriber`) finisce un run con dati nuovi, i membri che hanno
installato la PWA ricevono una notifica push.

Scelte già fissate con l'utente:

- **Trigger**: `Importer` e `Transcriber`, a fine run, fanno `POST` a un endpoint
  su Render con un secret condiviso. La chiave VAPID privata resta solo su Render
  (un solo punto d'invio).
- **Attivazione**: bottone **"🔔 Attiva notifiche"** in topbar del frontend, visibile
  dopo il login se il permesso non è ancora stato dato/negato. Niente prompt a
  sorpresa all'avvio.

```
Importer/Transcriber (PC)
   └─ POST /api/push/broadcast  { title, body, url }  + header X-Hook-Secret
        │
        ▼
Render · ComitatoFeste.Api
   ├─ legge le subscription da Aiven (tabella PushSubscriptions)
   ├─ per ognuna: Web Push firmato VAPID  ──▶  push service (Google/Apple/Mozilla)
   └─ elimina le subscription che rispondono 404/410
        │
        ▼
service worker sw.js  ──▶  notifica sul dispositivo  ──(tap)──▶  /?date=<data>
```

---

## 1 · Chiavi VAPID (una tantum)

Generare una coppia (es. `npx web-push generate-vapid-keys`, oppure con la libreria
.NET). Tre valori:

| Env (Render) | Contenuto |
|---|---|
| `COMITATOFESTE_VAPID_PUBLIC` | chiave pubblica base64url — servita al frontend da `GET /api/push/key` |
| `COMITATOFESTE_VAPID_PRIVATE` | chiave privata — **solo** su Render |
| `COMITATOFESTE_VAPID_SUBJECT` | `mailto:giovannilima800@gmail.com` (richiesto dallo spec VAPID) |

La pubblica **non** va hardcodata nel frontend (è statico, cambiarla richiederebbe
un redeploy): la serve l'API.

---

## 2 · Data model

Nuova entità `ComitatoFeste.Domain/Entities/PushSubscription.cs`:

| Colonna | Tipo | Note |
|---|---|---|
| `Id` | int identity | PK |
| `Endpoint` | text | **UNIQUE** — l'URL del push service, identifica la subscription |
| `P256dh` | text | chiave pubblica del client |
| `Auth` | text | secret di autenticazione del client |
| `MemberId` | int NULL | FK → `Members(Id)` `ON DELETE SET NULL` — chi l'ha attivata |
| `UserAgent` | varchar(400) NULL | solo per debug |
| `CreatedAt` | timestamptz | default `now()` |
| `LastNotifiedAt` | timestamptz NULL | aggiornata a ogni invio riuscito |

- `Configurations/PushSubscriptionConfiguration.cs` (Fluent API, come le altre).
- `DbSet<PushSubscription> PushSubscriptions` nel context.
- Migration `AddPushSubscriptions` nel progetto `ComitatoFeste.Data` — applicata
  in automatico da `Database.Migrate()` al boot (Render e locale).

---

## 3 · Endpoint API

DTO in `ComitatoFeste.Api/Contracts/`. Stile coerente con gli endpoint esistenti.

| Metodo · rotta | Auth | Body / risposta |
|---|---|---|
| `GET /api/push/key` | aperto | → `{ "publicKey": "<base64url>" }` |
| `POST /api/push/subscribe` | `[TokenAuth]` | body = `PushSubscription.toJSON()` del browser (`{ endpoint, keys:{ p256dh, auth } }`); `MemberId` preso dal token. **Upsert** su `Endpoint`. → 204 |
| `POST /api/push/unsubscribe` | `[TokenAuth]` | `{ "endpoint": "…" }` → delete → 204 |
| `POST /api/push/broadcast` | **secret** (`X-Hook-Secret: <COMITATOFESTE_HOOK_SECRET>`, non il token utente) | `{ title, body, url?, tag? }` → invia a tutte, pota le 404/410 → `{ "sent": n, "pruned": m }` |
| `POST /api/push/test` *(opz.)* | `[TokenAuth]` | manda una notifica di prova alle subscription del membro |

Nota: `subscribe`/`unsubscribe` sono `[TokenAuth]` perché il membro è loggato
quando preme il bottone. Se un domani il login venisse disattivato, renderli
aperti o gestire `MemberId == null`.

---

## 4 · Invio — libreria

- Aggiungere il pacchetto **`WebPush`** (NuGet, port .NET di web-push) a
  `ComitatoFeste.Api.csproj`.
- Service `PushSender`:
  - legge `COMITATOFESTE_VAPID_*` da env;
  - `SendAsync(sub, payloadJson)` → `WebPushClient.SendNotificationAsync`;
  - su `WebPushException` con `StatusCode` **404/410** → segnala "prune" (la
    subscription non esiste più, va cancellata); altri errori → log e continua.
- Payload JSON: `{ "title": …, "body": …, "url": …, "tag": … }`.

---

## 5 · Service worker (`wwwroot/sw.js`)

Verificare prima che non ci sia già un handler `push` e che lo scope copra `/`.
Aggiungere:

```js
self.addEventListener("push", (e) => {
  const d = (() => { try { return e.data.json(); } catch { return {}; } })();
  e.waitUntil(self.registration.showNotification(d.title || "Comitato feste 87", {
    body: d.body || "",
    icon: "/icon-192.png",
    badge: "/icon-192.png",
    tag: d.tag || "digest",          // stesso tag ⇒ la notifica si aggiorna invece di impilarsi
    renotify: true,
    data: { url: d.url || "/" },
  }));
});

self.addEventListener("notificationclick", (e) => {
  e.notification.close();
  const url = (e.notification.data && e.notification.data.url) || "/";
  e.waitUntil((async () => {
    const wins = await clients.matchAll({ type: "window", includeUncontrolled: true });
    for (const c of wins) {
      if (c.url.startsWith(location.origin)) { await c.focus(); c.navigate(url); return; }
    }
    await clients.openWindow(url);
  })());
});
```

---

## 6 · Frontend (`wwwroot/index.html`)

Bottone `🔔` in topbar con tre stati:

| Stato | Condizione | Aspetto |
|---|---|---|
| nascosto | `!("PushManager" in window)` o `!("serviceWorker" in navigator)` | — |
| da attivare | `Notification.permission !== "granted"` **o** nessuna subscription | 🔔 outline, cliccabile |
| attivo | permesso `granted` + subscription presente | 🔔 pieno; click = disattiva |
| bloccato | `Notification.permission === "denied"` | 🔔 disabilitato, tooltip "abilita dalle impostazioni del browser" |

**Attiva** (al click):
1. `await Notification.requestPermission()` → se non `granted`, stop.
2. `const reg = await navigator.serviceWorker.ready`
3. `const { publicKey } = await (await fetch(API + "/api/push/key")).json()`
4. `const sub = await reg.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey: urlB64ToUint8Array(publicKey) })`
5. `POST /api/push/subscribe` con `JSON.stringify(sub)` + `Authorization: Bearer`
6. `localStorage.setItem("cf87_push", "1")`, aggiorna icona.

**Disattiva**: `const sub = await reg.pushManager.getSubscription(); await sub?.unsubscribe(); POST /api/push/unsubscribe {endpoint}`; pulisci `cf87_push`.

**Al load**: se `Notification.permission === "granted"` e
`reg.pushManager.getSubscription()` restituisce una sub → stato "attivo".

Helper `urlB64ToUint8Array` (standard, ~6 righe).

---

## 7 · Hook nella pipeline

- Classe condivisa `PushHook` in **`ComitatoFeste.Data`** (già referenziata da
  Importer e Transcriber): `Task NotifyAsync(string title, string body, string url)`.
  - legge `COMITATOFESTE_HOOK_URL` (es. `https://comitatofeste.onrender.com`) e
    `COMITATOFESTE_HOOK_SECRET` da env; se una manca → **skip silenzioso** (log
    "notifiche push disattivate: HOOK_URL/SECRET non impostati").
  - `POST {HOOK_URL}/api/push/broadcast` con header `X-Hook-Secret`, timeout 5 s,
    best-effort: un errore **non** fa fallire il run (try/catch + log).
- `Importer/Program.cs`: dopo il riepilogo, se `totInserted > 0` →
  `await PushHook.NotifyAsync("Comitato feste 87", $"Digest {data} aggiornato — {totInserted} nuovi punti", $"/?date={data}")`.
  (`data` = la data del/dei file importati; se più file, citarne il conteggio.)
- `Transcriber/Program.cs`: se `trascritti > 0` →
  `"Digest {data}: {n} vocali trascritti"`, stesso `url`, `tag = "digest-{data}"`.
- **Tag per giorno** (`digest-<data>`): se Importer e Transcriber girano in
  sequenza, la seconda notifica **aggiorna** la prima invece di impilarsi.

---

## 8 · Config — nuove env var

| Dove | Variabili |
|---|---|
| **Render** (tab Environment, `sync:false` in `render.yaml`) | `COMITATOFESTE_VAPID_PUBLIC`, `COMITATOFESTE_VAPID_PRIVATE`, `COMITATOFESTE_VAPID_SUBJECT`, `COMITATOFESTE_HOOK_SECRET` |
| **PC locale** (per i CLI) | `COMITATOFESTE_HOOK_URL`, `COMITATOFESTE_HOOK_SECRET` |

Aggiornare `render.yaml`, la tabella env di `docs/DEPLOY.md` e lo schema di
`docs/ARCHITETTURA.md` (nuova freccia Importer/Transcriber → Render, e
Render → push service).

---

## 9 · Test

1. Locale (`docker compose up`), Chrome desktop: premi "Attiva notifiche",
   verifica la riga in `PushSubscriptions`.
2. `POST /api/push/test` → arriva la notifica.
3. `curl -X POST .../api/push/broadcast -H "X-Hook-Secret: …" -d '{"title":"x","body":"y"}'`.
4. Lancia `Importer` con un digest nuovo → notifica "N nuovi punti", il tap apre
   il giorno giusto.
5. Prune: cancella la subscription dal browser (DevTools → Application → Service
   Workers → Push) e verifica che il broadcast successivo la rimuova dal DB.

---

## 10 · Caveat

- **iOS**: Web Push funziona **solo** da PWA installata su home, iOS ≥ 16.4.
  `userVisibleOnly: true` è obbligatorio ovunque.
- **Cold start Render**: il primo `POST /api/push/broadcast` dopo inattività paga
  ~40-60 s (il container si sveglia). Accettabile — è il PC a chiamare, il run è
  già finito.
- **Doppio invio**: gestito col `tag` per giorno (vedi §7). In alternativa, far
  notificare solo il `Transcriber` se gira sempre come ultimo passo.
- **Dati personali**: si salvano endpoint push legati a un `MemberId`. Comitato di
  paese, ma vale una riga nell'eventuale informativa; l'unsubscribe cancella la
  riga.
- **Secret**: `COMITATOFESTE_HOOK_SECRET` è separato dalla passphrase utente —
  non riusare `COMITATOFESTE_AUTH_PASSWORD`.

---

## Stima

File toccati/nuovi: entità + configuration + migration (3), `PushSender` +
`PushHook` (2), endpoint + DTO (2-3), `sw.js` (+~30 righe), `index.html`
(+~80 righe), `csproj` (+1 pacchetto), `render.yaml` + doc. Feature media —
mezza giornata, tutta testabile in locale tranne iOS.
