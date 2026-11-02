#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-01 — solo dati di curatela, logica comune in digest_lib.py.

Giorno di Halloween/Ognissanti: Cesare condivide le foto dello stand
allestito con i dolci donati dalla Dolciaria Cerasani (vedi 30/10),
distribuiti gratis ai bambini in costume. Il gruppo reagisce con
entusiasmo. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-01"

CURATED = {}
AUDIO_CURATED = {}

MEDIA_OVERRIDES = {
    (DATE, "17:40", "Cesare Raglione", "IMG-20261101-WA0006.jpg"):
        "Un membro del comitato posa davanti allo stand allestito a "
        "tema Halloween, con i dolci della Dolciaria Cerasani e il "
        "cartello \"Dolci offerti dalla Dolciaria Cerasani e dalla "
        "Classe 1987\".",
    (DATE, "17:57", "Cesare Raglione", "IMG-20261101-WA0008.jpg"):
        "Bambini in costume ricevono i dolci allo stand del comitato, "
        "tra zucche decorate e addobbi di Halloween.",
    (DATE, "17:57", "Cesare Raglione", "IMG-20261101-WA0007.jpg"):
        "Altra foto dello stand con i dolci e i volantini \"Dolci "
        "offerti dalla Dolciaria Cerasani e dalla Classe 1987\", tra "
        "bambini in costume.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
