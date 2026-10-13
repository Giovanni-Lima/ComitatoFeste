#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-13 — solo dati di curatela, logica comune in digest_lib.py.

Giornata breve. Dopo mezzanotte (00:08-00:11) Barbara condivide un video e
riferisce di essere stata alla sagra di Canistro, dove ha preso un
cartoccio di castagne come riferimento di prezzo/quantità per la
castagnata di San Martino. Nel pomeriggio Emilio pubblica una terza
tabella aggiornata delle coppie per il 16 ottobre (con le nuove adesioni
di Cristina e Giampiero, segnalate ieri sera); Maikel ed Emanuele
segnalano probabile assenza a quell'incontro per impegni di lavoro.
Chiude Emilio con un aggiornamento pratico sul pullman per Corinaldo: per
i bambini non ci sono obblighi di seggiolino. Nessuna menzione di Giovanni
Lima da parte di altri in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-13"

CURATED = {
    ("00:11", "Barbara Rizio"): ("info",
        "Riferisce di essere stata alla sagra di Canistro, dove ha preso "
        "un cartoccio di castagne (almeno 200g) a 4€, come riferimento di "
        "prezzo e quantità per la castagnata del comitato."),
    ("14:42", "Maikel Montano"): ("info",
        "Comunica che venerdì 16 non potrà essere presente."),
    ("15:20", "Emanuele Sciarra"): ("info",
        "Segnala che è all'80% assente dall'incontro del 16, perché gli "
        "hanno assegnato il turno pomeridiano; avrà conferma il giorno "
        "dopo."),
    ("15:51", "Emilio Caniglia"): ("info",
        "Ha contattato l'azienda del pullman per la visita a Corinaldo: "
        "per i bambini non ci sono obblighi particolari, possono "
        "viaggiare anche senza seggiolino."),
}

AUDIO_CURATED = {}

MEDIA_OVERRIDES = {
    (DATE, "00:08", "Barbara Rizio", "VID-20261013-WA0000.mp4"):
        "Video legato al messaggio successivo: il cartoccio di castagne "
        "comprato da Barbara alla sagra di Canistro.",
    (DATE, "13:55", "Emilio Caniglia", "IMG-20261013-WA0004.jpg"):
        "Tabella \"Coppie\" per il 16 ottobre, terza versione (14 coppie su "
        "20 posti): rispetto alla precedente si aggiungono Giampiero "
        "(segnalato da Alessandra S.) con Cristina, e Donato (segnalato "
        "da Antonio S.) con Santina.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
