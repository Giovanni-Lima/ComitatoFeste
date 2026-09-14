#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-13 — solo dati di curatela, logica comune in digest_lib.py.

Giornata parziale (fino alle 22:31 all'atto di questo export), quasi
interamente dominata dagli auguri di compleanno a **Tina Giarrante**
(lei stessa lo annuncia alle 07:38, poi decine di messaggi "auguri" da
tutto il gruppo fino a mezzogiorno) — prima applicazione della regola
"Compleanni" (CLAUDE.md, 13/9/2026): un solo punto sintetico invece di
lasciare tutto rumore.

Resto della giornata: Chiara Gargano torna dopo 4 giorni di assenza dalla
chat e Maria Buttari le fa notare che "c'è l'app che riassume tutto"
(12:26-12:45) — rumore/meta, ma **menzione di Giovanni Lima** (regola
11/9/2026): Maria Buttari scrive "Monumento a Giovanni @Giovanni Lima"
(14:24), verosimilmente collegato proprio a questo scambio sull'app —
segnalato nel recap finale, non genera entry. Giovanni Lima condivide un
video (14:43, VID-20260913-WA0012.mp4) verificato via grep sui box MP4:
solo 'vide'/'avc1', **nessuna** traccia audio ('soun'/'mp4a' assenti) — è
una GIF di reazione travestita da video, scartata come tale. Chiude la
finestra un link Facebook di Emanuele Sciarra con battuta in dialetto per
Costantino Mariani (16:12-16:13) — banter, non contenuto attinente al
comitato, rumore.

Coda serale (20:24-22:31): Emanuele Sciarra riferisce che Andrea Leombruni
si è offerto di prestare la piastra per cuocere le salsicce per Sant'Antonio
(20:24); conferma che tra domani e dopodomani passerà al Comune per le
autorizzazioni del raduno auto d'epoca/street food proposto ieri, e ne
approfitterà per chiedere anche della piastra (21:01); rilancia con una
variante dell'idea — moto d'epoca anziché auto — allegando 4 screenshot di
una ricerca con un assistente AI (percorso "Anello Storico della Marsica":
San Benedetto dei Marsi → Ortucchio → Trasacco/Luco dei Marsi → Pescina,
~50-60km, più note su permessi/burocrazia e logistica) (21:04-21:06); spiega
che lungo quel percorso ci sono più paesi dove chiedere uno sponsor in
cambio di un punto ristoro garantito (21:08). Nessuna menzione di Giovanni
Lima in questa coda.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-13"

CURATED = {
    ("07:38", "Tina Giarrante"): ("info",
        "Oggi è il compleanno di Tina Giarrante: il gruppo si scambia "
        "auguri in chat per tutta la mattina."),
    ("20:24", "Emanuele Sciarra"): ("info",
        "Riferisce che Andrea Leombruni si è offerto di prestare la "
        "piastra per cuocere le salsicce per Sant'Antonio, procurandone "
        "altre se finissero."),
    ("21:01", "Emanuele Sciarra"): ("info",
        "Conferma che tra domani e dopodomani passerà al Comune per le "
        "autorizzazioni del raduno auto d'epoca/street food proposto ieri, "
        "chiedendo anche della piastra per Sant'Antonio."),
    ("21:04", "Emanuele Sciarra"): ("proposta",
        "Rilancia con una variante dell'idea del raduno: moto d'epoca "
        "anziché auto, allegando alcuni screenshot di una ricerca fatta "
        "con un assistente AI su percorso, permessi e logistica."),
    ("21:08", "Emanuele Sciarra"): ("info",
        "Spiega che lungo il percorso proposto per il moto raduno ci sono "
        "più paesi dove si potrebbe chiedere uno sponsor in cambio di un "
        "punto ristoro garantito."),
}

MEDIA_OVERRIDES = {
    (DATE, "21:06", "Emanuele Sciarra", "IMG-20260913-WA0019.jpg"):
        "Screenshot di una ricerca Google sul percorso per un moto raduno "
        "d'epoca (\"Anello Storico della Marsica\", ~50-60km): partenza da "
        "San Benedetto dei Marsi, tappe a Ortucchio, Trasacco o Luco dei "
        "Marsi, rientro/pranzo a Pescina.",
    (DATE, "21:06", "Emanuele Sciarra", "IMG-20260913-WA0020.jpg"):
        "Screenshot di un assistente AI con consigli di pianificazione e "
        "logistica per il moto raduno (data/percorso, iscrizioni, "
        "accoglienza/gadget).",
    (DATE, "21:06", "Emanuele Sciarra", "IMG-20260913-WA0021.jpg"):
        "Screenshot di una ricerca Google con l'itinerario dettagliato "
        "tappa per tappa del moto raduno (San Benedetto dei Marsi → "
        "Ortucchio → Trasacco/Luco dei Marsi → Pescina), con mappa.",
    (DATE, "21:06", "Emanuele Sciarra", "IMG-20260913-WA0022.jpg"):
        "Screenshot di un assistente AI su burocrazia e permessi per "
        "organizzare un moto raduno d'epoca (comunicazione di pubblica "
        "manifestazione, autorizzazioni comunali, assicurazione).",
}

# VID-20260913-WA0012.mp4: nessuna traccia audio (ispezionati i box MP4 —
# 'vide'/'avc1' presenti, 'soun'/'mp4a' assenti, ffprobe non disponibile in
# questa sessione). GIF di reazione travestita da video, va scartata.
_REACTION_GIF_MP4 = {
    "VID-20260913-WA0012.mp4",
}


def _skip_reaction_gif_mp4(time_, fname):
    return fname in _REACTION_GIF_MP4


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES,
                 extra_skip_media=_skip_reaction_gif_mp4,
                 extra_skip_label="GIF di reazione .mp4 senza audio, escluse")
