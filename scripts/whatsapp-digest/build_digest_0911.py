#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-11 — solo dati di curatela, logica comune in digest_lib.py.

Giornata (parziale, fino alle 10:12) dominata dai saluti mattutini e da un
lungo siparietto scherzoso in dialetto tra Elvis/Luca/Raffaele/Maria su
vecchi ricordi (incidente in bicicletta, mongolfiera, "panda verde") — rumore,
niente di attinente al comitato. Unico punto rilevante: Tina Giarrante
completa la lista di cosa porta per la riunione di stasera (vedi anche il
thread iniziato il 10/9 da Alessandra Toracchio/Barbara Rizio). Nessuna
menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-11"

CURATED = {
    ("08:53", "Tina Giarrante"): ("info",
        "Per la riunione di stasera comunica cosa ha preso: varie patatine, 2 "
        "bottiglie di acqua frizzante, un succo e un tè; il resto lo portano "
        "gli altri. Chiede comunque ad Alessandra Toracchio di mandare la "
        "posizione."),
}

MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
