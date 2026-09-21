# ComitatoFeste — istruzioni per Claude Code

## Cos'è questo repo

Data/API layer (EF Core Code-First su Postgres) di una pipeline più ampia
che riassume automaticamente la chat WhatsApp del gruppo "Comitato feste
87": legge i messaggi, li classifica (decisione/proposta/domanda/media/info),
scarica i media (foto, audio, documenti) e li persiste. Contesto completo
e razionale delle decisioni: @docs/CONTEXT.md. Istruzioni di setup/build:
@README.md.

## Stato attuale — leggi prima di toccare codice

Il backend .NET compila pulito e gira contro Postgres locale.

- **Solution**: `Src/backend/ComitatoFeste.slnx` — build con `dotnet build
  Src/backend/ComitatoFeste.slnx`. I progetti targettano `net8.0`; in
  macchina non c'è l'SDK 8 (solo 9/10) quindi i reference pack .NET 8
  arrivano da NuGet — funziona, ma per coerenza totale servirebbe l'SDK 8
  + un `global.json`.
- **DB locale = container `comitatofeste-db`** (dal 21/9/2026): definito da
  `docker-compose.db.yml` **nel repo** (`docker compose -f docker-compose.db.yml
  up -d`), immagine **`pgvector/pgvector:pg16`** (serve l'estensione `vector`
  per l'assistente AI, vedi sotto), dati in `./data/postgres/` (gitignorato,
  locale `C`), porta 5432, db `postgres`, `postgres/postgres`. Il vecchio
  container esterno `local-postgres` (compose `Desktop\Local Env`, ospitava
  anche `GatelockVanRules` di un altro progetto) è **fermato** per liberare la
  5432 e non va riavviato mentre gira `comitatofeste-db`; il suo vecchio
  `pgdata` alpine è conservato in
  `Desktop\Local Env\data\postgres\pgdata.bak-alpine-20260921`. Passare tra
  immagini alpine/Debian sullo stesso `pgdata` cambia la collation: si migra
  sempre con `pg_dump`/restore, mai riusando la cartella dati.
- **Migration applicate** a `comitatofeste-db`:
  `InitialCreate` + `AddMediaBlobs` + `AddMemberProfilePhotos` +
  `AddRumoreDigestPointType` (`'rumore'` nel CHECK di `DigestPoints.Type`) +
  `AddVerbali` (tabella `Verbali`: verbale giornaliero in cache, UNIQUE
  `(GroupId, Date)`) + `AddPropostaDigestPointType` (`'proposta'` nel CHECK
  di `DigestPoints.Type`: idea/proposta operativa non ancora decisa —
  distinta da `decisione`) + `AddPushSubscriptions` (tabella
  `PushSubscriptions`, `Endpoint` UNIQUE — notifiche push PWA, vedi
  `docs/PUSH-NOTIFICHE.md`) + `AddMemberRole` (colonna `Members.Role`,
  CHECK `'lettore'|'amministratore'`, default `lettore` — vedi login sotto) +
  `AddDigestPointImportant` (colonna `DigestPoints.IsImportant`, bool,
  default `false` — flag "importante" toggleabile solo dagli admin, vedi
  `PUT /api/digestpoints/{id}/important` sotto) + `AddImageThumbnails`
  (tabella `ImageThumbnails`: WebP ridimensionati e persistiti delle immagini
  servite dagli endpoint blob, chiave UNIQUE `(Kind, SourceId, Width)`, niente
  FK — vedi `?w=` e `ImageThumbnailer` sotto) + `AddMemberLastSeenAt` (colonna
  `Members.LastSeenAt`) + **`AddDigestPointEmbeddings`** (tabella
  `DigestPointEmbeddings`, `vector(768)`, estensione `vector` — **solo sul
  branch `feature/assistente_ai` e solo in locale**, vedi "Assistente AI").
  Tutte le migration **tranne l'ultima** sono applicate anche ad **Aiven**
  (da `Database.Migrate()` al boot dell'API; **non** far girare l'API di questo
  branch contro Aiven/Render: `AddDigestPointEmbeddings` richiede pgvector e
  farebbe fallire il boot). Connessione di default in
  `ComitatoFesteDbContextFactory` e in `appsettings.json`, override con env
  `COMITATOFESTE_CONNECTION`.
- **Contenuto del DB locale al 21/9/2026**: **solo i giorni 11–17/9** (233
  punti, 140 media, 22 run, 2 verbali, 33 membri), copiati da Aiven con un
  `pg_dump --data-only` ritagliato per data (escluse `PushSubscriptions` e
  `ImageThumbnails`, cache rigenerabile) dopo aver svuotato il locale; più 217
  embedding. Aiven ha invece lo storico completo. Il paragrafo qui sotto
  descrive lo stato storico di Aiven all'8/9.
