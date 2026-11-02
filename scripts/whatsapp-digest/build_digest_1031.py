#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-31 — solo dati di curatela, logica comune in digest_lib.py.

Seguito alla richiesta di premi per la tombolata (vedi 30/10, 22:49):
Alessandra Polce (ben ritrovata nel gruppo dopo un periodo di assenza) si
offre di preparare un cesto di prodotti alimentari, chiedendo indicazioni
su contenuto/entità; Emanuele spiega come si strutturano solitamente i
premi della tombolata per fascia (ambo/terna/quaterna/cinquina), con un
esempio di cesti da 10€. Alessandra chiede anche quando sarà la
tombolata: probabilmente tra Natale e Capodanno. Nessuna menzione di
Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-31"

CURATED = {
    ("09:48", "Alessandra Polce"): ("domanda",
        "Chiede quando sarà la tombolata."),
    ("09:52", "Emanuele Sciarra"): ("info",
        "Risponde: molto probabilmente tra Natale e Capodanno."),
}

AUDIO_CURATED = {
    (DATE, "09:22", "Alessandra Polce", "PTT-20261031-WA0001.opus"): ("proposta",
        "Si offre di preparare un cesto di prodotti alimentari come "
        "premio per la tombolata (salumi, formaggi, legumi, "
        "eventualmente frutta secca): chiede indicazioni su quale "
        "combinazione e di che entità."),
    (DATE, "09:37", "Emanuele Sciarra", "PTT-20261031-WA0002.opus"): ("info",
        "Spiega come si strutturano di solito i premi della tombolata, "
        "per fascia di vincita (ambo, terna, quaterna, cinquina) in "
        "base al valore: fa l'esempio di 5 cesti da 10€ l'uno, da "
        "assegnare alle fasce in base al valore complessivo."),
}

MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
