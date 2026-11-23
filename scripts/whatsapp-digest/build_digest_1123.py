#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-23 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:14-08:20 (export Dropbox delle 08:57, giornata appena iniziata).
Costantino preferisce il calendario al porta-foto (più commerciale, lo
comprerebbero anche i nonni), propone una "pesca" per la Befana legata alla
lunghezza della sua scopa, e chiede come gestire le prenotazioni per
Capodanno. Emanuele chiarisce che il porta-foto era solo un'opzione
aggiuntiva al calendario, non sostitutiva, e chiede se decidere subito sul
gruppo i numeri di telefono per le prenotazioni di Capodanno o aspettare la
riunione. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-23"

CURATED = {
    ("08:16", "Costantino Mariani"): ("info",
        "Trova carina l'idea del porta-foto, ma pensa che il "
        "calendario sia la scelta migliore: più \"commerciale\", lo "
        "comprerebbero in quantità maggiori anche i nonni."),
    ("08:17", "Costantino Mariani"): ("proposta",
        "Dopo aver fatto stamattina \"la rotonda\", propone una "
        "\"pesca\" per la Befana legata alla lunghezza della scopa "
        "della Befana."),
    ("08:18", "Costantino Mariani"): ("domanda",
        "Chiede come iniziare a gestire i nominativi per le "
        "prenotazioni di Capodanno."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "08:18",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Emanuele chiarisce che l'idea del porta-foto con la "
            "pinzetta era solo un'aggiunta: il calendario resta in "
            "ogni caso, e si potrebbe vendere il calendario a 10€ e il "
            "porta-foto a 5€, per dare un'opzione in più. Sul tema "
            "Capodanno, ricorda che si era detto di attivare almeno "
            "due o tre numeri per raccogliere le prenotazioni "
            "(passando poi tramite Chiara per la locandina), e chiede "
            "se decidere la cosa direttamente sul gruppo o aspettare "
            "la riunione."
        ),
        "members": ["PTT-20261123-WA0000.opus", "PTT-20261123-WA0001.opus"],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, {}, audio_merges=AUDIO_MERGES)