- **Dati importati** (gruppo `Comitato feste 87`, stato all'8/9/2026):
  **10 `IngestionRun`** dai `digest_2026-09-01.json` … `digest_2026-09-08.json`
  (i giorni "chiusi" — data < `digest_data` del checkpoint — vengono rimossi
  da `Export/` automaticamente a ogni export da
  `scripts/whatsapp-digest/close_past_days.py`, vedi sotto; al 12/9/2026
  resta solo `digest_2026-09-12.json`; alcuni
  giorni hanno più di un run per reimport). **DB Aiven e locale allineati**
  via `pg_dump`/`pg_restore` (workflow corrente: import + trascrizione si
  fanno **direttamente su Aiven** con `scripts/import-transcribe-aiven.ps1`
  — Importer poi Transcriber, notifica push automatica a fine run —, poi si
  riallinea il locale con un dump — vedi `docs/DEPLOY.md`. **Sicurezza
  aggiunta il 15/9/2026**: lo script limita sempre l'Importer a un target
  esplicito (default: `checkpoint.json` → `digest_data`, cioè il giorno
  appena curato), mai a "tutta `Export/`" — prima, se `close_past_days.py`
  non arrivava a fine script (run precedente fallito a metà), i
  `digest_*.json` di giorni vecchi non chiusi restavano in `Export/` e un
  Importer senza target li re-includeva, inserendo su Aiven punti storici
  non richiesti (successo reale il 15/9, 153 punti dei giorni 06-10/9,
  poi rimossi a mano). Un giorno diverso da quello corrente richiede
  `-Target <yyyy-MM-dd>` esplicito; **nota**: pg_dump
  18 emette sia `SET transaction_timeout` (GUC non riconosciuto da Postgres
  16) sia le direttive psql `\restrict`/`\unrestrict` (introdotte in pg_dump
  18, sconosciute al client psql 16) — **entrambe** vanno filtrate in fase
  di restore, non solo la prima).
  **Regola: quando si lancia l'import (o il Transcriber) puntando ad Aiven,
  vanno esportate nell'ambiente anche `COMITATOFESTE_HOOK_URL=https://comitatofeste.onrender.com`
  e `COMITATOFESTE_HOOK_SECRET`** (segreto dal dashboard Render), accanto a
  `COMITATOFESTE_CONNECTION`: così `PushHook.NotifyAsync` invia davvero la
  notifica push a fine run. **Solo il Transcriber notifica** (titolo "Comitato
  feste 87", corpo statico "Nuovi messaggi in arrivo!" — testo deciso il
  9/9/2026, prima riportava i conteggi): è l'ultimo passo della pipeline
  normale (Importer → Transcriber), una sola notifica a processo completato
  invece di una per l'import e una per la trascrizione. Senza quelle due env
  il Transcriber stampa `notifiche push: … non impostati — salto` e nessuno
  riceve nulla. **Gap corretto il 15/9/2026**: con la trascrizione anticipata
  dei vocali (vedi sotto) una giornata può arrivare all'Importer già
  interamente pre-classificata, lasciando il Transcriber senza nulla da fare
  (`ok == 0`) — la notifica, legata solo a `ok > 0`, non sarebbe mai partita
  per quei giorni pur essendoci punti nuovi importati. Fix: l'Importer
  stampa una riga `punti-inseriti-totale:N`; `import-transcribe-aiven.ps1` la
  legge e, se `N > 0`, passa al Transcriber `--force-notify <digest_data
  del checkpoint>`, che forza l'invio anche con 0 vocali classificati
  (usando quella data per `url`/`tag` se non ne ha classificato lui stesso
  esattamente una). Nessun cambiamento se lanciati manualmente senza quel
  flag. A DB:
  **804 `DigestPoint`** (per giorno dal 01-09 all'08-09: 211 / 167 / 131 /
  37 / 163 / 10 / 24 / 61; **288** classificati `rumore`), **597 `MediaAsset`**
  (523 audio, 60 foto, 14 documento) con altrettanti `MediaBlob`,
  **31 `Member`** (**24 con foto profilo** da `Export/profili/<Nome>.jpg`;
  senza foto: Emanuele Sciarra — 120 punti, manca il file —, Alessandra
  Toracchio, Alessandra Simonetti, Alessandro Di Benedetto, `Sistema`
  (pseudo-membro dei messaggi di servizio), Daniele Boscolo, Tina Giarrante),
  **6 `Verbale`** in cache (giorni 01-09 → 07-09). Il Transcriber ha girato
  su **tutti i 523 vocali** (`TranscribedAt` valorizzato ovunque, 0 pendenti).
  Import idempotente (dedup esatto + fuzzy; foto aggiornate solo se cambia
  lo SHA-256). `dotnet run --project Src/backend/ComitatoFeste.Importer`
  legge tutti i `C:\temp\ComitatoFeste\Export\digest_*.json` (o un singolo
  `<file.json | yyyy-MM-dd>` come argomento) — ma vedi l'avviso ⚠️ sotto:
  **non** rilanciarlo intero dopo il Transcriber.
- **Deploy**: **in produzione** su `https://comitatofeste.onrender.com` (Render Web
  Service Docker, autoDeploy da `main`) contro **DB Aiven** (`pg_dump`/`pg_restore`
  dal locale — Aiven gira **Postgres 18**, il `comitatofeste-db` di dev è alla **16**).
  Env impostate nel dashboard Render: `COMITATOFESTE_CONNECTION`, `_AUTH_PASSWORD`,
  `_AUTH_PASSWORD_ADMIN` (passphrase separata per il ruolo amministratore,
  vedi login sotto — impostata e testata in prod il 9/9/2026), `_AUTH_SECRET`,
  `GROQ_API_KEY`, e per le notifiche push `COMITATOFESTE_VAPID_PUBLIC`
  / `_PRIVATE` / `_SUBJECT` + `_HOOK_SECRET` (vedi `docs/PUSH-NOTIFICHE.md`).
  Backup: `scripts/backup-db.ps1`. Tutto in `docs/DEPLOY.md`.

## Struttura

- `Src/backend/` — la solution .NET (l'unico codice per ora).
  - `ComitatoFeste.Domain` — entità POCO pure, nessuna dipendenza EF.
  - `ComitatoFeste.Data` — `ComitatoFesteDbContext` + `Configurations/*.cs`
    (una classe Fluent API per entità: vincoli, indici, CHECK, 1:1) +
    `Migrations/` + `ComitatoFesteDbContextFactory` (design-time).
  - `ComitatoFeste.Api` — Web API ASP.NET Core.
    - **Login "casereccio"** (`AuthService` + `TokenAuthAttribute`):
      `GET /api/auth/status` → `{enabled}`; `POST /api/auth/login
      {username,password}` → `{token,username,memberId,displayName,role}`.
      Username = `iniziale.cognome` di un `Member` (derivato a runtime).
      Ogni `Member` ha un `Role` a DB (`Lettore` default | `Amministratore`,
      colonna `AddMemberRole`). **Due passphrase condivise**: quella lettore
      (env `COMITATOFESTE_AUTH_PASSWORD` o config `Auth:Password`; vuota →
      login disattivato) vale per chiunque e restituisce sempre un token
      `lettore`; quella admin (env `COMITATOFESTE_AUTH_PASSWORD_ADMIN` o
      config `Auth:PasswordAdmin`, opzionale) eleva a token `amministratore`
      **solo** se il membro che sta accedendo ha già `Role=Amministratore`
      a DB — un lettore che la indovina resta comunque respinto (401), non
      viene declassato silenziosamente. Nessun endpoint usa ancora il ruolo
      per bloccare l'accesso: `TokenAuthAttribute` accetta un
      `MemberRole` minimo opzionale (es. `[TokenAuth(MemberRole.Amministratore)]`)
      pronto per le prossime funzionalità admin-only. Token HMAC firmato
      (`username|ruolo|scadenza`, 30 gg) rimandato come `Authorization: Bearer`.
      `[TokenAuth]` protegge **solo** i due endpoint JSON qui sotto; gli
      endpoint binari (foto/media) restano aperti per `<img>/<audio>/<video>`.
    - `GET /api/digestpoints?date=yyyy-MM-dd` (+ filtri `author`, `type`) →
      lista `DigestPointDto`; **`date` opzionale**, se omesso restituisce
      tutti i giorni. Con `from`/`to` (yyyy-MM-dd, entrambi opzionali e
      inclusivi, ignorati se `date` è presente) restituisce un range —
      è quello che usa il frontend per caricare l'Agenda un mese alla volta
      invece di tutto lo storico (11/9/2026, dopo che una proiezione a un
      anno di attività ha mostrato che scaricare tutto ogni apertura non
      avrebbe retto la banda Render, vedi punto 5 sotto). `important=true`
      ignora `date`/`from`/`to` e restituisce solo i punti flaggati, storico
      completo: è la query dedicata della vista Importanti, separata da
      quella (paginata) dell'Agenda — pochi punti anche su base annua, non
      serve paginarla. Ogni punto porta `authorId` +
      `authorPhotoUrl` e, per i media, `media.contentUrl`. Senza `type`
      esplicito la vista è pulita: niente `rumore` e niente vocali non
      ancora digeriti (audio con `TranscribedAt == null`). Ogni punto porta
      anche `isImportant`.
    - `GET /api/digestpoints/bounds` → `{earliest, latest}` (date, fuso Roma;
      entrambe `null` se non c'è ancora nessun punto), i due estremi della
      vista pulita. Il frontend la interroga una volta all'avvio per
      scegliere il mese di default dell'Agenda — quello di `latest`, non il
      mese solare corrente, così un mese nuovo ancora senza punti non appare
      vuoto (si continua a vedere l'ultimo mese popolato) — e per nascondere
      il bottone "carica mese precedente" una volta raggiunto `earliest`.
    - `GET /api/digestpoints/media` → tutti i punti con un media scaricabile
      che non sia audio (foto/video/documento, stesso criterio del client
      `mediaKind()`), storico completo. Query dedicata della vista Media,
      separata da quella (paginata per mese) dell'Agenda perché la galleria
      deve restare sfogliabile per intero anche quando l'Agenda carica solo
      il mese corrente.
    - `PUT /api/digestpoints/{id}/important {important:bool}` → evidenzia/
      rimuove il flag "importante" su un punto. `[TokenAuth(MemberRole.
      Amministratore)]`: 403 se il token non è admin, 401 senza token.
      Nel frontend è la stellina in alto a destra su ogni card (non sui
      gruppi foto/documenti), **solo per gli admin** — un bottone on/off,
      colore pieno `--yellow` da acceso; i lettori non la vedono mai, né
      qui né in Agenda (`importantBtnHtml`).
    - `GET /api/digestpoints/recap?date=yyyy-MM-dd[&refresh=true][&format=md]`
      → verbale in prosa della giornata, **PDF** di default (`format=md` per
      il Markdown grezzo), `Content-Disposition: attachment`. Il testo è
      generato da Groq (`GroqRecapClient`, `openai/gpt-oss-120b`,
      `max_completion_tokens=4096`) alla prima richiesta e messo in cache in
      `Verbali` (Markdown); il PDF è reso al volo da quel Markdown con
      QuestPDF (`VerbalePdf`), senza nuove chiamate. Se Groq tronca la
      risposta (`finish_reason=="length"`) il client solleva un errore →
      502, niente cache di un verbale a metà. `refresh=true` rigenera il
      testo. 404 senza punti, 503 senza `GROQ_API_KEY`.
    - `GET /api/digestpoints/media/{mediaId}/content` → byte del blob inline.
    - `GET /api/members/{memberId}/photo` → foto profilo inline.
    - `GET /api/links/preview?url=…` → anteprima OpenGraph di un link
      (`{url,title,description,image,siteName}`, `LinkPreviewService` +
      `IMemoryCache`, TTL 12 h / 30 min sui fallimenti). `[TokenAuth]`. 204 se
      la pagina non espone meta utili, **404 se l'`url` non compare in nessun
      `DigestPoint.Text`** (così non è un proxy di fetch generico). Guardia
      SSRF: il `SocketsHttpHandler` del typed client ha un `ConnectCallback`
      (`LinkPreviewService.SafeConnectAsync`) che risolve e valida l'IP ad
      ogni hop, redirect inclusi — si esce solo verso IP pubblici; max 3
      redirect, timeout 6 s, corpo troncato a 512 KB, solo `Content-Type` HTML.
      Il frontend mostra la card sotto il testo (immagine `og:image` in
      hotlink dal sito originale).
    - **Assistente AI** (`feature/assistente_ai`, **solo locale finché la
      versione non è stabile**, vedi sezione dedicata sotto):
      `POST /api/assistant/ask {question, from?, to?}` → `{answer, sources[],
      model, reducedModel, retrieved}`. `[TokenAuth]`. Domanda max 500
      caratteri; `from`/`to` (yyyy-MM-dd, inclusivi, fuso Roma) restringono la
      ricerca. 400 su input non valido, 429 + `Retry-After` oltre i limiti, 503
      se manca `GEMINI_API_KEY` (`GROQ_API_KEY` è solo l'ultimo ripiego) o tutti i
      modelli sono saturi.
    DTO in `Contracts/`, Swagger in Development, CORS dev `localhost:5173/3000`.
    La chiave Groq (solo per `recap`) è risolta da `GroqKey.Resolve()`: env
    `GROQ_API_KEY`, poi file `key.txt` (in `.gitignore`, cercato risalendo
    fino alla radice del repo), poi config `Groq:ApiKey`.
    **Connessione**: env `COMITATOFESTE_CONNECTION` (come Importer/Transcriber),
    fallback `ConnectionStrings:ComitatoFeste`. All'avvio `Program.cs` esegue
    `Database.Migrate()` (primo boot su DB vuoto → crea lo schema; DB
    irraggiungibile → avvio fallito, voluto in deploy). **Frontend statico**:
    `UseDefaultFiles`/`UseStaticFiles` servono
    `ComitatoFeste.Api/wwwroot/index.html` (incluso dal Web SDK), stessa
    origine → in produzione niente CORS. Porta di ascolto da env `PORT` se
    presente (Render), altrimenti default Kestrel.
  - `ComitatoFeste.Importer` — console: legge i `digest_*.json` da Export e
    li scrive a DB (`DigestImporter` è la classe riusabile);
    `ImportProfilePhotosAsync` sincronizza `Export/profili/`.
    **Reimport della stessa giornata: idempotente** (serve perché un
    `digest_<data>.json` di oggi non è "chiuso" — la sera arrivano altri
    messaggi e il file viene rigenerato). Dedup a più livelli in
    `DigestImporter.ImportFileAsync`: (0) **identità media** — un'entry col
    `file` già presente nella finestra per lo stesso autore è lo stesso
    messaggio *anche se il Transcriber ne ha riscritto il `Text`*
    (placeholder → sintesi), match su `MediaAsset.FileName`; (1) esatto su
    `(GroupId, MemberId, OccurredAt, Text)`; (2) fuzzy pg_trgm su `Text`.
    Contatori distinti nell'output (`dup media` / `dup esatti` / `dup
    fuzzy`). **⚠️ Residuo**: un punto di **solo testo** riformulato in
    curatela così tanto da scendere sotto la soglia fuzzy 0.6 tra un import
    e l'altro verrebbe re-inserito duplicato — raro, ma se serve
    ripulire un giorno basta `DELETE FROM "IngestionRuns" WHERE ...`
    (cascade sui punti) e reimportare. Per aggiungere solo foto profilo:
    `--photos-only` (salta l'import dei digest).
    `MediaKind`
    mappa estensione → (`MediaType`, MIME): foto (jpg/png/webp/…), audio
    (ogg/opus/m4a/mp3/…), **video** (mp4/mov/webm/mkv/3gp/avi → restano
    `MediaType.Documento` ma con MIME `video/*`, vedi convenzione sotto),
    documento (pdf/doc/xls); sconosciute → `documento` +
    `application/octet-stream`.
  - `ComitatoFeste.Transcriber` — console: prende i `MediaAsset` audio da
    lavorare (`TranscriptionText == null` **oppure** `TranscribedAt ==
    null`), li trascrive con Groq Whisper e classifica la trascrizione con
    un modello gpt-oss (`GroqClient`) in
    decisione/proposta/domanda/info/media/`rumore` (`proposta` = idea/proposta
    operativa non ancora decisa; `decisione` solo se il gruppo l'ha confermata —
    nel dubbio il prompt sceglie `proposta`);
    poi riscrive `DigestPoint.Type` e `Text` (sintesi in una frase, o
    messaggio segnaposto se `rumore`).
    **Coppie di modelli intercambiabili con fallback su 429** (`GroqClient`,
    `WhisperModels` / `ClassifierModels`): default `whisper-large-v3` +
    `openai/gpt-oss-120b` (più accurati su dialetto e su rumore/info); al
    primo HTTP 429 su un modello si passa **stabilmente** al suo backup per
    il resto del run — `whisper-large-v3-turbo` e `openai/gpt-oss-20b` — che
    ha un contatore RPD/TPD separato e quindi di solito ancora budget. Al
    passaggio del classificatore il log del freno TPM viene azzerato. I
    `llama-3.x` sono deprecati (giu 2026). Free tier gpt-oss (20b **e** 120b,
    identici): 1.000 req/g, 200k token/g, 30/min, 8.000 token/min — ma
    **contatore separato per modello**. `GroqClient` ha un freno TPM adattivo (finestra 60 s su
    `usage.total_tokens`, soglia 6.500) perché il limite vero è quello al
    minuto; `--delay-ms` resta come freno per i 20 req/min di Whisper. Il
    limite giornaliero 200k token si sfora solo rifacendo girare il batch
    intero più volte (una passata ~140 vocali ≈ ~120-140k token). **Classificazione incerta** (JSON non valido: gpt-oss a
    volte incornicia in ```` ``` ````, antepone testo, o tronca — mitigato
    da `ParseClassification` che isola l'oggetto `{…}` + 3 tentativi):
    salva `TranscriptionText` ma lascia `TranscribedAt == null`, non tocca
    `Type`/`Text`. Così Whisper non si ripaga, il run dopo ritenta **solo**
    la classificazione, e la GUI (`GET /api/digestpoints` senza `type`)
    nasconde il punto finché `TranscribedAt` è null. Chiave via
    `GroqKey.Resolve()` (env `GROQ_API_KEY` o file `key.txt`). Opzioni:
    `--dry-run`, `--limit <n>`, `--delay-ms <n>`,
    `--group <nome>`. Ritenta su HTTP 429/5xx, Ctrl+C esce pulito dopo il
    vocale in corso.
  - `ComitatoFeste.Embedder` — console (solo branch `feature/assistente_ai`):
    calcola con Gemini (`gemini-embedding-2`, 768 dim, free tier) l'embedding
    dei punti della **vista pulita** (niente `rumore`, niente vocali non ancora
    digeriti) e lo salva in `DigestPointEmbeddings`. **Idempotente e
    incrementale**: ricalcola solo i punti senza embedding o il cui testo
    (prefisso autore incluso) ha cambiato `InputSha256` — quindi lo stesso
    comando fa da backfill e da aggiornamento dopo ogni import+trascrizione.
    Opzioni: `--dry-run` (conta, niente chiamate), `--limit <n>`,
    `--batch-size <n>` (default 50), `--delay-ms <n>` (default 500), `--group
    <nome>`, `--search "<domanda>" [--top <n>]` (non scrive: stampa i punti più
    vicini, utile per giudicare il retrieval). Chiave via `GeminiKey.Resolve()`
    (env `GEMINI_API_KEY`, poi `gemini.key.txt` in radice repo, gitignorato).
    Connessione: env `COMITATOFESTE_CONNECTION`, default `localhost:5432`.
    Lancio: `DOTNET_ROLL_FORWARD=Major dotnet run --project
    Src/backend/ComitatoFeste.Embedder`. **Va rilanciato dopo ogni
    import/Transcriber** (i testi dei vocali vengono riscritti dopo l'import).
    Fatto il primo backfill il 21/9/2026: 217 punti (11–17/9).
- `Src/backend/ComitatoFeste.Api/wwwroot/index.html` — frontend
  self-contained (vanilla JS, nessun build), "Comitato feste 87 — Agenda",
  servito dall'API stessa. Note operative in
  `Src/backend/ComitatoFeste.Api/README.md`. All'avvio chiama
  `GET /api/auth/status`: se
  `enabled` e non c'è token in `localStorage` (`cf87_token`) mostra un
  overlay di login (username membro + passphrase → `POST /api/auth/login`),
  altrimenti carica; il token va in `Authorization: Bearer` su ogni fetch
  JSON, un 401 riporta al login, il bottone "esci" in topbar lo cancella.
  **Tre fonti dati indipendenti** (`data`/`mediaData`/`importantData`),
  caricate in parallelo da `load()` all'avvio: l'Agenda **non** scarica più
  tutto lo storico (vedi sopra il perché), ma un mese alla volta via
  `GET /api/digestpoints?from=&to=` — di default il mese di
  `GET /api/digestpoints/bounds`'s `latest` (esteso a includere il mese di
  un eventuale `?date=` più vecchio); un bottone "carica mese precedente" in
  fondo alla timeline (`loadPreviousMonth`, nascosto da `canLoadPreviousMonth`
  quando si è già raggiunto `bounds.earliest`) estende `data` un mese indietro
  alla volta. Il date picker in topbar, se punta a un giorno non ancora
  caricato, fa risalire `goToDay` mese per mese prima di scrollarci (stesso
  meccanismo, silenzioso). Media e Importanti restano invece full-history,
  ciascuna con la propria query dedicata (`GET /api/digestpoints/media` e
  `?important=true`) indipendente dal mese caricato in Agenda — vedi sopra.
  `data` raggruppata lato client per giorno Roma in
  un **accordion**: una `<section class="day">` per data, collassata, con
  la timeline verticale (righe alternate sx/dx, badge per tipo) nel
  `.day-body`. All'atterraggio è espanso solo il giorno `?date=` (default
  oggi); il click sull'header di un giorno lo espande/collassa; il date
  picker in topbar fa `goToDay` → espande la sezione e ci scrolla
  (`scrollIntoView` + `scroll-margin-top`). Ogni header ha un pulsante
  download (con spinner) che chiama `GET /api/digestpoints/recap` e scarica
  il verbale **PDF** della giornata. Il testo dei punti passa da `linkify()`
  (escape HTML poi `http(s)://` → `<a>`); sotto ogni card con un link,
  `hydrateLinkPreviews()` chiama `GET /api/links/preview` e inserisce una card
  di anteprima OpenGraph (silenziosa su 204/404/errore, cache client per URL).
  Foto inline, `<audio>` /
  `<video>` player scelto dal prefisso di `media.contentType`
  (`image/`/`video/`/`audio/`), non dal `mediaType` (video `documento`
  comunque riprodotto); `<img loading="lazy">`. Base URL API: `?api=` se
  presente, altrimenti **stessa origine** (in produzione l'API serve questo
  file). In locale: `dotnet run` dell'API e apri `http://localhost:5065/`,
  oppure servi il file a parte con `?api=`; vedi
  `Src/backend/ComitatoFeste.Api/README.md`.
  **Quattro viste** nella sidebar (`setView`, ordine Agenda → Importanti →
  Media → Æsir), titolo in topbar con l'icona della vista (`VIEW_ICONS`): Agenda
  (l'accordion sopra), Media (griglia foto/video/documenti per giorno,
  **non** l'audio — vedi `mediaKind`), e **Importanti**
  (`viewImportant`/`renderImportant`) — punti con `isImportant=true`, stessi
  badge di tipo dell'Agenda ma **timeline unica e continua, non raggruppata
  in accordion**: i punti sono appiattiti in un solo `.rail` (giorno più
  recente in alto, cronologico nel giorno, come l'Agenda) con un componente
  separatore (`.date-sep`, una pillola che "buca" la linea verticale del
  rail, `id="isep-<data>"`) inserito ogni volta che il giorno cambia. La
  stellina in alto a destra su ogni card (`importantBtnHtml`) esiste **solo
  per gli admin** (bottone on/off, `PUT .../important`, colore pieno
  `--yellow` da acceso — niente cerchio/glow) — i lettori non la vedono mai,
  né qui né in Agenda. Il date picker in topbar è condiviso e attivo anche
  qui (`goToImportantDay` + `updatePickerFromScroll` esteso): segue lo
  scroll aggiornandosi sull'ultimo `.date-sep` il cui bordo alto ha superato
  la propria `scroll-margin-top` (non un `TOPBAR_H` fisso, per restare
  coerente col punto di arrivo di `goToImportantDay`), e cambiare data nel
  picker scorre al separatore corrispondente (no-op se quel giorno non ha
  punti importanti, come `goToDay` in Agenda). **Æsir** (`viewAesir`,
  `renderAesir`/`askAesir`, solo branch `feature/assistente_ai`) — l'assistente
  AI, **al posto della vecchia vista "Guida"** (le istruzioni di installazione
  PWA Android/iOS sono state rimosse dal menu il 21/9/2026: recuperabili dalla
  cronologia git, commit precedenti a quello di Æsir, se si vuole riproporle
  altrove). Pagina con un **volto solo-CSS** (schermata scura + due occhi
  luminosi ciano, stile robottino Emo; `.aesir-face[data-mood]`), un saluto
  ("Sono Æsir, chiedi quello che vuoi.") e una casella di testo (max 500
  caratteri, Invio invia, Maiusc+Invio va a capo). Stati JS in `aesir.state`:
  `idle` (occhi neutri che ammiccano; guardano in giù quando la casella ha il
  focus) → `thinking` (`working`: palpebre oblique e occhi che scansionano a
  destra/sinistra, con la domanda mostrata al posto della casella) → `done`
  (`happy`: occhi a "^" + risposta al posto della casella, badge `[n]` per le
  citazioni, "Fonti (N)" espandibile, modello usato in piccolo, pulsante "Fai
  un'altra domanda") oppure `error` (`sad`: messaggio del server, es. 429/503,
  e "Riprova" che conserva la domanda). Il testo del modello passa da
  `aesirFormat` (escape HTML, `**grassetto**`, elenchi `- `, `[n]` → badge solo
  se c'è la fonte). Chiama `POST /api/assistant/ask` con il token (401 → login).
  Il font pixel del tema non ha la "Æ" (solo Basic Latin): ricade sul font di
  sistema, come le lettere accentate. Rispetta `prefers-reduced-motion`.
  `sw.js` `CACHE_VERSION` alzato a v10.
- `Export/` — dati sorgente della pipeline sul PC dell'utente:
  `digest_<data>.json`, sottocartella `<data>/` con i media rinominati
  (le sottocartelle `_da-attribuire` / `_conflitto-autore` /
  `_gia-in-db-senza-media` sono triage manuale dell'utente, l'import le
  ignora), e `profili/<Nome-con-trattini>.jpg` per le foto profilo.
- `docs/sample-digest_2026-09-01.json` — sottoinsieme del digest del
  2026-09-01 (non più in `Export/`), committato per mostrare la forma del
  JSON sorgente (date/time/author/type/text/file).
- `README.md` (radice) — prerequisiti + comandi di build/migration/import/
  trascrizione/run, rimanda a questo file e a `docs/CONTEXT.md`.
- **Deploy** — `Dockerfile` (+ `.dockerignore`) builda l'immagine dell'API
  (che serve anche il frontend); `render.yaml` descrive il Web Service Render;
  `docker-compose.yml` è per lo sviluppo locale (Postgres + API). Target:
  Render (container) + **Aiven** PostgreSQL gestito. Guida passo-passo in
  `docs/DEPLOY.md`.
- `schema.reference.sql` — citato come passo previsto ma **non ancora
  presente** nel repo.

## Generazione di `digest_<data>.json` dall'export WhatsApp

Il repo (codice + `Export/` con i digest già generati) vive in
`C:\temp\ComitatoFeste` (spostato da `C:\Digest` il 4/9, poi da
`C:\ComitatoFeste` il 6/9). **L'export grezzo della chat WhatsApp non vive
più dentro il repo**: da oggi (6/9/2026) arriva sempre come file
`Chat WhatsApp con Il branco dei pazzi 87.zip` nella root di Dropbox
(`C:\Users\giova\Dropbox\Chat WhatsApp con Il branco dei pazzi 87.zip`,
~150 MB, contiene sia il `.txt` che tutti i media) — prima veniva
scompattato a mano in una sottocartella del progetto (`Chat WhatsApp con
Il branco dei pazzi 87\`), ora si parte direttamente dallo zip Dropbox e lo
si estrae dove serve per la rigenerazione (non necessariamente sotto
`C:\temp\ComitatoFeste`). **Si usa sempre e solo lo zip senza suffisso
numerico**: eventuali `..._1.zip` / `..._2.zip` nella stessa cartella sono
copie vecchie tenute dal download e vanno ignorati, anche se più grandi
(un export più recente può avere meno righe-media nel `.txt`, è normale —
vedi `scripts/whatsapp-digest/README.md` passo 1). Gli script Python che generano i
`digest_<data>.json` in `Export/` a partire dal `.txt` estratto sono
versionati nel repo in **`scripts/whatsapp-digest/`**: `parse_wa.py`,
**`digest_lib.py`** (logica comune: parsing/copia media, `is_reaction_gif`,
`media_text`, il loop di costruzione, scrittura del checkpoint — refactor
del 6/9/2026, prima duplicata in ognuno dei 6 script), un
`build_digest_MMGG.py` per ogni giorno già fatto (ora solo dati: `DATE`,
`CURATED`, `MEDIA_OVERRIDES`, ed eventuali eccezioni del giorno come la
finestra oraria del logo del 5/9, passate a `digest_lib.build_digest(...)`),
e `README.md` con la procedura passo-passo, più `export-prompt.md`
(aggiunto il 14/9/2026) — prompt autosufficiente da dare a una sessione
Claude Code **diversa** per far eseguire solo l'export/curatela di un
giorno, **senza** import/Transcriber/notifica push (quelli restano un
passo separato, deciso a parte). I `build_digest_MMGG.py` restano
comunque lo storico affidabile di come è stato costruito ogni digest —
copiali/adattali per un nuovo giorno invece di ripartire da zero, ma per
qualsiasi bug fix o miglioramento alla logica comune tocca **solo**
`digest_lib.py`, non serve più propagarlo a mano in ogni file (motivo del
refactor: un bug di deduplicazione trovato il 6/9/2026 — vedi sotto — era
comunque presente, non corretto, in tutti e 5 gli script dei giorni
precedenti). Restano da rigenerare ogni volta
nella sessione device-linked (leggono/scrivono file fuori dal repo, tipico
lo zip estratto altrove) perché serve `ffprobe`/`ffmpeg` e l'accesso
diretto ai file della chat sul PC dell'utente (o, quando manca una shell
diretta sul PC, nell'ambiente cloud della sessione, scaricando lì lo zip e
poi ricopiando `digest_<data>.json` + media + script sul PC). Regole
stabili da seguire in ogni rigenerazione (dettagliate anche nel README
sopra):

- **Trascrizione anticipata dei vocali + dedup semantico (regola aggiunta il
  15/9/2026, sostituisce la precedente "ogni vocale va sempre tenuto")**:
  prima di scrivere `CURATED`/`MEDIA_OVERRIDES`, lanciare
  `python transcribe_new.py` — recupera automaticamente i messaggi nuovi
  dopo il checkpoint e trascrive con Groq Whisper (solo trascrizione,
  niente classificazione) tutti i vocali nuovi, con cache di resume in
  `.transcript_cache.json` (gitignored: un crash/rate-limit a metà non fa
  ripagare le trascrizioni già fatte, si rilancia e riparte dai soli
  mancanti). Scrive `nuovi_messaggi_<data>.json`: è quello il file da
  leggere in curatela (testo + trascrizioni inline), invece di `grep`/`sed`
  sul `.txt` grezzo per i vocali. Con il testo dei vocali disponibile, in
  curatela si può riconoscere quando più vocali (anche di autori diversi)
  ripetono lo stesso concetto con parole diverse — su 14 giorni curati è
  successo in almeno 5 giornate, degradando la leggibilità del digest — e
  **accorparli in un'unica entry di sintesi** (`AUDIO_MERGES` in
  `build_digest_MMGG.py`, vedi `digest_lib.build_digest`): i file dei
  vocali accorpati si scartano, l'entry di sintesi ha `type` deciso dal
  curatore e nessun media. Un vocale che è di per sé un argomento atomico
  invece resta come oggi (entry propria, file tenuto) ma va comunque
  **classificato in curatela** invece di lasciato al Transcriber
  (`AUDIO_CURATED`, stesso file): il curatore ha il contesto dell'intera
  conversazione, il classificatore del Transcriber vede il vocale isolato.
  **Un vocale di rumore (saluti, battute, chiacchiere non legate al
  comitato) si classifica in `AUDIO_CURATED` con type `"rumore"` e viene
  scartato del tutto** (regola 19/9/2026): `digest_lib` non genera l'entry
  né copia il file, quindi né Importer né Transcriber lo vedono mai — così
  il Transcriber non ripaga Whisper su vocali già trascritti e inutili.
  Un vocale non coperto da nessuna delle strutture mantiene il
  comportamento di sempre (placeholder "non trascritto", il Transcriber lo
  classifica più tardi) — è la rete di sicurezza se la curatela non fa in
  tempo a coprire tutto. Lato Importer, l'entry porta anche `transcript`
  (letto dalla cache): quando presente e `type != "media"`,
  `DigestImporter` valorizza già `MediaAsset.TranscriptionText`/
  `TranscribedAt`, così la query del Transcriber
  (`TranscriptionText == null || TranscribedAt == null`) lo esclude da
  sola — nessuna modifica al Transcriber stesso. Perché farlo in curatela e
  non nel Transcriber: verificato che il freno TPM che oggi rallenta il
  Transcriber è solo del classificatore (`gpt-oss-120b`, soglia 6.500
  token/min) — Whisper da solo ha solo il limite 20 req/min, quindi la
  pre-trascrizione è molto più veloce dei run visti finora.
- **Sticker e GIF vanno ignorati**: non generano una entry nel digest e non
  vanno copiati in `Export/<data>/` (regola aggiunta il 4/9/2026 — prima
  venivano trattati come media generico).
- **Le GIF di reazione mascherate da `.mp4` vanno ignorate anch'esse**:
  WhatsApp Android salva le GIF (di reazione o da tastiera) come file `.mp4`
  muti e brevi, indistinguibili per estensione da un video vero. Prima di
  includere un `.mp4` nel digest si controlla con `ffprobe` se ha una
  traccia audio (`ffprobe -v error -select_streams a -show_entries
  stream=codec_type -of csv=p=0 <file>`): se l'output è vuoto (nessun
  audio) è una GIF e va scartata come sticker/GIF; se c'è audio è un video
  vero e va tenuto (regola aggiunta il 4/9/2026, dopo che alcune GIF erano
  finite nei digest come "video").
- Il testo "rumore" (saluti, emoji, conferme brevi tipo "grandi", reazioni)
  va scartato in fase di curatela manuale (dict `CURATED`), non inserito nel
  digest.
- Media effettivamente assenti dall'export (`<Media omessi>` nel `.txt`) si
  segnalano come non recuperabili, non si inventano placeholder.
- **I link condivisi nei messaggi di testo vanno riportati per intero**
  nel testo curato (`CURATED`), non solo descritti a parole — un punto
  che dice "condivide un link a X" senza l'URL vero e proprio è
  incompleto e inutilizzabile da chi legge il digest (regola aggiunta
  il 4/9/2026, dopo che un punto su un video Facebook era stato scritto
  senza il link).
- **Iterazioni di design (loghi, grafiche, bozze varie)**: quando il
  gruppo discute più versioni di uno stesso elemento grafico (es. due
  loghi diversi in lavorazione), NON si tengono tutte le bozze nel
  digest. Si tiene solo la versione che il testo della chat conferma
  come definitiva (un voto, un "usiamo questo", un "sì definitivo" —
  vedi il logo della maglietta del 2/9, già votato). Le bozze intermedie
  si escludono come i media non significativi. Se dal testo non risulta
  chiaro quale versione ha vinto, NON si indovina dalle immagini: si
  segnala all'utente qual è il candidato più probabile e si chiede
  conferma prima di scartare le altre (regola aggiunta il 4/9/2026).
  Esempio applicato: il 5/9/2026 la discussione logo/maglietta ha
  prodotto oltre 50 bozze in una finestra di poche ore (13:37-19:26);
  invece di elencare ogni singolo file, lo script di quel giorno
  esclude automaticamente tutte le .jpg cadute in quella finestra
  tranne le due immagini definitive indicate dall'utente (e due jpg
  della stessa finestra ma non legate al logo, tenute esplicitamente
  fuori dall'esclusione) — vedi `build_digest_0905.py` come esempio di
  esclusione per finestra oraria invece che per elenco di file.
- **Nome del gruppo**: la cartella grezza dell'export si chiama `Chat
  WhatsApp con Il branco dei pazzi 87/` (nome corrente del gruppo su
  WhatsApp), ma il gruppo canonico ovunque — DB, default dei tre eseguibili
  CLI, questi documenti — è **`Comitato feste 87`**. Non allineare l'uno
  all'altro senza chiedere: cambiare il default rinominerebbe di fatto il
  gruppo in tutta la pipeline.
- **Descrizione di foto/video con persone ritratte**: nelle didascalie di
  `MEDIA_OVERRIDES` non si descrivono i tratti fisici delle persone
  ritratte (corporatura, capelli, barba, tratti del viso, abbigliamento
  ecc.) — solo l'azione/il contesto. Es. "un uomo con testa rasata e barba
  folta sorride" va scritto semplicemente "un uomo sorride" (regola
  aggiunta il 6/9/2026). Il resto della scena (oggetti, luogo, cosa sta
  succedendo) va comunque descritto guardando l'immagine, come da regola
  generale sopra.
- **Checkpoint dell'ultimo messaggio letto**: durante la generazione di un
  digest (in particolare quando si legge un giorno intero messaggio per
  messaggio per popolare `CURATED`/`MEDIA_OVERRIDES`), va tenuta traccia
  dell'ultimo messaggio effettivamente esaminato in
  `scripts/whatsapp-digest/checkpoint.json` (data, ora, mittente, e la
  data del digest a cui appartiene), aggiornandolo mano a mano — non solo a
  fine giornata. Così, se la sessione si interrompe a metà curatela, si può
  ripartire esattamente da quel messaggio invece di rileggere tutto il
  giorno da capo (regola aggiunta il 6/9/2026). A digest di un giorno
  completato e verificato, il checkpoint riporta l'ultimo messaggio di
  quella giornata.
- **Bug di deduplicazione trovato/corretto il 6/9/2026** (ora in
  `digest_lib.build_digest`, prima duplicato in ogni script): se due
  messaggi di testo consecutivi hanno stesso `(time, sender)` — capita, es.
  due messaggi separati inviati nello stesso minuto — e quella chiave è
  presente in `CURATED`, lo script generava un'entry duplicata (una per
  ogni messaggio che matcha la stessa chiave) invece di una sola. Il fix
  (`used_curated_keys`) genera una sola entry per chiave. **Rilevanza per
  i digest già generati**: un confronto di regressione ha mostrato che
  questo bug era presente, non corretto, negli script (e quindi
  potenzialmente negli output) di tutti i giorni dall'1 al 5/9/2026 — un
  10-15% di entry testuali in più del dovuto in ciascuno. I file
  `Export/digest_2026-09-0[1-5].json` non sono più presenti nel repo
  (1-3 già importati a DB, vedi "Stato attuale"; l'`Importer` ha comunque
  un vincolo UNIQUE + dedup che potrebbe aver già filtrato i duplicati
  esatti in fase di import, ma non è stato verificato) — se serve
  controllare/pulire i conteggi già a DB per quei giorni, va fatto apposta,
  non è stato fatto in questo refactor (che ha toccato solo gli script).
- **Sondaggi WhatsApp (regola aggiunta l'8/9/2026)**: nel `.txt` esportato un
  sondaggio è un normale messaggio di testo multi-riga che inizia con
  `SONDAGGIO:`, seguito dal titolo/domanda e da una riga `OPZIONE: <testo>
  (N voti)` per ciascuna opzione — il parser lo tratta già come testo
  normale, nessuna modifica a `parse_wa.py`/`digest_lib.py` necessaria. In
  `CURATED` va sempre classificato come **`proposta`** (non `decisione`,
  anche se al momento dell'export ha già dei voti: i voti sono solo uno
  snapshot, il sondaggio resta aperto), riportando per intero sia la
  domanda/titolo sia tutte le opzioni con il relativo conteggio voti al
  momento dell'export (stessa logica della regola sui link condivisi:
  niente riassunti parziali). Se in un messaggio successivo il gruppo
  dichiara esplicitamente l'esito (es. "Considerato l'esito del sondaggio,
  la riunione viene confermata per..."), quello va curato come una entry
  separata di tipo `decisione`.
- **Menzioni di Giovanni Lima (regola aggiunta l'11/9/2026)**: quando un
  altro membro del gruppo nomina Giovanni Lima in un messaggio, non è
  necessario inserirlo automaticamente in `CURATED` (vale comunque la
  regola generale: se il contenuto è "rumore" si scarta come qualsiasi
  altro messaggio). Va però sempre segnalato a Giovanni nel recap finale
  della sessione di export — orario, autore e breve contesto — anche
  quando il messaggio non è finito nel digest, così può decidere se
  intervenire.
- **Condivisione di posizione (regola aggiunta l'11/9/2026)**: nel `.txt`
  una posizione condivisa è una riga di **testo** con un link Google Maps
  (`posizione: https://maps.google.com/?q=lat,long`), non un file media —
  quindi nessuna voce in `MEDIA_OVERRIDES`. Una posizione **statica** (un
  pin, es. il punto di ritrovo di una riunione) va curata come un link
  qualsiasi: testo integrale del link in `CURATED`, tipo `info` (o
  `decisione` se è la posizione definitiva di un appuntamento già deciso).
  Una posizione **in tempo reale** (`live location`) va invece sempre
  scartata come rumore in fase di curatela — l'eventuale visualizzazione
  lato frontend è da definire.
- **Compleanni (regola aggiunta il 13/9/2026)**: quando in una giornata
  compare un gruppo di messaggi "buongiorno"/"auguri" rivolti a un membro
  taggato (tipico pattern: decine di messaggi social sparsi nella mattina,
  finora sempre trattati come puro rumore), va sintetizzato **un solo
  punto** `("<primo orario del giorno>", "<primo autore degli auguri>")`,
  tipo `info`, testo tipo "Oggi è il compleanno di `<Nome>`, il gruppo si
  scambia auguri in chat" — va per primo nella giornata (usa l'orario del
  primo messaggio di auguri, così l'ordine cronologico lo mette in cima da
  solo). Deciso di dedurlo dalla chat (nessun `Members.BirthDate` a DB):
  funziona quando il gruppo festeggia quel giorno stesso, non è un
  calendario compleanni affidabile a prescindere — se in futuro serve
  quest'ultimo, richiede una colonna dedicata + raccolta dati, non ancora
  fatto. I singoli messaggi di auguri restano comunque rumore individuale,
  non generano più entry a parte.
- **Chiusura giorni passati (regola aggiunta il 12/9/2026)**: l'Importer fa
  dedup media confrontando `(Autore, NomeFile)` col DB **attuale**
  (`DigestImporter.cs`, set `existingMedia`), non con uno storico di "già
  visto in passato". Se un punto con media viene cancellato dall'app
  (`DELETE /api/digestpoints/{id}`) ma la sua entry è ancora nel
  `digest_<data>.json` sorgente, il giro successivo dell'Importer non trova
  più quel file tra i "già esistenti" e lo **re-inserisce** — un punto
  cancellato "resuscita". Per questo `scripts/whatsapp-digest/close_past_days.py`
  cancella da `Export/` (json + cartella media + eventuale `_rimossi_<data>/`)
  tutti i giorni con data **strettamente minore** di `digest_data` nel
  checkpoint. Gira in **automatico** a fine di `import-transcribe-aiven.ps1`
  (dopo Importer+Transcriber, non bloccante se fallisce — vedi il commento nello
  script, aggiunto il 13/9/2026 dopo che un giorno era rimasto "orfano" perché
  il check girava solo a inizio export, prima che il checkpoint avanzasse):
  a quel punto Aiven ha appena ricevuto l'aggiornamento, quindi qualunque
  giorno precedente a quello corrente è sicuro da rimuovere. Nessuna verifica
  incrociata su Aiven per non consumare token a ogni giro — si assume che il
  giorno appena chiuso sia stato importato/trascritto con successo nello
  stesso run. Rischio residuo
  accettato: se l'import di un giorno "chiuso" non fosse mai andato a buon
  fine, cancellarlo non perde nulla per davvero —
  `build_digest_<MMGG>.py` resta per sempre in git (è la "ricetta") e il
  `.txt` di WhatsApp è sempre cumulativo dall'inizio, quindi il giorno si
  rigenera comunque da un nuovo export.

## Convenzioni già in uso — seguile per coerenza

- Identificatori Postgres in PascalCase tra virgolette (niente snake_case).
- `DateTimeOffset` per ogni colonna `timestamptz` (non `DateTime`: Npgsql
  6+ è severo su `Kind` non specificato). Npgsql 8 in scrittura accetta
  **solo offset 0**: normalizza a UTC prima di salvare (l'importer converte
  gli orari `Europe/Rome` con `.ToUniversalTime()`).
- Campi enum-like (`DigestPoints.Type`, `MediaAssets.MediaType`) sono enum
  C# convertiti a stringa minuscola via `HasConversion(...)`, con CHECK
  constraint lato DB via `ToTable(name, t => t.HasCheckConstraint(...))`.
  `MediaType` ha solo `foto | audio | documento`: **i video non hanno un
  valore enum** (evitata la migration), sono `documento` con
  `MediaBlobs.ContentType` `video/*` e il frontend li riconosce dal MIME.
  Se servisse un tipo `video` di prima classe → enum + migration come
  `AddRumoreDigestPointType`.
- Un file di configurazione Fluent API per entità in
  `ComitatoFeste.Data/Configurations/`, applicati con
  `ApplyConfigurationsFromAssembly`.
- I byte dei file (`bytea`) stanno **sempre in una tabella 1:1 separata**,
  mai sulla tabella di metadati: `MediaAssets`→`MediaBlobs`,
  `Members`→`MemberProfilePhotos`. Ogni blob ha `ContentType` + `Sha256`.
  Le query di lista proiettano solo le colonne servite, così il `bytea`
  non viene mai caricato.
- I controller REST non espongono mai le entità EF con navigazioni
  cicliche: `DigestPoints`/`MediaAssets` passano da DTO in
  `ComitatoFeste.Api/Contracts/`.
- Dedup a due livelli su `DigestPoints` (vedi @docs/CONTEXT.md per il
  perché): vincolo UNIQUE hard per i rerun esatti + indice GIN pg_trgm per
  il fuzzy match applicativo sulle riformulazioni tra run diversi.
  Implementato in `DigestImporter`: match esatto in-memory, poi
  `EF.Functions.TrigramsSimilarity` (soglia 0.6, stessa persona, finestra
  ±2 min); i testi placeholder "non trascritto" sono esclusi dal fuzzy
  (template → trigram inaffidabile, collasserebbe vocali diversi).

## Assistente AI (branch `feature/assistente_ai`, in lavorazione)

**Stato (21/9/2026)**: backend fatto e provato end-to-end in locale
(embedding → retrieval → risposta con citazioni); **frontend fatto** (vista
Æsir, vedi "Struttura"; da rifinire con l'uso: niente selettore di date,
`from`/`to` dell'API non sono esposti in UI); **niente deploy** finché la versione non è stabile — le modifiche
esistono solo in locale/nel branch, Aiven e Render restano alla versione
`develop`/`main` senza pgvector.

RAG sui digest: `AssistantService` (1) embedda la domanda con Gemini
(`GeminiEmbeddingClient`, in `ComitatoFeste.Data` perché condiviso con
l'Embedder: **stesso modello, stessa dimensione, stessi prefissi asimmetrici
di input**, altrimenti i vettori non sono confrontabili), (2) recupera con
pgvector i **40 punti** più vicini per distanza coseno (`<=>`, scansione esatta
senza indice vettoriale — con qualche migliaio di righe è più precisa e regge il
filtro data) sulla vista pulita, (3) li passa in ordine cronologico e numerati a
una **catena di modelli** (`AssistantService.GenerateAnswerAsync`): **Gemini 3.5
Flash Lite** (`gemini-3.5-flash-lite`) → **Gemini 3.1 Flash Lite**
(`gemini-3.1-flash-lite`) → **Groq** (`GroqRecapClient.AskAsync`: `openai/gpt-oss-120b`,
poi `openai/gpt-oss-20b`). Si passa al successivo su 429/5xx/timeout o risposta
inutilizzabile (vuota, bloccata, troncata), senza retry (domanda interattiva);
ogni provider ha quota gratuita separata. Il campo `model` della risposta dice
chi ha risposto; `reducedModel=true` se non è il primo della catena. Client
Gemini in `GeminiChatClient` (`generateContent`, max 4096 token di uscita, Groq
resta a 1800 per il limite 8k token/min). Rispondono in italiano citando `[n]`.
Le citazioni `【n】` di gpt-oss sono normalizzate a `[n]`; `sources` contiene solo
i punti effettivamente citati. Verificata dal vivo solo la risposta del primo
modello (21/9/2026): il ripiego sui successivi non è ancora stato provato. Il prompt tratta i punti come materiale, non istruzioni (difesa da
prompt injection dai messaggi del gruppo) e dà precedenza ai punti più recenti.

- **`AssistantLimiter`** (in memoria, si azzera al riavvio/cold start): default
  10 domande/ora per utente, 80/giorno totali, 2 chiamate contemporanee;
  config `Assistant:PerUserPerHour` / `GlobalPerDay` / `MaxConcurrent`. Se la
  domanda fallisce per colpa dei servizi esterni il "biglietto" viene
  restituito. **Gli amministratori (`Role=Amministratore` nel token) sono
  esenti** dal limite per utente e da quello giornaliero (21/9/2026): restano
  solo il tetto di chiamate contemporanee e la quota reale dei provider, che
  la catena di modelli aggira scalando sul successivo. La quota Groq è condivisa con Transcriber e verbali.
- **Schema**: `DigestPointEmbeddings` (1:1 con `DigestPoints`, PK=FK
  `DigestPointId`, `Embedding vector(768)`, `Model`, `InputSha256`,
  `EmbeddedAt`, cascade). Tabella separata come i blob. Se cambia modello o
  dimensione va ricalcolato tutto.
- **`UseComitatoFesteNpgsql()`** (`ComitatoFesteDbOptionsExtensions`) è l'unico
  punto in cui si configura Npgsql: il modello contiene una colonna `vector`,
  quindi **ogni** consumatore del contesto (anche Importer/Transcriber) deve
  chiamare `UseVector()` — mai `UseNpgsql` diretto.
- **Privacy**: i testi dei punti vanno a Google (Gemini) per gli embedding; il
  gruppo ha dato l'ok. Free tier, limiti di quota non pubblicati (li mostra
  AI Studio).
- **Prova rapida in locale**: `comitatofeste-db` su, `gemini.key.txt` +
  `key.txt` presenti, `dotnet run --project Src/backend/ComitatoFeste.Api
  --launch-profile http`, poi Swagger su `http://localhost:5065/swagger`. In
  locale il login è attivo (passphrase negli user-secrets `Auth:Password`):
  fai `POST /api/auth/login` e usa il token in "Authorize". Attenzione
  all'encoding: `curl` da Git Bash con caratteri accentati nel JSON dà 400.
- **Da fare prima del deploy**: rifinire il frontend (fonti cliccabili verso
  l'Agenda, eventuale filtro per date), verificare che Aiven supporti pgvector (`CREATE EXTENSION vector`) e che i
  1 GB di storage reggano gli embedding (~3 KB/punto), aggiungere
  `GEMINI_API_KEY` alle env Render, inserire l'Embedder nella pipeline
  (`import-transcribe-aiven.ps1`, dopo il Transcriber), aggiornare
  `docs/DEPLOY.md` e l'immagine dei Docker compose/CI se serve.

## Domanda aperta

`Members` non ha tabella alias: match sull'autore per `DisplayName`
esatto. Se emergono nickname incoerenti tra un run e l'altro, valutare
normalizzazione lowercase+trim nel service layer (nessuna modifica allo
schema richiesta) — non ancora deciso con l'utente, chiedi prima di
implementarlo.

## Prossimi passi noti

0. **Assistente AI** (`feature/assistente_ai`): frontend + hardening + deploy
   — vedi sezione "Assistente AI" sopra.
1. Rifinire il frontend (`ComitatoFeste.Api/wwwroot/index.html`): filtro autore, thumbnail ridotte
   lato server, e — con giorni molto densi (~100 punti) — virtualizzazione
   o paginazione delle righe (la sezione espansa è pesante da renderizzare).
2. Transcriber: girato sui dati 2026-09-02/03, prompt iterato. Da rifinire
   il confine `rumore`/`info`/`proposta`/`decisione` su un campione (`--limit`).
3. Deploy: **fatto** — Render (`comitatofeste.onrender.com`) + Aiven, autoDeploy
   da `main`, env impostate. Guida in `docs/DEPLOY.md`. Da rifinire: keep-alive
   (cron-job.org o `.github/workflows/keep-alive.yaml`), prova notifiche push su
   telefono (`docs/PUSH-NOTIFICHE.md`).
4. **Proteggere gli endpoint binari** (`/api/digestpoints/media/{id}/content`,
   `/api/members/{id}/photo`): oggi senza `[TokenAuth]`, su URL pubblico sono
   enumerabili. Follow-up con token in querystring (tocca il rendering media
   del frontend).
5. **Ridurre la banda in uscita di Render** (il piano Hobby ha un tetto di
   **5 GB/mese**, sforato il 10/9/2026 → workspace sospeso, aggiunta una carta:
   overage $0,15/GB). Gli endpoint blob non hanno alcun header di cache, quindi
   ogni foto / PDF / vocale riprodotto viene ri-scaricato a ogni visita di ogni
   membro. Interventi previsti, dal più economico:
   a. **FATTO** (develop `e2ee28c`, non ancora su main): `Cache-Control` + `ETag`
      su `/api/digestpoints/media/{id}/content` (immutable, max-age 1 anno) e
      `/api/members/{id}/photo` (max-age 1 g). `recap` non toccato. Range/304 ok.
   b. **FATTO** (develop `88fb26b`, non ancora su main): response compression
      brotli/gzip (`Program.cs`) sulle risposte testuali — `GET /api/digestpoints`
      355 KB → ~76 KB, `index.html` 92 → 26 KB; binari non compressi.
   b-bis. keep-alive (quando si attiva) puntato **solo** su `/api/auth/status`
      (~200 byte), mai su `/` (92 KB);
   c. **FATTO** (develop): thumbnail WebP lato server via `?w=192|480|960` su
      `/api/digestpoints/media/{id}/content` e `/api/members/{id}/photo`
      (`ImageThumbnailer` + SixLabors.ImageSharp 3.1.x). Persistiti in
      `ImageThumbnails` (migration `AddImageThumbnails`), generati una volta
      sola: sopravvivono ai cold start, una richiesta calda legge una riga
      piccola dal DB senza toccare ImageSharp né il blob originale. Frontend:
      avatar `?w=192`, tile Media `?w=480`, foto inline card `?w=960`; l'`<a
      href>` resta sull'originale. Vista Media ~12 MB → ~1 MB;
   d. Cloudflare gratis davanti al dominio (CDN edge; richiede dominio custom +
      gli header di (a));
   e. blob su Cloudflare R2 (egress gratuito) — `MediaBlob` è già tabella 1:1
      separata, vedi `docs/DEPLOY.md` §"Storage Aiven". N.B. i **documenti**
      pesano ~2 MB l'uno (uno 7 MB), 26 MB su 66 MB di blob totali.
   Follow-up: `ETag`/`max-age` breve anche su `GET /api/digestpoints` (unica
   risposta testuale ancora rimandata intera a ogni apertura).
