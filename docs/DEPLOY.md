# Deploy — Render + Aiven

> **Stato:** in produzione su <https://comitatofeste.onrender.com> (Render + Aiven,
> autoDeploy da `main`, env impostate incluse quelle delle notifiche push). Le
> sezioni sotto restano come guida/riferimento per ricreare o modificare il setup.

Portale pubblico a costo zero. Un solo servizio applicativo su **Render**
(container Docker: API .NET + frontend statico sulla stessa origine), database
**PostgreSQL gestito su Aiven**. La pipeline `Importer`/`Transcriber` resta in
locale e scrive sul DB Aiven via `COMITATOFESTE_CONNECTION`.

```
   cron-job.org ──(GET /api/auth/status ogni 14', 6-23)──┐  keep-alive, non tocca il DB
   cron-job.org ──(HEAD / una volta al giorno, ore 6:01)──┤  sveglia dopo la notte (00-06 spento)
                                                           ▼
                 ┌─────────────────────────────┐
   browser  ───▶ │ Render Web Service (Docker)  │ ──▶  Aiven PostgreSQL (managed)
                 │  ComitatoFeste.Api           │ ──▶  Groq API (solo /recap: verbale non in cache)
                 │  + wwwroot/index.html        │ ──▶  push service (Web Push a fine import)
                 └─────────────────────────────┘
                          ▲
   PC locale: Importer / Transcriber ──┘  (COMITATOFESTE_CONNECTION = Aiven; Groq/Whisper per i vocali;
                                            POST /api/push/broadcast a fine run)
```

File in gioco: `Dockerfile`, `.dockerignore`, `render.yaml`, `docker-compose.yml`
e `docker-compose.db.yml` (gli ultimi due solo per lo sviluppo locale).
Schema completo dei servizi esterni e delle interazioni: `docs/ARCHITETTURA.md`.

---

## 1 · Database su Aiven

1. Registrati su <https://aiven.io> (no carta di credito per il piano free).
2. **Create service → PostgreSQL**.
   - Piano: **Free** (1 CPU / 1 GB RAM / **1 GB storage**, nodo singolo, sempre
     acceso — niente pausa).
   - Cloud/region: una **UE** (es. `google-europe-west1`, Belgio).
   - Nome: `comitatofeste`.
3. Quando lo stato è *Running*, apri la scheda **Connection information**.
   Aiven mostra una URI tipo:

   ```
   postgres://avnadmin:AVNS_xxxxxxxx@pg-xxxx-comitatofeste.a.aivencloud.com:23456/defaultdb?sslmode=require
   ```

4. Convertila in **formato Npgsql** (è quella che useremo ovunque):

   ```
   Host=pg-xxxx-comitatofeste.a.aivencloud.com;Port=23456;Database=defaultdb;Username=avnadmin;Password=AVNS_xxxxxxxx;SSL Mode=Require;Trust Server Certificate=true
   ```

   > `Trust Server Certificate=true` cifra la connessione ma non verifica la
   > catena del certificato Aiven (CA propria). Per l'irrigidimento: scarica la
   > CA da Aiven e usa `Root Certificate=/percorso/ca.pem` al posto del trust.

Nessun'altra configurazione: niente utenti, rete o backup da impostare a mano.

---

## 2 · Servizio su Render

1. Registrati su <https://render.com> con l'account GitHub (no carta per il
   piano free).
2. **New → Blueprint**, seleziona il repo `Giovanni-Lima/ComitatoFeste`.
   Render legge `render.yaml` e propone il servizio `comitatofeste`
   (Docker, region Frankfurt, piano Free, health check `/api/auth/status`).
   In alternativa **New → Web Service** manuale: runtime *Docker*, region
   *Frankfurt*, piano *Free*.
