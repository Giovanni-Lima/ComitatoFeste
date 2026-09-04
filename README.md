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
- **Postgres 16** — di default `Host=localhost;Port=5432;Database=postgres;
  Username=postgres;Password=postgres` (container `local-postgres`,
  `postgres:16-alpine`). Override con la env `COMITATOFESTE_CONNECTION`.
- **Chiave Groq** (solo per Transcriber e per l'endpoint `recap` dell'API):
  env `GROQ_API_KEY` oppure file `key.txt` nella radice del repo (in
  `.gitignore`). Chiave gratuita su <https://console.groq.com/keys>.

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

## API + frontend

L'API serve anche il frontend (`ComitatoFeste.Api/wwwroot/index.html`) sulla
stessa origine:

```powershell
dotnet run --project Src/backend/ComitatoFeste.Api --launch-profile http
# -> http://localhost:5065/   (Swagger su /swagger in Development)
```

Vedi [`Src/backend/ComitatoFeste.Api/README.md`](Src/backend/ComitatoFeste.Api/README.md)
per i parametri URL e il login.
