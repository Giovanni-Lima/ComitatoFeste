#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-18 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 15:02-19:07 (export Dropbox delle 23:32; nessun messaggio prima
delle 15:02). Emanuele cerca altri contatti per gli sparatori (ne ha uno di
Celano, che propone di incontrarsi la settimana prossima) perché servono
preventivi; Ugo e Elvis rimandano a contatti di Emilio. Emanuele condivide due
proposte di cappellino col logo 1987 fatte da Giacomo Gentile e chiede pareri;
Tina nota che richiamano lo "striscione". Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-18"

CURATED = {}

TEXT_MERGES = [
    {
        "anchor_time": "15:02", "anchor_sender": "Emanuele Sciarra",
        "type": "domanda",
        "text": (
            "Emanuele chiede se ci sono altri contatti per gli sparatori, "
            "oltre a quello che ha lui di Celano: servono preventivi. Ugo "
            "suggerisce di contattarlo intanto per un preventivo; Elvis "
            "ricorda che Emilio aveva dei contatti. Emanuele ha già "
            "sentito quello di Celano, che propone di incontrarsi la "
            "settimana prossima perché al momento è incasinato; se ci sono "
            "altri contatti si possono sentire per confrontare i costi."
        ),
        "members": [["15:02", "Emanuele Sciarra"], ["15:58", "Ugo Trinchini"],
                    ["15:59", "Elvis Ippoliti"], ["15:59", "Emanuele Sciarra"],
                    ["16:00", "Emanuele Sciarra"]],
    },
    {
        "anchor_time": "18:21", "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Emanuele condivide due proposte di cappellino col logo 1987 "
            "fatte da Giacomo Gentile e chiede cosa ne pensano. Tina "
            "osserva che richiamano lo \"striscione\" e Emanuele conferma."
        ),
        "members": [["18:21", "Emanuele Sciarra"], ["18:22", "Emanuele Sciarra"],
                    ["19:07", "Tina Giarrante"], ["19:07", "Emanuele Sciarra"]],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "18:21", "Emanuele Sciarra", "IMG-20261118-WA0004.jpg"):
        "Prima proposta di Giacomo Gentile: cappellino di lana nero con "
        "toppa tonda \"CLASSE 1987\", le cifre a pixel-art con scene di "
        "videogiochi d'epoca (Pac-Man, Super Mario, Street Fighter, Space "
        "Invaders).",
    (DATE, "18:21", "Emanuele Sciarra", "IMG-20261118-WA0005.jpg"):
        "Seconda proposta di Giacomo Gentile: cappellino di lana nero con "
        "toppa rettangolare con \"1987\" a grandi cifre composte da scene "
        "di videogiochi d'epoca.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, text_merges=TEXT_MERGES)
