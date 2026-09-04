# Backup giornaliero del DB Aiven -> Backups\cf-YYYY-MM-DD.dump (formato custom pg_dump),
# rotazione a 30 giorni. Zero segreti nel file: l'URI di connessione Aiven sta in
# scripts\aiven.uri (gitignorato), una riga sola:
#
#   postgres://avnadmin:PASSWORD@pg-....aivencloud.com:11068/defaultdb?sslmode=require
#
# Aiven gira Postgres 18; usa un client postgres:18 usa-e-getta via Docker (il container
# 'local-postgres' e' fermo alla 16 e non puo' esportare da un server piu' recente).
#
# Registrazione come task giornaliero (una volta, in PowerShell):
#   $a = New-ScheduledTaskAction -Execute "powershell.exe" `
#        -Argument '-NoProfile -File "C:\ComitatoFeste\scripts\backup-db.ps1"'
#   $t = New-ScheduledTaskTrigger -Daily -At 2am
#   Register-ScheduledTask -TaskName "ComitatoFeste-DB-Backup" -Action $a -Trigger $t
#
# Restore di un dump (in un DB Postgres >= 18):
#   docker run --rm -v "C:\ComitatoFeste\Backups:/backups" postgres:18-alpine `
#     pg_restore --no-owner --clean --if-exists -d "<uri>" /backups/cf-YYYY-MM-DD.dump

$ErrorActionPreference = "Stop"

$pgImage = "postgres:18-alpine"

$uriFile = Join-Path $PSScriptRoot "aiven.uri"
if (-not (Test-Path $uriFile)) { throw "Manca $uriFile (URI di connessione Aiven, una riga)." }
$uri = (Get-Content $uriFile -Raw).Trim()
if (-not $uri) { throw "$uriFile e' vuoto." }

$dir = Join-Path $PSScriptRoot "..\Backups"
New-Item -ItemType Directory -Force -Path $dir | Out-Null
$dir = (Resolve-Path $dir).Path
$name = "cf-{0}.dump" -f (Get-Date -Format "yyyy-MM-dd")

docker run --rm -v "${dir}:/backups" $pgImage `
    pg_dump --no-owner --no-privileges --no-comments -Fc -d $uri -f "/backups/$name"

$out = Join-Path $dir $name
if (-not (Test-Path $out) -or (Get-Item $out).Length -eq 0) { throw "Dump non creato o vuoto: $out" }

# Rotazione: elimina i dump piu' vecchi di 30 giorni.
Get-ChildItem $dir -Filter "cf-*.dump" |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-30) } |
    Remove-Item -Force

Write-Host ("OK  {0}  ({1:N1} MB)" -f $out, ((Get-Item $out).Length / 1MB))
