#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-07 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 09:16-13:13. Mattina: thread sulla stampa dei cartellini/badge
(Alessandra Toracchio vorrebbe procedere, Emanuele è d'accordo, Alessandro
Di Benedetto propone di cambiare la scritta, Elvis Ippoliti e Antonio
Sabatini frenano perché il comitato non esiste ancora giuridicamente —
09:16-09:33, raggruppato con TEXT_MERGES). Dante Caniglia (09:39, vocale)
chiede un chiarimento sulla roadmap degli eventi fino a fine 2026. Emanuele
condivide lo screenshot dell'approvazione della pagina Facebook (10:07) e
riassume in due vocali (10:18-10:19, AUDIO_MERGES) quanto deciso nelle
riunioni: Corinaldo, San Martino, Tombolata, Capodanno di massima
approvato. Propone poi (10:33-10:43, tre vocali + screenshot, AUDIO_MERGES)
una seconda gita all'Eurochocolate di Perugia (13-21 novembre), chiedendo
referenti che si impegnino a riempire il pullman; Dante (11:07) concorda
sulla gita a Napoli di fine novembre offrendo disponibilità. Emanuele
illustra poi (11:01, vocale) l'offerta aggiornata Bimby (promozione 4
venduti = 1 omaggio, 6 venduti = 100€ extra) proponendo una dimostrazione
culinaria per le coppie interessate, condivide il link del prodotto
(11:09-11:10) e lo screenshot con i prezzi (11:25). Emilio Caniglia (12:37)
decide di aspettare a stampare i cartellini fino alla costituzione
giuridica del comitato, con nome e cognome del membro ben visibili (anche
per quanto accaduto a Pescina), e conferma che Don Enzo ha dato il
programma definitivo per Corinaldo. Emanuele chiude (13:13) chiedendo
quando si può riusare il programma della gita dell'85 per fare la
locandina. Nessuna menzione di Giovanni Lima da parte di altri in questa
finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-07"

CURATED = {
    ("10:35", "Raffaele Di Cesare"): ("domanda",
        "Chiede se la serata del 16 è confermata."),
    ("12:37", "Emilio Caniglia"): ("decisione",
        "Sul cartellino identificativo: meglio aspettare, il comitato non "
        "esiste ancora giuridicamente, si potrà procedere solo dopo la sua "
        "registrazione, riportando la denominazione esatta; per il membro "
        "del comitato è meglio indicare nome e cognome, anche per via di "
        "quanto accaduto a Pescina — ne parleranno in riunione. Conferma "
        "inoltre che Don Enzo ha dato il programma definitivo per la visita "
        "a Corinaldo, che sarà riportato nella locandina ufficiale."),
    ("13:13", "Emanuele Sciarra"): ("domanda",
        "Chiede al \"Preside\" quando si può utilizzare il programma della "
        "gita dell'85, per fare la locandina."),
}

