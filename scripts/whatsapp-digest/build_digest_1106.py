#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-06 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 16:23-22:36 (export Dropbox delle 9:01 del 9/11). Giornata leggera:
Emilio ricorda la riunione serale (ore 21, dedicata principalmente a San
Martino) e segnala un posto libero nel pullman di domenica per Corinaldo.
Costantino avvisa che salta la riunione per un raffreddore. Il resto sono
logistica/arrivi, scartati come rumore. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-06"

CURATED = {
    ("18:47", "Emilio Caniglia"): ("info",
        "Ricorda la riunione di questa sera (ore 21 in sede), dedicata "
        "principalmente all'organizzazione di San Martino. Comunica "
        "inoltre che si è liberato un posto nel pullman di domenica per "
        "Corinaldo, disponibile a chi volesse aggiungersi last minute."),
}

MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
