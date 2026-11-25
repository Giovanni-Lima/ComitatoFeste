#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-25 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:42-16:05 (export Dropbox delle 16:38, giornata ancora in
corso). La coda di auguri per la nascita di Carlo (figlio di Barbara
Rizio) prosegue nelle prime ore del mattino: resta rumore individuale, il
punto riepilogativo è già nel digest del 24/11. Emilio gira l'invito di
Don Enzo per la Novena dell'Immacolata (turni di Rosario in parrocchia,
con il Comitato coinvolto in due giornate) e ricorda gli appuntamenti di
oggi (fuochi d'artificio e, in serata, Capodanno con Andrea Di Loreto) e
la riunione di venerdì 27. Emanuele condivide il post Facebook con le
prevendite delle calze della Befana aperte al pubblico. Nessuna menzione
di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-25"

CURATED = {
    ("07:42", "Emilio Caniglia"): ("info",
        "Gira l'invito di Don Enzo (vedi foto): locandina della "
        "Novena dell'Immacolata in parrocchia (San Benedetto Abate), "
        "con il calendario di chi anima il Rosario (ore 16:15) e la "
        "Messa (ore 17:00) giorno per giorno. Don Enzo chiede a chi "
        "parteciperà di venire con un proprio segno distintivo. Il "
        "Comitato risulta tra i turni elencati (verosimilmente "
        "domenica 6 dicembre, sotto la voce \"Comitato 2027\")."),
    ("07:51", "Emilio Caniglia"): ("info",
        "Appuntamenti di oggi: nel tardo pomeriggio incontro in sede "
        "per spari e fuochi d'artificio (da confermare in giornata); "
        "in serata, alle 21 a Gianvito (Bar Ragno), incontro con "
        "Andrea Di Loreto per Capodanno. Ricorda inoltre che venerdì "
        "27 novembre ci sarà, come di consueto, la riunione."),
    ("15:23", "Emanuele Sciarra"): ("info",
        "Condivide il link del post Facebook con cui si sono aperte "
        "ufficialmente le prevendite delle calze della Befana: "
        "https://www.facebook.com/share/p/18yGqnuJEy/?mibextid=wwXIfr "
        "(Emilio lo apprezza: \"Locandina 🔝\")."),
    ("16:05", "Emilio Caniglia"): ("info",
        "Ripromemoria degli appuntamenti del giorno: ore 18 in sede "
        "con Amiconi per spari e fuochi d'artificio; ore 21 a "
        "Gianvito (Bar Ragno) con Andrea Di Loreto per Capodanno."),
}

MEDIA_OVERRIDES = {
    (DATE, "07:42", "Emilio Caniglia", "IMG-20261125-WA0000.jpg"):
        "Locandina della Novena dell'Immacolata, parrocchia San "
        "Benedetto Abate: Messa ogni giorno alle 17:00, Rosario alle "
        "16:15, con il calendario dei gruppi che animano il Rosario "
        "dal 29 novembre al 7 dicembre (tra cui \"Comitato 2026\" il "
        "29/11 e \"Comitato 2027\" il 6/12).",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
