#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-23 — solo dati di curatela, logica comune in digest_lib.py.

Giorno della riunione mensile (sede, ore 21): i soli messaggi del giorno
sono logistica sulle presenze (chi viene/non viene), puro rumore. Il
contenuto vero della riunione arriva il giorno dopo con il recap di Emilio
Caniglia (vedi build_digest_1024.py, 12:24). Nessuna menzione di Giovanni
Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-23"

CURATED = {}
AUDIO_CURATED = {}
MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
