#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-11 — solo dati di curatela, logica comune in digest_lib.py.

Giornata quasi silenziosa: un solo messaggio, una foto di Costantino Mariani
senza commento (17:50). Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-11"

CURATED = {}
AUDIO_CURATED = {}

MEDIA_OVERRIDES = {
    (DATE, "17:50", "Costantino Mariani", "IMG-20261011-WA0013.jpg"):
        "Foto di una console giocattolo \"Mini Arcade Master\" ancora in "
        "confezione (26 giochi, 99 livelli), condivisa senza commento — "
        "probabile premio per una futura lotteria/estrazione del comitato.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