3. Imposta le variabili d'ambiente (tab **Environment**, sono `sync: false`
   nel blueprint → vanno messe qui, non nel repo):

   | Variabile | Valore |
   |---|---|
   | `COMITATOFESTE_CONNECTION` | la stringa Npgsql del passo 1 |
   | `COMITATOFESTE_AUTH_PASSWORD` | la passphrase condivisa del comitato |
   | `COMITATOFESTE_AUTH_PASSWORD_ADMIN` | *opzionale* — passphrase separata per il ruolo amministratore (eleva il token solo per i membri con `Role=Amministratore`; stellina "importante", nessun limite all'assistente AI). Assente → nessun admin |
   | `COMITATOFESTE_AUTH_SECRET` | **32+ caratteri casuali, fissi** (senza, ogni redeploy invalida tutti i login) |
   | `GEMINI_API_KEY` | *opzionale* — assistente AI Æsir (embedding delle domande + risposta, con Groq come ripiego). Assente → `POST /api/assistant/ask` risponde 503 |
   | `GROQ_API_KEY` | *opzionale* — solo per generare verbali di giorni non ancora in cache |
   | `COMITATOFESTE_R2_ACCOUNT_ID` / `_ACCESS_KEY_ID` / `_SECRET_ACCESS_KEY` / `_BUCKET` | *opzionali, tutte e quattro insieme* — byte dei file su Cloudflare R2 invece che in Postgres (vedi "Limiti" più sotto). Assenti → byte in Postgres |
   | `COMITATOFESTE_VAPID_PUBLIC` / `_PRIVATE` | *opzionale* — coppia VAPID per le notifiche push (vedi sotto). Assenti → bottone 🔔 nascosto |
   | `COMITATOFESTE_VAPID_SUBJECT` | `mailto:giovannilima800@gmail.com` (già nel blueprint) |
   | `COMITATOFESTE_HOOK_SECRET` | *opzionale* — secret condiviso con la pipeline locale per `POST /api/push/broadcast`. Stringa casuale, **diversa** da `COMITATOFESTE_AUTH_PASSWORD` |
   | `PORT` | `8080` (già nel blueprint) |

   > **Chiavi VAPID** (per le notifiche push): genera la coppia una volta con
   > `npx web-push generate-vapid-keys` — `publicKey` → `COMITATOFESTE_VAPID_PUBLIC`,
   > `privateKey` → `COMITATOFESTE_VAPID_PRIVATE` (segreto, solo su Render). Devono
   > essere della **stessa** coppia. Le stesse `COMITATOFESTE_HOOK_URL` (=
   > `https://comitatofeste.onrender.com`) e `COMITATOFESTE_HOOK_SECRET` vanno poi
   > sul PC locale per `Importer`/`Transcriber` (vedi §4). Dettaglio completo in
   > `docs/PUSH-NOTIFICHE.md`.

4. **Create / Deploy**. Primo build ~3-5 min. Al primo avvio l'API applica da
   sola le migration sul DB Aiven vuoto (`Database.Migrate()` in `Program.cs`).

---

## 3 · Verifica

- `https://comitatofeste.onrender.com/api/auth/status` → `{"enabled":true}`
- `https://comitatofeste.onrender.com/` → carica il portale
- Primo accesso: utente `iniziale.cognome` di un membro (es. `d.caniglia`),
  password = `COMITATOFESTE_AUTH_PASSWORD`.

La tabella dei dati è vuota finché non fai il primo import (passo 4).

---

## 4 · Caricare i dati (dal PC locale → Aiven)

La trascrizione/classificazione (Groq/Whisper) resta in locale: sul cloud non
gira nulla di pesante.

```powershell
$env:COMITATOFESTE_CONNECTION = "Host=pg-xxxx...;...;SSL Mode=Require;Trust Server Certificate=true"
# opzionale: notifica push ai membri a fine run (serve la coppia sul Web Service)
$env:COMITATOFESTE_HOOK_URL    = "https://comitatofeste.onrender.com"
$env:COMITATOFESTE_HOOK_SECRET = "<lo stesso valore impostato su Render>"

dotnet run --project Src/backend/ComitatoFeste.Importer      # digest_*.json + foto profilo
dotnet run --project Src/backend/ComitatoFeste.Transcriber   # vocali -> testo + classificazione
```

> Le notifiche push sono **best-effort**: se `COMITATOFESTE_HOOK_URL`/`_SECRET` non
> sono impostate, o Render è freddo/irraggiungibile, il run stampa un avviso e
> prosegue. `Importer` notifica se ha inserito ≥1 punto, `Transcriber` se ha
> trascritto ≥1 vocale; con un solo giorno la seconda notifica **aggiorna** la
> prima (stesso `tag`).

Il portale online riflette subito i nuovi dati (nessun redeploy).

> Su una macchina **senza il runtime .NET 8** installato (solo 9/10) i tre
> eseguibili — che targettano `net8.0` — compilano ma non partono
> (`Framework 'Microsoft.NETCore.App' 8.0.0 not found`). Anteponi
> `$env:DOTNET_ROLL_FORWARD = "Major"` (o `dotnet run --roll-forward Major`),
> oppure installa l'ASP.NET Core Runtime 8.

> Il reimport della stessa giornata è idempotente anche dopo il Transcriber
> (i punti media sono dedup per nome file, non per testo — vedi `CLAUDE.md`).
> Resta a rischio solo un punto di solo testo riformulato sotto la soglia
> fuzzy tra un import e l'altro. Per le sole foto: `-- --photos-only`.

---

## 4b · Propagare a Aiven un giorno già lavorato in locale (senza rifare Groq)

Se un giorno è già stato importato **e trascritto sul Postgres locale**, rifarlo su
Aiven con `Importer` + `Transcriber` rispenderebbe i token Groq/Whisper di quei
vocali. Alternativa: copiare solo le righe di quel giorno da locale ad Aiven con
`COPY`. Valido finché gli ID identity del locale non collidono con quelli di Aiven
— vero se il locale è nato da un dump di Aiven e da allora solo il locale ha
importato quel giorno (le sequenze proseguono da dove le ha lasciate Aiven).

```bash
AIVEN="postgresql://avnadmin:...@...:11068/defaultdb?sslmode=require"   # = scripts/aiven.uri
RUN=8   # Id dell'IngestionRun del giorno, sul Postgres locale

# in ordine di FK; il container locale del compose è "comitatofeste-db"
for pair in \
  'IngestionRuns|SELECT * FROM "IngestionRuns" WHERE "Id"='$RUN \
  'DigestPoints|SELECT * FROM "DigestPoints" WHERE "IngestionRunId"='$RUN \
  'MediaAssets|SELECT ma.* FROM "MediaAssets" ma JOIN "DigestPoints" dp ON dp."Id"=ma."DigestPointId" WHERE dp."IngestionRunId"='$RUN \
  'MediaBlobs|SELECT mb.* FROM "MediaBlobs" mb JOIN "MediaAssets" ma ON ma."Id"=mb."MediaAssetId" JOIN "DigestPoints" dp ON dp."Id"=ma."DigestPointId" WHERE dp."IngestionRunId"='$RUN ; do
  t="${pair%%|*}"; q="${pair#*|}"
  docker exec -i comitatofeste-db psql -U postgres -d postgres -c "\copy ($q) TO STDOUT" \
   | docker run --rm -i postgres:18-alpine psql "$AIVEN" -c "\copy \"$t\" FROM STDIN"
done

# riallinea le sequenze identity di Aiven al max(Id) copiato
docker run --rm -i postgres:18-alpine psql "$AIVEN" <<'SQL'
SELECT setval(pg_get_serial_sequence('"IngestionRuns"','Id'), (SELECT max("Id") FROM "IngestionRuns"));
SELECT setval(pg_get_serial_sequence('"DigestPoints"','Id'),  (SELECT max("Id") FROM "DigestPoints"));
SELECT setval(pg_get_serial_sequence('"MediaAssets"','Id'),   (SELECT max("Id") FROM "MediaAssets"));
SELECT setval(pg_get_serial_sequence('"MediaBlobs"','Id'),    (SELECT max("Id") FROM "MediaBlobs"));
SQL
```

Verifica i conteggi su Aiven dopo la copia. I `Verbali` non si copiano: quelli
veri li genera l'API online e restano solo su Aiven.

---

## 5 · Aggiornamenti

`git push` su `main` → Render ribuilda e ripubblica (`autoDeploy: true`).
Rollback a una versione precedente dalla dashboard Render (**Deploys → Rollback**).

## 6 · Backup del database

Il piano free di Aiven non offre backup/PITR affidabili. In più il DB locale
della pipeline è già un quasi-mirror (l'unico dato solo-cloud sono i `Verbali`
generati online). Backup giornaliero con `scripts/backup-db.ps1`:

- legge l'URI Aiven da `scripts/aiven.uri` (gitignorato, una riga:
  `postgres://avnadmin:...@...:11068/defaultdb?sslmode=require`);
