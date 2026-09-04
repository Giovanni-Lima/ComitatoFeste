# Deploy — Render + Aiven

Portale pubblico a costo zero. Un solo servizio applicativo su **Render**
(container Docker: API .NET + frontend statico sulla stessa origine), database
**PostgreSQL gestito su Aiven**. La pipeline `Importer`/`Transcriber` resta in
locale e scrive sul DB Aiven via `COMITATOFESTE_CONNECTION`.

```
                 ┌─────────────────────────────┐
   browser  ───▶ │ Render Web Service (Docker)  │
                 │  ComitatoFeste.Api           │ ──▶  Aiven PostgreSQL (managed)
                 │  + wwwroot/index.html        │
                 └─────────────────────────────┘
                          ▲
   PC locale: Importer / Transcriber ──┘  (COMITATOFESTE_CONNECTION = Aiven)
```

File in gioco: `Dockerfile`, `.dockerignore`, `render.yaml`, `docker-compose.yml`
(solo per lo sviluppo locale).

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
   | `COMITATOFESTE_AUTH_SECRET` | **32+ caratteri casuali, fissi** (senza, ogni redeploy invalida tutti i login) |
   | `GROQ_API_KEY` | *opzionale* — solo per generare verbali di giorni non ancora in cache |
   | `PORT` | `8080` (già nel blueprint) |

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

dotnet run --project Src/backend/ComitatoFeste.Importer      # digest_*.json + foto profilo
dotnet run --project Src/backend/ComitatoFeste.Transcriber   # vocali -> testo + classificazione
```

Il portale online riflette subito i nuovi dati (nessun redeploy).

> ⚠️ Vale sempre la regola dell'`Importer`: **dopo** che il Transcriber ha
> girato non rilanciare l'import completo (riscrive `DigestPoint.Text` e
> reinserisce duplicati). Per le sole foto: `-- --photos-only`.

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
  18, il container `local-postgres` è alla 16 e non può esportare da un
  server più recente);
- scrive `Backups/cf-YYYY-MM-DD.dump` (gitignorato) e ruota a 30 giorni.

Schedulazione giornaliera (una volta, in PowerShell):

```powershell
$a = New-ScheduledTaskAction -Execute "powershell.exe" `
     -Argument '-NoProfile -File "C:\ComitatoFeste\scripts\backup-db.ps1"'
$t = New-ScheduledTaskTrigger -Daily -At 2am
Register-ScheduledTask -TaskName "ComitatoFeste-DB-Backup" -Action $a -Trigger $t
```

Restore:

```powershell
docker run --rm -v "C:\ComitatoFeste\Backups:/backups" postgres:18-alpine `
  pg_restore --no-owner --clean --if-exists -d "<uri>" /backups/cf-YYYY-MM-DD.dump
```

Upgrade opzionale (offsite, gira anche a PC spento): workflow GitHub Actions
schedulato → `pg_dump` → Cloudflare R2 (10 GB free) con lifecycle a 30 giorni.

---

## Limiti e cose da sapere

- **Cold start**: il piano free di Render spegne il container dopo ~15 min di
  inattività; la richiesta successiva attende ~40-60 s. Per tenerlo caldo
  gratis: un ping schedulato (es. <https://cron-job.org>) su
  `/api/auth/status` ogni 10 min — quell'endpoint **non** tocca il DB, quindi
  non consuma risorse Aiven. Sta nelle 750 h/mese del free.
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
- **Storage Aiven 1 GB**: oggi il DB è ~46 MB. Quando i blob (PDF/video)
  stringono, spostali su object storage gratuito (Cloudflare R2, 10 GB) —
  `MediaBlob` è già una tabella 1:1 separata, la modifica è contenuta.

---

## Sviluppo locale con Docker

Replica la forma della produzione (Postgres + API dallo stesso `Dockerfile`):

```powershell
docker compose up --build      # -> http://localhost:8080/
```

Oppure, senza container per l'API: tieni `local-postgres` e lancia
`dotnet run --project Src/backend/ComitatoFeste.Api` (vedi
`Src/frontend/README.md`).
