#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-28 — solo dati di curatela, logica comune in digest_lib.py.

Compleanno di Ugo Trinchini (lunga sequenza di auguri, anche da Giovanni
Lima) ed Emilio gira l'invito di Don Enzo per le messe di Tutti i Santi e
Commemorazione dei defunti. Costantino chiede se la riunione è stasera:
Elvis conferma che è venerdì. In serata è anche il 10° anniversario di
sacerdozio di Don Emidio Cerasani, con un'altra lunga sequenza di auguri
(continuata nella notte/mattina del 29/10). Nessuna menzione di Giovanni
Lima da parte di altri (lui stesso scrive solo per fare gli auguri).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-28"

CURATED = {
    ("05:24", "Dante Caniglia"): ("info",
        "Oggi è il compleanno di Ugo Trinchini: il gruppo si scambia una "
        "lunga sequenza di auguri in chat, compreso un messaggio di "
        "Giovanni Lima."),
    ("19:39", "Costantino Mariani"): ("domanda",
        "Chiede se stasera c'è la riunione."),
    ("19:49", "Elvis Ippoliti"): ("info",
        "Risponde a Costantino: la riunione è venerdì, non stasera."),
    ("21:09", "Emilio Caniglia"): ("info",
        "Oggi è il 10° anniversario di sacerdozio di Don Emidio Cerasani: "
        "il gruppo si scambia un'altra lunga sequenza di auguri, "
        "proseguita nella notte e nella mattina del 29/10."),
}

AUDIO_CURATED = {
    (DATE, "21:13", "Costantino Mariani", "PTT-20261028-WA0003.opus"): ("rumore", ""),
    (DATE, "21:14", "Elvis Ippoliti", "PTT-20261028-WA0004.opus"): ("rumore", ""),
    (DATE, "21:14", "Costantino Mariani", "PTT-20261028-WA0005.opus"): ("rumore", ""),
    (DATE, "21:14", "Costantino Mariani", "PTT-20261028-WA0006.opus"): ("rumore", ""),
    (DATE, "21:15", "Elvis Ippoliti", "PTT-20261028-WA0007.opus"): ("rumore", ""),
    (DATE, "21:26", "Costantino Mariani", "PTT-20261028-WA0008.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {
    (DATE, "15:32", "Emilio Caniglia", "IMG-20261028-WA0002.jpg"):
        "Emilio gira l'invito di Don Enzo: locandina con gli orari delle "
        "messe per la Solennità di Tutti i Santi (1 novembre, ore 10 a "
        "San Cipriano, 11:30 in Chiesa grande, 15 al Cimitero in caso di "
        "maltempo) e per la Commemorazione dei defunti (2 novembre, ore "
        "17 in Chiesa grande).",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