- `pg_dump -Fc` via un client `postgres:18` usa-e-getta (Aiven gira Postgres
  18, il container `comitatofeste-db` è alla 16 e non può esportare da un
  server più recente);
- scrive `Backups/cf-YYYY-MM-DD.dump` (gitignorato) e ruota a 30 giorni.

Schedulazione giornaliera (una volta, in PowerShell):

```powershell
$a = New-ScheduledTaskAction -Execute "powershell.exe" `
     -Argument '-NoProfile -File "C:\ComitatoFeste\scripts\backup-db.ps1"'
$t = New-ScheduledTaskTrigger -Daily -At 2am
Register-ScheduledTask -TaskName "ComitatoFeste-DB-Backup" -Action $a -Trigger $t
```

Restore (in un DB Postgres >= 18, es. un altro Aiven):

```powershell
docker run --rm -v "C:\ComitatoFeste\Backups:/backups" postgres:18-alpine `
  pg_restore --no-owner --clean --if-exists -d "<uri>" /backups/cf-YYYY-MM-DD.dump
```

**Riallineare il locale (Postgres 16) da Aiven** (workflow corrente dopo
import/trascrizione su Aiven, vedi CLAUDE.md): `pg_restore` da un client 18
contro un server 16 fallisce — il dump va convertito in SQL testuale e
filtrato di due righe che il 16 non riconosce (`SET transaction_timeout` e
le direttive psql `\restrict`/`\unrestrict`, tutte introdotte in pg_dump 18):

