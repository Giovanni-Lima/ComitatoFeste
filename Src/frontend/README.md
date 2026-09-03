# Frontend — portale digest

`index.html` self-contained (vanilla JS, nessun build). Timeline verticale
per giorno che consuma `ComitatoFeste.Api`.

## Avvio

```powershell
# 1. API (da C:\Digest)
$env:ASPNETCORE_ENVIRONMENT="Development"
dotnet run --project Src/backend/ComitatoFeste.Api --launch-profile http   # -> http://localhost:5065

# 2. servire il frontend su una porta in whitelist CORS (5173 o 3000)
cd Src/frontend
python -m http.server 5173                                                 # -> http://localhost:5173
```

Apri `http://localhost:5173/`.

## Parametri URL

- `?date=2026-09-01` — giorno iniziale (default `2026-09-01`)
- `?api=http://host:porta` — base URL dell'API (default `http://localhost:5065`)

## Note

- Il CORS dell'API in Development ammette solo `http://localhost:5173` e
  `:3000` (vedi `Program.cs`): aprire il file con `file://` non funziona per
  le chiamate `fetch`.
- Filtri per tipo (chip) applicati lato client; navigazione giorno con `‹ ›`.
- Layout a due colonne sfalsate su desktop; su mobile collassa a colonna
  unica (i punti pari finiscono dopo i dispari — ordine cronologico non
  perfetto, da sistemare).
