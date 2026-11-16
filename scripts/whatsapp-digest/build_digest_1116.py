#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-16 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 12:45-20:27 (export Dropbox delle 20:28, giornata ancora in corso;
nessun messaggio prima delle 12:45). Il giorno dopo i conti di San Martino:
Emilio vuole comprare le castagne avanzate (5-6 kg), Sabatini si propone di
dividerle e Alessandro Di Benedetto ne vuole una parte. Sei vocali organizzano
lo smontaggio dei braceri/fuoconi (trattore e muletto, disponibilità dalle
14:30-15:30) e il conferimento dei rifiuti alla sede (carta, indifferenziata,
lattine e vetro). Emanuele condivide un link Facebook. Serena posta il
"problema inventato" di sua figlia (540 gite meno 170 annullate) e ne nasce
una serie di battute (rumore, foto scartata). In serata gli auguri di
compleanno a Gilda Di Iulio, a cui partecipa anche Giovanni Lima (suo
messaggio, nessuna menzione da parte di altri).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-16"

CURATED = {
    ("15:58", "Emanuele Sciarra"): ("info",
        "Condivide un post Facebook: "
        "https://www.facebook.com/share/p/1E2YAxDU8d/?mibextid=wwXIfr"),
    ("20:21", "Barbara Rizio"): ("info",
        "Oggi è il compleanno di Gilda Di Iulio, il gruppo si scambia "
        "auguri in chat."),
}

TEXT_MERGES = [
    {
        "anchor_time": "12:45", "anchor_sender": "Emilio Caniglia",
        "type": "domanda",
        "text": (
            "Emilio vuole acquistare la rimanenza delle castagne (5-6 kg) "
            "e chiede se qualcun altro è interessato. Antonio Sabatini ci "
            "pensava anche lui e chiede se si può dividere; Alessandro Di "
            "Benedetto è interessato a una parte; Dante conferma che sono "
            "buonissime."
        ),
        "members": [["12:45", "Emilio Caniglia"], ["12:45", "Antonio Sabatini"],
                    ["12:52", "Alessandro Di Benedetto"],
                    ["12:52", "Dante Caniglia"]],
    },
]

AUDIO_MERGES = [
    {
        "anchor_time": "12:58", "anchor_sender": "Maikel Montano",
        "type": "info",
        "text": (
            "Organizzazione di oggi pomeriggio. Maikel chiede come "
            "organizzarsi per andare a prendere il fuocone (è molto "
            "incasinato). Elvis ricorda che stasera alla sede va portata "
            "fuori la carta, e anche le bottiglie di vetro e le lattine, "
            "ormai fra due venerdì. Ugo è disponibile nel pomeriggio a "
            "togliere i braceri: se viene qualcuno con la chiave porta "
            "fuori la carta, l'indifferenziata se la porta a casa e la "
            "butta domani sera, lattine e vetro si aspettano il giorno "
            "giusto. Sabatini (a testo) ci sta dal primo pomeriggio, anche "
            "alle 15:30. Cesare chiede a Maikel a che ora è disponibile "
            "col trattore per organizzarsi con il muletto (meglio presto, "
            "per lui ideali le 14:30-15); Maikel non può a quell'ora ma "
            "alle 15:30 sì; Cesare gli chiede di fargli uno squillo, anche "
            "perché potrebbe piovere."
        ),
        "members": [
            "PTT-20261116-WA0003.opus", "PTT-20261116-WA0004.opus",
            "PTT-20261116-WA0006.opus", "PTT-20261116-WA0007.opus",
            "PTT-20261116-WA0008.opus", "PTT-20261116-WA0009.opus",
        ],
    },
]

MEDIA_OVERRIDES = {}

# IMG-20261116-WA0011.jpg (14:41 Serena): pagina di quaderno con un "problema
# inventato" della figlia (il comitato feste 1987 organizza 540 gite, 170
# annullate, ne rimangono 370): battuta, fuori tema, scartata.
_SKIP_FILES = {"IMG-20261116-WA0011.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_merges=AUDIO_MERGES,
                 text_merges=TEXT_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="foto di battuta fuori tema")
