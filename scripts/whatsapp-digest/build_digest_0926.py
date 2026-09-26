#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-26 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 13:29-20:29 (export Dropbox delle 20:48 del 26/9; nessun messaggio
la mattina). Emanuele Sciarra (13:29) posta il sondaggio per la messa di
domani (San Camillo de Lellis, 11:30: 12 Sì / 1 No al momento dell'export,
curato come proposta) e chiede chi ci sarà per accordarsi sul ritrovo; si
va con le maglie, "sperando faccia caldo". Da lì un thread su magliette,
felpe e badge (14:37-15:10): Emanuele preferisce rimandare la scelta di
magliette e felpe alla prossima riunione, vedendo cosa propone Giacomo
Gentile; Alessandro Di Benedetto, Costance Rossi e Maria Buttari segnalano
che serve roba più pesante, si suggerisce di lasciare libero ciascuno di
indossare la maglia; Emanuele propone i badge con il nome per tutti e li
affida ad Alessandra Toracchio, che li prepara: Emanuele cerca i portabadge
online (52 pezzi con cordini di 5 colori a 15€, o 50 pezzi gialli a 27€,
screenshot delle 14:56 tenuto), Alessandra chiede il logo scelto (15:25,
foto del logo arcade "1987") e le misure, Antonio Aceto (vocale 15:46) li
vorrebbe verticali, Emanuele (vocali 16:40 accorpati) chiede una prova sia
orizzontale sia verticale; le tre schermate Amazon delle misure (16:41-16:42)
sono riassunte nella entry delle 16:43 e scartate. Alle 19:44 Alessandra
posta la bozza del badge. Ugo Trinchini (20:29) chiede a che punto siamo
con le coppie di martedì. Restano rumore: le battute (Martina 14:51,
Alessandro 15:10 sulla spilla è invece nel thread), le conferme brevi.
Nessuna menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-26"

CURATED = {
    ("13:29", "Emanuele Sciarra"): ("proposta",
        "SONDAGGIO: Messa per San Camillo de Lellis ore 11:30 — Sì (12 "
        "voti), No (1 voto) al momento dell'export; il sondaggio resta "
        "aperto."),
    ("13:30", "Emanuele Sciarra"): ("domanda",
        "Chiede chi ci sarà domani alla messa, per mettersi d'accordo su "
        "dove vedersi; Alessandro Di Benedetto chiede se con le maglie e "
        "Emanuele risponde che è meglio, sperando faccia caldo."),
    ("14:38", "Emanuele Sciarra"): ("proposta",
        "Propone di aspettare la prossima riunione per parlare delle "
        "magliette del comitato e, una volta scelte, valutare anche le "
        "felpe (facoltative, per chi le vuole), vedendo cosa propone "
        "Giacomo Gentile. Alessandro Di Benedetto, Costance Rossi e Maria "
        "Buttari fanno notare che col fresco servirebbe roba più pesante; "
        "Alessandro suggerisce di lasciare ciascuno libero di indossare o "
        "meno la maglia e, in caso, di usare la spilla."),
    ("14:50", "Emanuele Sciarra"): ("proposta",
        "Propone che tutti abbiano un badge del comitato con il nome e chiede "
        "ad Alessandra Toracchio di occuparsene; cerca i portabadge online "
        "(52 pezzi con cordini di 5 colori a 15€, oppure 50 pezzi gialli a "
        "27€) e proverà a trovare un prezzo più basso. Alessandra si offre "
        "di preparare i badge e chiede se i cordini siano tutti colorati o "
        "di un solo colore."),
    ("15:17", "Alessandra Toracchio"): ("info",
        "Chiede che le rimandino il logo scelto per le maglie (non ha più "
        "le foto sul telefono) per preparare subito i badge."),
    ("16:43", "Emanuele Sciarra"): ("info",
        "Riporta le misure dei portabadge più comuni (variano da modello a "
        "modello): in orizzontale tessera 8,6x5,4 cm in custodia 10x8,5 cm; "
        "in verticale tessera 5,4x8,6 cm in custodia 6,8x11,6 cm, oppure "
        "formato A6 (105x150 mm)."),
    ("20:29", "Ugo Trinchini"): ("domanda",
        "Chiede a che punto siamo con le coppie per l'evento di martedì "
        "29/9."),
}

AUDIO_CURATED = {
    (DATE, "15:29", "Emanuele Sciarra", "PTT-20260926-WA0004.opus"): ("info",
        "Chiede ad Alessandra Toracchio di fare una bozza del badge con la "
        "dicitura \"Comitato Feste Patronali Classe 1987\" e il nome, da "
        "condividere nel gruppo."),
    (DATE, "15:39", "Alessandra Toracchio", "PTT-20260926-WA0005.opus"): ("domanda",
        "Chiede di sapere la misura del portabadge in plastica (e se è "
        "orizzontale o verticale), indicata nella scheda d'acquisto, per "
        "preparare subito i badge."),
    (DATE, "15:46", "Antonio Aceto", "PTT-20260926-WA0008.opus"): ("proposta",
        "Consiglia di fare i badge in verticale, perché il logo non rende "
        "in orizzontale, con la possibilità di allungarli un po' per "
        "scrivere sotto nome e cognome."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "16:40",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Chiede ad Alessandra Toracchio di fare intanto una prova sia "
            "orizzontale sia verticale del badge per scegliere la versione "
            "più bella: i portabadge si possono comprare in entrambi i "
            "formati (misure standard, le manderà la dimensione)."
        ),
        "members": ["PTT-20260926-WA0009.opus", "PTT-20260926-WA0010.opus"],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "14:56", "Emanuele Sciarra", "IMG-20260926-WA0002.jpg"):
        "Screenshot di un prodotto online: 52 portabadge orizzontali "
        "trasparenti impermeabili con cordini colorati (blu, arancione, "
        "verde, rosso, giallo), 14,59€.",
    (DATE, "15:25", "Emanuele Sciarra", "IMG-20260926-WA0003.jpg"):
        "Logo scelto del comitato: un cabinato arcade con la scritta "
        "\"INSERT COIN\" e \"1987\" in caratteri pixel, su sfondo giallo "
        "(girato ad Alessandra Toracchio per preparare i badge).",
    (DATE, "19:44", "Alessandra Toracchio", "IMG-20260926-WA0016.jpg"):
        "Foto dello schermo con la bozza del badge: cartoncino giallo con "
        "\"COMITATO FESTE - San Benedetto Dei Marsi\", il logo arcade "
        "\"1987\" e il nome \"EMILIO\" (Alessandra: i colori si vedono male "
        "in foto, ne manderà un'altra).",
}

# IMG-20260926-WA0012/13/14.jpg (16:41-16:42): tre schermate Amazon con le
# misure dei portabadge, riassunte nella entry delle 16:43 e scartate.
_SKIP_FILES = {"IMG-20260926-WA0012.jpg", "IMG-20260926-WA0013.jpg",
               "IMG-20260926-WA0014.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="schermate misure portabadge")
