#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-04 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:47-11:04 (export Dropbox delle 11:35 di oggi). Mattina presto:
Emilio posta il recap della riunione Pro Loco di ieri sera su San
Martino (ruoli definiti, dettagli alla riunione del 6/11) e un bilancio
molto positivo della stagione, con un richiamo motivazionale in vista di
San Martino. Poi lunga discussione sul Capodanno: aspetti economici
dell'accordo con Gianvito (percentuale sull'incasso), disponibilità di
Andrea Di Loreto per l'animazione, nomi alternativi, un sondaggio sulla
partecipazione dei membri e un confronto sul metodo (prima le
disponibilità, poi i contatti). Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-04"

CURATED = {
    ("07:47", "Emilio Caniglia"): ("decisione",
        "Posta il recap della riunione Pro Loco di ieri sera su San "
        "Martino: il comitato ha avanzato richieste precise (data, "
        "luogo, esclusione di stand gastronomici), con una prima "
        "definizione dei ruoli — al comitato la castagnata e il vin "
        "brulé, alla Pro Loco l'intrattenimento sociale. Tutti i "
        "dettagli operativi (utensili, materiale di consumo, "
        "scenografia, cottura delle castagne) saranno definiti alla "
        "riunione di venerdì 6 novembre, ore 21 in sede. Fa un bilancio "
        "molto positivo della stagione (serate sponsorizzate, "
        "collaborazioni, presenza sociale, successo clamoroso della "
        "gita a Corinaldo rispetto agli anni passati) e sottolinea che "
        "San Martino sarà un banco di prova per il collettivo, da "
        "superare con la collaborazione."),
    ("09:45", "Emanuele Sciarra"): ("proposta",
        "Apre un sondaggio: \"Chi parteciperà a capodanno?\" Al momento "
        "dell'export: Sì 6 voti, No 3 voti."),
    ("10:06", "Ilenia Piccozzi"): ("info",
        "Solleva una preoccupazione economica su chi debba pagare "
        "musica, animazione e SIAE per il Capodanno, proponendo (senza "
        "sapere che l'accordo era già stato chiarito, vedi vocale delle "
        "9:19) lo stesso modello a percentuale con Gianvito. Elvis "
        "ribadisce che sarebbe stato meglio verificare prima le "
        "disponibilità dei membri del comitato, prima di contattare "
        "Di Loreto; Ilenia concorda, non avendo sentito quella parte "
        "della discussione."),
}

