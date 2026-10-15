#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-14 — solo dati di curatela, logica comune in digest_lib.py.

Mattina: ultima adesione per il 16 ottobre (Antonella+Andrea), poi due
thread paralleli (TEXT_MERGES). Il primo sul buffet dell'incontro del 16:
Antonio Sabatini chiede chi si offre di portare qualcosa e incarica Elvis
di controllare le scorte in sede; Ilenia manda un dolce pur non essendo
presente, Barbara si offre per il salato. Il secondo sulla locandina della
gita a Corinaldo: Barbara chiede conferma che sia la versione definitiva,
Antonio e Alessandra Toracchio confermano (con Chiara pronta a correggere
se la stampa di prova non convince).

Pomeriggio: Emilio condivide la locandina di un evento esterno (Pro Loco),
"Marruvium & Pescina", sabato 17 ottobre a Pescina e San Benedetto dei
Marsi — non un'iniziativa del comitato, solo un'informazione condivisa al
gruppo. Ripete poi il promemoria dell'incontro sponsorizzato del 16
ottobre (servono 20 coppie); arrivano altre adesioni/assenze sparse
(TEXT_MERGES). Barbara mostra le locandine di Corinaldo stampate e chiede
se può affiggerle in giro per il paese; Elvis fotografa le scorte già
presenti in sede (acqua, bibite, bicchieri, tovaglioli, qualche snack) e
conferma a voce che serve procurare solo qualcosa da mangiare. Nessuna
menzione di Giovanni Lima da parte di altri in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-14"

CURATED = {
    ("08:14", "Antonella Profeta"): ("info",
        "Comunica che per il 16 ottobre ci saranno anche lei e Andrea."),
    ("15:56", "Emilio Caniglia"): ("info",
        "Ricorda l'incontro sponsorizzato del 16 ottobre (circa un'ora, "
        "nel dopocena): chi è disponibile può scriverlo in chat, serve "
        "raggiungere 20 coppie."),
}

AUDIO_CURATED = {
    (DATE, "18:42", "Elvis Ippoliti", "PTT-20261014-WA0013.opus"): ("info",
        "Conferma (con foto di supporto) che in sede ci sono già "
        "tovaglioli, bicchieri e bevande a sufficienza (quattro bottiglie "
        "più due casse d'acqua): serve procurare solo qualcosa da "
        "mangiare per il buffet."),
    (DATE, "21:42", "Emanuele Sciarra", "PTT-20261014-WA0014.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {
    (DATE, "15:51", "Emilio Caniglia", "IMG-20261014-WA0004.jpg"):
        "Locandina di \"Marruvium & Pescina\", visita guidata organizzata "
        "dalla Pro Loco e altri enti per sabato 17 ottobre 2026 (Pescina "
        "ore 15:00, San Benedetto dei Marsi ore 18:00, contributo "
        "consigliato 5€, posti limitati e prenotazione obbligatoria) — un "
        "evento esterno, non del comitato, condiviso da Emilio come "
        "informazione utile.",
    (DATE, "18:06", "Barbara Rizio", "IMG-20261014-WA0006.jpg"):
        "Foto delle locandine della gita a Corinaldo appena stampate da "
        "Barbara, che chiede se può affiggerle in giro per il paese; "
        "Emanuele la incoraggia entusiasticamente a \"tappezzare\" San "
        "Benedetto.",
    (DATE, "18:38", "Elvis Ippoliti", "IMG-20261014-WA0009.jpg"):
        "Foto delle scorte in sede per il buffet del 16: una bottiglia "
        "d'acqua e una confezione di bicchieri di plastica.",
    (DATE, "18:38", "Elvis Ippoliti", "IMG-20261014-WA0010.jpg"):
        "Foto delle scorte in sede: un sacchetto di tovaglioli/salviette "
        "e una confezione di biscotti.",
    (DATE, "18:38", "Elvis Ippoliti", "IMG-20261014-WA0011.jpg"):
        "Foto delle scorte in sede: due casse d'acqua in bottiglia.",
    (DATE, "18:39", "Elvis Ippoliti", "IMG-20261014-WA0007.jpg"):
        "Foto delle scorte in sede: bottiglie di bibite (Fanta, Pepsi e "
        "altre) in un sacchetto.",
    (DATE, "18:39", "Elvis Ippoliti", "IMG-20261014-WA0012.jpg"):
        "Foto delle scorte in sede: patatine, piatti di carta e una "
        "confezione di biscotti.",
    (DATE, "18:39", "Elvis Ippoliti", "IMG-20261014-WA0008.jpg"):
        "Foto delle scorte in sede: una confezione di biscotti Grisbì e "
        "patatine al paprika.",
}

TEXT_MERGES = [
    {
        "anchor_time": "10:15",
        "anchor_sender": "Antonio Sabatini",
        "type": "domanda",
        "text": (
            "Antonio chiede chi si offre di fare/portare qualcosa per il "
            "buffet dell'incontro del 16, per organizzarsi, e incarica "
            "Elvis di controllare in sede le rimanenze di bevande, "
            "bicchieri e tovaglioli. Elvis conferma che passerà in "
            "serata. Ilenia non potrà esserci ma manda un dolce; Barbara "
            "si offre di rifare qualcosa di salato."
        ),
        "members": [
            ["10:15", "Antonio Sabatini"], ["10:17", "Elvis Ippoliti"],
            ["10:30", "Ilenia Piccozzi"], ["11:25", "Barbara Rizio"],
            ["11:40", "Antonio Sabatini"],
        ],
    },
    {
        "anchor_time": "11:28",
        "anchor_sender": "Barbara Rizio",
        "type": "info",
        "text": (
            "Barbara chiede conferma se la locandina della gita a "
            "Corinaldo è ormai la versione definitiva, prima di "
            "stamparla; Antonio conferma. Alessandra Toracchio dà il via "
            "libera a una prova di stampa, segnalando che altrimenti sarà "
            "Chiara a correggerla."
        ),
        "members": [
            ["11:28", "Barbara Rizio"], ["12:33", "Emanuele Sciarra"],
            ["13:05", "Barbara Rizio"], ["13:12", "Alessandra Toracchio"],
        ],
    },
    {
        "anchor_time": "16:09",
        "anchor_sender": "Luca Cicchelli",
        "type": "info",
        "text": (
            "Altre adesioni/assenze per il 16 ottobre: Luca con Claudia, "
            "Costantino assente, Ugo segnala che si può aggiungere Annesa "
            "in coppia con Saba. Alessandro chiede anche lui cosa portare "
            "per il buffet, per organizzarsi."
        ),
        "members": [
            ["16:09", "Luca Cicchelli"], ["16:12", "Alessandro Di Benedetto"],
            ["19:01", "Costantino Mariani"], ["20:45", "Ugo Trinchini"],
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES)
