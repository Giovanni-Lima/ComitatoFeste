#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-11 — solo dati di curatela, logica comune in digest_lib.py.

Giornata (parziale, fino alle 14:07) dominata dai saluti mattutini e da un
lungo siparietto scherzoso in dialetto tra Elvis/Luca/Raffaele/Maria su
vecchi ricordi (incidente in bicicletta, mongolfiera, "panda verde") — rumore,
niente di attinente al comitato; la stessa vena nostalgica riprende con
Gilda (12:22, mongolfiera) e con Dante che ricorda di avere vecchie
videocassette (asilo, vendemmia 1991, 13:45/13:53) e la battuta di Raffaele
sul vino del '91 — trattati anch'essi come rumore/nostalgia, non risulta
un uso concreto per il comitato dal testo (segnalare se il gruppo ne parla
in modo più esplicito in una finestra successiva).

Punti rilevanti: Tina Giarrante completa la lista di cosa porta per la
riunione di stasera (vedi anche il thread iniziato il 10/9 da Alessandra
Toracchio/Barbara Rizio); Alessandra Toracchio manda la posizione del
rustico (pin statico via link Maps, non "in tempo reale" — vedi regola
11/9/2026 in CLAUDE.md) con due screenshot di Google Street View come
riferimento visivo; Emanuele Sciarra avvisa che stasera arriva più tardi;
Raffaele Di Cesare chiede a che ora è la riunione, Tina risponde. Nessuna
menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-11"

CURATED = {
    ("08:53", "Tina Giarrante"): ("info",
        "Per la riunione di stasera comunica cosa ha preso: varie patatine, 2 "
        "bottiglie di acqua frizzante, un succo e un tè; il resto lo portano "
        "gli altri. Chiede comunque ad Alessandra Toracchio di mandare la "
        "posizione."),
    ("11:55", "Alessandra Toracchio"): ("info",
        "Condivide la posizione del rustico per la riunione di stasera: "
        "https://maps.google.com/?q=42.0035863,13.6262866"),
    ("13:36", "Emanuele Sciarra"): ("info",
        "Avvisa che stasera arriva più tardi: stacca dal lavoro alle 22 e poi "
        "raggiunge il gruppo."),
    ("13:54", "Raffaele Di Cesare"): ("domanda",
        "Scherza con Dante sul portare il vino del '91, poi chiede a che ora "
        "è la riunione di stasera."),
    ("14:07", "Tina Giarrante"): ("info",
        "Risponde a Raffaele: la riunione di stasera è dopo le 21, o "
        "comunque sarà Alessandra ad avvisare quando è pronta."),
}

MEDIA_OVERRIDES = {
    (DATE, "12:02", "Alessandra Toracchio", "IMG-20260911-WA0039.jpg"):
        "Screenshot di Google Street View che inquadra un incrocio con una "
        "casa color pesca a due piani con balcone e persiane verdi, per "
        "mostrare com'è la zona sul retro del palazzo del ritrovo.",
    (DATE, "12:02", "Alessandra Toracchio", "IMG-20260911-WA0040.jpg"):
        "Screenshot di Google Street View su Via Italia con una freccia rossa "
        "disegnata a mano che indica l'ingresso esatto (una porta con tenda) "
        "tra due edifici rustici, per indicare dove trovare il punto di "
        "ritrovo.",
}

# VID-20260911-WA0042.mp4: nessuna traccia audio (ispezionati i box MP4 —
# 'vide'/'avc1' presenti, 'soun'/'mp4a' assenti — ffprobe non disponibile in
# questa sessione, stessa verifica manuale già usata per il digest del 10/9).
# È quindi una GIF di reazione travestita da video, va scartata come tale.
_REACTION_GIF_MP4 = {
    "VID-20260911-WA0042.mp4",
}


def _skip_reaction_gif_mp4(time_, fname):
    return fname in _REACTION_GIF_MP4


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES,
                 extra_skip_media=_skip_reaction_gif_mp4,
                 extra_skip_label="GIF di reazione .mp4 senza audio, escluse")
