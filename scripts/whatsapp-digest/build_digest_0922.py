#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-22 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:22-12:12. Emanuele Sciarra comunica di aver bloccato la data
del 29/9 per l'incontro promozionale materassi (il rappresentante ha
chiamato per fermarla, essendo richiesta anche da altri gruppi) e chiede la
lista delle coppie, con l'evento previsto alle 21 come la volta scorsa: la
lista riparte da zero e si popola nel corso della mattina fino a 7 coppie
(foto delle 12:12), con un breve thread su Ilenia (senza il compagno
Pietro) ed Elvis (in attesa di sapere su Federica, poi confermato da solo)
messi insieme come settima coppia da Raffaele. Due vocali di Emanuele
(10:35, accorpati) chiedono con che nome iscriversi come comitato per la
pratica coi materassi — Comitato Feste 87 o Comitato Feste Classe 1987 —
Antonio Aceto risponde "comitato feste patronali classe 1987". Resto
rumore (conferme brevi, un messaggio di sistema). Nessuna menzione di
Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-22"

CURATED = {
    ("08:22", "Emanuele Sciarra"): ("decisione",
        "Comunica di aver bloccato la data del 29/9 per l'incontro "
        "pubblicitario dei materassi (il promotore ha chiamato chiedendo "
        "di confermare, essendo la data richiesta anche da altri "
        "gruppi); chiede la lista delle coppie, l'evento si terrà alle "
        "21 come la volta scorsa."),
    ("09:26", "Antonio Aceto"): ("info",
        "Conferma la partecipazione sua e di Jennifer."),
    ("09:37", "Raffaele Di Cesare"): ("info",
        "Conferma la partecipazione sua e della compagna Verdiana."),
    ("09:38", "Valentina D'Arcadia"): ("info",
        "Conferma la partecipazione sua e di Maurizio."),
    ("09:38", "Barbara Rizio"): ("info",
        "Conferma la partecipazione sua e di Silvano."),
    ("09:54", "Tina Giarrante"): ("info",
        "Conferma la propria partecipazione insieme a Ugo Trinchini."),
    ("09:54", "Maikel Montano"): ("info",
        "Conferma la partecipazione sua e della moglie."),
    ("10:01", "Ilenia Piccozzi"): ("info",
        "Comunica che parteciperà senza il compagno Pietro, il cui "
        "turno di lavoro potrebbe non cambiare."),
    ("10:30", "Elvis Ippoliti"): ("info",
        "Conferma la propria partecipazione; per Federica farà sapere "
        "più avanti."),
    ("10:36", "Antonio Aceto"): ("info",
        "Risponde a Emanuele sul nome da usare per l'iscrizione del "
        "comitato: dovrebbe essere \"comitato feste patronali classe "
        "1987\"."),
    ("10:51", "Raffaele Di Cesare"): ("info",
        "Propone che, in mancanza di un partner sicuro per Ilenia ed "
        "Elvis, i due formino insieme la settima coppia."),
    ("10:57", "Elvis Ippoliti"): ("info",
        "Conferma che parteciperà da solo (Federica non ci sarà) e si "
        "rende disponibile a fare coppia."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "10:35",
        "anchor_sender": "Emanuele Sciarra",
        "type": "domanda",
        "text": (
            "Chiede come ci si dovrà chiamare in fase di iscrizione come "
            "comitato (\"Comitato Feste 87\" o \"Comitato Feste Classe "
            "1987\"): glielo ha chiesto il rappresentante dei materassi, "
            "pur non essendo necessarie fatture; chiede se qualcuno ne sa "
            "di più."
        ),
        "members": ["PTT-20260922-WA0001.opus", "PTT-20260922-WA0002.opus"],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "12:12", "Emilio Caniglia", "IMG-20260922-WA0003.jpg"):
        "Foto del foglio \"COPPIE\" per l'incontro pubblicitario del "
        "29/9, ripartito da zero rispetto alle liste precedenti: 7 "
        "coppie finora — Antonio A.-Jennifer, Raffaele-Verdiana, "
        "Maurizio-Valentina, Silvano-Barbara, Ugo-Tina, Mike-Lucianny, "
        "Elvis-Ilenia.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_merges=AUDIO_MERGES)
