#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-19 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 06:18-18:26 (export Dropbox delle 18:56 del 19/9). Mattina di
saluti (rumore) e battute sul Lotto. Luca Cicchelli (11:53) dice di aver
procurato uno sponsor durante il torneo di biliardino; Gilda Di Iulio
(12:06) segnala un'altra disponibilità per "il premio" (Selma). Thread
principale del pomeriggio: Emanuele Sciarra (12:49, vocale) ha altri due
contatti per serate materassi e due per depuratori, ma i suoi turni di
lavoro complicano le serate; Antonio Aceto (13:43) chiede se si possa fare
di sabato, Raffaele Di Cesare (13:45) dà disponibilità serale, Emanuele
(14:00, vocale) è scettico sul sabato ma si può provare, Emilio Caniglia
(14:29) dà il via libera a verificare le disponibilità. Emilio (14:52)
ripubblica e fissa in chat la locandina dell'incontro col Vescovo del 20/9
(stesso file già digest il 17/9 08:05) con una nota nuova: a breve un
sondaggio per la sede del Comitato (70 euro/mese + utenze). Restano rumore:
le chiacchiere sul torneo di biliardino (vocali di Dante e Luca 12:01-12:06),
lo screenshot Facebook della festa di classe 1986 di Dante (12:38, non legato
al comitato, scartato) e i due vocali sulla festa di classe (12:38/12:44),
la battuta di Raffaele (14:06) e quella di Costance sulla Ferrari (18:26).
Nessuna menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-19"

CURATED = {
    ("11:53", "Luca Cicchelli"): ("info",
        "Comunica di aver procurato uno sponsor durante il torneo di "
        "biliardino del giorno prima; non sa ancora quanto riscuoterà."),
    ("12:06", "Gilda Di Iulio"): ("info",
        "Comunica che anche Selma è disponibile per il premio (informazione "
        "ricevuta tramite terzi, non sa esattamente di cosa si tratti); "
        "andrà da lei appena possibile e aggiornerà il gruppo."),
    ("13:43", "Antonio Aceto"): ("domanda",
        "Osserva che con Emanuele i turni di lavoro non coincidono mai (lui "
        "la prossima settimana fa il pomeriggio) e chiede se non si possa "
        "organizzare la serata di sabato."),
    ("13:45", "Raffaele Di Cesare"): ("info",
        "Comunica che lui e Verdiana sono sempre disponibili la sera alle "
        "21 e danno già da ora la propria disponibilità."),
    ("14:29", "Emilio Caniglia"): ("info",
        "Dà il via libera: Emanuele verifichi le disponibilità dei "
        "rappresentanti, poi ci si organizza di conseguenza anche sul "
        "numero di persone."),
}

AUDIO_CURATED = {
    (DATE, "12:49", "Emanuele Sciarra", "PTT-20260919-WA0011.opus"): ("proposta",
        "Ha altri due contatti per serate materassi e due per depuratori e "
        "li sentirà lunedì; spiega che i suoi turni di lavoro (mattina la "
        "settimana entrante, poi notte e pomeriggio) gli rendono difficile "
        "esserci alle 21, e chiede al gruppo se organizzare comunque le "
        "serate tra due-tre settimane."),
    (DATE, "14:00", "Emanuele Sciarra", "PTT-20260919-WA0013.opus"): ("info",
        "Risponde che il sabato non ci aveva mai pensato ed è improbabile, "
        "perché i rappresentanti viaggiano dal lunedì al venerdì, ma si "
        "può provare a chiedere."),
    # Vocali di rumore (saluti, torneo di biliardino, festa di classe): scartati.
    (DATE, "06:18", "Emanuele Sciarra", "PTT-20260919-WA0000.opus"): ("rumore", ""),
    (DATE, "12:01", "Dante Caniglia", "PTT-20260919-WA0004.opus"): ("rumore", ""),
    (DATE, "12:04", "Luca Cicchelli", "PTT-20260919-WA0005.opus"): ("rumore", ""),
    (DATE, "12:04", "Luca Cicchelli", "PTT-20260919-WA0006.opus"): ("rumore", ""),
    (DATE, "12:38", "Dante Caniglia", "PTT-20260919-WA0009.opus"): ("rumore", ""),
    (DATE, "12:44", "Luca Cicchelli", "PTT-20260919-WA0010.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {
    (DATE, "14:52", "Emilio Caniglia", "IMG-20260917-WA0000.jpg"):
        "Ripubblica e fissa in chat la locandina dell'incontro su San "
        "Francesco col Vescovo, domenica 20/9 alle 16:30 ai locali della "
        "Parrocchia di San Cipriano, con questa nota: a breve un sondaggio "
        "per la sede del Comitato, per rendere definitiva l'indicazione "
        "emersa in riunione; costo della sede 70 euro mensili, più utenze a "
        "consumo e costo di attivazione (circa 25 euro per l'energia "
        "elettrica e circa 50 euro per il gas).",
}

# IMG-20260919-WA0008.jpg (12:38, Dante Caniglia): screenshot Facebook della
# festa di classe 1986, non legato al comitato, scartato.
_SKIP_FILES = {"IMG-20260919-WA0008.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="screenshot esterno non legato al comitato")
