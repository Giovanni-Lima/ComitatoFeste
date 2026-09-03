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
- **Dati importati**: `dotnet run --project
  Src/backend/ComitatoFeste.Importer` legge tutti i
  `C:\Digest\Export\digest_*.json` e li persiste (19 punti: 17 del
  2026-09-01 + 2 del 2026-09-02, 1 media), poi sincronizza le foto profilo
  da `Export/profili/<Nome>.jpg` (9 su 12 membri). Import idempotente
  (dedup esatto + fuzzy; foto aggiornate solo se cambia lo SHA-256).

## Struttura

- `Src/backend/` — la solution .NET (l'unico codice per ora).
  - `ComitatoFeste.Domain` — entità POCO pure, nessuna dipendenza EF.
  - `ComitatoFeste.Data` — `ComitatoFesteDbContext` + `Configurations/*.cs`
    (una classe Fluent API per entità: vincoli, indici, CHECK, 1:1) +
    `Migrations/` + `ComitatoFesteDbContextFactory` (design-time).
  - `ComitatoFeste.Api` — Web API ASP.NET Core.
    - `GET /api/digestpoints?date=yyyy-MM-dd` (+ filtri `author`, `type`) →
      lista `DigestPointDto`; **`date` opzionale**, se omesso restituisce
      tutti i giorni (non paginato). Ogni punto porta `authorId` +
      `authorPhotoUrl` e, per i media, `media.contentUrl`. Senza `type`
      esplicito la vista è pulita: niente `rumore` e niente vocali non
      ancora digeriti (audio con `TranscribedAt == null`).
    - `GET /api/digestpoints/recap?date=yyyy-MM-dd[&refresh=true][&format=md]`
      → verbale in prosa della giornata, **PDF** di default (`format=md` per
      il Markdown grezzo), `Content-Disposition: attachment`. Il testo è
      generato da Groq (`GroqRecapClient`, `openai/gpt-oss-120b`) alla prima
      richiesta e messo in cache in `Verbali` (Markdown); il PDF è reso al
      volo da quel Markdown con QuestPDF (`VerbalePdf`), senza nuove
      chiamate. `refresh=true` rigenera il testo. 404 senza punti, 503
      senza `GROQ_API_KEY`.
    - `GET /api/digestpoints/media/{mediaId}/content` → byte del blob inline.
    - `GET /api/members/{memberId}/photo` → foto profilo inline.
    DTO in `Contracts/`, Swagger in Development, CORS dev `localhost:5173/3000`.
    La chiave Groq (solo per `recap`) è risolta da `GroqKey.Resolve()`: env
    `GROQ_API_KEY`, poi file `key.txt` (in `.gitignore`, cercato risalendo
    fino alla radice del repo), poi config `Groq:ApiKey`.
  - `ComitatoFeste.Importer` — console: legge i `digest_*.json` da Export e
    li scrive a DB (`DigestImporter` è la classe riusabile);
    `ImportProfilePhotosAsync` sincronizza `Export/profili/`. `MediaKind`
    mappa estensione → (`MediaType`, MIME): foto (jpg/png/webp/…), audio
    (ogg/opus/m4a/mp3/…), **video** (mp4/mov/webm/mkv/3gp/avi → restano
    `MediaType.Documento` ma con MIME `video/*`, vedi convenzione sotto),
    documento (pdf/doc/xls); sconosciute → `documento` +
    `application/octet-stream`.
  - `ComitatoFeste.Transcriber` — console: prende i `MediaAsset` audio da
    lavorare (`TranscriptionText == null` **oppure** `TranscribedAt ==
    null`), li trascrive con Groq `whisper-large-v3` (non `-turbo`: meglio
    su dialetto/audio rumoroso, la velocità qui non serve) e classifica la
    trascrizione con `openai/gpt-oss-120b` (`GroqClient`) in
    decisione/domanda/info/media/`rumore`; poi riscrive `DigestPoint.Type`
    e `Text` (sintesi in una frase, o messaggio segnaposto se `rumore`).
    Modelli scelti per il tier gratuito Groq (i `llama-3.x` deprecati giu
    2026). Free tier gpt-oss (20b **e** 120b, identici): 1.000 req/g, 200k
    token/g, 30/min, 8.000 token/min — ma **contatore separato per
    modello**. `GroqClient` ha un freno TPM adattivo (finestra 60 s su
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
- `Src/frontend/` — `index.html` self-contained (vanilla JS, nessun build),
  "Comitato feste 87 — Agenda". Consuma `GET /api/digestpoints` **senza
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
  comunque riprodotto); `<img loading="lazy">`. Si serve su `:5173`
  (`python -m http.server 5173`); vedi `Src/frontend/README.md`.
- `Export/` — dati sorgente della pipeline sul PC dell'utente:
  `digest_<data>.json`, sottocartella `<data>/` con i media rinominati
  (le sottocartelle `_da-attribuire` / `_conflitto-autore` /
  `_gia-in-db-senza-media` sono triage manuale dell'utente, l'import le
  ignora), e `profili/<Nome-con-trattini>.jpg` per le foto profilo.
- `docs/sample-digest_2026-09-01.json` — sottoinsieme di `Export/digest_2026-09-01.json`,
  utile per capire la forma del JSON sorgente (date/time/author/type/text/file).
- `schema.reference.sql` / `docker-compose.yml` / `README.md` — citati come
  passi previsti ma **non ancora presenti** nel repo.

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

1. Rifinire il frontend `Src/frontend/`: filtro autore, thumbnail ridotte
   lato server, e — con giorni molto densi (~100 punti) — virtualizzazione
   o paginazione delle righe (la sezione espansa è pesante da renderizzare).
2. Transcriber: girato sui dati 2026-09-02/03, prompt iterato. Da rifinire
   il confine `rumore`/`info`/`decisione` su un campione (`--limit`).
3. Dockerfile per `ComitatoFeste.Api` + `docker-compose.yml` (o aggancio
   al compose esistente dell'utente). Nel compose serve passare
   `GROQ_API_KEY` all'API per l'endpoint `recap`.
