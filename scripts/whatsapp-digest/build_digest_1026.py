#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-26 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:04-08:15 (export Dropbox delle 09:09 di oggi). Il gruppo
raccoglie nominativi di animatori per bambini in vista del Capodanno
(contatti condivisi come vCard, non riportati nel digest per privacy — solo
i nomi); Emanuele aggiorna anche sui contatti delle associazioni dei paesi
vicini per la sponsorizzazione materassi (vedi 19/10). Nessuna menzione di
Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-26"

CURATED = {
    ("08:15", "Emanuele Sciarra"): ("info",
        "Aggiorna sui contatti delle associazioni dei paesi vicini "
        "(vedi 19/10): in settimana gli daranno i nominativi da "
        "presentare all'azienda di materassi; se va bene, stima un "
        "guadagno di 700-800€ per il comitato."),
}

AUDIO_CURATED = {}

MEDIA_OVERRIDES = {}

TEXT_MERGES = [
    {
        "anchor_time": "08:04",
        "anchor_sender": "Costantino Mariani",
        "type": "proposta",
        "text": (
            "Il gruppo raccoglie nominativi di animatori per bambini in "
            "vista del Capodanno (contatti condivisi come vCard, non "
            "riportati qui per privacy): Costantino segnala Marta "
            "(sentito dire che è brava); Ilenia propone Antonella, "
            "definendola bravissima ed economica, da contattare subito "
            "perché molto richiesta; Serena propone anche \"Magicabula\" "
            "e il nominativo di Anita D'Elia. Emanuele conferma di "
            "conoscere bene Marta (faceva hip hop a sua figlia, la trova "
            "molto brava) ma suggerisce di contattarle tutte per "
            "confrontare disponibilità e proposta economica."
        ),
        "members": [
            ["08:04", "Costantino Mariani"], ["08:09", "Ilenia Piccozzi"],
            ["08:10", "Serena Di Stefano"], ["08:11", "Emanuele Sciarra"],
        ],
    },
]

_SKIP_FILES = {
    # vCard di contatti (animatori bambini): nome riportato nel testo del
    # digest, numero di telefono volutamente non incluso (privacy).
    "Marta Animazione.vcf", "Antonella Animazione Bambini.vcf",
    "Anita D Elia.vcf",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="vCard contatto, info riportata nel testo")
