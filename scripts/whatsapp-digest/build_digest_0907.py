#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-07 — solo dati di curatela, logica comune in digest_lib.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-07"

CURATED = {
    ("13:47", "Giovanni Lima"): ("proposta",
        "Dopo alcuni vocali non trascritti (PTT-20260907-WA0017/18/19/20/21/22/23/24, "
        "13:17-13:43), invita tutto il gruppo a intervenire su una proposta: dai messaggi "
        "successivi risulta trattarsi dell'introduzione nel gruppo di un'app che genera "
        "automaticamente il riassunto dei messaggi (chiarito da Alessandra Simonetti alle "
        "14:16: \"Un app che fa i riassunti dei 300 messaggi\")."),
    ("15:58", "Elvis Ippoliti"): ("decisione",
        "Chiude con la propria approvazione una votazione informale durata tutto il "
        "pomeriggio (13:48-17:30): quasi l'intero gruppo (tra gli altri Cesare Raglione, "
        "Emanuele Sciarra, Tina Giarrante, Dante Caniglia, Antonio Aceto, Ilenia Piccozzi, "
        "Maikel Montano, Maria Buttari, Alessandra Simonetti, Chiara Gargano, Antonella "
        "Profeta, Emidio Cerasani, Ugo Trinchini, Antonio Sabatini, Luca Cicchelli, "
        "Alessandro Di Benedetto, Barbara Rizio, Alessandra Toracchio) risponde "
        "positivamente: il gruppo decide di introdurre l'app che genera il riassunto "
        "automatico dei messaggi proposta da Giovanni Lima."),
    ("08:27", "Maria Buttari"): ("info",
        "Racconta di aver scaricato l'app realizzata da Dante Caniglia e di trovarla molto "
        "utile, paragonandola a un'app simile già usata per la città di Luino."),
    ("08:41", "Dante Caniglia"): ("info",
        "Offre di inviare una notifica di prova a chi attiva le notifiche dell'app, per "
        "testarne il funzionamento."),
    ("08:51", "Maria Buttari"): ("info",
        "Conferma di aver ricevuto la notifica di prova generata dall'app, con il link "
        "all'evento: https://san-benedetto-eventi.vercel.app/evento/9fc5bb64-f8df-470c-bba2-f824fb8350e7 "
        "— segnala che la funzione può essere utile per ricordarsi scadenze come le riunioni "
        "(anche perché, dice, tende a dimenticarsene facilmente)."),
    ("19:28", "Emanuele Sciarra"): ("proposta",
        "Propone in via preliminare (solo per farsi un'idea di budget e numero di coppie "
        "necessario) la data di venerdì 18 settembre per l'evento discusso nei giorni "
        "precedenti, concordata a voce con Emidio; precisa che è ancora modificabile e che "
        "si può decidere insieme una data diversa che vada bene a tutti."),
    ("19:29", "Emanuele Sciarra"): ("info",
        "Invita a decidere una data definitiva così da poter richiedere la location per "
        "l'evento."),
    ("19:34", "Emanuele Sciarra"): ("info",
        "Spiega di essersi preso l'iniziativa di contattare la location per farsi un'idea "
        "di budget e numero di coppie necessario, sperando che al gruppo vada bene."),
    ("19:35", "Alessandra Simonetti"): ("info",
        "Approva l'iniziativa di Emanuele Sciarra e suggerisce di organizzare più eventi "
        "dello stesso tipo, per far rientrare prima qualche entrata economica."),
}

MEDIA_OVERRIDES = {
    (DATE, "08:21", "Dante Caniglia", "IMG-20260907-WA0009.jpg"):
        "Screenshot della rubrica WhatsApp con due contatti salvati evidenziati da un "
        "cerchio verde, per aiutare a capire quale dei nomi in rubrica corrisponda a una "
        "persona cercata in una foto del gruppo.",
    (DATE, "08:53", "Dante Caniglia", "IMG-20260907-WA0011.jpg"):
        "Screenshot della schermata home del telefono con l'icona dell'app del comitato "
        "(SB Eventi) evidenziata da un cerchio, a mostrare il pallino di notifica rimasto "
        "acceso sull'icona anche senza aver aperto l'app.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
