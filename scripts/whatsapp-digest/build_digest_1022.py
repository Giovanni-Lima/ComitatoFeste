#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-22 — solo dati di curatela, logica comune in digest_lib.py.

Giornata quasi silenziosa: Emanuele chiede l'orario della riunione di
domani (venerdì 23, già fissata alle 21 il 20/10), Emilio confirma.
Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-22"

CURATED = {
    ("19:01", "Emanuele Sciarra"): ("domanda",
        "Chiede a che ora ci si vede domani (venerdì 23, giorno della "
        "riunione)."),
    ("21:06", "Emilio Caniglia"): ("info",
        "Risponde confermando l'orario già fissato: alle 21."),
}

AUDIO_CURATED = {}
MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
