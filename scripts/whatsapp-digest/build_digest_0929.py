#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-29 — solo dati di curatela, logica comune in digest_lib.py.

Giornata del secondo incontro sponsorizzato (materassi, sala consiliare
del Comune, 20:15/20:30). Mattina: Tina Giarrante chiede se deve portare
qualcosa, Antonio Sabatini precisa (porta quello che ha, le rimanenze le
tiene lui, si deposita tutto in sede) e rimanda un aggiornamento al
pomeriggio; Valentina D'Arcadia, che stacca tardi dal lavoro, si offre di
far portare qualcosa dalla madre se serve. Dante Caniglia chiede se col
la Pro Loco si è organizzato qualcosa per Halloween/San Martino (nessuna
risposta in questa finestra): la domanda apre uno scambio nostalgico con
foto di passate feste in maschera del gruppo e di una gara "cuccagna" di
13 anni fa, tutto rumore a parte le foto stesse. Costantino Mariani
conferma la sua coppia con Marina. Nel pomeriggio: Emilio Caniglia ricorda
l'orario della serata (20:15/20:30) e la regola "porta & riporta" per il
buffet, annunciando che si valuterà se fare una riunione il 2 o il 3
ottobre per organizzare il prossimo evento sponsorizzato, la visita a
Corinaldo e le pagine social; Antonio Aceto segnala che Gino e Roberta
hanno dato buca all'ultimo e cerca un'altra coppia; Maikel Montano avvisa
che arriverà dopo le 21; Elvis Ippoliti chiede se manca altro per il
buffet e Antonio Sabatini elenca cosa c'è (crostata, ferrarelle, dolci
secchi, torta salata, patatine, bibite varie), con una foto di Antonio
Aceto della crostata appena sfornata. Due vocali di Emanuele Sciarra
(17:48) hanno una trascrizione incomprensibile (probabile audio di scarsa
qualità o scherzoso): scartati come rumore.

Coda pomeriggio/sera (18:20-20:10, aggiornata con l'export delle 20:14 del
29/9, che estende il giorno oltre le 17:58): Tina Giarrante chiede se
servono tovaglioli, vassoi per le patatine e un coltello, Antonio Sabatini
conferma di avere già tutto. Emilio Caniglia (19:37) posta una foto della
sala consiliare in allestimento per la serata. Emanuele Sciarra (19:42)
comunica che domani pomeriggio sentirà la promoter del Bimby e aggiornerà
il gruppo. Resto rumore (conferme di ritardo, battute).

Coda notturna (23:09-23:37, aggiornata con l'export delle 20:42 del 30/9):
a serata conclusa, il gruppo commenta l'esito: raggiunte 23 coppie (una in
meno delle 24 richieste), ma il rappresentante (Bonifacio) ha comunque
staccato l'assegno da 600€ senza fare questioni sulla coppia mancante;
venduto anche un materasso, che dovrebbe valere 100€ in più da confermare
alla consegna del prodotto — Emanuele Sciarra sentirà Bonifacio l'indomani
e aggiornerà. Antonio Aceto (23:37), scusandosi per essere andato via
presto, chiede a Emilio Caniglia se per la prossima riunione si può fare un
sondaggio (risposta il giorno dopo). Resto rumore (battute su orari di
lavoro e sveglie). Nessuna menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-29"

