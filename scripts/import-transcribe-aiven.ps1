# Lancia Importer + Transcriber puntati al DB Aiven (import + trascrizione "in
# produzione", vedi CLAUDE.md/docs/DEPLOY.md sezione 4), con le notifiche push
# verso Render abilitate. Zero segreti nel file, letti da due file locali
# gitignorati (una riga ciascuno):
#
#   scripts\aiven.uri     già in uso da backup-db.ps1
#                          postgres://avnadmin:PASSWORD@pg-....aivencloud.com:11068/defaultdb?sslmode=require
#   scripts\hook.secret    lo stesso valore di COMITATOFESTE_HOOK_SECRET impostato su Render
#
# GROQ_API_KEY per il Transcriber: risolto automaticamente da key.txt in radice
# repo (GroqKey.Resolve), non serve impostarlo qui.
#
# Uso:  powershell -File scripts\import-transcribe-aiven.ps1
#       (o --photos-only / altri argomenti dell'Importer: aggiungerli come
#       parametri extra, es. -ImporterArgs "--photos-only")
#
# SICUREZZA (regola aggiunta il 15/9/2026, dopo un incidente reale): l'Importer,
# senza un target esplicito, importa TUTTI i digest_*.json in Export/ — se
# close_past_days.py non e' mai arrivato a girare (es. run precedente fallito a
# meta'), quella cartella puo' contenere ancora giorni vecchi non chiusi. Lanciato
# cosi' contro Aiven ha inserito su Aiven 153 punti storici (06-10/9) non
# richiesti insieme ai punti del giorno corrente, poi rimossi a mano. Per questo
# questo script NON lascia mai l'Importer senza target: di default lo limita
# SEMPRE al solo giorno corrente (checkpoint.json -> digest_data). Usa -Target
# per un giorno diverso (backfill volontario, da usare consapevolmente).

param(
    [string]$Target = "",
    [string]$ImporterArgs = "",
    [string]$TranscriberArgs = "",
    [string]$EmbedderArgs = "",
    [switch]$SkipEmbedder
)

$ErrorActionPreference = "Stop"
$env:DOTNET_ROLL_FORWARD = "Major"   # su questo PC manca il runtime .NET 8 puro, vedi CLAUDE.md

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")

# --- COMITATOFESTE_CONNECTION da scripts\aiven.uri (formato libpq postgres://) ---
# convertito nel formato a keyword che si aspetta Npgsql/COMITATOFESTE_CONNECTION.
$uriFile = Join-Path $PSScriptRoot "aiven.uri"
if (-not (Test-Path $uriFile)) { throw "Manca $uriFile (URI Aiven, una riga: postgres://user:pass@host:port/db?sslmode=require)." }
$rawUri = (Get-Content $uriFile -Raw).Trim()
if (-not $rawUri) { throw "$uriFile e' vuoto." }
$u = [Uri]$rawUri
$userInfo = $u.UserInfo -split ':', 2
$env:COMITATOFESTE_CONNECTION = "Host=$($u.Host);Port=$($u.Port);Database=$($u.AbsolutePath.TrimStart('/'));Username=$($userInfo[0]);Password=$($userInfo[1]);SSL Mode=Require;Trust Server Certificate=true"

# --- COMITATOFESTE_HOOK_SECRET da scripts\hook.secret ---
$hookFile = Join-Path $PSScriptRoot "hook.secret"
if (-not (Test-Path $hookFile)) { throw "Manca $hookFile (lo stesso COMITATOFESTE_HOOK_SECRET impostato su Render, una riga)." }
$hookSecret = (Get-Content $hookFile -Raw).Trim()
if (-not $hookSecret) { throw "$hookFile e' vuoto." }
$env:COMITATOFESTE_HOOK_SECRET = $hookSecret
$env:COMITATOFESTE_HOOK_URL = "https://comitatofeste.onrender.com"

# --- Target dell'import: SEMPRE esplicito, mai "tutta Export/" di default ---
# (vedi commento SICUREZZA in testa al file). Default: il giorno del checkpoint
# della curatela WhatsApp corrente; -Target sovrascrive per un giorno diverso.
$checkpointPath = Join-Path $PSScriptRoot "whatsapp-digest/checkpoint.json"
$checkpointDate = $null
if (Test-Path $checkpointPath) {
    $checkpointDate = (Get-Content $checkpointPath -Raw | ConvertFrom-Json).digest_data
}
$importTarget = if ($Target) { $Target } else { $checkpointDate }
$photosOnly = $ImporterArgs -match '--photos-only'
if (-not $importTarget -and -not $photosOnly) {
    throw "Impossibile determinare il giorno da importare: manca $checkpointPath (o il suo campo digest_data) e non hai passato -Target. Passa -Target <yyyy-MM-dd> esplicitamente."
}

