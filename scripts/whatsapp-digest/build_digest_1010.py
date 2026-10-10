#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-10 — solo dati di curatela, logica comune in digest_lib.py.

Mattina (07:56-08:41): è il compleanno di Dante Caniglia, il gruppo si
scambia auguri in chat (nessun contenuto organizzativo, un solo punto di
sintesi). Prosegue poi tutto il giorno (fino a 14:14) una seconda ondata di
auguri, stavolta in ritardo per Vincenzo Lacasasanta (compleanno ieri,
9/10): anche qui un solo punto di sintesi, all'orario del primo messaggio
che se ne accorge. Tra chi fa gli auguri c'è anche Giovanni Lima (13:04):
è lui stesso a scrivere, non una menzione da parte di altri.

A metà mattina (11:29-14:23) prosegue il thread sul "girafusto" per
arrostire le castagne: Barbara chiede se prenderlo subito o aspettare,
Emanuele (vocale) ed Elvis consigliano di procurarlo comunque per mettersi
al sicuro, Barbara conferma che proverà oggi o a novembre.

Dalle 13:25 lungo dibattito sulla locandina della gita a Corinaldo,
realizzata da Chiara Gargano: Emanuele la presenta (screenshot) e invita a
condividerla; si segnala e corregge un refuso ("accoglimento" →
"accoglienza", due versioni successive di Alessandra Toracchio); si discute
se il logo del comitato debba comparire, dato che il comitato non è ancora
costituito giuridicamente e la gita è organizzata "come classe 87" (Elvis
contrario al logo, Chiara a favore ma non protagonista, Luca propone lo
sfondo giallo — poi effettivamente aggiunto nella versione finale); Elvis
ricorda anche l'importanza di affidarsi a un professionista per la stampa.
Chiara condivide anche il nuovo profilo Instagram della classe 87.
Nessuna menzione di Giovanni Lima da parte di altri in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-10"

CURATED = {
    ("07:56", "Luca Cicchelli"): ("info",
        "Oggi è il compleanno di Dante Caniglia, il gruppo si scambia "
        "auguri in chat."),
    ("10:00", "Costantino Mariani"): ("info",
        "Il gruppo si accorge che ieri (9 ottobre) era il compleanno di "
        "Vincenzo Lacasasanta: si scambiano auguri in ritardo in chat."),
    ("11:29", "Barbara Rizio"): ("domanda",
        "Chiede se deve procurarsi subito l'attrezzo per cuocere le "
        "castagne (il \"girafusto\"), aspettare i primi di novembre, o se "
        "non serve perché se ne occupa il comitato."),
    ("11:36", "Luca Cicchelli"): ("info",
        "Luca ed Elvis concordano con Emanuele: meglio farselo prestare/"
        "procurarselo subito, per mettersi al sicuro."),
    ("13:14", "Barbara Rizio"): ("info",
        "Conferma: proverà a prenderlo oggi, altrimenti a novembre."),
    ("13:26", "Alessandra Simonetti"): ("info",
        "Alessandra Simonetti e poi Alessandra Toracchio notano un refuso "
        "nella locandina (\"accoglimento\" invece di \"accoglienza\")."),
    ("13:36", "Dante Caniglia"): ("info",
        "Fa notare scherzosamente che il logo sulla locandina non è "
        "quello giusto del comitato, aprendo la discussione sul logo."),
    ("14:03", "Luca Cicchelli"): ("proposta",
        "Propone di mettere uno sfondo giallo sulla locandina, essendo il "
        "colore ufficiale del comitato."),
    ("14:08", "Elvis Ippoliti"): ("proposta",
        "Ricorda che la locandina va anche stampata, quindi meglio "
        "affidarsi a un professionista del mestiere piuttosto che a "
        "strumenti di intelligenza artificiale (che in stampa rendono "
        "male); ricorda inoltre che il logo è del comitato, mentre la "
        "gita viene organizzata dalla classe 87."),
    ("14:20", "Costantino Mariani"): ("proposta",
        "Propone di esporre la locandina anche nella sede."),
    ("14:23", "Chiara Gargano"): ("info",
        "Segnala il nuovo profilo Instagram da seguire della classe 87: "
        "https://www.instagram.com/class_e1987?rpxt=OHdxa3hkZWEyeW5l"),
    ("14:23", "Elvis Ippoliti"): ("proposta",
        "Propone di organizzare anche un pranzo tutti insieme per la "
        "classe."),
    ("14:24", "Cesare Raglione"): ("proposta",
        "Conferma: le locandine vanno esposte il prima possibile."),
    ("14:41", "Alessandra Toracchio"): ("proposta",
        "Essendo un'iniziativa di classe, propone di togliere anche il "
        "logo del comitato e scrivere semplicemente \"la classe 87 "
        "organizza...\"."),
    ("14:47", "Alessandra Toracchio"): ("info",
        "Fa notare che la locandina è già stata pubblicata con gli "
        "errori non ancora corretti."),
    ("14:50", "Chiara Gargano"): ("proposta",
        "Risponde che il logo deve restare (non da protagonista, ma "
        "comunque marchiata): l'attività è organizzata dalla classe, ma "
        "il comitato ne è la parte attiva."),
    ("14:54", "Elvis Ippoliti"): ("info",
        "Ribadisce che il logo identifica il comitato, non ancora "
        "costituito, mentre nei fatti si sta operando come classe; "
        "accetta comunque la decisione presa (\"ormai è fatta\")."),
}