CURATED = {
    ("08:44", "Tina Giarrante"): ("domanda",
        "Chiede ad Antonio Sabatini se non deve portare niente lei per "
        "la serata."),
    ("08:47", "Antonio Sabatini"): ("info",
        "Risponde a Tina Giarrante di portare quello che ha; le "
        "rimanenze le tiene lui e poi si deposita tutto in sede. "
        "Aggiorneranno più tardi in giornata."),
    ("08:51", "Valentina D'Arcadia"): ("info",
        "Comunica che staccherà tardi dal lavoro; se deve portare "
        "qualcosa per il buffet, manderà sua madre."),
    ("09:37", "Dante Caniglia"): ("domanda",
        "Chiede se con la Pro Loco si è organizzato qualcosa per "
        "Halloween e San Martino."),
    ("14:05", "Elvis Ippoliti"): ("domanda",
        "Chiede a che ora bisogna vedersi questa sera."),
    ("14:29", "Costantino Mariani"): ("info",
        "Conferma la propria coppia con Marina."),
    ("16:23", "Emilio Caniglia"): ("info",
        "Ricorda l'incontro sponsorizzato di questa sera alle 20:15/20:30 "
        "presso la sala consiliare del Comune (orario e data imposti "
        "dall'azienda); per il buffet vale la formula \"porta & riporta\" "
        "(chi porta qualcosa si impegna a riportare gli avanzi, per "
        "agevolare la pulizia della sala). Questa sera, in base alla "
        "disponibilità della sede, si valuterà se organizzare una "
        "riunione venerdì 2 o sabato 3 ottobre, per il prossimo evento "
        "sponsorizzato, la visita a Corinaldo, le pagine social e altro."),
    ("17:04", "Antonio Aceto"): ("info",
        "Comunica che una coppia (Gino e Roberta) ha dato buca "
        "all'ultimo momento; cercherà di trovarne un'altra al loro "
        "posto."),
    ("17:46", "Maikel Montano"): ("info",
        "Avvisa che non arriverà prima delle 21."),
    ("17:48", "Elvis Ippoliti"): ("domanda",
        "Chiede se c'è qualcos'altro da portare per il buffet."),
    ("17:54", "Antonio Sabatini"): ("info",
        "Risponde a Elvis Ippoliti elencando cosa è già coperto per il "
        "buffet: crostata, ferrarelle, dolci secchi, torta salata, "
        "patatine, bibite varie."),
    ("18:20", "Tina Giarrante"): ("domanda",
        "Chiede se servono tovaglioli e vassoi per le patatine, e chiede a "
        "qualcuno di portare un coltello; Antonio Sabatini conferma di "
        "avere già tutto."),
    ("19:42", "Emanuele Sciarra"): ("info",
        "Comunica che domani pomeriggio sentirà la promoter del Bimby e "
        "aggiornerà il gruppo."),
    ("23:09", "Emanuele Sciarra"): ("info",
        "A serata conclusa, il gruppo fa il punto: raggiunte 23 coppie "
        "(una in meno delle 24 richieste), ma il rappresentante (Bonifacio) "
        "ha comunque staccato l'assegno da 600€ senza fare questioni sulla "
        "coppia mancante; venduto anche un materasso, che dovrebbe valere "
        "100€ in più da confermare alla consegna del prodotto. Emanuele "
        "sentirà Bonifacio l'indomani e aggiornerà il gruppo."),
    ("23:37", "Antonio Aceto"): ("domanda",
        "Scusandosi per essere andato via presto dalla serata, chiede a "
        "Emilio Caniglia se per la prossima riunione si può fare un "
        "sondaggio (Emilio risponderà di sì il giorno dopo)."),
}

AUDIO_CURATED = {
    (DATE, "17:48", "Emanuele Sciarra", "PTT-20260929-WA0009.opus"): ("rumore", ""),
    (DATE, "17:48", "Emanuele Sciarra", "PTT-20260929-WA0010.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {
    (DATE, "09:38", "Dante Caniglia", "IMG-20260929-WA0003.jpg"):
        "Foto di gruppo da una passata festa in maschera per Halloween "
        "del comitato: quattro persone in costume (un fantasma, un "
        "pirata, un volto dipinto metà bianco e metà rosso, un uomo con "
        "bombetta e bretelle) con bicchieri in mano.",
    (DATE, "09:38", "Elvis Ippoliti", "IMG-20260929-WA0002.jpg"):
        "Foto di due persone truccate da Halloween (volti dipinti di "
        "bianco e nero) con bicchieri in mano, dietro un bancone bar.",
    (DATE, "10:14", "Dante Caniglia", "IMG-20260929-WA0001.jpg"):
        "Screenshot di un post Facebook del 2013 con una foto notturna di "
        "una gara di \"cuccagna\" (mangiare un piatto di pasta su un "
        "tavolo senza usare le mani) durante una festa di paese, con "
        "persone in maglietta del comitato intorno al tavolo.",
    (DATE, "17:55", "Antonio Aceto", "IMG-20260929-WA0011.jpg"):
        "Foto di una crostata con marmellata appena sfornata, per il "
        "buffet della serata.",
    (DATE, "19:37", "Emilio Caniglia", "IMG-20260929-WA0012.jpg"):
        "Foto della sala consiliare in allestimento per la serata: sul "
        "tavolo la valigetta di Imperial-life, sullo sfondo gli stendardi "
        "del Comune di San Benedetto dei Marsi e un crocifisso.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
