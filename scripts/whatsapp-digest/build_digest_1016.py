#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-16 — solo dati di curatela, logica comune in digest_lib.py.

Mattina, giorno dell'incontro sponsorizzato materassi: Ugo completa la
ventesima coppia (Amanda con Mike). Valentina chiede cosa portare e a che
ora; Antonio Sabatini riepiloga il buffet (dolce di Ilenia, salati di
Barbara, crostata sua, eventuali pasticcini) e conferma l'appuntamento
entro le 21 alla sala consiliare; Valentina si offre per le bibite, Luca
segnala che Claudia sta preparando delle pizzette.

Pomeriggio/sera (16:56-21:03, aggiornata con l'export delle 9:32 del 18/10):
Emilio Caniglia posta l'elenco definitivo delle coppie (20, foto) e ricorda
il ritrovo alle 20:45, incontro sponsorizzato alle 21. Tina Giarrante (18:04)
comunica che stasera non può venire ma al suo posto viene Giusy (di Sakis);
Alessandra Simonetti (18:47) comunica che al posto di Cristina e Giampiero
vengono Antonietta e Gigi; Ugo Trinchini (20:12) comunica che al posto di
Annesa rientra Tina. Due video senza audio (Emanuele 20:20, Elvis 20:23) sono
GIF di reazione, scartate in automatico. Resto rumore (battute, risate,
conferme di ritardo). Nessuna menzione di Giovanni Lima in questa finestra.
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
    ("16:58", "Emilio Caniglia"): ("info",
        "Ricorda l'appuntamento di questa sera, alle 20:45, presso la sala "
        "consiliare del Comune: l'incontro sponsorizzato comincerà alle "
        "21."),
    ("18:04", "Tina Giarrante"): ("info",
        "Comunica che stasera non può venire, ma al suo posto viene Giusy "
        "(di Sakis)."),
    ("18:47", "Alessandra Simonetti"): ("info",
        "Comunica che al posto di Cristina e Giampiero vengono Antonietta "
        "e Gigi."),
    ("20:12", "Ugo Trinchini"): ("info",
        "Comunica che al posto di Annesa rientra Tina."),
}

AUDIO_CURATED = {}
MEDIA_OVERRIDES = {
    (DATE, "16:56", "Emilio Caniglia", "IMG-20261016-WA0026.jpg"):
        "Foglio \"COPPIE\" definitivo per l'incontro del 16 ottobre, 20 "
        "righe complete.",
}

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

# ffprobe non è installato su questa macchina: is_reaction_gif() non riesce a
# verificarlo da sola (eccezione silenziosa -> non esclude). Verificato a mano
# cercando l'handler audio ("soun"/"mp4a") nei box del container mp4: assente
# in entrambi (solo "vide"), quindi sono GIF di reazione mute, non video veri.
_SKIP_FILES = {"VID-20261016-WA0047.mp4", "VID-20261016-WA0048.mp4"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="gif di reazione mp4 (verificata a mano, niente ffprobe)")
