#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-06 — solo dati di curatela, logica comune in digest_lib.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-06"

CURATED = {
    ("01:03", "Elvis Ippoliti"): ("domanda",
        "Mezzo ubriaco, chiede a Dante se l'app di cui si era parlato (per le notifiche degli "
        "eventi) sia gratuita o a pagamento."),
    ("01:04", "Dante Caniglia"): ("info",
        "Risponde (in due messaggi di seguito) che l'app è del tutto gratuita."),
    ("01:05", "Elvis Ippoliti"): ("domanda",
        "Chiede allora a chi serva l'app, se è solo per le notifiche degli eventi."),
    ("01:08", "Elvis Ippoliti"): ("info",
        "Fa notare che, se fosse solo per le notifiche, questo lo fanno già Facebook e Instagram "
        "con gli algoritmi e i follower: l'app deve offrire qualcosa in più. Dante rimanda una "
        "spiegazione più completa al giorno dopo."),
    ("09:16", "Emanuele Sciarra"): ("info",
        "Ha chiesto al comitato \"85\" come avevano organizzato loro l'evento dei materassi: "
        "appena si deciderà una data, contatterà la referente dei materassi per accordarsi."),
    ("10:14", "Ugo Trinchini"): ("decisione",
        "Propone di buttare giù alcune date per l'evento (presumibilmente ballo/serata a coppie) e "
        "metterle a votazione, così da iniziare a trovare le coppie partecipanti; chiede conferma "
        "che servano almeno 20 coppie per andare in pareggio/incasso."),
    ("10:16", "Antonio Aceto"): ("decisione",
        "D'accordo con la proposta; suggerisce però di fissare l'evento di sabato, per massimizzare "
        "il numero di coppie partecipanti."),
    ("10:19", "Ugo Trinchini"): ("info",
        "Per il piccolo buffet, una volta fissata la data si offre di chiedere alla Dolciaria un "
        "paio di chili di dolcetti in omaggio."),
}

MEDIA_OVERRIDES = {
    (DATE, "00:09", "Costantino Mariani", "IMG-20260906-WA0000.jpg"):
        "Foto di un sacchetto di plastica verde con quattro bottiglie di birra (marca Nord Fresca "
        "con Spina), con la didascalia \"Cena da asporto\".",
    (DATE, "00:14", "Elvis Ippoliti", "IMG-20260906-WA0007.jpg"):
        "Selfie in casa: un uomo sorride in camera mostrando una bottiglia di birra Nord "
        "(etichetta \"Fresca come Spina\") appena stappata.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
