#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-06 — solo dati di curatela, logica comune in digest_lib.py.

Giornata silenziosa fino a sera: unica finestra 20:54-21:37. Tra una serie
di vocali scherzosi (battute dialettali, un gioco della "rotonda" tra
Emanuele e Costantino), Emanuele dà due aggiornamenti: ha sentito la
referente Bimby, oggi a una riunione a Pescara sulle nuove offerte, e la
promozione (4 Bimby venduti = 1 in omaggio) resta valida; e ha sentito
quello dei depuratori, che vedrà in settimana. Chiede inoltre se qualcuno
ha trovato il contatto per il Kirby/Folletto. In chiusura, Emilio Caniglia
fissa due punti: sul badge serve doppia identificazione (logo e nome del
comitato, più nome del membro); per l'incontro sponsorizzato Bimby propone
fine mese o metà novembre (dopo Corinaldo) e si rende disponibile a
incontrarsi in settimana anche fuori dalle riunioni ufficiali. Nessuna
menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-06"

CURATED = {
    ("21:33", "Emilio Caniglia"): ("decisione",
        "Chiarisce che sul badge serve una doppia identificazione: devono "
        "essere ben visibili il logo e il nome del comitato (per "
        "identificare il comitato) e il nome del membro."),
    ("21:35", "Emilio Caniglia"): ("proposta",
        "Propone di fare l'incontro sponsorizzato Bimby a fine mese o a "
        "metà novembre, dopo Corinaldo."),
    ("21:37", "Emilio Caniglia"): ("info",
        "Si rende disponibile a incontrarsi in settimana, anche fuori dalle "
        "riunioni ufficiali, per organizzare meglio impegni ed eventi."),
}

AUDIO_CURATED = {
    (DATE, "20:55", "Costantino Mariani", "PTT-20261006-WA0008.opus"): ("domanda",
        "Chiede se ha risposto quello delle castagne (il fornitore per la "
        "castagnata di San Martino)."),
    (DATE, "21:03", "Emanuele Sciarra", "PTT-20261006-WA0011.opus"): ("info",
        "Riferisce di aver sentito la referente Bimby: oggi erano a Pescara "
        "per una riunione sulle nuove offerte; resta valida la promozione (4 "
        "Bimby venduti danno diritto a uno in omaggio), spera si aggiunga "
        "anche qualche gadget; un'altra referente per Bimby e Folletto va "
        "risentita."),
    (DATE, "21:04", "Emanuele Sciarra", "PTT-20261006-WA0012.opus"): ("domanda",
        "Chiede se qualcuno ha trovato il contatto per il Kirby (il "
        "Folletto)."),
    (DATE, "21:05", "Emanuele Sciarra", "PTT-20261006-WA0014.opus"): ("domanda",
        "Dice di aver sentito anche quello dei depuratori, che vedrà questa "
        "settimana di mattina; chiede che data comunicargli."),
    # Vocali scherzosi/rumore legati al gioco della "rotonda" e battute varie.
    (DATE, "20:54", "Emanuele Sciarra", "PTT-20261006-WA0006.opus"): ("rumore", ""),
    (DATE, "20:54", "Costantino Mariani", "PTT-20261006-WA0007.opus"): ("rumore", ""),
    (DATE, "20:56", "Costantino Mariani", "PTT-20261006-WA0009.opus"): ("rumore", ""),
    (DATE, "20:59", "Emanuele Sciarra", "PTT-20261006-WA0010.opus"): ("rumore", ""),
    (DATE, "21:04", "Emanuele Sciarra", "PTT-20261006-WA0013.opus"): ("rumore", ""),
    (DATE, "21:05", "Costantino Mariani", "PTT-20261006-WA0015.opus"): ("rumore", ""),
    (DATE, "21:06", "Costantino Mariani", "PTT-20261006-WA0016.opus"): ("rumore", ""),
    (DATE, "21:06", "Emanuele Sciarra", "PTT-20261006-WA0017.opus"): ("rumore", ""),
    (DATE, "21:16", "Emanuele Sciarra", "PTT-20261006-WA0018.opus"): ("domanda",
        "Chiede se qualcuno si è informato sui badge (nella trascrizione "
        "compare \"beige\", probabile errore di trascrizione per \"badge\")."),
}

MEDIA_OVERRIDES = {}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
