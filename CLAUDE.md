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
  `InitialCreate` + `AddMediaBlobs` + `AddMemberProfilePhotos`. Connessione
  di default in `ComitatoFesteDbContextFactory` e in `appsettings.json`,
  override con env `COMITATOFESTE_CONNECTION`.
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
      lista `DigestPointDto` della giornata (fuso Roma); ogni punto porta
      `authorId` + `authorPhotoUrl` e, per i media, `media.contentUrl`.
    - `GET /api/digestpoints/media/{mediaId}/content` → byte del blob inline.
    - `GET /api/members/{memberId}/photo` → foto profilo inline.
    DTO in `Contracts/`, Swagger in Development, CORS dev `localhost:5173/3000`.
  - `ComitatoFeste.Importer` — console: legge i `digest_*.json` da Export e
    li scrive a DB (`DigestImporter` è la classe riusabile);
    `ImportProfilePhotosAsync` sincronizza `Export/profili/`.
- `Src/frontend/` — `index.html` self-contained (vanilla JS, nessun build):
  timeline verticale per giorno (righe alternate sx/dx su linea centrale,
  badge per tipo), consuma `GET /api/digestpoints`
  (audio player, foto inline, avatar da `/api/members/{id}/photo`). Si serve
  su `:5173` (`python -m http.server 5173`); vedi `Src/frontend/README.md`.
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

1. Rifinire il frontend `Src/frontend/` (v1 timeline già funzionante):
   layout mobile a colonna unica cronologica, filtro autore, thumbnail
   ridotte lato server invece dell'originale full-size.
2. Integrazione Groq Whisper per popolare `MediaAssets.TranscriptionText`
   sui vocali non trascritti.
3. Dockerfile per `ComitatoFeste.Api` + `docker-compose.yml` (o aggancio
   al compose esistente dell'utente).
