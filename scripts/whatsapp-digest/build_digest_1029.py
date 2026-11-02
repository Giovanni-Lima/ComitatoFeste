#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-29 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 00:28-21:15 (aggiornata con l'export Dropbox delle 08:57 del
2/11). Mattina/pomeriggio: coda degli auguri per il 10° anniversario di
sacerdozio di Don Emidio Cerasani, iniziati il 28/10 — puro rumore. Unico
punto utile: Alessandra Toracchio chiede se portare le castagne che ha
per domani sera (riunione del 30/10) e come cuocerle. Nessuna menzione di
Giovanni Lima da parte di altri (lui stesso aveva scritto solo per fare
gli auguri, già alle 00:28).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-29"

CURATED = {
    ("20:14", "Alessandra Toracchio"): ("domanda",
        "Ha un po' di castagne: chiede se portarle alla riunione di "
        "domani sera e come cuocerle."),
}

AUDIO_CURATED = {}
MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
