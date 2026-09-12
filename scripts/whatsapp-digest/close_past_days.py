#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ripulisce Export/ dei giorni ormai "chiusi", per evitare il bug della
"resurrezione": l'Importer fa dedup media confrontando col DB attuale (vedi
DigestImporter.cs, set `existingMedia`), non con uno storico di "già visto
in passato". Se un punto viene cancellato dall'app (DELETE /api/digestpoints/{id})
ma la sua entry è ancora nel digest_<data>.json sorgente, il prossimo giro di
Importer non trova più quel file tra i "già esistenti" e lo re-inserisce.

Regola (decisa con l'utente l'12/9/2026): un giorno è "chiuso" — quindi il
suo digest_<data>.json e la sua cartella Export/<data>/ (media rinominati)
sono cancellabili — quando la sua data è STRETTAMENTE MINORE di
`digest_data` nel checkpoint (il giorno su cui si sta correntemente
curando/esportando). Nessuna verifica incrociata su Aiven: si assume che
l'import+trascrizione del giorno precedente sia già avvenuto prima di
passare al giorno successivo (workflow seguito finora in ogni sessione).

Rischio residuo accettato: se per qualche motivo l'import di un giorno
"chiuso" non fosse mai andato a buon fine, cancellarlo qui non perde nulla
per davvero — build_digest_<MMGG>.py resta per sempre in git (è la
"ricetta") e il .txt esportato da WhatsApp è sempre cumulativo dall'inizio,
quindi il giorno si può sempre rigenerare da un nuovo export.

Uso:  python close_past_days.py            (esegue davvero)
      python close_past_days.py --dry-run  (mostra solo cosa cancellerebbe)
"""
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EXPORT = os.path.join(HERE, "..", "..", "Export")
CHECKPOINT = os.path.join(HERE, "checkpoint.json")

DIGEST_RE = re.compile(r"^digest_(\d{4}-\d{2}-\d{2})\.json$")


def main():
    dry_run = "--dry-run" in sys.argv

    if not os.path.isfile(CHECKPOINT):
        print(f"Checkpoint non trovato: {CHECKPOINT}")
        return 1
    with open(CHECKPOINT, encoding="utf-8") as f:
        checkpoint = json.load(f)
    cutoff = checkpoint.get("digest_data")
    if not cutoff:
        print("Checkpoint senza 'digest_data': non so quale sia il giorno corrente, non cancello nulla.")
        return 1

    if not os.path.isdir(EXPORT):
        print(f"Export/ non trovata: {EXPORT}")
        return 1

    to_close = []
    for name in sorted(os.listdir(EXPORT)):
        m = DIGEST_RE.match(name)
        if m and m.group(1) < cutoff:
            to_close.append(m.group(1))

    if not to_close:
        print(f"Nessun giorno da chiudere (cutoff: giorni < {cutoff}).")
        return 0

    print(f"Giorno corrente (checkpoint digest_data): {cutoff}")
    print(f"Giorni da chiudere: {', '.join(to_close)}" + (" (dry-run, nessuna modifica)" if dry_run else ""))

    for date in to_close:
        paths = [
            os.path.join(EXPORT, f"digest_{date}.json"),
            os.path.join(EXPORT, date),
            os.path.join(EXPORT, f"_rimossi_{date}"),
        ]
        for path in paths:
            if not os.path.exists(path):
                continue
            kind = "file" if os.path.isfile(path) else "cartella"
            print(f"  {'[dry-run] ' if dry_run else ''}rimuovo {kind}: {os.path.relpath(path, EXPORT)}")
            if not dry_run:
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)

    print("OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
