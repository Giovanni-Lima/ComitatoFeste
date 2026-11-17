#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-17 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:22-17:02 (export Dropbox delle 17:47, giornata ancora in corso).
Il punto riepilogativo degli auguri di compleanno a Gilda Di Iulio resta in
build_digest_1116.py (primo messaggio della sera prima): i proseguimenti di
auguri che ricadono già nel 17/11 (incluso quello di Giovanni Lima) restano
rumore individuale, non ripetuti qui. La mattina Emanuele riceve un commento
dal tono politico sotto il reel dei ringraziamenti di San Martino: lunga
discussione nel gruppo su come reagire (ignorare o rispondere, se sia un bot
o una persona reale), risolta con cancellazione del commento, segnalazione e
blocco dell'autore, senza alcuna risposta pubblica — tra i pareri anche
quello di Giovanni Lima (ipotesi bot di propaganda), ripreso esplicitamente
da Elvis. Antonio Sabatini rendiconta la vendita delle ultime castagne.
Emanuele propone un cappellino invernale col logo della classe 87 al posto
di felpe/cappotti, accolto bene dal gruppo.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-17"

CURATED = {
    ("08:23", "Antonio Sabatini"): ("info",
        "Comunica che le ultime castagne rimaste sono state divise "
        "equamente tra tre membri del comitato: tutto venduto. "
        "Venerdì in riunione verrà esposto, per chiarezza, il "
        "resoconto della giornata di sabato scorso (San Martino)."),
}

MEDIA_OVERRIDES = {
    (DATE, "07:22", "Emanuele Sciarra", "IMG-20261117-WA0000.jpg"):
        "Screenshot di un commento (di un profilo esterno al "
        "comitato, dai contenuti perlopiù politici) lasciato sotto il "
        "reel di ringraziamento per San Martino pubblicato da "
        "Emanuele: un attacco politico scollegato dal video, "
        "percepito come fuori contesto.",
    (DATE, "11:28", "Costance Rossi", "IMG-20261117-WA0028.jpg"):
        "Locandina di un evento culturale non legato al comitato: "
        "doppio incontro con l'autrice Catena Fiorello Galeano, "
        "domenica 22 novembre 2026, Sala Consiliare del Comune di San "
        "Benedetto dei Marsi (rassegna \"Un autunno da sfogliare\").",
    (DATE, "16:36", "Emanuele Sciarra", "IMG-20261117-WA0031.jpg"):
        "Cosa ne pensate se al posto di felpe o cappotti facciamo un "
        "cappellino con logo e scritta classe 87? Credo che d'inverno "
        "sia comodo per tutti e bene o male tutti lo usiamo... "
        "(immagine di esempio: un berretto personalizzabile con "
        "ricamo di testo/logo, disponibile in molti colori).",
}

AUDIO_CURATED = {
    (DATE, "08:02", "Costantino Mariani", "PTT-20261117-WA0020.opus"): ("rumore", ""),
    (DATE, "08:21", "Luca Cicchelli", "PTT-20261117-WA0021.opus"): ("rumore", ""),
    (DATE, "08:21", "Luca Cicchelli", "PTT-20261117-WA0022.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {
        "anchor_time": "07:23",
        "anchor_sender": "Emanuele Sciarra",
        "type": "decisione",
        "text": (
            "Dopo aver pubblicato il reel di ringraziamento per San "
            "Martino, Emanuele trova sotto al post un commento dal "
            "tono politico (vedi foto) e, preoccupato di aver "
            "involontariamente dato un'impressione politica, chiede "
            "consiglio al gruppo su come comportarsi, rileggendo più "
            "volte il proprio testo senza trovarvi riferimenti "
            "politici. Alessandra Simonetti consiglia di non "
            "rispondere, facendo notare che il commento è palesemente "
            "fuori luogo; Luca è incerto se rispondere o lasciar "
            "perdere, osservando che anche rispondere potrebbe "
            "insinuare qualcosa. Emanuele valuta anche l'idea di far "
            "intervenire un profilo esterno al comitato per chiedere "
            "chiarimenti, preoccupato per l'immagine del comitato; "
            "Maria lo rassicura di lasciar perdere, spiegando che è "
            "pura provocazione e analizzando il profilo dell'autore "
            "(solo 8 follower contro 5.000 seguiti, tutti post a "
            "sfondo politico, a suo dire \"il solito coglione di "
            "turno\"): non merita risposta. Emanuele propone quindi di "
            "bloccare, e Luca è d'accordo per evitare polemiche senza "
            "fine. Giovanni Lima ipotizza che possano essere bot "
            "automatici di propaganda che attaccano a caso, e invita "
            "a bloccare e andare avanti; Dante pensa invece sia una "
            "persona vera. Elvis concorda sull'approccio "
            "segnalare-bloccare-andare avanti senza rispondere, "
            "riprendendo esplicitamente l'ipotesi di Giovanni sulla "
            "propaganda/incitamento all'odio. Emanuele conferma che "
            "eliminerà il commento, lo segnalerà e bloccherà l'autore. "
            "Costantino concorda sulla pericolosità di esporsi così "
            "apertamente politicamente, scherzando sul rischio di "
            "guai; Elvis ribadisce lo stesso concetto. Valentina pensa "
            "si tratti di commenti generati da intelligenza "
            "artificiale e di aver già bannato lei stessa l'autore; "
            "Elvis dissente, ritenendo dal profilo che si tratti "
            "invece di una persona reale ossessionata di politica. "
            "Emanuele chiude dicendo che, bot o persona reale che "
            "sia, ha comunque già eliminato il commento e bloccato "
            "l'autore. Più tardi Dante ribadisce che si tratta "
            "probabilmente di una persona normale che si è sbagliata "
            "(\"i bot su Facebook non esistono più\"), consigliando di "
            "nascondere il commento; Emanuele conferma di aver già "
            "eliminato tutto e bloccato la persona, nella speranza di "
            "evitare ulteriori attriti."
        ),
        "members": [
            "PTT-20261117-WA0001.opus", "PTT-20261117-WA0002.opus",
            "PTT-20261117-WA0003.opus", "PTT-20261117-WA0004.opus",
            "PTT-20261117-WA0005.opus", "PTT-20261117-WA0006.opus",
            "PTT-20261117-WA0007.opus", "PTT-20261117-WA0008.opus",
            "PTT-20261117-WA0009.opus", "PTT-20261117-WA0010.opus",
            "PTT-20261117-WA0011.opus", "PTT-20261117-WA0012.opus",
            "PTT-20261117-WA0014.opus", "PTT-20261117-WA0015.opus",
            "PTT-20261117-WA0016.opus", "PTT-20261117-WA0017.opus",
            "PTT-20261117-WA0018.opus", "PTT-20261117-WA0019.opus",
            "PTT-20261117-WA0023.opus", "PTT-20261117-WA0024.opus",
            "PTT-20261117-WA0025.opus", "PTT-20261117-WA0026.opus",
            "PTT-20261117-WA0027.opus",
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES)
