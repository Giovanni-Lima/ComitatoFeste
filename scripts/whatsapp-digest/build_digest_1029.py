#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-29 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 00:28-10:45 (export Dropbox delle 11:41 di oggi): solo la coda
degli auguri per il 10° anniversario di sacerdozio di Don Emidio Cerasani,
iniziati il 28/10 (vedi build_digest_1028.py) — puro rumore, nessuna
nuova entry. Nessuna menzione di Giovanni Lima da parte di altri (lui
stesso scrive solo per fare gli auguri, già alle 00:28).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-29"

CURATED = {}
AUDIO_CURATED = {}
MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
