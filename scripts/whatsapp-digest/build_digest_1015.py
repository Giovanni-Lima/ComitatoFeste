#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-15 — solo dati di curatela, logica comune in digest_lib.py.

Pomeriggio: Costantino aggiorna sul fronte castagne (un contatto può
fornire fino a 100 kg tra tre castagneti, roscette a 7€/kg o seconda scelta
a 6€/kg). Emilio ricorda il traguardo delle 20 coppie per l'incontro di
domani (16 ottobre), con due tabelle coppie aggiornate nel corso della
sera: si arriva esattamente a quota 20. In serata Emanuele riferisce di
una nuova proposta di sponsorizzazione materassi per date future (compenso
diretto di 500€ al comitato per 18 coppie, diverse date libere tra
novembre), aprendo un confronto con Antonio Sabatini sul ritmo di questi
eventi (si converge su diradarli, tenendo conto anche dei prossimi impegni
di fine anno — calze e tombolata di Natale). Nessuna menzione di Giovanni
Lima da parte di altri in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-15"

CURATED = {
    ("14:38", "Costantino Mariani"): ("info",
        "Riferisce di aver sentito un contatto per le castagne: tra tre "
        "castagneti potrebbero fornire fino a 100 kg, proponendo le "
        "roscette a 7€/kg o una seconda scelta a 6€/kg; dovrà aggiornare "
        "anche sul metodo di conservazione."),
    ("16:18", "Emilio Caniglia"): ("info",
        "Ricorda che serve arrivare a 20 coppie per l'incontro di domani "
        "(16 ottobre): chi vuole aggiungersi può farlo anche "
        "singolarmente."),
    ("16:28", "Antonio Aceto"): ("domanda",
        "Chiede a che ora è l'incontro di domani."),
    ("19:16", "Emanuele Sciarra"): ("proposta",
        "Riferisce di essere stato contattato per un'altra serata "
        "sponsorizzata, stavolta di materassi: la proposta è di 18 "
        "coppie a 25€, per un compenso diretto al comitato di 450€ più "
        "50€ di bonus (500€ totali). Le date libere comunicate vanno dal "
        "2 al 5 novembre, dal 9 all'11, poi 16, 18, 23, 24, 26 e 30 "
        "novembre."),
    ("20:04", "Antonio Sabatini"): ("proposta",
        "Propone di rallentare con questi eventi sponsorizzati, diventa "
        "sempre più faticoso reperire persone disponibili: suggerisce "
        "fine novembre, rimettendosi comunque al parere della "
        "maggioranza."),
    ("20:14", "Emanuele Sciarra"): ("proposta",
        "Concorda con Antonio: propone di distanziare di più questi "
        "eventi per dare respiro a chi viene sempre coinvolto, ricordando "
        "che a breve bisognerà pensare anche alle calze e alla tombolata "
        "di Natale; propone una riunione per dividersi i compiti in vista "
        "dei prossimi impegni."),
    ("20:20", "Barbara Rizio"): ("info",
        "Per l'incontro materassi di domani, aggiunge Donato e Marina "
        "(i suoi genitori)."),
    ("21:47", "Maikel Montano"): ("info",
        "Comunica che domani sarà a Roma, con rientro previsto prima "
        "delle 21: potrà esserci, ma verrà da solo."),
}

AUDIO_CURATED = {}

MEDIA_OVERRIDES = {
    (DATE, "16:17", "Emilio Caniglia", "IMG-20261015-WA0002.jpg"):
        "Tabella \"Coppie\" aggiornata per l'incontro del 16 ottobre (17 "
        "coppie su 20 posti): rispetto alla versione precedente si "
        "aggiungono Andrea-Antonella, Luca-Claudia, Alessio "
        "(segnalato da Antonio S.)-Miriam.",
    (DATE, "21:49", "Emilio Caniglia", "IMG-20261015-WA0003.jpg"):
        "Tabella \"Coppie\" aggiornata, obiettivo raggiunto (20 coppie su "
        "20 posti): si aggiungono Emanuele-Liberata, Donato (segnalato da "
        "Barbara)-Marina, e Mike da solo (senza partner indicata).",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
