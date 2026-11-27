#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-26 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:10-23:54 (giornata completa). In risposta allo scambio di
ieri sera sulla locandina, Alessandra condivide (foto) l'unica locandina
del Comitato 1986 che è riuscita a trovare, come riferimento. In serata
Vincenzo gira il listino di un fornitore di dolciumi per le calze della
Befana; Emanuele aggiorna su un preventivo per i tagliandini della
Tombolata (Lutech, 120€/1000 pezzi) e sulla ricerca di un'alternativa;
risponde infine (vocale) ad Antonio sull'esito dell'incontro con lo
sparatore per i fuochi d'artificio. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-26"

CURATED = {
    ("08:16", "Alessandra Toracchio"): ("info",
        "In risposta alla discussione di ieri sera sulla locandina, "
        "condivide (foto) l'unica locandina del Comitato 1986 che è "
        "riuscita a trovare, come riferimento."),
    ("21:31", "Vincenzo Lacasasanta"): ("info",
        "Gira (PDF) il listino di un fornitore di dolciumi per le "
        "calze della Befana, precisando che i prezzi dovrebbero "
        "essere scontati di circa l'8% (0,24€ in meno), ma lo sconto "
        "viene applicato dopo, non calcolabile direttamente sul "
        "listino. Alessandra Polce chiede se i prezzi del listino "
        "sono già comprensivi di IVA: Vincenzo conferma di sì."),
    ("22:26", "Emanuele Sciarra"): ("info",
        "Comunica un preventivo di Lutech per i tagliandini della "
        "Tombolata (120€ per 1000 pezzi); tramite il marito di Maria "
        "si sta valutando anche un'altra tipografia."),
}

AUDIO_CURATED = {
    (DATE, "23:54", "Emanuele Sciarra", "PTT-20261126-WA0007.opus"): ("info",
        "Risponde (vocale) ad Antonio Aceto, che chiedeva come fosse "
        "andato l'incontro con lo sparatore per il preventivo dei "
        "fuochi d'artificio: erano presenti lui, Vincenzo e Ugo, "
        "insieme ad Amiconi; i preventivi li hanno Antonio e Vincenzo, "
        "e se ne discuterà direttamente alla riunione di venerdì."),
}

MEDIA_OVERRIDES = {
    (DATE, "08:16", "Alessandra Toracchio", "IMG-20261126-WA0001.jpg"):
        "Locandina del Comitato 1986 per l'evento \"Arriva la Befana\" "
        "(6 gennaio, ore 15:30, palestra della Scuola Elementare di Via "
        "Fucino), condivisa come esempio di una locandina precedente.",
    (DATE, "21:31", "Vincenzo Lacasasanta", "dolfood.pdf"):
        "Listino prezzi di un fornitore di dolciumi/snack monoporzione "
        "(crostatine, caramelle, barrette, patatine, lecca-lecca), con "
        "un esempio di combinazione da 3,03€ a confezione.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
