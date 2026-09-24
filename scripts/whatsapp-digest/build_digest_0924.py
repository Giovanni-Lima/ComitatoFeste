#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-24 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 06:05-12:27 (nessun vocale). Mattina di saluti (rumore). Antonio
Aceto (08:09) chiede di aggiungere Gino e Roberta alla serata di martedì
29/9 e un resoconto delle coppie; Emilio Caniglia (12:05) risponde con la
foto aggiornata della lista (22 righe, 3 posizioni ancora incomplete).
Alessandra Toracchio (08:40) chiede a Emanuele aggiornamenti sull'incontro
del pomeriggio (quello con il rappresentante dei materassi, spostato a
giovedì); Valentina D'Arcadia (12:06) chiede se si farà un'altra serata
materassi, Emanuele (12:26) risponde di sì. Giovanni Lima (08:32-08:33)
posta un video con una breve spiegazione su come usare l'assistente del
portale (risposta alla domanda di Aceto sul resoconto): il video non ha
traccia audio (verificato a mano sugli atom MP4, niente ffprobe su questa
macchina), quindi per regola è escluso, e i suoi messaggi riguardano il
portale, non il comitato — non generano entry. Nessuna menzione di Giovanni
Lima da parte di altri in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-24"

CURATED = {
    ("08:09", "Antonio Aceto"): ("info",
        "Chiede di aggiungere Gino e Roberta alla serata di martedì "
        "29/9 e di fare un resoconto delle coppie."),
    ("08:40", "Alessandra Toracchio"): ("domanda",
        "Chiede a Emanuele Sciarra un aggiornamento sull'incontro di "
        "oggi pomeriggio (presumibilmente quello con il rappresentante "
        "dei materassi, spostato a giovedì)."),
    ("12:06", "Valentina D'Arcadia"): ("domanda",
        "Chiede se si farà anche un'altra serata dei materassi."),
    ("12:26", "Emanuele Sciarra"): ("info",
        "Risponde di sì a Valentina D'Arcadia: si farà un'altra serata "
        "materassi; aggiornerà a breve Alessandra Toracchio "
        "sull'incontro di oggi."),
}

MEDIA_OVERRIDES = {
    (DATE, "12:05", "Emilio Caniglia", "IMG-20260924-WA0005.jpg"):
        "Aggiornamento del foglio \"COPPIE\" per l'incontro sponsorizzato "
        "del 29/9, ora a 22 righe: Antonio A.-Jennifer, Raffaele-"
        "Verdiana, Maurizio-Valentina, Silvano-Barbara, Ugo (senza "
        "partner), Tina (senza partner), Mike-Lucianny, Elvis (senza "
        "partner), Ilenia (senza partner), Alessandro-Patrizia, "
        "Costantino-Alexa, Cesare-Valentina, Antonio S. (senza partner), "
        "Andrea-Rossella, Donato-Santina, Donato-Marina, Emilio-Federica, "
        "Alessio-Miriam, Tonino-Giovanna, Alessio-Margherita, Geo-Alice, "
        "Gino-Roberta.",
}

# VID-20260924-WA0003.mp4 (08:32, Giovanni Lima): nessuna traccia audio
# (nessun handler "soun" negli atom MP4, verificato a mano — niente ffprobe
# su questa macchina, dove is_reaction_gif() non esclude nulla). Escluso per
# regola sui .mp4 muti; è comunque un video sull'uso del portale, non
# contenuto del comitato.
_SKIP_FILES = {"VID-20260924-WA0003.mp4"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, extra_skip_media=_extra_skip,
                 extra_skip_label="mp4 muto verificato a mano")
