#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-17 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 17:40-22:14 (export Dropbox delle 9:32 del 18/10; nessun messaggio
prima delle 17:40). Giornata della dimostrazione Bimby organizzata al
"grottino" di Ugo Trinchini: Emanuele Sciarra posta foto del pranzo/degustazione
preparato con i robot da cucina (pane, verdure, dolci, le due postazioni
Bimby) e un video della dimostratrice al lavoro. In serata arrivano i
risultati: tre Bimby venduti, merito soprattutto dei contatti portati da Ugo
(i suoi non erano riusciti a venire); il gruppo festeggia con una lunga
sequenza di emoji. Tre vocali di Emanuele (20:02-20:07, accorpati) spiegano
che la vendita si chiama "Sting Innovation", ringraziano Ugo per la
disponibilità del locale e per gli acquirenti, notano che con un quarto
Bimby venduto si otterrebbe un Bimby in omaggio, e c'è la possibilità di un
quinto Bimby a maggio se i contatti assenti oggi rispondono più avanti (se
ne parlerà in riunione, sperabilmente venerdì); descrive anche il pranzo
(minestra di farro con patate, verdure, pane e crema caffè fatti col Bimby).
Ugo Trinchini (21:52) aggiunge che vendendone un altro si otterrebbe il
secondo o terzo premio della lotteria. Un video di Emanuele (18:07) mostra
la dimostratrice al lavoro; uno sticker di Dante è ignorato in automatico.
Resto rumore (battute, figurine di assenso, ringraziamenti). Nessuna
menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-17"

CURATED = {
    ("19:20", "Emanuele Sciarra"): ("info",
        "Comunica che sono stati venduti 3 Bimby; ringrazia Ugo Trinchini "
        "per la disponibilità e per aver portato gli acquirenti (\"grande "
        "la classe\"); Ugo risponde che il merito è di tutti."),
    ("21:52", "Ugo Trinchini"): ("info",
        "Comunica che vendendone un altro si otterrebbe anche il secondo o "
        "il terzo premio della lotteria."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "20:02",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Spiega l'esito della dimostrazione Bimby (\"Sting "
            "Innovation\"): il merito dei tre Bimby venduti è soprattutto "
            "di Ugo Trinchini, che ha trovato lui gli acquirenti dopo che "
            "i contatti di Emanuele non sono potuti venire; ringrazia Ugo "
            "per la disponibilità del locale (il suo \"grottino\") e per "
            "la partecipazione. Con un quarto Bimby venduto si "
            "otterrebbe un Bimby in omaggio; c'è anche la possibilità di "
            "un quinto Bimby a maggio se i contatti assenti oggi "
            "rispondono più avanti, ma se ne parlerà tutti insieme in "
            "riunione (sperabilmente venerdì). Descrive infine il pranzo "
            "offerto, tutto preparato con il Bimby: una minestra di farro "
            "con patate, carote, zucchine e peperoni, pane fatto in casa "
            "e una crema al caffè."
        ),
        "members": [
            "PTT-20261017-WA0009.opus",
            "PTT-20261017-WA0010.opus",
            "PTT-20261017-WA0011.opus",
        ],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "17:40", "Emanuele Sciarra", "IMG-20261017-WA0000.jpg"):
        "Foto della dimostrazione Bimby al grottino: alcuni membri del "
        "comitato seduti a tavola mentre assaggiano i piatti preparati.",
    (DATE, "17:40", "Emanuele Sciarra", "IMG-20261017-WA0001.jpg"):
        "Foto della dimostratrice Bimby (maglietta del marchio) che "
        "mostra un contenitore del robot da cucina, sorridente.",
    (DATE, "17:40", "Emanuele Sciarra", "IMG-20261017-WA0002.jpg"):
        "Altra foto della tavolata durante la dimostrazione, con dolci, "
        "bibite e una macchina da caffè sullo sfondo.",
    (DATE, "17:42", "Emanuele Sciarra", "IMG-20261017-WA0003.jpg"):
        "Foto del pane fatto in casa col Bimby, su un canovaccio, con "
        "coltello, cialde di caffè e una macchina Lavazza sul tavolo; "
        "didascalia \"Ecc se magn e se bev\" (ecco cosa si mangia e si "
        "beve).",
    (DATE, "17:42", "Emanuele Sciarra", "IMG-20261017-WA0004.jpg"):
        "Foto ravvicinata di uno dei due robot Bimby, con il display che "
        "mostra la cottura a vapore in corso.",
    (DATE, "18:07", "Emanuele Sciarra", "VID-20261017-WA0007.mp4"):
        "Video della dimostratrice Bimby al lavoro in cucina durante la "
        "degustazione.",
}

# IMG-20261017-WA0005.jpg (17:42, Emanuele Sciarra): foto quasi identica
# alla precedente (stesso robot Bimby, stessa schermata), scartata come
# ridondante.
_SKIP_FILES = {"IMG-20261017-WA0005.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_merges=AUDIO_MERGES,
                 extra_skip_media=_extra_skip, extra_skip_label="foto ridondante")