AUDIO_CURATED = {
    (DATE, "09:11", "Antonio Aceto", "PTT-20261104-WA0004.opus"): ("proposta",
        "Propone di iniziare la pubblicità del Capodanno subito dopo "
        "San Martino, eventualmente già dopo la gita di Corinaldo, "
        "visto che San Martino è ormai organizzato."),
    (DATE, "09:43", "Dante Caniglia", "PTT-20261104-WA0010.opus"): ("proposta",
        "Nota che non è il comitato a mettere i soldi per il Capodanno: "
        "per rispetto dell'attività di Gianvito, propone di avere già "
        "pronti dei nomi sostituti da contattare rapidamente, per non "
        "rischiare di arrivare a Capodanno senza un cantante."),
    (DATE, "10:10", "Antonio Aceto", "PTT-20261104-WA0011.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {}

TEXT_MERGES = [
    {
        "anchor_time": "09:33",
        "anchor_sender": "Serena Di Stefano",
        "type": "info",
        "text": (
            "Serena aggiorna: Andrea Di Loreto farà sapere entro oggi o "
            "domani se sarà disponibile per il Capodanno; ha già "
            "precisato che le locandine con il suo nome usciranno solo "
            "quando lo deciderà lui (per ragioni di marketing), anche "
            "se nel frattempo si può già fare pubblicità generica. "
            "Elvis conferma di averlo incontrato: oggi ha una proposta "
            "per un matrimonio, se gliela confermano non sarà "
            "disponibile per il comitato, altrimenti farà Capodanno con "
            "loro."
        ),
        "members": [
            ["09:33", "Serena Di Stefano"], ["09:34", "Serena Di Stefano"],
            ["09:35", "Serena Di Stefano"], ["09:35", "Elvis Ippoliti"],
            ["09:36", "Serena Di Stefano"],
        ],
    },
    {
        "anchor_time": "09:39",
        "anchor_sender": "Dante Caniglia",
        "type": "proposta",
        "text": (
            "Dante propone di iniziare subito a contattare altri nomi "
            "per essere coperti, notando che chi lavora di serate sa "
            "già ora dove andrà a Capodanno. Elvis osserva che prima "
            "bisognerebbe verificare quanti membri del comitato "
            "garantiscono la propria presenza, perché con poche persone "
            "sarebbe difficile gestire l'evento (lotterie comprese) — "
            "ritiene prematuro essersi già mossi con Di Loreto senza "
            "prima questa certezza. Serena propone un sondaggio per "
            "regolarsi."
        ),
        "members": [
            ["09:38", "Elvis Ippoliti"], ["09:39", "Dante Caniglia"],
            ["09:41", "Serena Di Stefano"], ["09:43", "Elvis Ippoliti"],
            ["09:43", "Emanuele Sciarra"], ["09:44", "Elvis Ippoliti"],
            ["09:45", "Serena Di Stefano"],
        ],
    },
    {
        "anchor_time": "10:46",
        "anchor_sender": "Tina Giarrante",
        "type": "info",
        "text": (
            "Tina suggerisce un'alternativa a Rossano (probabilmente "
            "già impegnato da un anno): il gruppo di Pietro, per cui "
            "Ilenia potrebbe fare da tramite. Emanuele nota che anche "
            "Pietro sembra impegnato; Ilenia corregge: non è ancora "
            "confermato, stanno solo valutando un'altra proposta."
        ),
        "members": [
            ["10:46", "Tina Giarrante"], ["10:47", "Emanuele Sciarra"],
            ["11:04", "Ilenia Piccozzi"],
        ],
    },
]

AUDIO_MERGES = [
    {
        "anchor_time": "09:03",
        "anchor_sender": "Emanuele Sciarra",
        "type": "decisione",
        "text": (
            "Emanuele chiede un punto economico sul Capodanno prima di "
            "procedere a organizzare/pubblicizzare: ha paura che, se il "
            "comitato dovesse pagare di tasca propria musica, "
            "animazione e SIAE (stimati sui 1.700€ complessivi), con "
            "l'incasso stimato (10€ a persona su circa 200 persone = "
            "2.000€) il margine resterebbe troppo basso (circa 300€) "
            "per valerne la pena. Antonio Aceto chiarisce: lui e Ugo "
            "avevano già parlato con Gianvito, che paga tutto lui "
            "(SIAE, musica, animazione) e lascia al comitato una "
            "percentuale sull'incasso (9-10%) in base al numero di "
            "partecipanti. Emanuele, che non era alla riunione "
            "precedente, prende atto e conferma che si può procedere."
        ),
        "members": [
            "PTT-20261104-WA0002.opus", "PTT-20261104-WA0003.opus",
            "PTT-20261104-WA0005.opus", "PTT-20261104-WA0006.opus",
            "PTT-20261104-WA0007.opus",
        ],
    },
    {
        "anchor_time": "09:37",
        "anchor_sender": "Emanuele Sciarra",
        "type": "domanda",
        "text": (
            "Emanuele chiede quali alternative ci siano nell'eventualità "
            "che Andrea Di Loreto non sia disponibile, citando come "
            "possibile contatto Rossano di Castellafiume."
        ),
        "members": [
            "PTT-20261104-WA0008.opus", "PTT-20261104-WA0009.opus",
        ],
    },
]

_SKIP_FILES = {
    # GIF di reazione muta (verificata: nessuna traccia audio)
    "VID-20261104-WA0000.mp4",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES, audio_merges=AUDIO_MERGES,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="GIF di reazione mp4 (verificata a mano)")
