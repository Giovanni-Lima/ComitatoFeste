#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-20 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 11:06-16:42 (export Dropbox delle 00:06 del 21/10). Mattina:
Costantino Mariani (13:22) chiede come procedere con le castagne per San
Martino. Emanuele Sciarra condivide sei foto di un'auto (Range Rover Evoque
nera) di una collega in vendita, con relative battute di Valentina ("ho una
moto da vendere"), Dante e lui stesso sul fare il rivenditore — tutto
rumore, fuori tema comitato, scartato (foto comprese). Nel pomeriggio
Emanuele posta lo screenshot di un post Facebook del Santuario di Santa
Maria Goretti che conferma la gita a Corinaldo di domenica 8 novembre.
Emilio Caniglia (16:36) ricorda la riunione di venerdì 23 ottobre alle 21
in sede, con l'ordine del giorno (Corinaldo, San Martino, calze Befana);
segue un breve scambio su chi porta da bere (Campari, borsa frigo, il
frigo di Maikel Montano). Resto rumore (battute, dialetto). Nessuna
menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-20"

CURATED = {
    ("13:22", "Costantino Mariani"): ("domanda",
        "Saluta la classe e chiede come procedere con le castagne per "
        "l'evento di San Martino."),
    ("16:36", "Emilio Caniglia"): ("info",
        "Ricorda che, come concordato venerdì scorso, al termine "
        "dell'incontro sponsorizzato di venerdì 23 ottobre alle 21 presso "
        "la sede ci sarà una riunione, con priorità su: punto della "
        "situazione per la visita a Corinaldo (prenotazioni, "
        "pianificazione del viaggio); organizzazione dell'evento di San "
        "Martino (disponibilità, acquisto del castagno); pianificazione "
        "delle calze della Befana (disponibilità, acquisto materiale). "
        "Ne parleranno venerdì."),
}

TEXT_MERGES = [
    {
        "anchor_time": "16:37",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Raccomanda a Tina Giarrante di portare i Campari per la "
            "riunione di venerdì; Tina conferma e aggiunge la borsa frigo. "
            "Elvis Ippoliti suggerisce che sarebbe meglio se il frigo lo "
            "portasse Maikel Montano, con battute sul fatto che non si fa "
            "sentire."
        ),
        "members": [
            ["16:37", "Emanuele Sciarra"], ["16:38", "Tina Giarrante"],
            ["16:39", "Emanuele Sciarra"], ["16:39", "Elvis Ippoliti"],
            ["16:40", "Emanuele Sciarra"], ["16:40", "Tina Giarrante"],
            ["16:40", "Emanuele Sciarra"], ["16:41", "Elvis Ippoliti"],
            ["16:42", "Elvis Ippoliti"],
        ],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "15:59", "Emanuele Sciarra", "IMG-20261020-WA0013.jpg"):
        "Screenshot di un post Facebook del Santuario Santa Maria Goretti "
        "di Corinaldo: comunicato per la \"Classe 1987 - San Benedetto dei "
        "Marsi\" che conferma la gita a Corinaldo di domenica 8 novembre "
        "2026, in occasione del gemellaggio con la città natale di Santa "
        "Maria Goretti.",
}

AUDIO_CURATED = {
    (DATE, "11:17", "Dante Caniglia", "PTT-20261020-WA0003.opus"): ("rumore", ""),
    (DATE, "11:23", "Emanuele Sciarra", "PTT-20261020-WA0005.opus"): ("rumore", ""),
    (DATE, "11:36", "Dante Caniglia", "PTT-20261020-WA0006.opus"): ("rumore", ""),
}

# Le sei foto dell'auto (Range Rover Evoque) in vendita tramite una collega
# di Emanuele: compravendita personale, fuori tema comitato, scartate come
# il relativo scambio di battute.
_SKIP_FILES = {
    "IMG-20261020-WA0007.jpg", "IMG-20261020-WA0008.jpg",
    "IMG-20261020-WA0009.jpg", "IMG-20261020-WA0010.jpg",
    "IMG-20261020-WA0011.jpg", "IMG-20261020-WA0012.jpg",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="compravendita auto personale, fuori tema")
