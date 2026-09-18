#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-18 — solo dati di curatela, logica comune in digest_lib.py.

Giornata dell'incontro sponsorizzato Sanimed Italia (sala consiliare, ore
21). Mattina di soli saluti (rumore), più un video di Raffaele Di Cesare
(08:59, VID-20260918-WA0002.mp4) con traccia audio (verificato a mano,
niente ffprobe su questa macchina) quindi un video vero, ma senza ffmpeg/cv2
non è stato possibile vederne il contenuto: tenuto con didascalia
generica di default, segnalato a parte. Nel pomeriggio (14:21) Emanuele
Sciarra inoltra un vocale della referente Sanimed sul pagamento della
serata (contanti o bonifico) e sul tipo di ricevuta fiscale da emettere
(donazione all'associazione se registrata con timbro, altrimenti
prestazione occasionale sul codice fiscale del presidente); segue lo
scambio con Emilio Caniglia (che deciderà sentendo Antonio Sabatini) e
la conferma dell'orario della serata (21:00, dimostratrice sul posto
verso le 20:30, monta il suo baldacchino). Nessuna menzione di Giovanni
Lima da parte di altri in questa finestra (unico messaggio con il suo nome:
un suo "Buongiorno", rumore).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-18"

CURATED = {
    ("14:22", "Emanuele Sciarra"): ("info",
        "Comunica che per il pagamento della serata di stasera il comitato "
        "accetterà i contanti."),
    ("14:23", "Emanuele Sciarra"): ("domanda",
        "Chiede a Emilio Caniglia (presidente) il suo codice fiscale per "
        "poter emettere la ricevuta come prestazione occasionale, e se va "
        "bene procedere così per poter rispondere alla referente Sanimed."),
    ("14:28", "Emilio Caniglia"): ("info",
        "Risponde che sentirà più tardi Antonio Sabatini e decideranno "
        "come procedere."),
    ("14:34", "Elvis Ippoliti"): ("domanda",
        "Chiede a che ora inizia la serata di stasera."),
    ("14:35", "Emanuele Sciarra"): ("info",
        "Risponde che la serata inizia alle 21, ma la ragazza che farà la "
        "dimostrazione sarà sul posto verso le 20:30 e intanto monta il "
        "suo baldacchino."),
}

AUDIO_CURATED = {
    (DATE, "14:21", "Emanuele Sciarra", "AUD-20260918-WA0007.opus"): ("domanda",
        "Inoltra il vocale ricevuto dalla referente Sanimed Italia sui "
        "dettagli del pagamento di stasera: serve sapere se sarà in "
        "contanti o con bonifico, e quale ricevuta fiscale emettere — se "
        "l'associazione è registrata (con timbro) la ricevuta sarà una "
        "donazione all'associazione; altrimenti si può usare il codice "
        "fiscale del presidente con descrizione \"prestazione "
        "occasionale\". Chiede una risposta entro il pomeriggio, prima "
        "dell'arrivo della relatrice."),
}

MEDIA_OVERRIDES = {}

# Video di Raffaele (08:59) escluso su richiesta di Giovanni: contenuto non
# visibile (niente ffmpeg/cv2 su questa macchina), non vale tenerlo con
# didascalia generica.
_SKIP_FILES = {"VID-20260918-WA0002.mp4"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="video escluso su richiesta")
