#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-01 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 16:32-17:14 (export Dropbox delle 18:21 del 1/10; nessun vocale).
Antonio Sabatini condivide il rendiconto di cassa di settembre: due
movimenti in entrata, l'evento promozionale del 18/9 (500€) e quello del
29/9 (600€), nessuna uscita, saldo 1.100€. Resto rumore (un applauso).
Nessuna menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-01"

CURATED = {}

MEDIA_OVERRIDES = {
    (DATE, "16:32", "Antonio Sabatini", "Comitato feste 1987-Settembre .pdf"):
        "Rendiconto di cassa di settembre: due movimenti in entrata, "
        "\"Evento promozionale 1\" del 18/9 (500€) ed \"Evento promozionale "
        "2\" del 29/9 (600€); nessuna uscita registrata. Totale entrate "
        "1.100€, saldo 1.100€.",
}


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