```bash
docker run --rm postgres:18-alpine sh -c \
  'pg_dump --no-owner --no-privileges --no-comments -Fc -d "$AIVEN_URI" \
   | pg_restore --no-owner --no-privileges --clean --if-exists -f -' \
  | grep -v -F 'SET transaction_timeout' | grep -v -F '\restrict' | grep -v -F '\unrestrict' \
  > dump.sql
docker exec -i comitatofeste-db psql -U postgres -d postgres -v ON_ERROR_STOP=1 < dump.sql
```

(`--clean --if-exists` include i `DROP` necessari: il locale viene svuotato
e ricreato da zero, non serve droppare a mano.)

Upgrade opzionale (offsite, gira anche a PC spento): workflow GitHub Actions
schedulato → `pg_dump` → Cloudflare R2 (10 GB free) con lifecycle a 30 giorni.

---

## Limiti e cose da sapere

- **Cold start**: il piano free di Render spegne il container dopo ~15 min di
  inattività; la richiesta successiva attende ~40-60 s. **Keep-alive attivo
  dal 22/9/2026** su <https://cron-job.org>, due job:
  1. `*/14 6-23 * * *` → `GET /api/auth/status`, ogni 14 min nella fascia
     6:00-24:00 — quell'endpoint **non** tocca il DB, quindi non consuma
     risorse Aiven;
  2. `1 6 * * *` → `HEAD /` una volta al giorno, sveglia esplicita subito
     dopo la finestra di sonno notturna.

  Tra le 00:00 e le 06:00 non c'è nessun ping: il container si spegne e chi
  apre l'app in quella finestra paga il cold start — accettato, il traffico
  reale a quell'ora è trascurabile. Con la fascia 6-24 coperta: ~18 h/giorno
  × 31 = 558 h/mese, ben sotto le 750 h/mese del free; estendere a 24/7
  costerebbe ~744 h/mese (margine ~6 h nei mesi da 31 giorni, sul filo se in
  futuro girano altri servizi free nello stesso workspace Render) — per
  questo si è preferita la sveglia mirata invece delle 24 ore coperte.
  **Un keep-alive ricorrente deve restare un `GET`/`HEAD` leggero
  (`/api/auth/status`, o un `HEAD /`), mai un `GET /` ripetuto**: l'HTML è
  ~92 KB e a 4320 ping/mese sarebbe ~400 MB di banda in uscita (vedi punto
  sotto) — un `HEAD` invece non scarica il body, quindi il job 2 non pesa
  pur puntando a `/`.

  Il vecchio `.github/workflows/keep-alive.yaml` (GitHub Actions, pingava
  `GET /` ogni 14 min 6:00-24:00 CET/CEST, ridondante col job 1 di
  cron-job.org) è stato **rimosso il 22/9/2026**: cron-job.org basta da solo.
