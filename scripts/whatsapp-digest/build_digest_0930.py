#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-30 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:10-18:51 (export Dropbox delle 20:42 del 30/9). Emilio Caniglia
(08:10) conferma che nel pomeriggio farà il sondaggio per la data della
prossima riunione, come chiesto la sera prima da Antonio Aceto. Alessandro
Di Benedetto (13:09) comunica di essere stato contattato dal rappresentante
di Ipoh (materassi) per ricordare la serata del 16 ottobre: un nuovo
incontro sponsorizzato già in calendario. Emilio (15:20) lancia il
sondaggio sulla data della riunione (Venerdì 2 ottobre 5 voti, Sabato 3
ottobre 13 voti al momento dell'export, curato come proposta). Tina
Giarrante (15:36) chiede se è arrivato un frigorifero per la sede, Elvis
Ippoliti risponde di no. Emidio Cerasani (15:41, poi vocale 16:15) fa
notare che la sera di sabato 3 ottobre c'è già un'iniziativa per il
transito di San Francesco (coinvolge i diciottenni e venticinquenni,
partenza dalla sacrestia verso Santa Sabina): Elvis (16:12) non crede sia
un problema, l'iniziativa durerà una decina di minuti — un'ora secondo
Emidio — e nulla vieta di parteciparvi e poi tornare alla riunione; Raffaele
Di Cesare (16:23) chiede a che ora si vuole fare la riunione. Emilio
(18:39) posta quattro foto inoltrate da Don Enzo del comitato (magliette
gialle 1987) durante l'offertorio della messa per San Camillo del 27/9,
con il parroco e altri gruppi parrocchiali; Raffaele (18:51) chiude il
thread notando che quindi il problema della sovrapposizione con San
Francesco non si pone nemmeno. Restano rumore i complimenti per la serata
di ieri (Alessandra Toracchio, Maria Buttari) e le battute notturne di fine
29/9. Nessuna menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-30"

CURATED = {
    ("08:10", "Emilio Caniglia"): ("info",
        "Conferma che nel pomeriggio farà il sondaggio per la data della "
        "prossima riunione, come chiesto la sera prima da Antonio Aceto."),
    ("13:09", "Alessandro Di Benedetto"): ("info",
        "Comunica di essere stato contattato dal rappresentante di Ipoh "
        "(materassi) per ricordare la serata del 16 ottobre: un nuovo "
        "incontro sponsorizzato già in calendario."),
    ("15:20", "Emilio Caniglia"): ("proposta",
        "SONDAGGIO: Prossima riunione — Venerdì 2 ottobre (5 voti), Sabato "
        "3 ottobre (13 voti) al momento dell'export; il sondaggio resta "
        "aperto."),
    ("15:36", "Tina Giarrante"): ("domanda",
        "Chiede se è arrivato un frigorifero per la sede; Elvis Ippoliti "
        "risponde che ancora no."),
    ("15:41", "Emidio Cerasani"): ("domanda",
        "Fa notare che la sera di sabato 3 ottobre c'è già un'iniziativa "
        "per il transito di San Francesco (coinvolge i diciottenni e "
        "venticinquenni, partenza dalla sacrestia verso Santa Sabina) e "
        "chiede se non sia il caso di far coincidere le due cose. Elvis "
        "Ippoliti non crede sia un problema: l'iniziativa durerà circa "
        "un'ora, nulla vieta di parteciparvi e poi tornare alla riunione, "
        "e col poco tempo a disposizione conviene comunque il giorno con "
        "più presenza; Raffaele Di Cesare chiede a che ora si vuole fare "
        "la riunione."),
}

AUDIO_CURATED = {
    (DATE, "16:15", "Emidio Cerasani", "PTT-20260930-WA0005.opus"): ("info",
        "Concorda con Elvis: l'iniziativa per San Francesco coinvolge un "
        "po' tutti e dura al massimo un'oretta, lo segnalava solo per "
        "notifica; sono coinvolti i diciottenni e i venticinquenni."),
}

MEDIA_OVERRIDES = {
    (DATE, "18:39", "Emilio Caniglia", "IMG-20260930-WA0008.jpg"):
        "Foto di gruppo del comitato (magliette gialle \"1987\") durante la "
        "messa per San Camillo de Lellis del 27/9, davanti all'urna delle "
        "reliquie, insieme al parroco.",
    (DATE, "18:39", "Emilio Caniglia", "IMG-20260930-WA0009.jpg"):
        "Foto dell'offertorio della messa: un uomo con la maglietta \"1987\" "
        "porta al sacerdote un cesto di pane insieme a una volontaria "
        "dell'Unitalsi.",
    (DATE, "18:39", "Emilio Caniglia", "IMG-20260930-WA0010.jpg"):
        "Foto dell'offertorio della messa: un uomo con la maglietta \"1987\" "
        "e una volontaria dell'Unitalsi portano al sacerdote un cestino con "
        "melagrana e uva.",
    (DATE, "18:39", "Emilio Caniglia", "IMG-20260930-WA0011.jpg"):
        "Foto dell'offertorio della messa: un uomo con la maglietta \"1987\" "
        "e una volontaria portano al sacerdote un cesto regalo.",
}


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