AUDIO_CURATED = {
    (DATE, "09:39", "Dante Caniglia", "PTT-20261007-WA0001.opus"): ("domanda",
        "Non essendo stato alle ultime riunioni per lavoro, chiede: il "
        "briefing di Emilio copre le idee da convalidare fino a fine 2026, "
        "ma di solito un evento si organizza con anticipo (es. Capodanno, "
        "casa di Babbo Natale) — per queste cose non si è ancora iniziato a "
        "chiedere nulla."),
    (DATE, "11:01", "Emanuele Sciarra", "PTT-20261007-WA0008.opus"): ("proposta",
        "Riferisce che il prezzo del Bimby è sceso (circa 1.600-1.640€ con "
        "finanziamento a tasso zero su 24 mesi, incluso il kit per il pane); "
        "vendendo 4 Bimby uno arriva in omaggio, vendendone 6 si ottengono "
        "100€ extra a Bimby venduto più il secondo boccale per chi compra. "
        "Propone, per le 5-6 coppie già interessate, di organizzare una "
        "dimostrazione culinaria pomeridiana in un'unica serata (e "
        "altrettanto per il Folletto con un'altra referente)."),
    (DATE, "11:07", "Dante Caniglia", "PTT-20261007-WA0009.opus"): ("info",
        "Concorda con Emanuele sulla gita a Napoli: essendo tanti, con un "
        "pullman pieno ognuno può portare anche un familiare; si rende "
        "disponibile a dare una mano a organizzare."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "10:18",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Riassume quanto deciso nell'ultima riunione: Capodanno e le "
            "altre iniziative verranno approfondite riunione per riunione "
            "(almeno una al mese) fino a fine mandato; per ora si concentra "
            "la gita a Corinaldo, poi San Martino e l'organizzazione della "
            "tombolata. Il Capodanno risulta già \"tra virgolette\" "
            "approvato — sembra che sia l'ultimo anno che chi lo organizzava "
            "finora lo fa — e ci si può già organizzare anche per quello."
        ),
        "members": ["PTT-20261007-WA0002.opus", "PTT-20261007-WA0003.opus"],
    },
    {
        "anchor_time": "10:33",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Propone, oltre a Corinaldo, una seconda gita all'Eurochocolate "
            "di Perugia (13-21/22 novembre): non tutti vorranno andare a "
            "Corinaldo, e viceversa, quindi le due gite si completerebbero. "
            "Riconosce che organizzare due gite richiede la collaborazione "
            "di tutti; per questa come per le prossime (es. Napoli fine "
            "novembre) propone che due o tre persone si prendano la "
            "responsabilità di cercare partecipanti e riempire ogni "
            "pullman, citando come esempio Emilio e Alessandro per Perugia, "
            "e chiede se tutti sono d'accordo a organizzarsi così."
        ),
        "members": ["PTT-20261007-WA0004.opus", "PTT-20261007-WA0005.opus",
                    "PTT-20261007-WA0006.opus"],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "10:07", "Emanuele Sciarra", "IMG-20261007-WA0010.jpg"):
        "Screenshot del post Facebook della pagina del comitato con la "
        "locandina della gita a Corinaldo, finalmente approvato dagli "
        "amministratori del gruppo di San Benedetto.",
    (DATE, "10:34", "Emanuele Sciarra", "IMG-20261007-WA0007.jpg"):
        "Screenshot di una ricerca Google su \"Eurochocolate Perugia 2026\", "
        "che mostra le date dell'evento (13-22 novembre 2026) nel centro "
        "storico di Perugia.",
    (DATE, "11:25", "Emanuele Sciarra", "IMG-20261007-WA0011.jpg"):
        "Foto di un proiettore con il listino prezzi Bimby TM7: con 4 "
        "vendite il Bimby è gratuito completo di accessori più un anno di "
        "abbonamento Cookidoo; prezzo 1.638€ a tasso zero (rata 68,25€ su "
        "24 mesi) oppure 1.599€ pagando in contanti/bonifico/carta, 1.420€ "
        "con IVA agevolata al 4%; vendendone 6 si ottiene anche il secondo "
        "boccale in omaggio.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=[
        {
            "anchor_time": "09:16",
            "anchor_sender": "Alessandra Toracchio",
            "type": "proposta",
            "text": (
                "Riferendosi all'opzione uscita vincente dal sondaggio, "
                "chiede quando può andare a stampare i cartellini/badge, "
                "dato che per lei sono leggibili e chiari. Emanuele Sciarra "
                "è d'accordo a procedere; Alessandro Di Benedetto propone di "
                "scrivere \"comitato feste patronali\" invece "
                "dell'immagine. Elvis Ippoliti e Antonio Sabatini invitano "
                "invece ad aspettare e a informarsi meglio, non essendoci "
                "fretta e non essendo chiaro se il cartellino si possa "
                "usare prima della costituzione ufficiale del comitato."
            ),
            "members": [
                ["09:16", "Alessandra Toracchio"],
                ["09:17", "Alessandra Toracchio"],
                ["09:19", "Emanuele Sciarra"],
                ["09:27", "Alessandra Toracchio"],
                ["09:28", "Alessandro Di Benedetto"],
                ["09:30", "Elvis Ippoliti"],
                ["09:31", "Alessandra Toracchio"],
                ["09:32", "Elvis Ippoliti"],
                ["09:33", "Antonio Sabatini"],
            ],
        },
    ])
