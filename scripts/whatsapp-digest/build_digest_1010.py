#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-10 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:56-08:41: è il compleanno di Dante Caniglia, il gruppo si
scambia auguri in chat (nessun contenuto organizzativo). Un solo punto di
sintesi all'orario del primo messaggio, come da regola compleanni. Tra chi
fa gli auguri c'è anche Giovanni Lima (08:28): è lui stesso a scrivere, non
una menzione da parte di altri, quindi non richiede segnalazione a parte.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-10"

CURATED = {
    ("07:56", "Luca Cicchelli"): ("info",
        "Oggi è il compleanno di Dante Caniglia, il gruppo si scambia "
        "auguri in chat."),
}

AUDIO_CURATED = {}
MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
