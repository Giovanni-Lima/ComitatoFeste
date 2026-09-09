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
dotnet run --project (Join-Path $repoRoot "Src/backend/ComitatoFeste.Importer") -- $ImporterArgs.Split(" ", [StringSplitOptions]::RemoveEmptyEntries)
if ($LASTEXITCODE -ne 0) { throw "Importer terminato con errore (exit $LASTEXITCODE)." }

Write-Host "`n== Trascrizione verso Aiven ==" -ForegroundColor Cyan
dotnet run --project (Join-Path $repoRoot "Src/backend/ComitatoFeste.Transcriber") -- $TranscriberArgs.Split(" ", [StringSplitOptions]::RemoveEmptyEntries)
if ($LASTEXITCODE -ne 0) { throw "Transcriber terminato con errore (exit $LASTEXITCODE)." }

Write-Host "`nOK." -ForegroundColor Green
