#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-04 — solo dati di curatela, logica comune in digest_lib.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-04"

CURATED = {
    ("08:10", "Costantino Mariani"): ("info",
        "Riferisce (sentito da Luca Trinchini) che tutti i totem sono stati tolti."),
    ("15:50", "Alessandra Toracchio"): ("domanda",
        "Chiede cosa è stato deciso per la riunione."),
    ("15:50", "Emilio Caniglia"): ("info",
        "Riepilogo dopo il riposizionamento delle statue di ieri sera: incontro breve con Don Enzo "
        "con novità importanti, e rimozione di tutti i totem (saranno riutilizzati il prossimo anno, "
        "piccola spesa risparmiata per il Comitato). Novità: invito da parte di Don Enzo alla messa "
        "delle 11:30 del 27 settembre con le magliette del Comitato (sarà esposto il corpo di San "
        "Camillo de Lellis); la visita a Corinaldo è posticipata all'8 novembre per impegni di Don "
        "Enzo e accordi con Don Luigi di Corinaldo; probabile un nuovo incontro con Don Enzo in "
        "settimana per definire l'impegno per le Feste Patronali."),
    ("15:57", "Alessandra Simonetti"): ("info",
        "Il 27 settembre, oltre alla messa, ci sarà anche la benedizione degli operatori sanitari."),
    ("16:06", "Costance Rossi"): ("domanda",
        "Propone di fare una riunione prima di vedere Don Enzo, per arrivare con idee comuni tra "
        "tutti."),
    ("16:10", "Elvis Ippoliti"): ("info",
        "Conferma che se ne era già parlato la sera prima con Emidio e altri (di persona), anche per "
        "decidere le cariche finali e scegliere la sede."),
    ("16:17", "Luca Cicchelli"): ("info",
        "Propone una piccola quota di partecipazione da parte di tutti per gli incontri/eventi, da "
        "definire in base alle esigenze e al consenso del gruppo."),
    ("16:19", "Costance Rossi"): ("decisione",
        "Propone di provare a organizzare l'incontro entro fine settembre."),
    ("16:19", "Emidio Cerasani"): ("info",
        "Riferisce che Costantino Mariani (imprenditore) ha detto di mettere una quota alta di "
        "partecipazione."),
    ("16:20", "Costance Rossi"): ("domanda",
        "Visto che il 27 settembre ci sarà molta partecipazione per la benedizione, chiede se si può "
        "organizzare qualcosa in quell'occasione."),
    ("16:21", "Emilio Caniglia"): ("decisione",
        "Per lui va bene organizzare l'incontro prima di quello con Don Enzo (la prossima settimana, "
        "infrasettimanale): bisogna decidere se farlo stasera, domani sera o domenica sera."),
    ("16:22", "Elvis Ippoliti"): ("info",
        "Pensa si possa fare l'incontro lunedì o martedì, dato che con Don Enzo ci si vedrà mercoledì "
        "o giovedì."),
    ("16:24", "Emanuele Sciarra"): ("info",
        "La \"ragazza dei materassi\" (sponsor per la lotteria) aspetta solo che le venga data una "
        "data."),
    ("16:25", "Emanuele Sciarra"): ("decisione",
        "Bisogna chiedere la sala al Comune per l'incontro; propone di organizzare un piccolo buffet "
        "per l'occasione."),
    ("16:26", "Emanuele Sciarra"): ("info",
        "Con 5€ a testa si compra da mangiare e da bere per il buffet, oppure chi vuole e sa fare "
        "porta dolci fatti in casa."),
    ("18:30", "Dante Caniglia"): ("info",
        "Sta seguendo in diretta un evento per bambini e genitori (gruppo \"Snack club\") ad "
        "Avezzano: nota stupito quanta gente porti, a suo dire più del concerto dei The Kolors "
        "(condivide diversi video dall'evento)."),
    ("18:38", "Maria Buttari"): ("info",
        "Osserva che gli eventi che attirano i bambini fanno soldi — spunto per la pianificazione di "
        "futuri eventi del comitato."),
    ("18:42", "Emanuele Sciarra"): ("info",
        "Condivide un link a un video Facebook, relativo allo stesso evento per bambini di cui si "
        "stava parlando: https://www.facebook.com/share/r/1EUmPSTZqM/?mibextid=wwXIfr"),
}

MEDIA_OVERRIDES = {
    (DATE, "07:07", "Serena Di Stefano", "IMG-20260904-WA0007.jpg"):
        "Foto di un cervo in un prato nella nebbia mattutina, condivisa insieme al saluto \"sono in "
        "compagnia\".",
    (DATE, "14:08", "Elvis Ippoliti", "IMG-20260904-WA0046.jpg"):
        "Meme: fotogramma da \"Il Signore degli Anelli - Il Ritorno del Re\" con la scritta scherzosa "
        "\"PER COSTANTINO!\" al posto di \"per Frodo\" — battuta rivolta a Costantino Mariani.",
    (DATE, "18:33", "Elvis Ippoliti", "IMG-20260904-WA0054.jpg"):
        "Selfie con un bicchiere di birra in mano e occhiali da sole — foto conviviale della serata.",
    (DATE, "19:21", "Elvis Ippoliti", "IMG-20260904-WA0064.jpg"):
        "Foto all'aperto in un locale/bar, momento conviviale della serata.",
    (DATE, "19:35", "Ugo Trinchini", "IMG-20260904-WA0065.jpg"):
        "Selfie di due persone con da bere in mano, sorridenti — foto conviviale della serata.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
