#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-30 — solo dati di curatela, logica comune in digest_lib.py.

Giorno della riunione su Corinaldo (sede, ore 21): Emilio ricorda
l'appuntamento e riferisce risultati sopra le attese, un pullman già sold
out e pochi posti rimasti per un secondo pullman più piccolo. Ugo
condivide le foto dei dolci a tema Halloween donati dalla Dolciaria
Cerasani, proponendo di distribuirli gratis ai bambini a San Martino (poi
realizzato, vedi build_digest_1101.py). A fine riunione Costantino chiede
premi per la tombolata (risposte il giorno dopo, vedi
build_digest_1031.py). Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-30"

CURATED = {
    ("08:26", "Emilio Caniglia"): ("info",
        "Ricorda la riunione di questa sera (ore 21, in sede), dedicata "
        "principalmente alla visita a Corinaldo ma anche ai prossimi "
        "eventi. Riferisce risultati sopra le attese: un pullman è già "
        "sold out e restano pochissimi posti per un secondo pullman più "
        "piccolo."),
    ("22:49", "Costantino Mariani"): ("domanda",
        "A riunione conclusa, chiede premi per la tombolata: risposte "
        "nei giorni successivi."),
}

AUDIO_CURATED = {
    (DATE, "15:34", "Ugo Trinchini", "PTT-20261030-WA0013.opus"): ("proposta",
        "Comunica che la Dolciaria Cerasani ha donato al comitato dolci "
        "a tema Halloween (vedi foto): propone di distribuirli "
        "gratuitamente ai bambini all'evento di San Martino. Porterà "
        "tutto alla riunione di stasera."),
}

MEDIA_OVERRIDES = {
    (DATE, "15:34", "Ugo Trinchini", "IMG-20261030-WA0017.jpg"):
        "Scatola di biscotti a forma di zucca di Halloween, decorati, "
        "donati dalla Dolciaria Cerasani.",
    (DATE, "15:34", "Ugo Trinchini", "IMG-20261030-WA0016.jpg"):
        "Diverse scatole di dolci a tema Halloween della Dolciaria "
        "Cerasani (zucche farcite, teschi al cacao) pronte per essere "
        "distribuite.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
