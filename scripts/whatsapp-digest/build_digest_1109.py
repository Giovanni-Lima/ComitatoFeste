#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-09 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:41-14:13 (export Dropbox delle 9:01, giornata ancora in corso
al momento dell'export). Emanuele, dopo la gita di ieri, si attiva per
cercare altre animatrici da proporre a Gianvito per Capodanno, e gira la
locandina di "Christmas World" a Villa Borghese (Roma) come possibile
nuova meta di gita, chiedendo il parere del gruppo. Ilenia mette a
disposizione dei faretti e delle aste del comitato, utili per
l'illuminazione di San Martino. Antonio Sabatini comunica l'incasso di
880€ dalla gita di Corinaldo. Ugo è in contatto con Paolo degli "Uncini
d'Abruzzo", disponibili a venire in sede in serata per un preventivo.
Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-09"

CURATED = {
    ("07:41", "Emanuele Sciarra"): ("proposta",
        "Dopo la bella giornata di ieri, comunica che proverà a sentire "
        "Marta Malatesti per vedere se conosce altre animatrici, in modo "
        "da avere più preventivi da presentare a Gianvito per Capodanno. "
        "Gira poi la locandina di \"Christmas World\", il villaggio di "
        "Natale a Villa Borghese (Roma, dal 28 novembre al 10 gennaio), "
        "come possibile nuova meta di gita; chiede il parere del gruppo "
        "e, se d'accordo, si informerà sul prezzo d'ingresso."),
    ("10:17", "Ilenia Piccozzi"): ("proposta",
        "Comunica di avere 3 faretti (già usati da Pietro per suonare) "
        "e delle aste di supporto, chiedendo se possano servire per "
        "l'illuminazione di San Martino. Barbara ed Elvis confermano "
        "che sarebbero utili; Antonio Aceto nota che potrebbero servire "
        "anche per la cottura delle castagne. Emilio annota la "
        "disponibilità, osservando che i faretti sono comodi perché "
        "direzionabili tramite l'asta."),
    ("10:19", "Ilenia Piccozzi"): ("info",
        "Comunica di aver ricontattato Antonella, che a breve girerà "
        "qualche contatto per l'animazione."),
    ("11:30", "Antonio Sabatini"): ("info",
        "Comunica che dalla giornata di ieri sono entrati nella cassa "
        "del comitato ben 880€, un risultato definito un successo "
        "assoluto che dà energia ed entusiasmo verso il prossimo "
        "obiettivo."),
}

MEDIA_OVERRIDES = {
    (DATE, "07:41", "Emanuele Sciarra", "IMG-20261109-WA0000.jpg"):
        "Screenshot di un post Facebook su \"Christmas World\", il "
        "villaggio di Natale a Villa Borghese (Roma), con luna park, "
        "pista di pattinaggio e mercatini, dal 28 novembre 2026 al 10 "
        "gennaio 2027, ingresso a pagamento.",
    (DATE, "10:16", "Ilenia Piccozzi", "IMG-20261109-WA0005.jpg"):
        "Foto di un faretto da lavoro con lungo cavo elettrico e "
        "innesto filettato per il montaggio su un'asta.",
}

AUDIO_CURATED = {
    (DATE, "11:41", "Ugo Trinchini", "PTT-20261109-WA0008.opus"): ("proposta",
        "Comunica di essere in contatto con Paolo degli \"Uncini "
        "d'Abruzzo\", disponibili a venire in sede stasera per "
        "illustrare un preventivo; invita chi può a essere presente per "
        "ascoltare la proposta. Più tardi conferma che l'incontro è "
        "fissato per le 20 circa."),
    (DATE, "11:50", "Emanuele Sciarra", "PTT-20261109-WA0009.opus"): ("info",
        "Risponde a Ugo confermando la propria disponibilità per "
        "l'incontro con Paolo degli \"Uncini d'Abruzzo\", chiedendo solo "
        "l'orario."),
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
