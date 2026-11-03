#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-03 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 12:30-16:41 (export Dropbox delle 17:09 di oggi): Emilio annuncia
un cambio di programma per il trasporto a Corinaldo, confermando (con
acconto) un pullman da 64 posti con Bianchi Tour al posto di Passalacqua +
mezzo aggiuntivo: risparmio netto per il comitato. Stasera riunione della
Pro Loco su San Martino, il comitato è invitato. Resto rumore (presenze
per stasera, battute). Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-03"

CURATED = {
    ("12:30", "Emilio Caniglia"): ("decisione",
        "Annuncia un brusco cambio di programma per il trasporto a "
        "Corinaldo: confermato (con acconto) Bianchi Tour al posto di "
        "Passalacqua, prenotando un pullman da 64 posti invece che il "
        "pullman da 54 posti più un mezzo aggiuntivo (furgone da 9 "
        "posti a 500€ o secondo pullman da 19 posti a 750-800€, oltre "
        "ai 1100€ del pullman da 54). Il nuovo pullman unico costa "
        "1250€ in tutto: il comitato risparmia e massimizza l'entrata. "
        "Stasera riunione della Pro Loco per l'organizzazione di San "
        "Martino: il comitato è invitato, chi vuole aggiungersi scriva "
        "a Emilio in privato."),
    ("13:22", "Emilio Caniglia"): ("info",
        "Precisa: Passalacqua era stato scelto per un servizio "
        "migliore, ma aggiungere un mezzo in più rendeva la soluzione "
        "poco conveniente rispetto al pullman unico."),
}

AUDIO_CURATED = {
    (DATE, "12:36", "Antonio Aceto", "PTT-20261103-WA0003.opus"): ("rumore", ""),
    (DATE, "13:24", "Antonio Aceto", "PTT-20261103-WA0005.opus"): ("rumore", ""),
    (DATE, "13:24", "Antonio Aceto", "PTT-20261103-WA0006.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {}

_SKIP_FILES = {
    # GIF di reazione muta (verificata: nessuna traccia audio)
    "VID-20261103-WA0011.mp4",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="GIF di reazione mp4 (verificata a mano)")
