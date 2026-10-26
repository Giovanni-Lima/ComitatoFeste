#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-25 — solo dati di curatela, logica comune in digest_lib.py.

Mattina: Emilio chiarisce che il comitato fa solo San Martino, non
Halloween (Elvis condivide lo screenshot del post della Pro Loco che le
accomuna); Emanuele chiede se qualcuno ha incontrato Gianvito per il
Capodanno (Emilio: non c'era, lo risentirà domani) e racconta un vocale
su un possibile logo/locandina condivisa con Giorgio per la "costa di San
Martino delle Zucche" (esito incerto). A mezzogiorno Dante condivide un
link su un evento itinerante chiedendo che passi anche da San Benedetto;
Emanuele ha già chiesto alla Pro Loco locale, che l'anno scorso ne aveva
parlato con Pescina senza esito. Alessandra propone l'acquisto di un
cassetto portavalori per le serate; Ilenia condivide la locandina della
Castagnata di San Martino di Pescina e chiede come si sta organizzando la
Pro Loco locale per i bambini — Emilio risponde: attività bambini, un
contest zucche per Halloween, e un quintale di castagne (~400 cartocci).
In serata Emilio riepiloga: aggiornamento Capodanno (sarà l'ultimo
all'"Ragno", dettagli il 30/10, si incontrerà anche l'animatore Andrea Di
Loreto) e annuncia un nuovo incontro sponsorizzato materassi per il 4
dicembre. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-25"

CURATED = {
    ("08:29", "Emilio Caniglia"): ("info",
        "Chiarisce che il comitato organizza solo l'evento di San "
        "Martino: non Halloween."),
    ("08:49", "Emanuele Sciarra"): ("domanda",
        "Chiede se qualcuno ieri è andato da Gianvito per discutere del "
        "Capodanno."),
    ("09:05", "Emilio Caniglia"): ("info",
        "Risponde a Emanuele: Gianvito non c'era; domani risentirà la "
        "Pro Loco."),
    ("09:47", "Emilio Caniglia"): ("info",
        "Risentirà Giorgio anche per farsi inviare il logo per la "
        "locandina di San Martino."),
    ("12:43", "Dante Caniglia"): ("info",
        "Condivide un link Facebook "
        "(https://www.facebook.com/share/1E3FCJJTjk/) su un evento "
        "itinerante, chiedendo che passi anche da San Benedetto."),
    ("18:07", "Ilenia Piccozzi"): ("domanda",
        "Chiede come si sta organizzando la Pro Loco locale per San "
        "Martino, soprattutto per l'intrattenimento dei bambini."),
    ("20:52", "Emilio Caniglia"): ("info",
        "Risponde a Ilenia: anche la Pro Loco locale farà attività per "
        "bambini, ci sarà un contest delle zucche legato ad Halloween, e "
        "il comitato porterà un quintale di castagne (equivalente a più "
        "di 400 cartocci)."),
    ("21:16", "Emilio Caniglia"): ("info",
        "Aggiorna sul Capodanno: questa mattina Ugo e Costantino hanno "
        "parlato con Gianvito, sarà l'ultimo Capodanno organizzato "
        "all'\"Ragno\" — dettagli alla riunione di venerdì 30 ottobre, "
        "dove si incontrerà anche Andrea Di Loreto per l'animazione e si "
        "finalizzerà la visita a Corinaldo. Annuncia inoltre un nuovo "
        "incontro sponsorizzato con un'azienda di materassi per venerdì "
        "4 dicembre, ringraziando Emanuele."),
}

AUDIO_CURATED = {
    (DATE, "09:30", "Emanuele Sciarra", "PTT-20261025-WA0002.opus"): ("info",
        "Racconta un vecchio scambio con Giorgio su un logo/locandina "
        "comune per la \"costa di San Martino delle Zucche\" (da "
        "accostare alla vendita delle castagne): Giorgio si era detto "
        "disponibile a sentirsi con Emilio per farla insieme, ma "
        "Emanuele non sa se la cosa si concretizzerà."),
    (DATE, "12:44", "Emanuele Sciarra", "PTT-20261025-WA0003.opus"): ("info",
        "Collegandosi al link di Dante, racconta di aver già chiesto "
        "alla Pro Loco di San Benedetto: l'anno scorso ne avevano "
        "parlato anche con quelli di Pescina, ma l'evento non si era "
        "fatto né a Pescina né a San Benedetto."),
}

MEDIA_OVERRIDES = {
    (DATE, "08:37", "Elvis Ippoliti", "IMG-20261025-WA0000.jpg"):
        "Screenshot di un post Facebook della Pro Loco San Benedetto dei "
        "Marsi: iniziativa \"Porta a casa la tua zucca\" (zucche "
        "acquistabili a 5€, da decorare ed esporre il 14 novembre in "
        "occasione della festa di San Martino) — da qui l'osservazione "
        "di Elvis che la locandina Halloween cita comunque San Martino.",
    (DATE, "12:50", "Alessandra Toracchio", "IMG-20261025-WA0004.jpg"):
        "Foto di un cassetto portavalori da cassa: Alessandra chiede se "
        "può essere utile al comitato; Emanuele conferma che potrebbe "
        "servire per le serate come San Martino o Sant'Antonio.",
    (DATE, "17:59", "Ilenia Piccozzi", "IMG-20261025-WA0005.jpg"):
        "Screenshot di un post Facebook della Pro Loco di Pescina: "
        "\"Castagnata di San Martino\" il 14 novembre 2026 alle 17:00 in "
        "piazza Mazzarino, con caldarroste, vin brulé e attività per "
        "bambini.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
