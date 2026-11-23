#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-20 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 05:30-23:43. Emanuele si informa (con un assistente AI) su cosa
scrivere su un badge identificativo, risolvendo il dubbio sollevato il
giorno prima da Elvis; il gruppo poi conferma la dicitura "Comitato Feste
Patronali" (come il comitato dell'85) e gira alcune varianti grafiche
aggiornate del badge. Emilio ricorda la riunione di stasera e il tavolo
convocato dal Comune per lunedì 23 sul calendario natalizio; gira anche il
link di un fornitore di calze della Befana. Si chiude il sondaggio sul
cappellino: vince nettamente l'opzione 4 (beanie antracite, toppa gialla
"1987" a cifre composte da scene di videogiochi). In serata lungo filo di
ringraziamenti a Maikel Montano per il vino donato a San Martino; due video
di Daniele Boscolo (contenuto personale/sociale, scartati). Nessuna
menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-20"

CURATED = {
    ("07:34", "Emilio Caniglia"): ("info",
        "Ricorda la riunione di questa sera, ore 21 in sede: non sarà "
        "possibile calendarizzare eventi, ma ci sarà un confronto "
        "sull'argomento e un resoconto di San Martino. L'amministrazione "
        "comunale ha indetto per lunedì 23 novembre un tavolo aperto a "
        "tutte le associazioni (compreso il Comitato) per il calendario "
        "natalizio e la giornata dell'accensione dell'albero. Si "
        "discuterà anche della banda (visti gli ultimi aggiornamenti), "
        "della Tombolata, delle calze della Befana, di Capodanno e si "
        "inizierà a pensare alla costituzione formale del Comitato (atto "
        "costitutivo, con possibili forme di adesione \"a distanza\")."),
    ("15:25", "Emilio Caniglia"): ("info",
        "Anticipo sulle calze della Befana: Maria ha individuato "
        "un'azienda online che vende sia calze vuote (vari modelli e "
        "misure) sia già confezionate, oltre a dolciumi e caramelle. "
        "Link: https://www.rigato.net/ (sezione \"feste e ricorrenze\")."),
    ("15:32", "Emanuele Sciarra"): ("proposta",
        "Chiude il sondaggio per scegliere il cappellino (si vedano le "
        "4 bozze girate poco prima), precisando che è solo per capire "
        "quale piaccia di più e che eventuali altre idee si "
        "valuteranno con Giacomo per la fattibilità.\n\nSONDAGGIO: "
        "Cappello comitato\nOPZIONE: 1 (1 voto)\nOPZIONE: 2 (0 voti)\n"
        "OPZIONE: 3 (0 voti)\nOPZIONE: 4 (9 voti)"),
    ("23:04", "Elvis Ippoliti"): ("info",
        "Il gruppo ringrazia Maikel Montano per il vino donato in "
        "occasione di San Martino (Maria, Daniele, Antonio, Ilenia, "
        "Cesare, Alessandra, Alessandro, Ugo, Valentina, Barbara, "
        "Emanuele e Dante si uniscono ai ringraziamenti)."),
}

MEDIA_OVERRIDES = {
    (DATE, "05:30", "Emanuele Sciarra", "IMG-20261120-WA0001.jpg"):
        "Screenshot di una ricerca con un assistente AI su cosa scrivere "
        "su un badge identificativo del comitato: nome "
        "dell'organizzazione (es. \"Comitato Feste Patronali [Nome]\"), "
        "ruolo/qualifica, nome e cognome ben visibili, anno "
        "dell'edizione.",
    (DATE, "15:30", "Emanuele Sciarra", "IMG-20261118-WA0004.jpg"):
        "Cappellino, opzione 1: beanie antracite con toppa circolare "
        "\"CLASSE 1987\" a cifre composte da scene di videogiochi.",
    (DATE, "15:31", "Emanuele Sciarra", "IMG-20261118-WA0005.jpg"):
        "Cappellino, opzione 2: beanie antracite con toppa "
        "rettangolare (senza bordo) \"1987\" a cifre di videogiochi "
        "contornate di rosa/viola.",
    (DATE, "11:23", "Emanuele Sciarra", "IMG-20261120-WA0004.jpg"):
        "Bozza finale del cappellino (realizzata da Giacomo Gentile): "
        "beanie antracite con toppa gialla rettangolare \"1987\" a "
        "cifre composte da scene di videogiochi — poi proposta nel "
        "sondaggio come opzione 4, la più votata.",
    (DATE, "15:31", "Emanuele Sciarra", "IMG-20261119-WA0039.jpg"):
        "Cappellino, opzione 3 del sondaggio: cappellino giallo con "
        "toppa \"1987\" a cifre di videogiochi (stesso file già "
        "condiviso il 19/11).",
    (DATE, "15:31", "Emanuele Sciarra", "IMG-20261120-WA0004.jpg"):
        "Cappellino, opzione 4 del sondaggio: la bozza finale di "
        "Giacomo (stesso file già condiviso stamattina alle 11:23), "
        "poi risultata la più votata.",
    (DATE, "15:42", "Emanuele Sciarra", "IMG-20261121-WA0000.jpg"):
        "\"Questo é il badge degli 85\": badge fisico del comitato "
        "1985 (edizione 2025), con portabadge blu, logo \"1985\" e la "
        "dicitura \"Comitato Organizzativo Feste Patronali, San "
        "Benedetto dei Marsi\" — esempio concreto a sostegno "
        "dell'inclusione di \"patronali\".",
    (DATE, "16:51", "Alessandra Toracchio", "IMG-20261120-WA0007.jpg"):
        "Variante grafica aggiornata del badge, ora con la dicitura "
        "\"Comitato Feste Patronali, San Benedetto dei Marsi 2027\" e "
        "cabinato arcade/\"1987\" sullo sfondo giallo.",
    (DATE, "16:51", "Alessandra Toracchio", "IMG-20261120-WA0009.jpg"):
        "Altra variante dello stesso badge aggiornato (\"Comitato "
        "Feste Patronali\"), con una resa grafica leggermente diversa "
        "del cabinato arcade.",
    (DATE, "16:53", "Alessandra Toracchio", "IMG-20261120-WA0008.jpg"):
        "Terza variante dello stesso badge aggiornato, con la scritta "
        "\"Comitato Feste Patronali\" su un'unica riga.",
    (DATE, "23:13", "Emilio Caniglia", "IMG-20261121-WA0001.jpg"):
        "Esempio di calza della Befana già confezionata (dal "
        "fornitore segnalato nel pomeriggio), con wafer, caramelle "
        "Haribo e cioccolatini.",
}

# VID-20261121-WA0002/3.mp4 (23:42-23:43 Daniele Boscolo): video di una
# serata/uscita tra amici (contenuto personale/sociale, nessun collegamento
# chiaro con l'attività del comitato), scartati come le foto personali.
_SKIP_FILES = {"VID-20261121-WA0002.mp4", "VID-20261121-WA0003.mp4"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, extra_skip_media=_extra_skip,
                 extra_skip_label="video personale/sociale senza collegamento al comitato")
