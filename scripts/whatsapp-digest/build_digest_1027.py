#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-27 — solo dati di curatela, logica comune in digest_lib.py.

Giornata quasi silenziosa per il comitato: molte battute sul compleanno
(imminente) di Ugo Trinchini, in realtà il 28/10 — puro rumore. L'unico
punto utile: Emanuele chiede a che punto sono le prenotazioni per
Corinaldo, con due conteggi diversi riportati. Resto rumore/personale
(link e battute su una foto di classe del 1987, fuori tema). Nessuna
menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-27"

CURATED = {
    ("15:57", "Emanuele Sciarra"): ("domanda",
        "Chiede a che punto sono le prenotazioni per la gita a "
        "Corinaldo."),
}

AUDIO_CURATED = {
    (DATE, "10:24", "Antonio Aceto", "PTT-20261027-WA0028.opus"): ("rumore", ""),
    (DATE, "10:24", "Luca Cicchelli", "PTT-20261027-WA0029.opus"): ("rumore", ""),
    (DATE, "11:44", "Cesare Raglione", "PTT-20261027-WA0030.opus"): ("rumore", ""),
    (DATE, "17:15", "Serena Di Stefano", "PTT-20261027-WA0033.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {}

TEXT_MERGES = [
    {
        "anchor_time": "16:39",
        "anchor_sender": "Alessandro Di Benedetto",
        "type": "info",
        "text": (
            "Alessandro Di Benedetto risponde di averne segnate 8; poco "
            "dopo Antonio Sabatini ne comunica 17 (probabilmente un "
            "conteggio diverso, es. un secondo pullman)."
        ),
        "members": [
            ["16:39", "Alessandro Di Benedetto"], ["16:48", "Antonio Sabatini"],
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES)
