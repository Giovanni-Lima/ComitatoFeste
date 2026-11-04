#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-03 — solo dati di curatela, logica comune in digest_lib.py.

Pomeriggio: Emilio annuncia un cambio di programma per il trasporto a
Corinaldo, confermando (con acconto) un pullman da 64 posti con Bianchi
Tour al posto di Passalacqua + mezzo aggiuntivo: risparmio netto per il
comitato. Stasera riunione della Pro Loco su San Martino, il comitato è
invitato. In serata: invito importante di Don Enzo a chiudere la Novena
dell'Immacolata domenica 6 dicembre; Elvis chiede il programma della gita
di domenica 8, che Antonio Sabatini posta. Resto rumore (presenze,
battute). Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-03"

CURATED = {
    ("12:30", "Emilio Caniglia"): ("decisione",
        "Annuncia un brusco cambio di programma per il trasporto a "
        "Corinaldo: confermato (con acconto) Bianchi Tour al posto di "
        "Passalacqua, prenotando un pullman da 64 posti invece che il "
        "pullman da 54 posti più un mezzo aggiuntivo (furgone da 9 "
        "posti a 500€ o secondo pullman da 19 posti a 750-800€, oltre "
        "ai 1100€ del pullman da 54). Il nuovo pullman unico costa "
        "1250€ in tutto: il comitato risparmia e massimizza l'entrata. "
        "Stasera riunione della Pro Loco per l'organizzazione di San "
        "Martino: il comitato è invitato, chi vuole aggiungersi scriva "
        "a Emilio in privato."),
    ("13:22", "Emilio Caniglia"): ("info",
        "Precisa: Passalacqua era stato scelto per un servizio "
        "migliore, ma aggiungere un mezzo in più rendeva la soluzione "
        "poco conveniente rispetto al pullman unico."),
    ("19:37", "Emilio Caniglia"): ("info",
        "Avviso importante: Don Enzo invita il comitato (\"la classe "
        "1987\") a chiudere la Novena dell'Immacolata domenica 6 "
        "dicembre alle 16:15, recitando il Rosario (il Comitato 1986 "
        "apre la novena, loro la chiudono) seguito dalla Messa; chiede "
        "di venire con le proprie magliette del comitato. Fornirà lui "
        "il kit per il Rosario."),
    ("19:58", "Elvis Ippoliti"): ("domanda",
        "Chiede di reinviare il programma della gita di domenica 8 "
        "(Corinaldo)."),
    ("20:45", "Serena Di Stefano"): ("info",
        "Per il 6 dicembre (Novena dell'Immacolata) segnala un "
        "possibile impegno sportivo con la figlia."),
}

AUDIO_CURATED = {
    (DATE, "12:36", "Antonio Aceto", "PTT-20261103-WA0003.opus"): ("rumore", ""),
    (DATE, "13:24", "Antonio Aceto", "PTT-20261103-WA0005.opus"): ("rumore", ""),
    (DATE, "13:24", "Antonio Aceto", "PTT-20261103-WA0006.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {
    (DATE, "20:18", "Antonio Sabatini", "IMG-20261103-WA0015.jpg"):
        "Locandina ufficiale della gita a Corinaldo di domenica 8 "
        "novembre 2026: partenza ore 6:30 da Piazza Risorgimento (San "
        "Benedetto dei Marsi), arrivo ore 10, Santa Messa nel Santuario "
        "alle 11:15, pranzo al sacco alle 13 (primo piatto caldo "
        "offerto dal Santuario), pellegrinaggio a piedi al Santuario "
        "alle 16, partenza per il ritorno alle 18. Quota di "
        "partecipazione 30€; contatti per informazioni e prenotazioni "
        "di Alessandro, Antonio e Serena.",
}

_SKIP_FILES = {
    # GIF di reazione muta (verificata: nessuna traccia audio)
    "VID-20261103-WA0011.mp4",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="GIF di reazione mp4 (verificata a mano)")