AUDIO_CURATED = {
    (DATE, "11:30", "Emanuele Sciarra", "PTT-20261010-WA0004.opus"): ("info",
        "Risponde a Barbara: può prenderlo oggi o ai primi di novembre, è "
        "indifferente; lui nel frattempo si sta muovendo per farsene "
        "costruire uno, tenendone due a disposizione."),
    (DATE, "14:15", "Elvis Ippoliti", "PTT-20261010-WA0009.opus"): ("proposta",
        "Ribadisce che il logo non andrebbe messo sulla locandina, visto "
        "che si sta lavorando come classe 87: propone di scrivere invece "
        "\"la classe 87, in collaborazione con il parroco Don Enzo, "
        "organizza la gita a Corinaldo\"."),
    (DATE, "14:47", "Elvis Ippoliti", "PTT-20261010-WA0010.opus"): ("info",
        "Chiarisce di non avercela con nessuno: per eventuali modifiche "
        "alla locandina meglio chiederle direttamente a Chiara, che l'ha "
        "realizzata, così non esce male in stampa. Ribadisce che "
        "l'iniziativa è della classe, non del comitato, quindi a suo "
        "parere andrebbe tolto anche il logo."),
}

MEDIA_OVERRIDES = {
    (DATE, "13:25", "Emanuele Sciarra", "IMG-20261010-WA0005.jpg"):
        "Locandina della gita a Corinaldo realizzata da Chiara Gargano, "
        "prima versione: domenica 8 novembre 2026, partenza alle 6:30 da "
        "Piazza Risorgimento (San Benedetto dei Marsi), arrivo alle "
        "10:00, Santa Messa nel Santuario alle 11:15, pranzo al sacco "
        "alle 13:00 presso il centro di accoglienza (con primo piatto "
        "caldo offerto dal Santuario — nella locandina c'è un refuso, "
        "\"accogliimento\"), pellegrinaggio a piedi al Santuario alle "
        "16:00 e partenza per il ritorno alle 18:00; quota di "
        "partecipazione 30€, contatti per prenotazioni Alessandro, "
        "Antonio e Serena. Emanuele invita a condividerla sui social e "
        "negli stati WhatsApp.",
    (DATE, "13:56", "Alessandra Toracchio", "IMG-20261010-WA0007.jpg"):
        "Seconda versione della locandina: stesso contenuto, refuso "
        "corretto in \"accoglienza\" e logo del comitato ingrandito.",
    (DATE, "13:57", "Alessandra Toracchio", "IMG-20261010-WA0008.jpg"):
        "Terza versione della locandina: come la precedente, con in più "
        "uno sfondo giallo (colore ufficiale del comitato) dietro il "
        "logo.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
