# ComitatoFeste.Api — API + frontend "Agenda"

Web API ASP.NET Core che serve anche il frontend statico
(`wwwroot/index.html`, vanilla JS, nessun build) sulla stessa origine.

## Frontend

`wwwroot/index.html` scarica **tutti** i punti (`GET /api/digestpoints`
senza `date`) e li raggruppa per giorno in un accordion — ogni giorno è una
sezione collassabile con la timeline verticale (righe alternate sx/dx,
badge per tipo). All'apertura è espanso solo il giorno corrente (o quello
in `?date=`); si espandono gli altri cliccando l'intestazione, o dal date
picker in alto che scrolla alla sezione e la apre.

## Avvio

```powershell
# dalla radice del repo, C:\ComitatoFeste
$env:ASPNETCORE_ENVIRONMENT="Development"
dotnet run --project Src/backend/ComitatoFeste.Api --launch-profile http
```

Apri `http://localhost:5065/` (Swagger su `/swagger`). Serve Postgres con
pgvector (`docker compose -f docker-compose.db.yml up -d`, vedi README radice).
Le modifiche a `wwwroot/index.html` si vedono
con un semplice refresh (in Development `dotnet watch` ricarica, altrimenti
riavvia).

Per iterare sul solo frontend senza toccare l'API si può servire il file a
parte e puntare l'API con `?api=`:

```powershell
cd Src/backend/ComitatoFeste.Api/wwwroot
python -m http.server 5173   # -> http://localhost:5173/?api=http://localhost:5065
```

(il CORS in Development ammette `:5173` e `:3000`).

## Parametri URL

- `?date=2026-09-03` — giorno da espandere e a cui scrollare all'apertura
  (default: oggi, fuso Roma)
- `?api=http://host:porta` — base URL dell'API. Default: **stessa origine**
  della pagina (in produzione l'API serve anche il frontend)

## Login

Se l'API ha `COMITATOFESTE_AUTH_PASSWORD` impostata, il sito chiede il
login: **utente** = `iniziale.cognome` di un membro (es. `g.lima`,
`d.caniglia`), **password** = la passphrase condivisa. Il token dura 30
giorni in `localStorage`; "esci" in alto a destra lo cancella. Senza quella
variabile d'ambiente il login è disattivato e il sito è aperto.

## Assistente AI

`POST /api/assistant/ask {question, from?, to?}` (`[TokenAuth]`) risponde a
domande in linguaggio naturale sui punti del digest: embedding della domanda con
Gemini → 40 punti più vicini con pgvector → risposta con citazioni `[n]` dalla
catena Gemini 3.5 Flash Lite → Gemini 3.1 Flash Lite → Groq (vedi `CLAUDE.md`,
sezione "Assistente AI"). Richiede `GEMINI_API_KEY` (o `gemini.key.txt`) e gli
embedding già calcolati (`ComitatoFeste.Embedder`); `GROQ_API_KEY` (o `key.txt`)
serve solo come ultimo ripiego. Senza chiave Gemini risponde 503. Limiti per utente/giorno
in memoria (`Assistant:PerUserPerHour|GlobalPerDay|MaxConcurrent`). In locale il
login è attivo: `POST /api/auth/login` e poi "Authorize" in Swagger.
Il frontend ha la vista **Æsir** (voce di menu al posto di "Guida"): un volto con
occhi espressivi (neutro → concentrato → felice) sopra la casella della domanda.

## Note

- Servito dall'API (stessa origine) le `fetch` sono relative e non serve
  CORS. Aprendo il file con `file://` o da `:5173` le chiamate `fetch`
  funzionano solo verso un'origine in whitelist CORS (Development: `:5173`,
  `:3000`).
- Filtri per tipo (chip) applicati lato client, su tutti i giorni; `‹ ›` e
  il date picker aprono la sezione del giorno scelto e ci scrollano.
- Il pulsante ⬇ su ogni header scarica il **verbale PDF** della giornata
  (`GET /api/digestpoints/recap`, spinner mentre genera): testo prodotto da
  Groq alla prima richiesta e messo in cache, PDF reso al volo con QuestPDF.
  Richiede `GROQ_API_KEY` nell'ambiente dell'API. `?format=md` per il
  Markdown grezzo.
- I `rumore` e i vocali non ancora digeriti (audio senza `TranscribedAt`)
  sono esclusi dall'API di default.
- Gli URL nel testo di un punto diventano link cliccabili; sotto la card
  compare un'anteprima OpenGraph (`GET /api/links/preview`, cache in memoria
  lato API, serve solo per URL già presenti in un punto). Immagine in hotlink
  dal sito originale; se la pagina non espone meta la card non compare.
- Con giorni molto densi (~100 punti) la sezione espansa è pesante da
  renderizzare: `<img loading="lazy">` mitiga, ma resta un candidato per
  virtualizzazione / paginazione lato server.
- Tipografia: topbar, titoli dei giorni, voci di menu, badge dei filtri,
  badge/nomi utente usano il font pixel **Thaleah Fat** (Rick Hoppmann,
  CC-BY 4.0, in `wwwroot/fonts/`), via la variabile CSS `--font-display`.
  Il font copre **solo Basic Latin** (niente à/è/ì/ò/ù): l'`@font-face` ha
  un `unicode-range` esplicito così gli accenti ricadono sul font di
  sistema, e `fmtDay` usa il giorno della settimana **abbreviato**
  (`sab/dom/lun/…`) per evitare del tutto la "ì" nei titoli. Se aggiungi
  `--font-display` a testo che può contenere accenti, aspettati quel
  fallback per-glifo.
