#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-10 — solo dati di curatela, logica comune in digest_lib.py.

Giornata dominata dal tema "fondo cassa" in vista della riunione di venerdì
11/9 (non ancora deciso -> proposta) e da molti feedback sull'app comitatofeste
lanciata la sera prima. Nessuna decisione formale presa in chat.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-10"

CURATED = {
    ("00:20", "Valentina D'Arcadia"): ("info",
        "Nelle ore successive diversi membri segnalano di non riuscire ad accedere "
        "all'app (Valentina D'Arcadia, poi Luca Cicchelli e Alessandra Simonetti verso "
        "le 07:14-07:17); Giovanni Lima sistema gli accessi e in mattinata i problemi "
        "risultano risolti."),
    ("06:48", "Tina Giarrante"): ("proposta",
        "Propone che alla riunione ciascuno porti qualcosa da bere/mangiare e che si "
        "lasci un \"fondo cassa\"; chiede ad Alessandra Toracchio se le serve una mano. "
        "Elvis Ippoliti precisa (06:50) che la riunione non è la sera stessa ma il "
        "giorno dopo, venerdì."),
    ("07:24", "Emanuele Sciarra"): ("proposta",
        "Rilancia la questione del fondo cassa per la riunione: da messaggi precedenti "
        "sembrava condivisa l'idea di mettere 20€ a testa; propone di portarli comunque, "
        "salvo parlarne in riunione per verificare che tutti siano d'accordo. Tina "
        "Giarrante e Antonio Sabatini si dicono favorevoli ma vogliono sentire il "
        "parere di tutti; Elvis Ippoliti fa notare che ci sono spese imminenti (es. il "
        "buffet per la dimostrazione) che senza fondo cassa non si saprebbe come "
        "coprire."),
    ("07:39", "Tina Giarrante"): ("proposta",
        "Propone di fare subito un sondaggio nel gruppo sul fondo cassa, così da "
        "arrivare alla riunione avvantaggiati almeno su quel punto; Antonio Sabatini è "
        "d'accordo, Emanuele Sciarra è invece contrario a fare sondaggi. Alla "
        "generazione del digest il sondaggio non risulta ancora creato."),
    ("07:44", "Emanuele Sciarra"): ("info",
        "Riferisce che Antonio gli ha dato il contatto dell'assessore di Corinaldo "
        "(Mirka), che avrebbe in mente di organizzare qualcosa insieme ai ragazzi di "
        "San Benedetto; spiegherà meglio alla riunione."),
    ("08:42", "Serena Di Stefano"): ("domanda",
        "Chiede conferma che la riunione sia venerdì al rustico della nonna di "
        "Alessandra Toracchio."),
    ("08:48", "Antonio Aceto"): ("info",
        "Conferma a Serena Di Stefano che la riunione è venerdì al rustico della nonna "
        "di Alessandra Toracchio."),
    # N.B. la segnalazione delle 09:07 di Elvis ("l'app non si aggiorna") è un
    # messaggio con immagine allegata: il suo contenuto è curato nella
    # MEDIA_OVERRIDES per IMG-20260910-WA0028.jpg qui sotto, non in CURATED
    # (che vale solo per i messaggi di solo testo).
    ("09:15", "Elvis Ippoliti"): ("proposta",
        "Propone di aggiornare l'app più volte al giorno (ogni ora o mezz'ora) invece "
        "di una sola volta la sera, così da poterla consultare durante la giornata "
        "quando i messaggi sono tanti; precisa che non è una critica, l'app è utile, ma "
        "su questo aspetto si potrebbe migliorare."),
    ("09:56", "Giovanni Lima"): ("info",
        "Spiega che i riassunti li lancia a mano dal proprio PC dopo cena, per avere la "
        "giornata completa e scremare meglio, e che WhatsApp non permette di "
        "automatizzare il processo; valuterà se lanciarli anche dopo pranzo. Ricorda "
        "che in alto nell'app c'è una campanella per attivare le notifiche a ogni nuovo "
        "aggiornamento."),
    ("10:00", "Dante Caniglia"): ("info",
        "Avvisa che probabilmente non riuscirà a esserci alla riunione di venerdì; al "
        "limite passa da Elvis Ippoliti a lasciargli i soldi del fondo cassa."),
    # --- coda pomeridiana importata l'11/9/2026 (nuovi messaggi dopo il checkpoint 12:42) ---
    ("13:35", "Alessandra Toracchio"): ("info",
        "In vista della riunione: Alessandra Toracchio sarà sul posto per le 21:00 e "
        "manderà la posizione; ha già procurato bicchieri, acqua e caffè e chiede agli "
        "altri di portare da bere e qualcosa da stuzzicare. Ci si divide i compiti: "
        "Barbara Rizio porta il dolce, Tina Giarrante le patatine."),
    ("14:00", "Emilio Caniglia"): ("info",
        "Condivide l'aggiornamento dei preventivi per il trasporto in autobus per la "
        "visita a Corinaldo (tabella allegata): Bianchi Tour 1100€ per 54 posti / "
        "1250€ per 64 / 1800€ per 83; Di Curzio 1200€ per 54 posti; Passalacqua 1100€ "
        "per 54 posti."),
}

