#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-02 — solo dati di curatela, logica comune in digest_lib.py.

Mattina: Antonio Sabatini condivide il rendiconto di cassa di ottobre.
Pomeriggio: Emilio posta la sintesi della riunione di venerdì 30/10
(pullman Corinaldo pieno, si valuta un furgone da 9 posti o un secondo
pullman da 750€; confronto su San Martino e altri eventi; incontro con
Andrea Di Loreto per il Capodanno; prossima riunione venerdì 6/11 su San
Martino); Cesare riporta in sede i dolci Halloween avanzati. In serata
brutta notizia: l'arnese per cuocere le castagne preso in prestito non è
più disponibile (proprietà privata, il proprietario l'ha ripreso) — ma
Emanuele rassicura che quello che il comitato sta costruendo è quasi
pronto. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-02"

CURATED = {
    ("15:00", "Emilio Caniglia"): ("decisione",
        "Posta la sintesi della riunione di venerdì 30 ottobre: per il "
        "pellegrinaggio a Corinaldo un pullman è già pieno, si valuta "
        "un furgone da 9 posti per il comitato per massimizzare "
        "l'entrata, vista la spesa elevata (750€) per un secondo "
        "pullman da 19 posti. Confronto sull'evento di San Martino e su "
        "altri eventi di interesse. Incontro con Andrea Di Loreto per "
        "organizzare il Capodanno: servirà valutare le disponibilità "
        "dei membri del comitato. Prossima riunione venerdì 6 novembre, "
        "dedicata a San Martino."),
    ("21:30", "Barbara Rizio"): ("info",
        "Brutta notizia: l'arnese per cuocere le castagne, che pensava "
        "fosse della Pro Loco/comunale, è in realtà di proprietà "
        "privata e il proprietario l'ha ripreso, decidendo di non "
        "prestarlo più a nessuno."),
    ("21:31", "Emanuele Sciarra"): ("info",
        "Rassicura il gruppo: quello che stanno costruendo loro è quasi "
        "ultimato."),
}

AUDIO_CURATED = {}

MEDIA_OVERRIDES = {
    (DATE, "08:14", "Antonio Sabatini", "Comitato feste 1987-Ottobre.pdf"):
        "Rendiconto di cassa di ottobre: saldo al 30/9 di 1.100€, "
        "entrate nel mese per 980€ (480€ di quote di preadesione, 24 "
        "persone a 20€; 500€ dall'evento promozionale del 16/10), "
        "nessuna uscita registrata — saldo finale 2.080€.",
    (DATE, "17:28", "Cesare Raglione", "IMG-20261102-WA0005.jpg"):
        "Scatole di dolci Halloween della Dolciaria Cerasani avanzati: "
        "Cesare li riporta in sede venerdì.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
