#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-27 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:39-07:45 (export Dropbox delle 15:25, giornata ancora in
corso). Emilio ricorda la riunione di stasera (ore 21, sede), importante
per decidere data della Tombolata, modalità di partecipazione
all'accensione dell'albero/mercatini, calze della Befana, costituzione
formale del Comitato; riporta anche la richiesta della Pro Loco di un
"nome accattivante" per gli eventi del Comitato, da inserire nella
locandina del calendario natalizio. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-27"

CURATED = {
    ("07:39", "Emilio Caniglia"): ("info",
        "Ricorda la riunione di questa sera, ore 21 in sede: "
        "importante, è prioritario decidere la data della Tombolata, "
        "le modalità di partecipazione alla giornata dell'accensione "
        "dell'albero/mercatini di Natale, le calze della Befana, la "
        "costituzione del Comitato ed altro. Ci sarà anche un "
        "resoconto dell'attività della settimana (incontri per spari "
        "e fuochi d'artificio, incontro per Capodanno). Riporta "
        "infine che la Pro Loco ha chiesto di dare un \"nome "
        "accattivante\" agli eventi del Comitato (Capodanno, "
        "Tombolata, Befana, ecc.), da inserire nella locandina del "
        "calendario natalizio."),
}

MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
