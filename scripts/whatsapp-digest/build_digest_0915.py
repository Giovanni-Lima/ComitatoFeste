#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-15 — solo dati di curatela, logica comune in digest_lib.py.

Prima giornata curata con la trascrizione anticipata dei vocali
(transcribe_new.py, vedi CLAUDE.md): tutti i vocali di questa finestra sono
già classificati in AUDIO_CURATED, letti col contesto della trascrizione.

Finestra breve (22:58 del 14/9 - 10:07), dominata dal mattino: dopo i saluti
di rito (rumore), Ugo Trinchini (07:28) ed Emanuele Sciarra (08:06) chiedono
ad Alessandra Toracchio di aggiungere due nuove coppie alla lista per
l'incontro sponsorizzato del 18/9; Emilio Caniglia condivide (08:55) la foto
aggiornata della lista (16/20 coppie) e Emanuele conferma a voce (08:59) che
restano 4 coppie da trovare. Segue un thread sul materasso-sponsor Sanimed
Italia: Ugo chiede il nome dell'azienda (09:37), Emilio risponde con nome e
link Facebook (10:01-10:02), Emanuele conferma a Ugo il suo turno di visita
(10:04); Ugo segnala che la coppia che aveva disponibile è "bruciata" perché
ha comprato lui stesso un materasso altrove (10:05), Emanuele lo rassicura
che va bene lo stesso, è già capitato in passato (10:07). In mezzo, Emanuele
propone (10:06, vocale lungo) un raduno di macchine d'epoca a San Benedetto,
da organizzare col fidanzato di Alessandra (che si occupa di veicoli
d'epoca) anche in ricordo di Mattia, appassionato di camion; data ipotizzata
in prossimità di Santa Maria Goretti per il maggior afflusso di pubblico.
Uno screenshot di un evento quiz esterno ("Dr Why" allo Stammtisch Tavern,
Chieti) condiviso da Costantino con un commento di Emanuele resta rumore:
non riguarda il comitato. Nessuna menzione di Giovanni Lima in questa
finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-15"

CURATED = {
    ("07:28", "Ugo Trinchini"): ("info",
        "Chiede ad Alessandra Toracchio di aggiungere alla lista coppie per "
        "l'incontro del 18/9 anche Giovanni (istruttore) e Martina."),
    ("08:06", "Emanuele Sciarra"): ("info",
        "Chiede ad Alessandra Toracchio di aggiungere alla lista coppie anche "
        "il suocero Massimo e la moglie Eugenia; prova a portare oggi stesso "
        "anche i cognati, se riesce."),
    ("10:01", "Emilio Caniglia"): ("info",
        "Risponde a Ugo Trinchini che l'azienda di materassi si chiama "
        "Sanimed Italia, condividendo anche un link Facebook: "
        "https://www.facebook.com/share/1Dif7i9wtn/"),
}

AUDIO_CURATED = {
    (DATE, "08:59", "Emanuele Sciarra", "PTT-20260915-WA0003.opus"): ("info",
        "Comunica che restano da trovare quattro coppie per completare la "
        "lista del 18/9; farà sapere più tardi se riesce a rimediare."),
    (DATE, "09:37", "Ugo Trinchini", "PTT-20260915-WA0005.opus"): ("domanda",
        "Chiede conferma del nome della società di materassi (risponde poi "
        "Emilio Caniglia)."),
    (DATE, "10:04", "Emanuele Sciarra", "PTT-20260915-WA0006.opus"): ("info",
        "Conferma a Ugo Trinchini che il presidente lo ha già informato — "
        "era in riunione con Attilio — e che tocca proprio al turno di Ugo "
        "per la visita al materassaio."),
    (DATE, "10:05", "Ugo Trinchini", "PTT-20260915-WA0007.opus"): ("info",
        "Comunica che la coppia che aveva disponibile per la visita al "
        "materassaio è ormai \"bruciata\": ha acquistato lui stesso un "
        "materasso altrove, quindi non la propone."),
    (DATE, "10:06", "Emanuele Sciarra", "PTT-20260915-WA0008.opus"): ("proposta",
        "Propone di organizzare un raduno di macchine d'epoca a San "
        "Benedetto, da concordare col fidanzato di Alessandra Toracchio "
        "(che si occupa di veicoli d'epoca) — anche in ricordo di Mattia, "
        "appassionato di camion — con data ipotizzata in prossimità di "
        "Santa Maria Goretti per il maggior afflusso di pubblico; chiede il "
        "parere del gruppo."),
    (DATE, "10:07", "Emanuele Sciarra", "PTT-20260915-WA0009.opus"): ("info",
        "Rassicura Ugo Trinchini: i rappresentanti che seguono le coppie "
        "cambiano di volta in volta, quindi va bene lo stesso se qualcuno ha "
        "già acquistato — è già capitato l'anno scorso alla manifestazione "
        "materassi ed è anzi un incoraggiamento per gli altri clienti "
        "presenti."),
}

MEDIA_OVERRIDES = {
    (DATE, "08:55", "Emilio Caniglia", "IMG-20260915-WA0004.jpg"):
        "Foto aggiornata del foglio \"COPPIE\" per l'incontro del 18/9: 16 "
        "coppie compilate su 20 posti (nuove rispetto alla versione del "
        "14/9): Elvis-Federica, Raffaele-Verdiana, Ugo-Tina, Cesare-"
        "Alessandra S., Emanuele-Liberata, Maikel-Lucianny, Roberto-Dalila, "
        "Cesare-Costance, Antonio S.-Alessandra T., Silvano-Barbara, "
        "Vincenzo-Lara, Emilio-Antonella, Daniele-Jessica, Giovanni-Martina, "
        "Massimo-Eugenia, Donato-Onorina.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
