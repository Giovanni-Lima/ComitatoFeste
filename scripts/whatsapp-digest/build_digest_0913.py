#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-13 — solo dati di curatela, logica comune in digest_lib.py.

Giornata parziale (fino alle 16:13 all'atto di questo export), quasi
interamente dominata dagli auguri di compleanno a **Tina Giarrante**
(lei stessa lo annuncia alle 07:38, poi decine di messaggi "auguri" da
tutto il gruppo fino a mezzogiorno) — prima applicazione della regola
"Compleanni" (CLAUDE.md, 13/9/2026): un solo punto sintetico invece di
lasciare tutto rumore.

Resto della giornata: Chiara Gargano torna dopo 4 giorni di assenza dalla
chat e Maria Buttari le fa notare che "c'è l'app che riassume tutto"
(12:26-12:45) — rumore/meta, ma **menzione di Giovanni Lima** (regola
11/9/2026): Maria Buttari scrive "Monumento a Giovanni @Giovanni Lima"
(14:24), verosimilmente collegato proprio a questo scambio sull'app —
segnalato nel recap finale, non genera entry. Giovanni Lima condivide un
video (14:43, VID-20260913-WA0012.mp4) verificato via grep sui box MP4:
solo 'vide'/'avc1', **nessuna** traccia audio ('soun'/'mp4a' assenti) — è
una GIF di reazione travestita da video, scartata come tale. Chiude la
finestra un link Facebook di Emanuele Sciarra con battuta in dialetto per
Costantino Mariani (16:12-16:13) — banter, non contenuto attinente al
comitato, rumore.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-13"

CURATED = {
    ("07:38", "Tina Giarrante"): ("info",
        "Oggi è il compleanno di Tina Giarrante: il gruppo si scambia "
        "auguri in chat per tutta la mattina."),
}

MEDIA_OVERRIDES = {}

# VID-20260913-WA0012.mp4: nessuna traccia audio (ispezionati i box MP4 —
# 'vide'/'avc1' presenti, 'soun'/'mp4a' assenti, ffprobe non disponibile in
# questa sessione). GIF di reazione travestita da video, va scartata.
_REACTION_GIF_MP4 = {
    "VID-20260913-WA0012.mp4",
}


def _skip_reaction_gif_mp4(time_, fname):
    return fname in _REACTION_GIF_MP4


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES,
                 extra_skip_media=_skip_reaction_gif_mp4,
                 extra_skip_label="GIF di reazione .mp4 senza audio, escluse")