Write-Host "== Import verso Aiven (target: $(if ($photosOnly) { '--photos-only, nessun digest' } else { $importTarget })) ==" -ForegroundColor Cyan
# --export-root esplicito: il default hardcoded nel Program.cs dell'Importer
# (C:\ComitatoFeste\Export) e' il vecchio percorso pre-trasloco, non esiste piu'.
$exportRoot = Join-Path $repoRoot "Export"
$importerExtra = $ImporterArgs.Split(" ", [StringSplitOptions]::RemoveEmptyEntries)
# BUG (trovato il 16/9/2026): "$importerPositional = if (...) { @($importTarget) }
# else { @() }" sembra costruire un array, ma PowerShell "spacchetta" un
# array a un solo elemento quando attraversa il flusso di output implicito
# di un blocco if/else usato come espressione — l'assegnazione riceve la
# stringa scalare "2026-09-16", non un array che la contiene. Lo splat
# @importerPositional su una stringa scalare la itera CARATTERE PER
# CARATTERE, passando "2" come primo argomento posizionale all'Importer
# (che quindi cerca digest_2.json e fallisce). Fix: assegnare direttamente
# dentro ciascun branch, non tramite return implicito raccolto dall'esterno
# — così l'array-ness si preserva anche con un solo elemento.
if ($importTarget) {
    $importerPositional = @($importTarget)
} else {
    $importerPositional = @()
}
# Catturato riga per riga (oltre che stampato dal vivo) per leggere
# "punti-inseriti-totale:N" e decidere se forzare la notifica push sotto (vedi
# commento più giù).
$importerOutput = @()
dotnet run --project (Join-Path $repoRoot "Src/backend/ComitatoFeste.Importer") -- @importerPositional --export-root $exportRoot @importerExtra | ForEach-Object {
    Write-Host $_
    $importerOutput += $_
}
if ($LASTEXITCODE -ne 0) { throw "Importer terminato con errore (exit $LASTEXITCODE)." }

$totalInserted = 0
foreach ($line in $importerOutput) {
    if ($line -match 'punti-inseriti-totale:(\d+)') { $totalInserted = [int]$Matches[1] }
}

Write-Host "`n== Trascrizione verso Aiven ==" -ForegroundColor Cyan
$transcriberExtra = $TranscriberArgs.Split(" ", [StringSplitOptions]::RemoveEmptyEntries)
# Trascrizione anticipata dei vocali (vedi CLAUDE.md): se la curatela ha già
# classificato tutti i vocali della giornata, il Transcriber qui sotto non ha
# nulla da fare e non noterebbe da solo che l'Importer ha appena inserito punti
# nuovi — niente notifica push altrimenti. --force-notify usa la data corrente
# del checkpoint (digest_data), il giorno su cui si sta lavorando in questo giro.
if ($totalInserted -gt 0 -and $checkpointDate) {
    $transcriberExtra += @("--force-notify", $checkpointDate)
}
dotnet run --project (Join-Path $repoRoot "Src/backend/ComitatoFeste.Transcriber") -- @transcriberExtra
if ($LASTEXITCODE -ne 0) { throw "Transcriber terminato con errore (exit $LASTEXITCODE)." }

# Embedding per l'assistente AI (Aesir, vedi CLAUDE.md "Assistente AI"): dopo il Transcriber, perche'
# quest'ultimo riscrive il testo dei vocali. L'Embedder e' incrementale (embedda solo i punti nuovi o
# cambiati), quindi qui recupera anche cio' che un run precedente non aveva fatto in tempo. NON e'
# bloccante: se la quota gratuita di Gemini e' finita (exit 10) o c'e' un errore, si va avanti e i
# punti mancanti vengono ripresi al prossimo run. Ritmo ridotto (batch da 40, 30 s tra un batch e
# l'altro = ~80 richieste/min) e 2 soli tentativi per richiesta: con la quota finita si rinuncia in
# pochi secondi invece di attendere i backoff da batch. -SkipEmbedder lo salta.
if (-not $SkipEmbedder) {
    Write-Host "`n== Embedding (assistente AI) verso Aiven ==" -ForegroundColor Cyan
    $embedderExtra = $EmbedderArgs.Split(" ", [StringSplitOptions]::RemoveEmptyEntries)
    dotnet run --project (Join-Path $repoRoot "Src/backend/ComitatoFeste.Embedder") -- --batch-size 40 --delay-ms 30000 --max-attempts 2 @embedderExtra
    switch ($LASTEXITCODE) {
        0  { }
        10 { Write-Host "Embedding parziale: quota Gemini esaurita - i punti mancanti verranno ripresi al prossimo run." -ForegroundColor Yellow }
        default { Write-Host "Embedder non riuscito (exit $LASTEXITCODE) - non bloccante, i punti mancanti verranno ripresi al prossimo run." -ForegroundColor Yellow }
    }
}

# Chiusura giorni passati (vedi CLAUDE.md, regola 12/9/2026): a questo punto Aiven ha
# appena ricevuto import+trascrizione, quindi qualunque giorno precedente a quello
# corrente e' sicuro da rimuovere da Export/ (l'Importer non potra' piu' "resuscitare"
# un punto cancellato dall'app per quei giorni). Non fatale: un fallimento qui non deve
# far sembrare fallito l'aggiornamento Aiven appena riuscito.
Write-Host "`n== Chiusura giorni passati ==" -ForegroundColor Cyan
python (Join-Path $PSScriptRoot "whatsapp-digest/close_past_days.py")
if ($LASTEXITCODE -ne 0) { Write-Host "close_past_days.py non riuscito (exit $LASTEXITCODE) - non bloccante." -ForegroundColor Yellow }

Write-Host "`nOK." -ForegroundColor Green
