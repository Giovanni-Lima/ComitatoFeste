# ComitatoFeste

Data/API layer (EF Core Code-First su Postgres) della pipeline che riassume
la chat WhatsApp del gruppo "Comitato feste 87": importa i digest giornalieri,
trascrive/classifica i vocali con Groq, li espone via Web API e li mostra in
un frontend timeline.

Contesto e razionale delle decisioni: [`docs/CONTEXT.md`](docs/CONTEXT.md).
Istruzioni operative per chi mette mano al codice: [`CLAUDE.md`](CLAUDE.md).

## Prerequisiti

- **.NET SDK** — i progetti targettano `net8.0`; in macchina basta un SDK
  recente (9/10), i reference pack .NET 8 arrivano da NuGet.
- **Postgres 16 con pgvector** — di default `Host=localhost;Port=5432;
  Database=postgres;Username=postgres;Password=postgres`. Si avvia con
  `docker compose -f docker-compose.db.yml up -d` (container `comitatofeste-db`,
  immagine `pgvector/pgvector:pg16`, dati in `./data/postgres/`). L'estensione
  `vector` serve alla migration dell'assistente AI. Override con la env
  `COMITATOFESTE_CONNECTION`.
- **Chiave Groq** (solo per Transcriber e per l'endpoint `recap` dell'API):
  env `GROQ_API_KEY` oppure file `key.txt` nella radice del repo (in
  `.gitignore`). Chiave gratuita su <https://console.groq.com/keys>.
- **Chiave Gemini** (solo per l'Embedder e l'assistente AI): env
  `GEMINI_API_KEY` oppure file `gemini.key.txt` nella radice (in `.gitignore`).
  Chiave gratuita su <https://aistudio.google.com/apikey>.

## Build

```powershell
dotnet build Src/backend/ComitatoFeste.slnx
```

## Migration

```powershell
dotnet ef database update --project Src/backend/ComitatoFeste.Data
```

## Import dei digest

Legge tutti i `Export/digest_*.json` e sincronizza le foto profilo da
`Export/profili/`. Idempotente (dedup esatto + fuzzy pg_trgm).

```powershell
dotnet run --project Src/backend/ComitatoFeste.Importer
```

> ⚠️ Dopo che il Transcriber ha girato **non** rilanciare l'import completo:
> riscriverebbe `DigestPoint.Text` con la sintesi e reinserirebbe i punti
> come duplicati. Per le sole foto profilo: `-- --photos-only`.

## Trascrizione + classificazione dei vocali

```powershell
dotnet run --project Src/backend/ComitatoFeste.Transcriber
# opzioni: --dry-run  --limit <n>  --delay-ms <n>  --group <nome>
```

## Embedding per l'assistente AI

Calcola (con Gemini) l'embedding dei punti nuovi o cambiati e lo salva in
`DigestPointEmbeddings`. Idempotente: serve sia da backfill sia da
aggiornamento dopo import + trascrizione. Su `develop`, non ancora su `main`.
Exit code 10 = quota Gemini esaurita (run parziale, non è un errore). Lo lancia da solo
`scripts/import-transcribe-aiven.ps1` dopo il Transcriber, senza bloccare la pipeline.

```powershell
dotnet run --project Src/backend/ComitatoFeste.Embedder
# opzioni: --dry-run  --limit <n>  --batch-size <n>  --delay-ms <n>  --max-attempts <n>  --group <nome>
#          --search "<domanda>" [--top <n>]   (non scrive: mostra i punti più vicini)
```

## API + frontend

L'API serve anche il frontend (`ComitatoFeste.Api/wwwroot/index.html`) sulla
stessa origine:

```powershell
dotnet run --project Src/backend/ComitatoFeste.Api --launch-profile http
# -> http://localhost:5065/   (Swagger su /swagger in Development)
```

L'assistente AI (`POST /api/assistant/ask`) richiede `GEMINI_API_KEY` e
`GROQ_API_KEY` e gli embedding già calcolati. Vedi [`Src/backend/ComitatoFeste.Api/README.md`](Src/backend/ComitatoFeste.Api/README.md)
per i parametri URL e il login.
