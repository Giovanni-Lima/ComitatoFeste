#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-05 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 12:44-15:40 (export Dropbox delle 15:59 di oggi). Emanuele conferma
che le castagne per San Martino stanno asciugando e saranno pronte la
settimana prossima (foto). Propone poi di far rivivere la vecchia
tradizione dei barattolini di latta attaccati alle biciclette dei
bambini (Cesare conferma la fattibilità). Ilenia ed Elvis portano
concretezza alla discussione sulle calze della Befana aperta ieri da
Emanuele: foto di esempio, un modello trovato su unigadget.it e un
confronto sui prezzi in base alla quantità. Costantino interviene sulla
discussione Capodanno con una proposta di mediazione (chi non partecipa
aiuta con la pubblicità, chi festeggia di solito altrove fa un piccolo
sacrificio), trovando consenso. Emanuele si informa sui costi dei
tagliandini/cartelle della tombola. Infine logistica sui pagamenti della
gita a Corinaldo. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-05"

CURATED = {
    ("13:50", "Costantino Mariani"): ("proposta",
        "Riallacciandosi alla discussione sul Capodanno, concorda sul "
        "peso economico per le famiglie ma propone che chi non "
        "partecipa al veglione possa comunque aiutare a pubblicizzare "
        "l'evento per portare gente, e che chi di solito festeggia "
        "fuori casa provi comunque a fare un piccolo sacrificio per "
        "stare insieme al comitato quella sera. Ugo ed Elvis si dicono "
        "d'accordo."),
    ("15:23", "Maria Buttari"): ("info",
        "Chiede a chi versare i soldi per la gita a Corinaldo; Antonio "
        "Sabatini risponde che può darli a lui, precisando che non è "
        "urgente (va bene anche il giorno dopo in riunione) e che il "
        "pullman Bianchi Tour è già stato pagato. Confermano insieme 3 "
        "posti: Maria, il marito Cesidio e il figlio Gabriele."),
}

AUDIO_CURATED = {
    (DATE, "14:55", "Emanuele Sciarra", "PTT-20261105-WA0015.opus"): ("info",
        "Riferisce di aver chiesto alla moglie dove sono stati fatti i "
        "tagliandini e le cartelle della tombola e quanto sono "
        "costati: la grafica è di Alessia Costanza, ma non sa ancora "
        "se siano stati stampati dove lavora lei o in tipografia, né "
        "il costo esatto; si aggiorna appena ha notizie."),
}

MEDIA_OVERRIDES = {
    (DATE, "12:44", "Emanuele Sciarra", "IMG-20261105-WA0009.jpg"):
        "Foto di grandi quantità di castagne stese ad asciugare a terra "
        "in un locale di deposito, in vista di San Martino; Emanuele "
        "conferma che la settimana prossima saranno pronte e portate a "
        "casa.",
    (DATE, "13:37", "Ilenia Piccozzi", "IMG-20261105-WA0011.jpg"):
        "Foto di una calza di Natale rossa e bianca, semplice, appesa a "
        "una parete, con una spilletta rotonda applicata: esempio delle "
        "calze usate l'anno scorso dal comitato.",
    (DATE, "13:37", "Ilenia Piccozzi", "IMG-20261105-WA0012.jpg"):
        "Screenshot dal sito unigadget.it di una calza di Natale "
        "personalizzabile modello \"Nobo\" (cod. CX1013-05), prezzo a "
        "partire da 0,39€, disponibilità 48.555 pezzi.",
    (DATE, "13:44", "Elvis Ippoliti", "IMG-20261105-WA0014.jpg"):
        "Screenshot della tabella sconti-quantità dello stesso "
        "prodotto: 0,47€ da 1 pezzo, 0,43€ da 250, 0,39€ da 500 (IVA "
        "esclusa).",
}

AUDIO_MERGES = [
    {
        "anchor_time": "13:35",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Emanuele propone di far rivivere una vecchia tradizione "
            "del paese: decorare le biciclette dei bambini con "
            "barattolini di latta attaccati dietro (spunto venuto dalla "
            "moglie, per il figlio), per poi regalarne anche agli altri "
            "bambini del comitato — pensando inizialmente ai propri "
            "figli e a quelli di Antonio Aceto, in modo che gli altri "
            "si aggreghino di conseguenza. Cesare conferma che si può "
            "fare, servono solo i barattoli."
        ),
        "members": [
            "PTT-20261105-WA0007.opus", "PTT-20261105-WA0008.opus",
        ],
    },
    {
        "anchor_time": "13:37",
        "anchor_sender": "Ilenia Piccozzi",
        "type": "proposta",
        "text": (
            "Ilenia posta due foto come esempio per le calze della "
            "Befana (idea aperta il giorno prima da Emanuele): la calza "
            "semplice usata l'anno scorso e lo screenshot di una calza "
            "personalizzabile \"Nobo\" trovata su unigadget.it, a "
            "partire da 0,39€. Il gruppo apprezza ed Emanuele, "
            "scherzosamente, ne sottolinea la convenienza visto il "
            "prezzo (\"aggiudicate!\"). Segue un confronto sui prezzi in "
            "base alla quantità: Elvis calcola 0,47€ per 200 pezzi, "
            "0,43€ per 250; Barbara segnala che anche Ugo aveva trovato "
            "lo stesso sito allo stesso prezzo. Elvis posta anche lo "
            "screenshot della tabella sconti del prodotto e, con almeno "
            "800 pezzi (quantità minima indicata da Ilenia), calcola un "
            "prezzo di 0,39€ a pezzo; condivide infine il link del "
            "prodotto: https://www.unigadget.it/it/calza-di-natale-"
            "nobo---PP9484"
        ),
        "members": [
            "PTT-20261105-WA0013.opus",
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES)
