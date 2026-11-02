#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-02 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:14 (export Dropbox delle 08:57 di oggi): Antonio Sabatini
condivide il rendiconto di cassa di ottobre. Nessuna menzione di Giovanni
Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-02"

CURATED = {}
AUDIO_CURATED = {}

MEDIA_OVERRIDES = {
    (DATE, "08:14", "Antonio Sabatini", "Comitato feste 1987-Ottobre.pdf"):
        "Rendiconto di cassa di ottobre: saldo al 30/9 di 1.100€, "
        "entrate nel mese per 980€ (480€ di quote di preadesione, 24 "
        "persone a 20€; 500€ dall'evento promozionale del 16/10), "
        "nessuna uscita registrata — saldo finale 2.080€.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
