#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-24 — solo dati di curatela, logica comune in digest_lib.py.

Mattina: Emanuele tratta l'acquisto di castagne tramite un contatto di
famiglia (3,50€/kg per il comitato, un quintale prenotato per il 9-10
novembre). Seguono alcuni video/foto di scherzi tra Antonio Aceto ed Elvis
(GIF di reazione mute e uno screenshot di un videogioco, tutti fuori tema,
scartati). Valentina ed Elvis aggiungono familiari alla lista Corinaldo.
Emilio posta il recap della riunione di ieri sera: prossime riunioni
calendarizzate (30/10 Corinaldo, 6/11 San Martino) e avviso sul pullman
Corinaldo già sold out. In serata Serena avvisa che Gianni Colangelo non
ci sarà ma diffonderà la locandina al gruppo Avis; Elvis condivide un link
Facebook lamentando che il comitato non viene mai menzionato nelle
collaborazioni, proponendo una locandina propria. Nessuna menzione di
Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-24"

CURATED = {
    ("10:51", "Valentina D'Arcadia"): ("info",
        "Per Corinaldo, chiede a Serena di aggiungere lei, la madre e zia "
        "Assunta; porterà i soldi in giornata."),
    ("12:24", "Emilio Caniglia"): ("decisione",
        "Posta il recap della riunione di venerdì 23 ottobre: le prossime "
        "riunioni (monotematiche) sono calendarizzate per venerdì 30 "
        "ottobre (visita a Corinaldo) e venerdì 6 novembre (San Martino). "
        "Avviso importante: un pullman per Corinaldo è già sold out — chi "
        "vuole unirsi (o ha prenotazioni) deve comunicarlo subito; si sta "
        "valutando un secondo pullman o altre soluzioni."),
    ("13:51", "Elvis Ippoliti"): ("info",
        "Chiede a Serena di aggiungere anche sua zia Assunta per "
        "Corinaldo, se c'è ancora posto."),
    ("14:21", "Cesare Raglione"): ("info",
        "Sulle castagne, propone di prendere intanto un campione per "
        "provarle prima di impegnarsi su quantità maggiori."),
    ("20:19", "Serena Di Stefano"): ("info",
        "Avvisa Emilio che Gianni Colangelo non potrà essere presente, ma "
        "invierà la foto della locandina al gruppo Avis."),
    ("23:29", "Elvis Ippoliti"): ("domanda",
        "Condivide un link Facebook "
        "(https://www.facebook.com/share/p/1B6xf1knEQ/) su una "
        "collaborazione in cui nota che il comitato non viene menzionato "
        "da nessuna parte; si chiede se non fosse il caso di essere "
        "almeno interpellati, e propone di realizzare una locandina "
        "propria per sponsorizzare l'evento del comitato."),
}

AUDIO_CURATED = {
    (DATE, "09:46", "Emanuele Sciarra", "PTT-20261024-WA0002.opus"): ("rumore", ""),
    (DATE, "17:04", "Emanuele Sciarra", "PTT-20261024-WA0017.opus"): ("info",
        "Chiede a Serena di aggiungere anche suo figlio Alessandro "
        "Daniele per Corinaldo: saranno in due."),
}

MEDIA_OVERRIDES = {}

AUDIO_MERGES = [
    {
        "anchor_time": "08:05",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Emanuele riferisce che, tramite il marito della nipote, ha "
            "trovato un venditore di castagne: 5€/kg normalmente, ma "
            "3,50€/kg per il comitato; chiede al gruppo se prenderle a "
            "quintali. Dopo i primi via libera, conferma: si potranno "
            "ritirare intorno al 9-10 novembre (prodotto fresco, non "
            "congelato, come suggerito dal presidente), e ha già "
            "prenotato un quintale a 3,50€/kg — non roscette, ma una "
            "varietà marrone."
        ),
        "members": [
            "PTT-20261024-WA0000.opus",
            "PTT-20261024-WA0001.opus",
        ],
    },
]

_SKIP_FILES = {
    # GIF di reazione mascherate da .mp4 (verificate: nessuna traccia audio)
    "VID-20261024-WA0004.mp4", "VID-20261024-WA0006.mp4",
    "VID-20261024-WA0007.mp4", "VID-20261024-WA0009.mp4",
    # screenshot di un videogioco (Campo minato), scherzo fuori tema
    "IMG-20261024-WA0005.jpg",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="GIF di reazione mp4 / scherzo fuori tema")
