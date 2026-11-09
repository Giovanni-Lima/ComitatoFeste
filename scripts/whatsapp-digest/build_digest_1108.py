#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-08 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:01-21:49 (export Dropbox delle 9:01 del 9/11). Giornata della
gita/pellegrinaggio a Corinaldo della classe 1987, con tappa al Santuario
di Santa Maria Goretti — coincidenza con la ricorrenza liturgica del
giorno e col compleanno di Maria Buttari, per cui il gruppo si scambia
auguri. Pranzo al sacco sotto un tendone (con un primo caldo offerto dalla
Comunità di Corinaldo). Giornata molto fotografata: su una settantina di
foto/video condivisi nel gruppo, per decisione dell'utente (9/11/2026) se
ne tiene solo una selezione rappresentativa — le altre, perlopiù scatti
ridondanti dello stesso evento, sono escluse (vedi _extra_skip sotto),
sullo stesso spirito della regola sulle bozze di design ripetute. In
serata Ilenia condivide uno screenshot che conferma che l'animatrice
Antonella non lavora a Capodanno (già discusso a parole lo stesso
pomeriggio). Nessuna menzione di Giovanni Lima (che pure scrive in chat,
complimentandosi per le foto del gruppo).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-08"

CURATED = {
    ("07:15", "Emilio Caniglia"): ("info",
        "Oggi è Santa Maria Goretti e compleanno di Maria Buttari: il "
        "gruppo si scambia auguri in chat."),
    ("21:31", "Ilenia Piccozzi"): ("info",
        "Comunica di aver contattato lei stessa Antonella (animatrice) "
        "e che a Capodanno non lavora, quindi non sarà disponibile per "
        "il veglione."),
    ("21:46", "Ilenia Piccozzi"): ("proposta",
        "Chiede ad Antonella se conosce qualcun'altra brava, ricordando "
        "che alla comunione di Manuel si era presentata una ragazza "
        "altrettanto brava. Elvis è d'accordo nel provare a contattarla "
        "subito, perché più passa il tempo meno possibilità ci sono di "
        "ottenere preventivi."),
}

# Giornata della gita a Corinaldo: selezione rappresentativa dei ~70 media
# condivisi (decisione utente 9/11/2026), vedi docstring sopra.
_KEEP_MEDIA_1108 = {
    "IMG-20261108-WA0000.jpg",
    "IMG-20261108-WA0010.jpg",
    "IMG-20261108-WA0034.jpg",
    "IMG-20261108-WA0040.jpg",
    "IMG-20261108-WA0045.jpg",
    "IMG-20261108-WA0089.jpg",
    "VID-20261108-WA0044.mp4",
    "Antonella Animatrice Feste.vcf",
}


def _extra_skip(time_, fname):
    return fname not in _KEEP_MEDIA_1108


MEDIA_OVERRIDES = {
    (DATE, "07:01", "Emanuele Sciarra", "IMG-20261108-WA0000.jpg"):
        "Foto scherzosa di un membro del comitato addormentato sul "
        "pullman durante il viaggio di andata, con didascalia ironica "
        "\"comitato attivo\".",
    (DATE, "12:19", "Emanuele Sciarra", "IMG-20261108-WA0010.jpg"):
        "Foto di gruppo davanti al Santuario di Santa Maria Goretti a "
        "Corinaldo, i partecipanti alla gita in maglietta/t-shirt del "
        "comitato.",
    (DATE, "13:09", "Vincenzo Lacasasanta", "IMG-20261108-WA0034.jpg"):
        "Foto del gruppo durante il pranzo al sacco, seduto a lunghe "
        "tavolate sotto un tendone.",
    (DATE, "16:20", "Emanuele Sciarra", "IMG-20261108-WA0040.jpg"):
        "Foto di gruppo in una piazza/parco con lampioni, altra tappa "
        "della gita a Corinaldo.",
    (DATE, "17:34", "Elvis Ippoliti", "IMG-20261108-WA0045.jpg"):
        "Foto scherzosa sul pullman di ritorno: un compagno finge di "
        "asciugare con un panno la testa di chi si è appena "
        "addormentato, proseguendo la battuta della foto del mattino.",
    (DATE, "17:31", "Emanuele Sciarra", "VID-20261108-WA0044.mp4"):
        "Video riepilogativo/montaggio della giornata, realizzato da "
        "Emanuele con l'app CapCut e condiviso con il gruppo.",
    (DATE, "19:33", "Elvis Ippoliti", "Antonella Animatrice Feste.vcf"):
        "Contatto vCard dell'animatrice \"Antonella\" condiviso da "
        "Elvis, come riferimento per i preventivi di animazione in "
        "discussione.",
    (DATE, "21:43", "Ilenia Piccozzi", "IMG-20261108-WA0089.jpg"):
        "Screenshot di una conversazione privata tra Ilenia e "
        "l'animatrice Antonella: alla domanda se fosse disponibile per "
        "un veglione di Capodanno, Antonella risponde che quella sera "
        "festeggia lei stessa, confermando di non essere disponibile a "
        "lavorare.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES,
                  extra_skip_media=_extra_skip,
                  extra_skip_label="foto/video ridondanti della gita, esclusi per selezione rappresentativa")
