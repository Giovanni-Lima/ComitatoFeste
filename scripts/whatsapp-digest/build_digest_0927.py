#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-27 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 09:29-15:03 (export Dropbox delle 21:06 del 27/9; nessun vocale).
Giornata della Peregrinatio delle reliquie di San Camillo de Lellis a San
Benedetto Abate. Emilio Caniglia posta l'ultimo aggiornamento della lista
coppie (foto, 24 righe, Costantino ora senza accompagnatrice indicata) e
(09:39) comunica che, per il maltempo, Don Enzo ha chiesto le magliette ma
si può indossarle sotto un altro capo (giubbino, felpa): basta lasciarne
vedere un po' di giallo. Serena Di Stefano (09:44) chiede l'orario di
ritrovo; Emilio (09:48) posta la locandina della Peregrinatio con
l'appuntamento per la messa delle 11:30 (stessa locandina già digest il
17/9, ripubblicata come promemoria). Emanuele Sciarra (09:50) sollecita
Giacomo Gentile a portare campioni di felpe alla prossima riunione. Barbara
Rizio (10:45) comunica un contrattempo e non riesce a venire. Alessandra
Simonetti (12:29) avvisa che dopo la messa Don Enzo vuole il gruppo in
sacrestia. Dante Caniglia (13:33-13:34) propone di organizzare in fretta un
pullman per San Francesco d'Assisi la settimana prossima, chiedendo di
parlarne con Don Enzo; Ilenia Piccozzi conferma che se ne sta già
occupando qualcuno. Foto della giornata: Elvis Ippoliti (13:48) manda una
foto delle reliquie di San Camillo esposte in chiesa, Daniele Boscolo
(14:42) manda una foto di gruppo del comitato (magliette gialle "1987")
insieme a Don Enzo davanti alle reliquie. Emanuele (15:03) rilancia,
ipotizzando Napoli a fine novembre come possibile meta (non è chiaro se
per lo stesso pullman o un'altra occasione). Nessuna menzione di Giovanni
Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-27"

CURATED = {
    ("09:39", "Emilio Caniglia"): ("info",
        "Comunica che, viste le condizioni meteo proibitive, Don Enzo ha "
        "comunque chiesto di indossare le magliette del comitato; su "
        "suggerimento di Antonio Sabatini, chi vuole può metterle sotto un "
        "altro capo (giubbino, felpa, ecc.), lasciando intravedere un po' "
        "di giallo."),
    ("09:44", "Serena Di Stefano"): ("domanda",
        "Chiede a che ora si va, se alla messa delle 11."),
    ("09:50", "Emanuele Sciarra"): ("domanda",
        "Sollecita Giacomo Gentile a portare qualche campione di felpa "
        "alla prossima riunione."),
    ("10:45", "Barbara Rizio"): ("info",
        "Comunica un contrattempo: non riesce a venire."),
    ("12:29", "Alessandra Simonetti"): ("info",
        "Avvisa che dopo la messa Don Enzo vuole il gruppo in sacrestia."),
    ("13:33", "Dante Caniglia"): ("proposta",
        "Propone di organizzare in fretta, per la settimana prossima, un "
        "pullman per San Francesco d'Assisi, e di parlarne con Don Enzo; "
        "Ilenia Piccozzi risponde che qualcuno se ne sta già occupando."),
    ("15:03", "Emanuele Sciarra"): ("proposta",
        "Rilancia l'idea di una gita, ipotizzando Napoli a fine novembre "
        "come possibile meta (non è chiaro se in alternativa o in aggiunta "
        "al pullman per Assisi proposto da Dante)."),
}

MEDIA_OVERRIDES = {
    (DATE, "09:48", "Emilio Caniglia", "IMG-20260927-WA0022.jpg"):
        "Ripubblica come promemoria la locandina della Peregrinatio delle "
        "reliquie di San Camillo de Lellis (Diocesi di Avezzano, Parrocchia "
        "San Benedetto Abate), oggi domenica 27/9: arrivo reliquie alle "
        "9:30, messa con i bambini alle 10:00, messa con gli operatori "
        "sanitari del territorio alle 11:30, saluto finale alle 15:30 "
        "(stessa locandina già digest il 17/9).",
    (DATE, "13:48", "Elvis Ippoliti", "IMG-20260927-WA0031.jpg"):
        "Foto delle reliquie di San Camillo de Lellis esposte in chiesa, "
        "in un'urna di vetro sull'altare.",
    (DATE, "14:42", "Daniele Boscolo", "IMG-20260927-WA0032.jpg"):
        "Foto di gruppo del comitato (magliette gialle con il logo \"1987\") "
        "davanti all'urna delle reliquie di San Camillo, insieme a Don "
        "Enzo.",
}

# IMG-20260927-WA0018.jpg (09:29, Emilio Caniglia): stessa identica lista
# coppie (24 righe) già digest ieri sera alle 21:24, nessun dato nuovo,
# scartata come duplicato.
_SKIP_FILES = {"IMG-20260927-WA0018.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, extra_skip_media=_extra_skip,
                 extra_skip_label="lista coppie duplicata")
