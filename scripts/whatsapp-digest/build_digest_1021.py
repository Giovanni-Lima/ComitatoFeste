#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-21 — solo dati di curatela, logica comune in digest_lib.py.

Export senza media (zip Dropbox di oggi conteneva solo il .txt, confermato
con l'utente: si procede comunque col solo testo). Due soli messaggi:
Emanuele posta un sondaggio sulla disponibilità per il San Martino di
sabato 14 (novembre), e un messaggio media_omitted (non recuperabile in
ogni caso, nessuna entry). Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-21"

CURATED = {
    ("16:58", "Emanuele Sciarra"): ("proposta",
        "Apre un sondaggio sulla disponibilità per il San Martino di "
        "sabato 14 (novembre). Al momento dell'export: Sì 11 voti, No 4 "
        "voti."),
}

AUDIO_CURATED = {}
MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
