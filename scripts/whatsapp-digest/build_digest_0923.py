#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-23 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 05:17-16:43. Punto principale: Costantino Mariani (08:18-08:22)
riferisce di un incontro con Perinetti (concessionario, già segnalato come
possibile sponsor il 17/9) sulla possibilità di fornire un'auto come premio
di una lotteria del comitato — prezzo per il veicolo finito di IVA e su
strada, contratto con pagamento solo al ritiro (possibilmente senza
acconto), ritiro in sede da parte del vincitore, e se il premio non esce
l'auto resta di Perinetti senza costi per il comitato; ancora da
approfondire. Emanuele Sciarra (11:32) chiarisce a Martina Del Gizzi che la
Fiat 500 non è un premio del comitato: è l'estrazione di febbraio legata
alla serata materassi del 29/9. Ugo Trinchini (05:17) non è sicuro di
tornare in tempo per la messa dell'evento di Padre Pio, e più tardi (13:42)
aggiunge Geo e Alice alla lista del 29/9; Antonio Aceto (08:06) aggiunge
Alessio e Margherita. Una foto di Elvis Ippoliti (16:10) mostra sullo
schermo di un computer una vecchia immagine di due auto decorate con fiocchi
verdi in una strada di paese, commentata con tono nostalgico. Resto rumore:
saluti, battute sulla 500 e su Tina (compreso un vocale di Emanuele 12:29,
scartato), commenti dialettali. Nessuna menzione di Giovanni Lima in questa
finestra.

Coda serale (17:50-21:47, export del 24/9): solo rumore ("sto alla chiesa",
"arrivo", una richiesta di foto), nessuna entry aggiunta.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-23"

CURATED = {
    ("05:17", "Ugo Trinchini"): ("info",
        "Comunica che non sa se riesce a tornare in tempo per la messa "
        "della manifestazione di oggi."),
    ("08:06", "Antonio Aceto"): ("info",
        "Chiede di segnare Alessio e Margherita per martedì (la serata "
        "del 29/9)."),
    ("08:18", "Costantino Mariani"): ("proposta",
        "Riferisce di un incontro con Perinetti, da approfondire ma già "
        "con qualcosa in mano, sulla possibilità di avere un'auto come "
        "premio di lotteria: il prezzo che proporranno è per il veicolo "
        "finito di IVA e messo su strada; si dovrebbe firmare un "
        "contratto tra Perinetti e il comitato in cui si specifica che il "
        "pagamento avverrà al ritiro del veicolo, non prima, e se "
        "possibile senza alcun acconto; il ritiro sarà fatto in sede "
        "Perinetti direttamente dal vincitore con il biglietto; se il "
        "premio non esce, la proprietà resta a Perinetti senza alcun "
        "costo per il comitato. L'incontro era stato fatto per altri "
        "motivi e ne ha approfittato per questo discorso."),
    ("11:32", "Emanuele Sciarra"): ("info",
        "Risponde a Martina Del Gizzi, che chiedeva se il comitato "
        "mettesse in palio una 500: no, con la serata del 29 i promotori "
        "daranno dei biglietti alle coppie presenti e a febbraio ci sarà "
        "un'estrazione con la possibilità di vincere una Fiat 500."),
    ("13:42", "Ugo Trinchini"): ("info",
        "Chiede di aggiungere Geo e Alice alla lista per la serata del "
        "29/9."),
}

MEDIA_OVERRIDES = {
    (DATE, "16:10", "Elvis Ippoliti", "IMG-20260923-WA0004.jpg"):
        "Foto dello schermo di un computer che mostra una vecchia "
        "immagine di due auto decorate con fiocchi verdi, parcheggiate "
        "in una strada di paese; condivisa con tono nostalgico (i "
        "commenti seguenti rimpiangono i bei tempi).",
}

AUDIO_CURATED = {
    (DATE, "12:29", "Emanuele Sciarra", "PTT-20260923-WA0002.opus"): ("rumore", ""),
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
