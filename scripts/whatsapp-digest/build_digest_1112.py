#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-12 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:55-12:09 (export Dropbox delle 12:15, giornata ancora in corso
al momento dell'export — mancano due giorni a San Martino, sabato 14/11).
Emilio gira il preventivo della banda di Pescina "I Leoncini d'Abruzzo"
(date confermate da Don Enzo, manca solo Venerdì Santo) per un totale di
8.000€, invitando chi ha altri contatti a proporre preventivi alternativi;
più tardi Vincenzo riferisce la disponibilità della banda di Avezzano per
un confronto. Luca propone di raccogliere foto/video di tutti gli eventi
dell'anno per un video-ricordo finale, idea che Elvis rilancia proponendo
una serata di chiusura ("La Festa prima delle Feste") per proiettarlo;
Maria chiede di cominciare a raccogliere materiale già da San Martino.
Valentina propone di recuperare le "quartieriadi" di un tempo, un evento
per ciascuno dei 4 quartieri del paese. Il gruppo conferma la scritta del
banchetto ("Da Zio Elvis Vin Brulè", con relativa grafica) tra scherzi sul
vestirsi da Babbo Natale, e Alessandra prepara la scenografia (funghi di
cartone). Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-12"

CURATED = {
    ("07:55", "Emilio Caniglia"): ("proposta",
        "Gira il preventivo della banda di Pescina \"I Leoncini "
        "d'Abruzzo\": le date indicate sono già state confermate da Don "
        "Enzo (manca solo Venerdì Santo); chi ha contatti con altre "
        "bande può comunque contattarle o proporle al Comitato per un "
        "preventivo alternativo. Preventivo del Circolo Musicale Banda "
        "\"I Leoncini D'Abruzzo\" (Pescina): domenica 17 gennaio "
        "(Sant'Antonio) 1.000€ per 15/16 elementi; domenica 28 "
        "febbraio (San Gabriele) 1.000€ per 15/16 elementi; 5 e 6 "
        "giugno (feste di Giugno) 1.200€ al giorno per 20/22 elementi; "
        "27, 28 e 29 agosto (feste di Agosto) 1.200€ al giorno per "
        "20/22 elementi — totale 8.000€. Propone di sentirsi al "
        "telefono e incontrarsi appena possibile."),
    ("10:03", "Valentina D'Arcadia"): ("proposta",
        "Ripensando alle quartieriadi degli anni passati, propone di "
        "organizzare un evento per ciascuno dei 4 quartieri del paese, "
        "per coinvolgere ancora di più tutta la cittadinanza."),
    ("10:09", "Emanuele Sciarra"): ("info",
        "Ritiene che si potrebbe fare, ma non è sicuro se per "
        "iniziative di questo tipo serva prima il via libera della Pro "
        "Loco."),
    ("12:09", "Vincenzo Lacasasanta"): ("proposta",
        "Riferisce che domenica mattina la banda di Avezzano è "
        "disponibile a parlare per un preventivo alternativo a quello "
        "dei Leoncini d'Abruzzo, e chiede se qualcuno può "
        "accompagnarlo per intanto sentire cosa propongono."),
}

MEDIA_OVERRIDES = {
    (DATE, "10:46", "Valentina D'Arcadia", "IMG-20261112-WA0013.jpg"):
        "Grafica scelta per il banchetto: \"Da Zio Elvis Vin Brulè\", "
        "scritta su sfondo bordeaux con decorazioni di uva, ulivi e "
        "calici di vino.",
    (DATE, "11:03", "Alessandra Toracchio", "IMG-20261112-WA0012.jpg"):
        "Decorazioni a tema bosco (funghi di cartone e cespugli, ceste "
        "di vimini) caricate in auto, parte della scenografia che sta "
        "preparando.",
}

