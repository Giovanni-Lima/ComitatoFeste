#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-07 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 09:31-23:42 (export Dropbox delle 9:01 del 9/11). Elvis chiede dei
termos per il vin brulé di San Martino. Emanuele propone una gita a Napoli
(preventivo pullman, data 29/11, conti su costo/guadagno), con adesione di
massima di Ilenia e Maria. Vincenzo riceve da Attilio un listino prezzi per
le calze della Befana (100+ foto, inviate in privato per non intasare il
gruppo). Ilenia chiede se si è già parlato con "Amanda" (domanda rimasta
senza risposta in questa finestra). In serata il gruppo si ritrova da
Gianvito al "Ragno" per un aperitivo informale. Emilio anticipa la
logistica del pranzo al sacco per la gita di Corinaldo di domani e
promette un resoconto della riunione di ieri sera. Antonio Sabatini
condivide le ricevute di acconto e saldo pagati a Bianchi Tour per la gita.
Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-07"

CURATED = {
    ("09:50", "Elvis Ippoliti"): ("proposta",
        "Chiede a Emilio di procurare anche dei termos per il vin "
        "brulé di San Martino, così da poterlo servire più comodamente "
        "al bicchiere."),
    ("12:57", "Emanuele Sciarra"): ("proposta",
        "Riferisce di aver ottenuto un preventivo per un'eventuale gita "
        "a Napoli: 1200-1300€ per un pullman da 54 posti, 1400-1500€ "
        "per uno da 64; chiede al gruppo se è d'accordo a organizzarla, "
        "proponendo come data domenica 29 novembre per evitare "
        "l'affluenza dei mercatini di Natale nel periodo più a ridosso "
        "delle feste. Spiega che il comitato guadagnerebbe 6-8€ a "
        "persona (400-500€ totali secondo il pullman scelto) più 100€ "
        "di lotteria, per un prezzo finale di circa 30€ a persona "
        "(22-24€ di costo base). Ilenia si dice d'accordo, e Maria "
        "apprezza l'idea soprattutto per i mercatini di Natale."),
    ("13:22", "Vincenzo Lacasasanta"): ("info",
        "Comunica di aver ricevuto da Attilio il listino prezzi di "
        "molti prodotti da mettere nelle calze della Befana; trattandosi "
        "di oltre 100 foto, per non intasare il gruppo le invierà in "
        "privato a chi mette \"mi piace\" al suo messaggio."),
    ("14:00", "Ilenia Piccozzi"): ("domanda",
        "Chiede se nel frattempo si è andati a parlare con Amanda "
        "(nessuna risposta in questa finestra)."),
    ("17:48", "Ugo Trinchini"): ("info",
        "Il gruppo si organizza per un ritrovo informale in serata da "
        "Gianvito, al \"Ragno\": Ugo avvisa che Gianvito va via verso le "
        "19 e invita ad arrivare prima di quell'ora. Emanuele, Serena ed "
        "Emilio si organizzano sugli orari d'arrivo (tra le 18 e le "
        "18:20); Ugo è già sul posto ed Emanuele, in lieve ritardo, "
        "conferma che sta arrivando."),
    ("21:19", "Emilio Caniglia"): ("info",
        "Per la gita di domani a Corinaldo, ricorda che il pranzo sarà "
        "al sacco: la Comunità di Corinaldo offrirà solo un primo "
        "caldo, quindi consiglia di portare panini, frutta e snack, "
        "data la partenza al primo mattino e il rientro in tarda "
        "serata. Promette per domani mattina una sintesi della riunione "
        "di ieri sera e i recenti sviluppi su Capodanno."),
    ("21:34", "Antonio Sabatini"): ("info",
        "Condivide, per chiarezza, le ricevute dei bonifici di acconto "
        "(400€, 2/11) e saldo (850€, 7/11) versati a Bianchi Tour per "
        "la gita/pellegrinaggio a Corinaldo della classe 1987."),
}

MEDIA_OVERRIDES = {
    (DATE, "17:46", "Ugo Trinchini", "IMG-20261107-WA0004.jpg"):
        "Foto di una birra Heineken sul bancone del bar \"Il Ragno\", "
        "durante il ritrovo informale della sera.",
    (DATE, "21:32", "Antonio Sabatini", "DOC-20261102-WA0006.pdf"):
        "Ricevuta del bonifico SEPA di 400€ (2/11/2026) versato da "
        "Antonio Sabatini a BT Vacanze Srl, causale \"Acconto "
        "pellegrinaggio Corinaldo classe 1987 San Benedetto dei Marsi\".",
    (DATE, "21:32", "Antonio Sabatini", "DOC-20261107-WA0002.pdf"):
        "Ricevuta del bonifico SEPA di 850€ (7/11/2026) versato da "
        "Antonio Sabatini a BT Vacanze Srl, causale \"Saldo gita "
        "Corinaldo classe 1987 San Benedetto dei Marsi\".",
}

AUDIO_CURATED = {
    (DATE, "17:44", "Emanuele Sciarra", "PTT-20261107-WA0003.opus"): ("info",
        "Risponde scherzosamente a chi è rimasto a bere, dicendo che "
        "arriverà con qualche minuto di ritardo."),
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
