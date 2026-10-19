#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-19 — solo dati di curatela, logica comune in digest_lib.py.

Pomeriggio (14:26-15:49): Emanuele propone di cercare referenti di comitati
feste/Pro Loco dei paesi vicini per girare i contatti della sponsorizzazione
materassi (bonus 50€ per associazione nuova presentata), con Cesare che
suggerisce Pro Loco Pescina e il circolo anziani di San Benedetto; Alessandra
intanto chiede già informazioni a Ortucchio. In coda, Barbara chiede se le
stampe della locandina di Corinaldo bastano: Cesare ne tiene due per i
negozi, Emilio conferma che le affiggeranno nei prossimi giorni. Nessuna
menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-19"

CURATED = {
    ("14:38", "Alessandra Toracchio"): ("info",
        "Comunica di aver già chiesto informazioni al comitato di "
        "Ortucchio: appena saprà qualcosa aggiornerà il gruppo."),
    ("15:19", "Barbara Rizio"): ("domanda",
        "Chiede se le stampe già fatte della locandina di Corinaldo sono "
        "sufficienti, o se conviene farne altre."),
    ("15:48", "Emilio Caniglia"): ("info",
        "Risponde che tra oggi e domani vedranno di affiggere le "
        "locandine di Corinaldo."),
}

AUDIO_CURATED = {
    (DATE, "15:47", "Cesare Raglione", "PTT-20261019-WA0008.opus"): ("info",
        "Risponde, sulle locandine di Corinaldo, che se gliene danno due "
        "ne metterà una nel suo negozio e una in quello della sorella."),
}

MEDIA_OVERRIDES = {}

AUDIO_MERGES = [
    {
        "anchor_time": "14:26",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Emanuele propone di cercare i referenti/presidenti di "
            "comitati feste o Pro Loco dei paesi vicini (Ortucchio, Lecce, "
            "Gioia, Pescina) per girargli i contatti della sponsorizzazione "
            "materassi: ogni associazione nuova presentata frutta al "
            "comitato un bonus di 50€, oltre al guadagno già previsto "
            "sulla propria serata. Cesare segnala che il presidente della "
            "Pro Loco di Pescina potrebbe andare bene (non sa se hanno già "
            "fatto demo con l'azienda) e propone anche il circolo anziani "
            "di San Benedetto, con un compenso vicino ai 500€ (cifra esatta "
            "incerta nella trascrizione del vocale). Emanuele concorda "
            "sulla Pro Loco di San Benedetto se non già coinvolta, precisa "
            "che l'azienda accetta qualsiasi tipo di associazione (non "
            "solo comitati feste) e propone di informarsi se altri "
            "comitati/Pro Loco hanno già collaborato con loro: se i "
            "comitati feste cambiano ogni anno come il loro potrebbe non "
            "essere un problema, se una Pro Loco è sempre la stessa "
            "potrebbe aver già saturato la disponibilità; si offre di "
            "chiedere anche a Trasacco tramite conoscenze sue. Propone di "
            "raccogliere le informazioni e discuterne in riunione."
        ),
        "members": [
            "PTT-20261019-WA0001.opus",
            "PTT-20261019-WA0002.opus",
            "PTT-20261019-WA0003.opus",
            "PTT-20261019-WA0004.opus",
            "PTT-20261019-WA0005.opus",
            "PTT-20261019-WA0006.opus",
            "PTT-20261019-WA0007.opus",
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES)
