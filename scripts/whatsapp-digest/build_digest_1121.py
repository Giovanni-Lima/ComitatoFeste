#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-21 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 00:25-23:50. Emanuele propone l'acquisto di 600 cartelle a strappo
(14€, già usate dall'85) per la Tombolata; approvazione generale. Sondaggio
per scegliere il colore del portabadge (colorati vs nero): vincono i
colorati. Scherzo di Daniele Boscolo sulle calze di Natale del McDonald's
(scartato, rumore). Antonio Aceto aggiorna sulla vendita delle prevendite
delle calze della Befana (prime 5 vendute). A fine giornata, un post
Facebook del Comitato Classe 1986 segna la chiusura del loro mandato con un
augurio alla Classe 1987. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-21"

CURATED = {
    ("00:25", "Emanuele Sciarra"): ("proposta",
        "Propone l'acquisto di 600 cartelle a strappo per la "
        "Tombolata a 14€, già usate dal comitato dell'85. Link "
        "Amazon: https://amzn.eu/d/0eoDGMmI (domande sul prodotto: "
        "https://amzn.eu/d/08ewcdY4). Antonio Aceto e Barbara "
        "concordano che a questo prezzo conviene."),
    ("13:33", "Emanuele Sciarra"): ("proposta",
        "Chiede di rispondere al sondaggio sul portabadge, in modo "
        "che Alessandra possa fare i badge con le misure giuste; "
        "precisa che quelli colorati sono misti (circa 10 per "
        "colore), ma si possono trovare anche in versione "
        "monocolore.\n\nSONDAGGIO: Quale porta badge preferita\n"
        "OPZIONE: Colorati (16 voti)\nOPZIONE: Nero (3 voti)"),
    ("21:03", "Antonio Aceto"): ("info",
        "Aggiorna sulla vendita delle prevendite delle calze della "
        "Befana: comunica \"1 di 10 fatto!\" e poco dopo le prime 5 "
        "calze vendute."),
}

MEDIA_OVERRIDES = {
    (DATE, "13:32", "Emanuele Sciarra", "IMG-20261121-WA0007.jpg"):
        "Portabadge, opzione nero: set da 50 su Amazon (cordino + "
        "porta tesserino trasparente).",
    (DATE, "13:33", "Emanuele Sciarra", "IMG-20261121-WA0008.jpg"):
        "Portabadge, opzione colorati: set misto (blu, arancione, "
        "verde, rosso, giallo) su Amazon, 14,59€.",
    (DATE, "21:02", "Antonio Aceto", "IMG-20261121-WA0013.jpg"):
        "Foto delle calze della Befana messe in vendita.",
    (DATE, "21:02", "Antonio Aceto", "IMG-20261121-WA0012.jpg"):
        "Altra foto delle calze della Befana messe in vendita.",
    (DATE, "21:16", "Antonio Aceto", "IMG-20261121-WA0014.jpg"):
        "Foto a corredo del messaggio \"Prime 5 calze vendute!\".",
    (DATE, "23:50", "Dante Caniglia", "IMG-20261122-WA0000.jpg"):
        "Screenshot di un post Facebook del Comitato Classe 1986: "
        "annunciano la chiusura del proprio mandato (\"l'ultima "
        "firma\") e augurano buona fortuna alla Classe 1987 San "
        "Benedetto dei Marsi, con una foto di gruppo.",
}

# IMG-20261121-WA0010/11.jpg (20:39 Daniele Boscolo, "Ragazzi tutti al Mc ho
# trovato le calze"): scherzo su un paio di calzini natalizi a tema
# McDonald's, gioco di parole con le "calze" della Befana — battuta, scartata.
_SKIP_FILES = {"IMG-20261121-WA0010.jpg", "IMG-20261121-WA0011.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, extra_skip_media=_extra_skip,
                 extra_skip_label="foto di battuta fuori tema")
