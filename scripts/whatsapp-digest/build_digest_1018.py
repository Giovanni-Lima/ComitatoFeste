#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-18 — solo dati di curatela, logica comune in digest_lib.py.

Giornata silenziosa: un solo messaggio, "Grandi!!!" di Costantino Mariani
(11:40, probabile reazione a quanto discusso il 17/10) — puro rumore,
nessuna entry. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-18"

CURATED = {}
AUDIO_CURATED = {}
MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