MEDIA_OVERRIDES = {
    (DATE, "08:50", "Emanuele Sciarra", "IMG-20260910-WA0013.jpg"):
        "Foto di un gruppo di persone sedute su sedie di plastica sotto un porticato, "
        "riprese di spalle, come a un'assemblea o a un raduno all'aperto.",
    (DATE, "09:07", "Elvis Ippoliti", "IMG-20260910-WA0028.jpg"):
        "Screenshot dell'app comitatofeste ferma alla giornata del 9 settembre 2026, "
        "allegato alla segnalazione di Elvis Ippoliti che l'app non si aggiorna e "
        "resta sulla data del giorno prima; Dante Caniglia risponde che "
        "l'aggiornamento dipende da un backup con orari fissi.",
    (DATE, "10:06", "Elvis Ippoliti", "IMG-20260910-WA0054.jpg"):
        "Screenshot di una spiegazione grammaticale sull'uso di \"per chi volesse\" "
        "(congiuntivo) rispetto a \"per chi vorrebbe\", condiviso nel botta e risposta "
        "scherzoso con Dante Caniglia.",
    (DATE, "11:06", "Antonio Aceto", "IMG-20260910-WA0056.jpg"):
        "Foto di gruppo di studenti in fila lungo un muro sotto un porticato, con un "
        "cerchio verde disegnato a mano attorno a tre ragazzi sulla destra; condivisa "
        "nel siparietto scherzoso sulla scuola.",
    (DATE, "13:12", "Dante Caniglia", "IMG-20260910-WA0064.jpg"):
        "Foto di nuvole a mammatus (formazioni a sacche) su una strada con passanti e "
        "auto e una croce verde di farmacia; didascalia scherzosa \"Avezzano "
        "marshmallow\".",
    (DATE, "14:00", "Emilio Caniglia", "IMG-20260910-WA0068.jpg"):
        "Tabella \"Trasporto Corinaldo\" con i preventivi di tre ditte di autobus: "
        "Bianchi Tour (54 posti 1100€ / 64 posti 1250€ / 83 posti 1800€), Di Curzio "
        "(54 posti 1200€), Passalacqua (54 posti 1100€), con il costo per posto "
        "calcolato per ciascuna riga (~19-22€).",
}

# Le 5 GIF di reazione del giorno travestite da .mp4: nessuna ha traccia audio
# (verificato ispezionando i box MP4 -> nessun handler 'soun'), quindi vanno
# escluse come sticker/GIF (regola 4/9/2026). Sono elencate qui esplicitamente
# perché nella sessione in cui è stato generato questo digest ffprobe non era
# disponibile e is_reaction_gif() non poteva intercettarle da sola; su una
# macchina con ffprobe la funzione le scarterebbe comunque.
_REACTION_GIF_MP4 = {
    "VID-20260910-WA0029.mp4",
    "VID-20260910-WA0052.mp4",
    "VID-20260910-WA0053.mp4",
    "VID-20260910-WA0058.mp4",
    "VID-20260910-WA0066.mp4",
}


def _skip_reaction_gif_mp4(time_, fname):
    return fname in _REACTION_GIF_MP4


# Attributi letti dal runner di sessione (scratchpad/run_session.py).
EXTRA_SKIP_MEDIA = _skip_reaction_gif_mp4
EXTRA_SKIP_LABEL = "GIF di reazione .mp4 senza audio, escluse"

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES,
                 extra_skip_media=_skip_reaction_gif_mp4,
                 extra_skip_label="GIF di reazione .mp4 senza audio, escluse")
