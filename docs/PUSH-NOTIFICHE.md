# Piano — notifiche push a fine import

Stato: **codice completo (step 1-7), test end-to-end su Chrome desktop OK — manca
il deploy (env su Render) e la prova su telefono**. Dettaglio nella sezione "Stato
implementazione" qui sotto; il resto del documento è il piano di riferimento.
Obiettivo: quando la pipeline locale (`Importer` / `Transcriber`) finisce un run con
dati nuovi, i membri che hanno installato la PWA ricevono una notifica push.

---

## Stato implementazione — aggiornato 7/9/2026

Branch: **`develop`**. **main non toccato, niente deploy.** Postgres locale migrato
(`AddPushSubscriptions` + `AddPropostaDigestPointType`).

### Fatto — step 1-3 di 7 (commit "feat: notifiche push — backend")

**Step 1 · Data model** — migration `20260907154355_AddPushSubscriptions`
(applicata al `local-postgres`; su Aiven la applica `Database.Migrate()` al boot):
- `ComitatoFeste.Domain/Entities/PushSubscription.cs` — `Id`, `Endpoint`, `P256dh`,
  `Auth`, `MemberId?`, `UserAgent?`, `CreatedAt`, `LastNotifiedAt?`.
- `ComitatoFeste.Data/Configurations/PushSubscriptionConfiguration.cs` — `Endpoint`
  UNIQUE (`UX_PushSubscriptions_Endpoint`, serve per l'upsert), FK a `Members`
  `ON DELETE SET NULL`, `CreatedAt` default `now()`.
- `DbSet<PushSubscription> PushSubscriptions` nel context.

**Step 2 · Endpoint API** — `ComitatoFeste.Api/Controllers/PushController.cs`:
- `GET /api/push/key` (aperto) → `{ publicKey }`; **503** se VAPID non configurato.
- `POST /api/push/subscribe` `[TokenAuth]` — body = `PushSubscription.toJSON()` del
  browser; **upsert su `Endpoint`**; `MemberId` ricavato dal token Bearer.
- `POST /api/push/unsubscribe` `[TokenAuth]` — delete idempotente su `Endpoint`.
- DTO in `Contracts/PushContracts.cs`.
- `Services/PushKeys.cs` (singleton) — VAPID da env `COMITATOFESTE_VAPID_PUBLIC` /
  `_PRIVATE` / `_SUBJECT`, fallback config `Vapid:*`.

**Step 3 · Invio** — pacchetto **`WebPush 1.0.13`** in `ComitatoFeste.Api.csproj`:
- `Services/PushSender.cs` — `BroadcastAsync` (tutte) / `SendToMemberAsync` (una
  persona); firma VAPID; un solo `HttpClient` (`AddHttpClient<PushSender>`);
  **prune su 404/410**; `LastNotifiedAt` aggiornata sugli invii riusciti.
- `POST /api/push/broadcast` — auth header **`X-Hook-Secret`**
  (`COMITATOFESTE_HOOK_SECRET`, confronto a tempo costante), **non** il token
  utente; body `{ title, body, url?, tag? }` → `{ sent, pruned }`.
- `POST /api/push/test` `[TokenAuth]` — notifica di prova alle subscription del
  membro loggato.
- Payload JSON `{ title, body, url, tag }` (default `url:"/"`, `tag:"digest"`).

Verificato in locale: auth `broadcast` (401 senza/errato), validazione (400),
0 subscription (`{sent:0,pruned:0}`), invio verso endpoint morto → il push service
risponde 410 → **prune** (`{sent:0,pruned:1}`, riga cancellata). L'invio
*riuscito* verso un device reale si prova nello step 5.

### Fatto — step 4-7 (commit "feat: notifiche push — sw.js, frontend, hook pipeline")

**Step 4 · Service worker** — `wwwroot/sw.js`: handler `push` (mostra la notifica,
icona `/icon-192.png`, `tag`/`renotify` per aggiornare invece di impilare) e
`notificationclick` (focus di una window esistente + `navigate` all'`url`, altrimenti
`openWindow`). `CACHE_VERSION` alzato a `"v2"`.

**Step 5 · Frontend** — `wwwroot/index.html`: bottone `#btnPush` (`🔔`) in topbar,
CSS `.pushbtn` (stato `.on` = pieno accent). Modulo JS: `pushSupported`,
`apiHasVapid()` (cache di `GET /api/push/key`), `currentPushSub()`,
`paintPushBtn(state)` (hidden/off/on/blocked/busy), `refreshPushBtn()` (nasconde
se: no supporto / login aperto / no VAPID / permesso `denied`), `enablePush()`
(`requestPermission` → `serviceWorker.ready` → `subscribe` → `POST /api/push/subscribe`
con Bearer; `localStorage["cf87_push"]`), `disablePush()` (unsubscribe lato server +
browser). `refreshPushBtn()` chiamato da `showLogin`/`hideLogin`, fine IIFE auth,
e dopo `register("/sw.js")`. Helper `urlB64ToUint8Array`. Icone `bell`/`bellOff`.

**Step 6 · Hook pipeline** — `ComitatoFeste.Data/PushHook.cs`:
`NotifyAsync(title, body, url?, tag?)`, legge `COMITATOFESTE_HOOK_URL` +
`_SECRET` (se una manca → log "salto"), `POST {url}/api/push/broadcast` con header
`X-Hook-Secret`, `HttpClient` con timeout 6 s, tutto in try/catch (non fa fallire il
run). Chiamata da:
- `Importer/Program.cs` — se `totInserted > 0`; `insertedDays` raccoglie la data da
  ogni `SourceFile`; 1 giorno → `"Digest <data>: N nuovi punti"`, `url=/?date=<data>`,
  `tag=digest-<data>`; più giorni → messaggio aggregato, `tag=digest`.
- `Transcriber/Program.cs` — se `!dryRun && ok > 0`; `doneDays` (HashSet) raccoglie
  la data Roma di ogni punto classificato; `"Digest <data>: N vocali trascritti"`,
  stesso `tag=digest-<data>` → la notifica del Transcriber **aggiorna** quella
  dell'Importer.

Verificato in locale (API con VAPID+HOOK secret, `comitatofeste-db`):
`Importer` su una giornata di test → `notifica push inviata: {"sent":0,"pruned":0}`;
`Transcriber --limit 1` → idem. La chiamata pipeline→Render→PushSender funziona
end-to-end; `sw.js`/`index.html` passano il parser.

**Step 7 · Config/doc** — `render.yaml` (+4 env `sync:false`), tabella env di
`docs/DEPLOY.md` + nota VAPID + §4 con `COMITATOFESTE_HOOK_URL/_SECRET`,
`docs/ARCHITETTURA.md` (nodo `push service`, frecce Importer/Transcriber → Render e
Render → push service, riga in tabella + paragrafo flusso dati).

### Da fare — chiusura

- ~~**Test end-to-end su Chrome desktop**~~ ✅ **fatto il 7/9/2026**: `npx web-push
  generate-vapid-keys` → API locale con quelle env → `http://localhost:5065` su
  Chrome → 🔔 → Consenti → riga in `PushSubscriptions` → `POST /api/push/broadcast`
  (`X-Hook-Secret`) → **la notifica compare e il click apre `/?date=…`**. Verificati
  anche: prune automatico di una subscription stale (SW sostituito da reload → 410 →
  `{sent:1,pruned:1}`), e recupero dopo un "Non consentire" (reset da
  `chrome://settings/content/notifications`).
- **Deploy**: impostare le env su Render (vedi sotto — **rigenerare** la coppia
  VAPID, quella di test è finita nei log di sessione), pushare `main`, mettere
  `COMITATOFESTE_HOOK_URL`/`_SECRET` sul PC per Importer/Transcriber.
- **Android / iOS**: verificare sul dominio Render (o via tunnel HTTPS). iOS solo
  da PWA installata su home, ≥ 16.4.

### Env var necessarie

| Dove | Variabili |
|---|---|
| **Render** | `COMITATOFESTE_VAPID_PUBLIC`, `COMITATOFESTE_VAPID_PRIVATE`, `COMITATOFESTE_VAPID_SUBJECT` (`mailto:giovannilima800@gmail.com`), `COMITATOFESTE_HOOK_SECRET` |
| **PC locale** (per i CLI, quando ci sarà lo step 6) | `COMITATOFESTE_HOOK_URL` (es. `https://comitatofeste.onrender.com`), `COMITATOFESTE_HOOK_SECRET` |

**Chiavi VAPID**: la coppia generata durante la sessione **non è stata committata**
(la privata è un segreto). Rigenerane una con `npx web-push generate-vapid-keys`
(oppure `WebPush.VapidHelper.GenerateVapidKeys()` da .NET) — pubblica e privata
devono essere della **stessa coppia**. `COMITATOFESTE_HOOK_SECRET` = una stringa
casuale a scelta, diversa da `COMITATOFESTE_AUTH_PASSWORD`.

### Riprendere / testare in locale

```bash
# il local-postgres ha già la tabella PushSubscriptions. Avvia l'API con le env:
COMITATOFESTE_VAPID_PUBLIC=<pub> COMITATOFESTE_VAPID_PRIVATE=<priv> \
COMITATOFESTE_VAPID_SUBJECT=mailto:giovannilima800@gmail.com \
COMITATOFESTE_HOOK_SECRET=una-stringa-a-caso \
dotnet run --project Src/backend/ComitatoFeste.Api --launch-profile http
# -> http://localhost:5065

# simula la pipeline (broadcast a tutte le subscription):
curl -X POST http://localhost:5065/api/push/broadcast \
  -H "X-Hook-Secret: una-stringa-a-caso" -H "Content-Type: application/json" \
  -d '{"title":"Comitato feste 87","body":"prova","url":"/?date=2026-09-05"}'
```

### Gotcha incontrati

- `dotnet ef` locale è **9.x su progetti net8**: dopo `migrations add` fai
  `dotnet build` del progetto Data **prima** di `has-pending-model-changes`
  (il comando guarda l'assembly compilato, non i sorgenti — altrimenti dà un
  falso "pending").
- `WebPush 1.0.13`: si costruisce con `new WebPushClient(httpClient)` — **non**
  esiste `SetHttpClient`.
- `PushController.ResolveMemberIdAsync` duplica lo schema token → member di
  `AuthController.Login`. Se lo tocchi, allinea i due (o, meglio, fai stashare
  lo username in `HttpContext.Items` dentro `TokenAuthAttribute`).
- `[TokenAuth]` lascia passare tutto se il login è disattivato: in quel caso
  `subscribe` funziona lo stesso ma con `MemberId = null`.

---

*Piano originale (riferimento per gli step 4-7):*

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