- **Banda in uscita (5 GB/mese sul piano Hobby)**: sforata il 10/9/2026 →
  *"Workspace suspended — you've used the 5 GB of free bandwidth"*; sbloccata
  aggiungendo una carta (overage $0,15/GB; Pro include 25 GB). Causa: gli
  endpoint che servono i byte dal DB
  (`/api/digestpoints/media/{id}/content`, `/api/members/{id}/photo`,
  `recap`) **non emettono header di cache**, quindi ogni foto / PDF / vocale
  riprodotto viene ri-scaricato per intero a ogni visita di ogni membro. Con
  ~20 persone che aprono l'app più volte al giorno dal telefono, 5 GB si
  bruciano in ~2 settimane. Mitigazioni in `CLAUDE.md` → "Prossimi passi noti"
  punto 5 (la prima: `Cache-Control` + `ETag` sui blob, immutabili perché
  hanno lo `Sha256`).
- **Endpoint media non autenticati**: `/api/digestpoints/media/{id}/content` e
  `/api/members/{id}/photo` non hanno `[TokenAuth]` (servono agli
  `<img>`/`<audio>`). Su un URL pubblico sono enumerabili da chiunque
  conosca il dominio. Follow-up previsto: protezione con token in querystring.
- **Chiave Groq**: senza `GROQ_API_KEY` il deploy funziona; `recap` per un
  giorno non ancora in cache risponde 503. Genera i verbali in locale (restano
  in cache nella tabella `Verbali`) oppure aggiungi la env var su Render.
- **RAM 512 MB** (free): l'API a riposo sta a ~150-200 MB, la generazione PDF
  fa un picco. Se compaiono OOM nei log, è il segnale per passare al piano
  Starter ($7/mese) o alleggerire.