# Foto-ricordo/scherzo personale (selfie legato alla battuta su Costantino
# e la curia) senza alcun contenuto organizzativo: esclusa come le foto
# ridondanti già scartate in altre giornate.
_SKIP_EXTRA_1112 = {"IMG-20261112-WA0011.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_EXTRA_1112


AUDIO_CURATED = {
    (DATE, "09:28", "Emanuele Sciarra", "PTT-20261112-WA0004.opus"): ("rumore", ""),
    (DATE, "11:47", "Emidio Cerasani", "PTT-20261112-WA0009.opus"): ("rumore", ""),
    (DATE, "11:47", "Emanuele Sciarra", "PTT-20261112-WA0010.opus"): ("rumore", ""),
    (DATE, "12:00", "Luca Cicchelli", "PTT-20261112-WA0014.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {
        "anchor_time": "09:15",
        "anchor_sender": "Luca Cicchelli",
        "type": "proposta",
        "text": (
            "Luca propone di raccogliere foto e video di tutti gli "
            "eventi dell'anno per montare, a fine percorso, un "
            "video-ricordo che ciascuno potrà tenersi; fa notare che "
            "del materiale esiste già (l'infiorata con la classe '86 "
            "dell'anno scorso, la gita a Corinaldo). Antonio chiede "
            "conferma che non sia una battuta; Luca risponde che era "
            "serio. Elvis trova l'idea bella e rilancia: si potrebbe "
            "proiettare il video in una serata di chiusura dedicata a "
            "ringraziare tutti per l'anno appena trascorso, con "
            "intrattenimento e atmosfera, da studiare se tutti sono "
            "d'accordo. Luca cita come precedente la festa di fine "
            "estate con cui la classe 1986 aveva concluso il proprio "
            "percorso, proponendo di fare qualcosa di simile per "
            "chiudere."
        ),
        "members": [
            "PTT-20261112-WA0000.opus", "PTT-20261112-WA0001.opus",
            "PTT-20261112-WA0002.opus", "PTT-20261112-WA0003.opus",
            "PTT-20261112-WA0005.opus", "PTT-20261112-WA0006.opus",
        ],
    },
    {
        "anchor_time": "10:30",
        "anchor_sender": "Alessandra Toracchio",
        "type": "decisione",
        "text": (
            "Alessandra propone di scrivere sul banchetto \"VIN BRULÈ "
            "DI ZIO ELVIS\"; il gruppo approva tra le risate (Emanuele "
            "la trova simpatica, Elvis è d'accordo e scherza sul "
            "vestirsi da Babbo Natale con dei sacchi di iuta, di cui "
            "Barbara ha la disponibilità). Emanuele fa sapere di non "
            "avere una barba da Babbo Natale — verificherà a casa nel "
            "pomeriggio — e chiede se si siano trovate le due balle di "
            "paglia o se restino solo i rotoloni; Alessandra conferma "
            "che si sta procurando qualcosa anche per quello. Valentina "
            "condivide poi la grafica della scritta, che il gruppo "
            "conferma come versione definitiva (Alessandra: "
            "\"decidetevi prima che inizio la scritta\"; Maria ed "
            "Elvis: \"questa è la migliore\"; Alessandra: \"andata\"). "
            "Emanuele chiede infine di fare qualche foto del risultato, "
            "da allegare a quelle dell'allestimento di sabato per "
            "risparmiare un reel a parte."
        ),
        "members": ["PTT-20261112-WA0007.opus", "PTT-20261112-WA0008.opus"],
    },
]

TEXT_MERGES = [
    {
        "anchor_time": "09:27",
        "anchor_sender": "Maria Buttari",
        "type": "proposta",
        "text": (
            "Sulla stessa idea, Maria chiede di raccogliere già da San "
            "Martino qualche foto in più per il video di Chiara; Elvis "
            "propone di chiamare la serata di proiezione \"La Festa "
            "prima delle Feste\"."
        ),
        "members": [["09:27", "Maria Buttari"], ["09:31", "Elvis Ippoliti"]],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="foto personale senza contenuto organizzativo")
