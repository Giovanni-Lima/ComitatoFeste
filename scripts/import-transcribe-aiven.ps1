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

param(
    [string]$ImporterArgs = "",
    [string]$TranscriberArgs = ""
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

Write-Host "== Import verso Aiven ==" -ForegroundColor Cyan
# --export-root esplicito: il default hardcoded nel Program.cs dell'Importer
# (C:\ComitatoFeste\Export) e' il vecchio percorso pre-trasloco, non esiste piu'.
$exportRoot = Join-Path $repoRoot "Export"
$importerExtra = $ImporterArgs.Split(" ", [StringSplitOptions]::RemoveEmptyEntries)
# Catturato riga per riga (oltre che stampato dal vivo) per leggere
# "punti-inseriti-totale:N" e decidere se forzare la notifica push sotto (vedi
# commento più giù).
$importerOutput = @()
dotnet run --project (Join-Path $repoRoot "Src/backend/ComitatoFeste.Importer") -- --export-root $exportRoot @importerExtra | ForEach-Object {
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
if ($totalInserted -gt 0) {
    $checkpointPath = Join-Path $PSScriptRoot "whatsapp-digest/checkpoint.json"
    if (Test-Path $checkpointPath) {
        $checkpointDate = (Get-Content $checkpointPath -Raw | ConvertFrom-Json).digest_data
        if ($checkpointDate) { $transcriberExtra += @("--force-notify", $checkpointDate) }
    }
}
dotnet run --project (Join-Path $repoRoot "Src/backend/ComitatoFeste.Transcriber") -- @transcriberExtra
if ($LASTEXITCODE -ne 0) { throw "Transcriber terminato con errore (exit $LASTEXITCODE)." }

# Chiusura giorni passati (vedi CLAUDE.md, regola 12/9/2026): a questo punto Aiven ha
# appena ricevuto import+trascrizione, quindi qualunque giorno precedente a quello
# corrente e' sicuro da rimuovere da Export/ (l'Importer non potra' piu' "resuscitare"
# un punto cancellato dall'app per quei giorni). Non fatale: un fallimento qui non deve
# far sembrare fallito l'aggiornamento Aiven appena riuscito.
Write-Host "`n== Chiusura giorni passati ==" -ForegroundColor Cyan
python (Join-Path $PSScriptRoot "whatsapp-digest/close_past_days.py")
if ($LASTEXITCODE -ne 0) { Write-Host "close_past_days.py non riuscito (exit $LASTEXITCODE) - non bloccante." -ForegroundColor Yellow }

Write-Host "`nOK." -ForegroundColor Green
