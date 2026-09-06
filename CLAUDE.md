# ComitatoFeste — istruzioni per Claude Code

## Cos'è questo repo

Data/API layer (EF Core Code-First su Postgres) di una pipeline più ampia
che riassume automaticamente la chat WhatsApp del gruppo "Comitato feste
87": legge i messaggi, li classifica (decisione/domanda/media/info),
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
- **Migration applicate** al container `local-postgres` (compose esterno
  dell'utente, `postgres:16-alpine`, db `postgres`, `postgres/postgres`):
  `InitialCreate` + `AddMediaBlobs` + `AddMemberProfilePhotos` +
  `AddRumoreDigestPointType` (`'rumore'` nel CHECK di `DigestPoints.Type`) +
  `AddVerbali` (tabella `Verbali`: verbale giornaliero in cache, UNIQUE
  `(GroupId, Date)`). Connessione di default in
  `ComitatoFesteDbContextFactory` e in `appsettings.json`, override con env
  `COMITATOFESTE_CONNECTION`.
- **Dati importati** (gruppo `Comitato feste 87`, stato al 4/9/2026): 3
  `IngestionRun` da `digest_2026-09-02.json` + `digest_2026-09-03.json`
  (il `digest_2026-09-01.json` era stato importato prima ed è ora fuori da
  `Export/`). A DB: **298 `DigestPoint`** (167 del 02-09, 131 del 03-09;
  122 già classificati `rumore` dal Transcriber), **240 `MediaAsset`**,
  **20 `Member`** (14 con foto profilo da `Export/profili/<Nome>.jpg`),
  **2 `Verbale`** in cache. Il Transcriber ha già girato su tutti i 207
  vocali (`TranscribedAt` valorizzato ovunque). Import idempotente (dedup
  esatto + fuzzy; foto aggiornate solo se cambia lo SHA-256).
  `dotnet run --project Src/backend/ComitatoFeste.Importer` legge tutti i
  `C:\ComitatoFeste\Export\digest_*.json` — ma vedi l'avviso ⚠️ sotto:
  **non** rilanciarlo intero dopo il Transcriber.
- **Deploy**: immagine testata in locale (build + boot + migrate + endpoint
  OK). **DB Aiven già creato e popolato** (`pg_dump`/`pg_restore` dal locale,
  298/240/20/2, `pg_trgm` + indici + `__EFMigrationsHistory` OK) — Aiven gira
  **Postgres 18**, il `local-postgres` di dev è alla **16**. Manca solo il Web
  Service su Render (creare account + env var). Backup: `scripts/backup-db.ps1`
  (primo dump fatto in `Backups/`, non committato). Tutto in `docs/DEPLOY.md`.

## Struttura

- `Src/backend/` — la solution .NET (l'unico codice per ora).
  - `ComitatoFeste.Domain` — entità POCO pure, nessuna dipendenza EF.
  - `ComitatoFeste.Data` — `ComitatoFesteDbContext` + `Configurations/*.cs`
    (una classe Fluent API per entità: vincoli, indici, CHECK, 1:1) +
    `Migrations/` + `ComitatoFesteDbContextFactory` (design-time).
  - `ComitatoFeste.Api` — Web API ASP.NET Core.
    - **Login "casereccio"** (`AuthService` + `TokenAuthAttribute`):
      `GET /api/auth/status` → `{enabled}`; `POST /api/auth/login
      {username,password}` → `{token,username,memberId,displayName}`.
      Username = `iniziale.cognome`
      di un `Member` (derivato a runtime, niente colonna DB), password =
      passphrase condivisa (env `COMITATOFESTE_AUTH_PASSWORD` o config
      `Auth:Password`; vuota → login disattivato). Token HMAC firmato
      (`username|scadenza`, 30 gg) rimandato come `Authorization: Bearer`.
      `[TokenAuth]` protegge **solo** i due endpoint JSON qui sotto; gli
      endpoint binari (foto/media) restano aperti per `<img>/<audio>/<video>`.
    - `GET /api/digestpoints?date=yyyy-MM-dd` (+ filtri `author`, `type`) →
      lista `DigestPointDto`; **`date` opzionale**, se omesso restituisce
      tutti i giorni (non paginato). Ogni punto porta `authorId` +
      `authorPhotoUrl` e, per i media, `media.contentUrl`. Senza `type`
      esplicito la vista è pulita: niente `rumore` e niente vocali non
      ancora digeriti (audio con `TranscribedAt == null`).
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
    **⚠️ Dopo che il Transcriber ha girato NON rilanciare l'import completo**:
    riscrive `DigestPoint.Text` (sintesi), il dedup esatto chiave su `Text`
    non riconosce più i punti e li reinserisce duplicati. Per aggiungere
    solo foto profilo usare `--photos-only` (salta l'import dei digest).
    `MediaKind`
    mappa estensione → (`MediaType`, MIME): foto (jpg/png/webp/…), audio
    (ogg/opus/m4a/mp3/…), **video** (mp4/mov/webm/mkv/3gp/avi → restano
    `MediaType.Documento` ma con MIME `video/*`, vedi convenzione sotto),
    documento (pdf/doc/xls); sconosciute → `documento` +
    `application/octet-stream`.
  - `ComitatoFeste.Transcriber` — console: prende i `MediaAsset` audio da
    lavorare (`TranscriptionText == null` **oppure** `TranscribedAt ==
    null`), li trascrive con Groq Whisper e classifica la trascrizione con
    un modello gpt-oss (`GroqClient`) in decisione/domanda/info/media/`rumore`;
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
- `Src/backend/ComitatoFeste.Api/wwwroot/index.html` — frontend
  self-contained (vanilla JS, nessun build), "Comitato feste 87 — Agenda",
  servito dall'API stessa. Note operative in
  `Src/backend/ComitatoFeste.Api/README.md`. All'avvio chiama
  `GET /api/auth/status`: se
  `enabled` e non c'è token in `localStorage` (`cf87_token`) mostra un
  overlay di login (username membro + passphrase → `POST /api/auth/login`),
  altrimenti carica; il token va in `Authorization: Bearer` su ogni fetch
  JSON, un 401 riporta al login, il bottone "esci" in topbar lo cancella.
  Consuma `GET /api/digestpoints` **senza
  `date`** (tutti i giorni) e li raggruppa lato client per giorno Roma in
  un **accordion**: una `<section class="day">` per data, collassata, con
  la timeline verticale (righe alternate sx/dx, badge per tipo) nel
  `.day-body`. All'atterraggio è espanso solo il giorno `?date=` (default
  oggi); il click sull'header di un giorno lo espande/collassa; il date
  picker in topbar fa `goToDay` → espande la sezione e ci scrolla
  (`scrollIntoView` + `scroll-margin-top`). Ogni header ha un pulsante
  download (con spinner) che chiama `GET /api/digestpoints/recap` e scarica
  il verbale **PDF** della giornata. Foto inline, `<audio>` /
  `<video>` player scelto dal prefisso di `media.contentType`
  (`image/`/`video/`/`audio/`), non dal `mediaType` (video `documento`
  comunque riprodotto); `<img loading="lazy">`. Base URL API: `?api=` se
  presente, altrimenti **stessa origine** (in produzione l'API serve questo
  file). In locale: `dotnet run` dell'API e apri `http://localhost:5065/`,
  oppure servi il file a parte con `?api=`; vedi
  `Src/backend/ComitatoFeste.Api/README.md`.
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

Il repo intero (compreso l'export della chat) vive ora in `C:\ComitatoFeste`
(spostato da `C:\Digest` il 4/9). Gli script Python che generano i
`digest_<data>.json` in `Export/` a partire dal `.txt` esportato da
WhatsApp Android ("esporta chat con media") sono ora versionati nel repo
in **`scripts/whatsapp-digest/`** (`parse_wa.py` + un `build_digest_MMGG.py`
per ogni giorno già fatto, `README.md` con la procedura passo-passo) — sono
lo storico affidabile di come è stato costruito ogni digest, copiali/
adattali per un nuovo giorno invece di ripartire da zero. Restano da
rigenerare ogni volta nella sessione device-linked (leggono/scrivono file
nella home della VM, fuori dal repo) perché serve `ffprobe`/`ffmpeg` e
l'accesso diretto ai file della chat sul PC dell'utente. Regole stabili da
seguire in ogni rigenerazione (dettagliate anche nel README sopra):

- **Ogni vocale (audio) va tenuto**, una entry per vocale, anche se simile a
  uno precedente — l'audio non va mai trattato come "rumore" in fase di
  generazione del digest (il filtro sul contenuto poco utile è compito del
  Transcriber via Groq, non di questo script).
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

## Domanda aperta

`Members` non ha tabella alias: match sull'autore per `DisplayName`
esatto. Se emergono nickname incoerenti tra un run e l'altro, valutare
normalizzazione lowercase+trim nel service layer (nessuna modifica allo
schema richiesta) — non ancora deciso con l'utente, chiedi prima di
implementarlo.

## Prossimi passi noti

1. Rifinire il frontend (`ComitatoFeste.Api/wwwroot/index.html`): filtro autore, thumbnail ridotte
   lato server, e — con giorni molto densi (~100 punti) — virtualizzazione
   o paginazione delle righe (la sezione espansa è pesante da renderizzare).
2. Transcriber: girato sui dati 2026-09-02/03, prompt iterato. Da rifinire
   il confine `rumore`/`info`/`decisione` su un campione (`--limit`).
3. Deploy: `Dockerfile` + `render.yaml` + `docker-compose.yml` pronti, guida
   in `docs/DEPLOY.md` (Render + Aiven). Da fare: creare gli account,
   impostare le env su Render, primo deploy.
4. **Proteggere gli endpoint binari** (`/api/digestpoints/media/{id}/content`,
   `/api/members/{id}/photo`): oggi senza `[TokenAuth]`, su URL pubblico sono
   enumerabili. Follow-up con token in querystring (tocca il rendering media
   del frontend).