- **Storage Aiven 1 GB → byte dei file su Cloudflare R2** (**attivo dal 24/9/2026**; senza le
  env R2 il codice ripiega su Postgres). Foto, audio, documenti, foto profilo e
  thumbnail WebP vanno su un bucket R2 (10 GB free) invece che in Postgres; a DB resta solo
  la riga di metadati con `Content = NULL`. Senza le env tutto resta com'è (byte in Postgres).
  - **Env** (Importer, Transcriber e API — le stesse quattro ovunque):
    `COMITATOFESTE_R2_ACCOUNT_ID`, `COMITATOFESTE_R2_ACCESS_KEY_ID`,
    `COMITATOFESTE_R2_SECRET_ACCESS_KEY`, `COMITATOFESTE_R2_BUCKET`. Token R2 con permesso
    *Object Read & Write* limitato a quel bucket; bucket **privato** (nessun accesso pubblico:
    i file passano sempre dall'API, che fa da proxy).
  - **Chiavi**: `media/{mediaAssetId}/{sha256}`, `memberphoto/{memberId}/{sha256}`,
    `thumb/{kind}/{sourceId}/{width}/{sha256 sorgente}` — immutabili (lo SHA è nella chiave).
  - **Regola: `Content == NULL` ⇒ il byte è su R2.** Se un oggetto manca, l'endpoint risponde 404
    (le thumbnail invece si rigenerano da sole).
  - **Ordine di rilascio** (seguito il 24/9/2026, tutto completato): 1) applicare a mano la migration `BlobContentNullable` ad Aiven
    (`DROP NOT NULL`, istantanea, il codice vecchio non ne risente); 2) creare il bucket e le
    env su Render e sul PC; 3) deploy; 4) backfill dei dati storici (sotto).
  - **Backfill storico** (`COMITATOFESTE_CONNECTION` = Aiven + le 4 env R2):
    `dotnet run --project Src/backend/ComitatoFeste.Importer -- --blobs-to-r2 --dry-run`
    (solo elenco), poi `--blobs-to-r2` (carica e verifica, **il DB non cambia**), controllare
    a campione dal sito, infine `--blobs-to-r2 --clear-db` (azzera i byte a DB solo per gli
    oggetti verificati su R2). Idempotente e riprendibile.
  - **Spazio su disco Aiven dopo `--clear-db`**: Postgres di norma riusa lo spazio liberato
    senza restituirlo al sistema. Il 24/9 però è sceso quasi subito (DB ~31 MB; `MediaBlobs`
    1,3 MB) perché l'autovacuum di Aiven è passato; `ImageThumbnails` (~14 MB) è rimasta
    indietro. Se una tabella non scende, `VACUUM FULL "<Tabella>"` (blocca la tabella per la
    durata) o `pg_repack` se abilitato sul piano Aiven.
  - **Credenziali sul PC**: `scripts/r2.env` (gitignorato; modello `scripts/r2.env.template`)
    letto da `import-transcribe-aiven.ps1`, che stampa `R2: attivo` in verde o un avviso
    rosso se mancano. Per i comandi lanciati a mano (`--blobs-to-r2`, Embedder ecc.)
    esportare le stesse quattro variabili.
  - **Riconciliazione bucket ↔ DB**: le chiavi attese sono derivabili dal DB (id + SHA), quindi
    orfani (in R2 ma non a DB) e mancanti (a DB ma non in R2) si trovano confrontando
    `ListObjectsV2` con le righe di `MediaBlobs`/`MemberProfilePhotos`/`ImageThumbnails`.
    Fatta il 24/9: 627/627, 0 orfani. Gli orfani nascono da test con DB locali (stessi id,
    contenuti diversi) e dalle foto profilo sostituite.
  - **Backup**: i dump di `backup-db.ps1` contengono solo i metadati; **i byte stanno solo su
    R2** (nessun backup né versioning del bucket, da decidere). Il dump del 24/9 mattina
    (`Backups/cf-2026-09-24.dump`, 83,6 MB) è l'ultimo con i byte anche a DB.
  - **Pipeline**: l'Importer carica su R2 dopo il salvataggio; se l'upload fallisce il byte
    resta a DB (avviso nell'output) e verrà preso dal backfill successivo.
  - **Cancellazione punto** (`DELETE /api/digestpoints/{id}`): rimuove anche gli oggetti R2
    (best effort). Le foto profilo sostituite lasciano il vecchio oggetto orfano (pochi KB).

---

## Sviluppo locale con Docker

Replica la forma della produzione (Postgres + API dallo stesso `Dockerfile`):

```powershell
docker compose up --build      # -> http://localhost:8080/
```

Oppure, con l'API lanciata a parte via `dotnet run`, serve solo Postgres:

```powershell
docker compose -f docker-compose.db.yml up -d   # container "comitatofeste-db", dati in ./data/postgres/
dotnet run --project Src/backend/ComitatoFeste.Api   # (vedi Src/backend/ComitatoFeste.Api/README.md)
```

`docker-compose.db.yml` monta i dati su file system (`./data/postgres/`, gitignorato)
invece di un named volume, così la cartella è ispezionabile e cancellabile a mano;
il `container_name` è `comitatofeste-db`. Dal 21/9/2026 usa l'immagine
`pgvector/pgvector:pg16` (serve all'assistente AI) e **è il DB locale ufficiale**:
il vecchio `local-postgres` esterno (compose `Desktop\Local Env`) va lasciato
fermo, perché occupa la stessa porta 5432.

> ⚠️ **Assistente AI e deploy**: la migration `AddDigestPointEmbeddings`
> richiede l'estensione `vector`. **Aiven la ha già** (pgvector 0.8.6 e migration
> applicati a mano il 21/9/2026 *prima* del deploy: backup, poi `dotnet ef database
> update` con `COMITATOFESTE_CONNECTION` = Aiven; provato che `avnadmin`, pur non
> superuser, può fare `CREATE EXTENSION vector`). Serve `GEMINI_API_KEY` tra le env
> Render (senza: `POST /api/assistant/ask` risponde 503, il resto funziona); il
> backfill degli embedding lo completa da solo il passo Embedder di
> `import-transcribe-aiven.ps1`.
