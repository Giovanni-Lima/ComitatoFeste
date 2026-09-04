# Frontend — Agenda

`index.html` self-contained (vanilla JS, nessun build). Consuma
`ComitatoFeste.Api`: scarica **tutti** i punti (`GET /api/digestpoints`
senza `date`) e li raggruppa per giorno in un accordion — ogni giorno è una
sezione collassabile con la timeline verticale (righe alternate sx/dx,
badge per tipo). All'apertura è espanso solo il giorno corrente (o quello
in `?date=`); si espandono gli altri cliccando l'intestazione, o dal date
picker in alto che scrolla alla sezione e la apre.

## Avvio

```powershell
# 1. API (dalla radice del repo, C:\ComitatoFeste)
$env:ASPNETCORE_ENVIRONMENT="Development"
dotnet run --project Src/backend/ComitatoFeste.Api --launch-profile http   # -> http://localhost:5065

# 2. servire il frontend su una porta in whitelist CORS (5173 o 3000)
cd Src/frontend
python -m http.server 5173                                                 # -> http://localhost:5173
```

Apri `http://localhost:5173/`.

## Parametri URL

- `?date=2026-09-03` — giorno da espandere e a cui scrollare all'apertura
  (default: oggi, fuso Roma)
- `?api=http://host:porta` — base URL dell'API (default `http://localhost:5065`)

## Login

Se l'API ha `COMITATOFESTE_AUTH_PASSWORD` impostata, il sito chiede il
login: **utente** = `iniziale.cognome` di un membro (es. `g.lima`,
`d.caniglia`), **password** = la passphrase condivisa. Il token dura 30
giorni in `localStorage`; "esci" in alto a destra lo cancella. Senza quella
variabile d'ambiente il login è disattivato e il sito è aperto.

## Note

- Il CORS dell'API in Development ammette solo `http://localhost:5173` e
  `:3000` (vedi `Program.cs`): aprire il file con `file://` non funziona per
  le chiamate `fetch`.
- Filtri per tipo (chip) applicati lato client, su tutti i giorni; `‹ ›` e
  il date picker aprono la sezione del giorno scelto e ci scrollano.
- Il pulsante ⬇ su ogni header scarica il **verbale PDF** della giornata
  (`GET /api/digestpoints/recap`, spinner mentre genera): testo prodotto da
  Groq alla prima richiesta e messo in cache, PDF reso al volo con QuestPDF.
  Richiede `GROQ_API_KEY` nell'ambiente dell'API. `?format=md` per il
  Markdown grezzo.
- I `rumore` e i vocali non ancora digeriti (audio senza `TranscribedAt`)
  sono esclusi dall'API di default.
- Con giorni molto densi (~100 punti) la sezione espansa è pesante da
  renderizzare: `<img loading="lazy">` mitiga, ma resta un candidato per
  virtualizzazione / paginazione lato server.
