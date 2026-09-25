#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-25 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 06:07-08:24 (nessun vocale). Mattina quasi solo di saluti (rumore).
Unico punto: Emilio Caniglia (07:13) ricorda l'invito di Don Enzo per la
Messa di domenica 27/9 alle 11:30, in cui la parrocchia accoglierà il corpo
di San Camillo de Lellis, evento che coinvolge tutte le associazioni del
territorio. La locandina rimandata alle 07:14 è lo stesso file
(IMG-20260917-WA0001.jpg) già digest il 17/9 alle 08:05: scartata come
duplicato. Nessuna menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-25"

CURATED = {
    ("07:13", "Emilio Caniglia"): ("info",
        "Ricorda l'invito di Don Enzo per la Messa di domenica 27/9 alle "
        "11:30: la parrocchia accoglierà il corpo di San Camillo de "
        "Lellis, patrono dei malati e degli operatori sanitari, in un "
        "evento eccezionale che coinvolgerà tutte le associazioni del "
        "territorio e tutta la comunità."),
}

MEDIA_OVERRIDES = {}

# IMG-20260917-WA0001.jpg (07:14): stessa identica locandina delle reliquie
# di San Camillo già digest il 17/9 alle 08:05, rimandata da Emilio — scartata
# come duplicato per non ripetere lo stesso contenuto in due giorni.
_SKIP_FILES = {"IMG-20260917-WA0001.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, extra_skip_media=_extra_skip,
                 extra_skip_label="forward duplicato locandina")
