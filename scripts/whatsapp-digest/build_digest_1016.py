#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-16 — solo dati di curatela, logica comune in digest_lib.py.

Mattina, giorno dell'incontro sponsorizzato materassi: Ugo completa la
ventesima coppia (Amanda con Mike). Valentina chiede cosa portare e a che
ora; Antonio Sabatini riepiloga il buffet (dolce di Ilenia, salati di
Barbara, crostata sua, eventuali pasticcini) e conferma l'appuntamento
entro le 21 alla sala consiliare; Valentina si offre per le bibite, Luca
segnala che Claudia sta preparando delle pizzette. Nessuna menzione di
Giovanni Lima da parte di altri in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-16"

CURATED = {
    ("07:38", "Ugo Trinchini"): ("info",
        "Per l'incontro di stasera, comunica di poter aggiungere Amanda "
        "in coppia con Mike."),
}

AUDIO_CURATED = {}
MEDIA_OVERRIDES = {}

TEXT_MERGES = [
    {
        "anchor_time": "08:13",
        "anchor_sender": "Valentina D'Arcadia",
        "type": "domanda",
        "text": (
            "Valentina chiede cosa portare per il buffet di stasera e a "
            "che ora è l'appuntamento. Antonio Sabatini riepiloga: un "
            "dolce da Ilenia, salati da Barbara, una crostata sua ed "
            "eventuali pasticcini; appuntamento entro le 21 alla sala "
            "consiliare. Valentina si offre di portare delle bibite; "
            "Luca segnala che Claudia sta preparando delle pizzette al "
            "sugo."
        ),
        "members": [
            ["08:13", "Valentina D'Arcadia"], ["08:14", "Valentina D'Arcadia"],
            ["08:37", "Antonio Sabatini"], ["08:52", "Valentina D'Arcadia"],
            ["08:54", "Luca Cicchelli"],
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES)
