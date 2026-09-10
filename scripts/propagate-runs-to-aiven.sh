#!/usr/bin/env bash
# Propaga a Aiven gli IngestionRun indicati (default 19 20 21 22) copiando SOLO le
# loro righe da locale -> Aiven, senza rifare Groq/Whisper e senza toccare le
# tabelle solo-cloud (Verbali, PushSubscriptions, DigestPoints.IsImportant).
# Variante bash di docs/DEPLOY.md §4b (copia per-run invece che per-file).
#
# Presupposti (verificati in sessione il 10/9/2026):
#  - il DB locale nasce da un dump di Aiven e da allora SOLO il locale ha
#    importato quei giorni -> gli Id dei nuovi record locali sono > del max di
#    Aiven, nessuna collisione;
#  - i Member/Group referenziati esistono già su Aiven con lo stesso Id.
#
# Uso:  bash scripts/propagate-runs-to-aiven.sh              # runs 19 20 21 22
#       bash scripts/propagate-runs-to-aiven.sh 23 24
set -euo pipefail
export MSYS_NO_PATHCONV=1

IMG="postgres:18-alpine"
LOCAL="postgresql://postgres:postgres@host.docker.internal:5432/postgres"
HERE="$(cd "$(dirname "$0")" && pwd)"
AIVEN="$(tr -d '[:space:]' < "$HERE/aiven.uri")"

RUNS=("$@"); [ ${#RUNS[@]} -eq 0 ] && RUNS=(19 20 21 22)
IN="$(IFS=,; echo "${RUNS[*]}")"
echo "== IngestionRun da propagare: $IN =="

lpsql() { docker run --rm "$IMG" psql "$LOCAL" -v ON_ERROR_STOP=1 "$@"; }
apsql() { docker run --rm -i "$IMG" psql "$AIVEN" -v ON_ERROR_STOP=1 "$@"; }
apsql_ro() { docker run --rm "$IMG" psql "$AIVEN" -v ON_ERROR_STOP=1 "$@"; }

# --- guard: i Member referenziati esistono su Aiven? ---
USED="$(lpsql -At -c "select string_agg(distinct \"MemberId\"::text,',') from \"DigestPoints\" where \"IngestionRunId\" in ($IN)")"
echo "MemberId referenziati: $USED"
MISSING="$(apsql_ro -At -c "select coalesce(string_agg(x::text,','),'') from unnest(ARRAY[$USED]) x where x not in (select \"Id\" from \"Members\")")"
[ -n "$MISSING" ] && { echo "STOP: Member mancanti su Aiven: $MISSING"; exit 1; }
echo "guard OK: tutti i Member presenti su Aiven"

# --- copia in ordine di FK (pipe = OS pipe di bash, byte-accurato) ---
copy() {
  local tbl="$1" q="$2"
  echo ">>> $tbl"
  lpsql -c "\copy ($q) TO STDOUT" | apsql -c "\copy \"$tbl\" FROM STDIN"
}
copy IngestionRuns 'SELECT * FROM "IngestionRuns" WHERE "Id" IN ('"$IN"')'
copy DigestPoints  'SELECT * FROM "DigestPoints" WHERE "IngestionRunId" IN ('"$IN"')'
copy MediaAssets   'SELECT ma.* FROM "MediaAssets" ma JOIN "DigestPoints" dp ON dp."Id"=ma."DigestPointId" WHERE dp."IngestionRunId" IN ('"$IN"')'
copy MediaBlobs    'SELECT mb.* FROM "MediaBlobs" mb JOIN "MediaAssets" ma ON ma."Id"=mb."MediaAssetId" JOIN "DigestPoints" dp ON dp."Id"=ma."DigestPointId" WHERE dp."IngestionRunId" IN ('"$IN"')'

# --- riallinea le sequenze identity di Aiven ---
echo ">>> setval sequenze"
apsql_ro -c "
SELECT setval(pg_get_serial_sequence('\"IngestionRuns\"','Id'), (SELECT max(\"Id\") FROM \"IngestionRuns\"));
SELECT setval(pg_get_serial_sequence('\"DigestPoints\"','Id'),  (SELECT max(\"Id\") FROM \"DigestPoints\"));
SELECT setval(pg_get_serial_sequence('\"MediaAssets\"','Id'),   (SELECT max(\"Id\") FROM \"MediaAssets\"));
SELECT setval(pg_get_serial_sequence('\"MediaBlobs\"','Id'),    (SELECT max(\"Id\") FROM \"MediaBlobs\"));
"

# --- verifica ---
echo; echo "== Aiven dopo la copia =="
apsql_ro -At -c "select 'IR='||count(*) from \"IngestionRuns\"" \
  -c "select 'DP='||count(*) from \"DigestPoints\"" \
  -c "select 'MA='||count(*) from \"MediaAssets\"" \
  -c "select 'MB='||count(*) from \"MediaBlobs\"" \
  -c "select 'Verbali='||count(*) from \"Verbali\"" \
  -c "select 'Push='||count(*) from \"PushSubscriptions\""
apsql_ro -At -F' = ' -c "select \"OccurredAt\"::date, count(*) from \"DigestPoints\" where \"OccurredAt\">='2026-09-08' group by 1 order by 1"
apsql_ro -At -c "select '10/9 audio senza trascrizione = '||count(*) from \"MediaAssets\" ma join \"DigestPoints\" dp on dp.\"Id\"=ma.\"DigestPointId\" where dp.\"OccurredAt\"::date='2026-09-10' and ma.\"MediaType\"='audio' and ma.\"TranscribedAt\" is null"
echo "OK."
