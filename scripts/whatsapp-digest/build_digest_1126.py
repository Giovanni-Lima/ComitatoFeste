#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-26 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:10-08:16 (export Dropbox delle 15:47, giornata ancora in
corso). In risposta allo scambio di ieri sera sulla locandina, Alessandra
condivide (foto) l'unica locandina del Comitato 1986 che è riuscita a
trovare, come riferimento. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-26"

CURATED = {
    ("08:16", "Alessandra Toracchio"): ("info",
        "In risposta alla discussione di ieri sera sulla locandina, "
        "condivide (foto) l'unica locandina del Comitato 1986 che è "
        "riuscita a trovare, come riferimento."),
}

MEDIA_OVERRIDES = {
    (DATE, "08:16", "Alessandra Toracchio", "IMG-20261126-WA0001.jpg"):
        "Locandina del Comitato 1986 per l'evento \"Arriva la Befana\" "
        "(6 gennaio, ore 15:30, palestra della Scuola Elementare di Via "
        "Fucino), condivisa come esempio di una locandina precedente.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
