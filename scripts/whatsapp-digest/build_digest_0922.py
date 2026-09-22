#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-22 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:22-12:12. Emanuele Sciarra comunica di aver bloccato la data
del 29/9 per l'incontro promozionale materassi (il rappresentante ha
chiamato per fermarla, essendo richiesta anche da altri gruppi) e chiede la
lista delle coppie, con l'evento previsto alle 21 come la volta scorsa: la
lista riparte da zero e si popola nel corso della mattina fino a 7 coppie
(foto delle 12:12), con un breve thread su Ilenia (senza il compagno
Pietro) ed Elvis (in attesa di sapere su Federica, poi confermato da solo)
messi insieme come settima coppia da Raffaele. Due vocali di Emanuele
(10:35, accorpati) chiedono con che nome iscriversi come comitato per la
pratica coi materassi — Comitato Feste 87 o Comitato Feste Classe 1987 —
Antonio Aceto risponde "comitato feste patronali classe 1987". Resto
rumore (conferme brevi, un messaggio di sistema).

Coda pomeridiana/serale (aggiornata con l'export delle 17:40 del 22/9, che
estende il giorno oltre le 12:12): la lista coppie per il 29/9 continua a
crescere (foto delle 15:32: 15 righe compilate). Emilio Caniglia (16:48)
comunica un invito ricevuto per la commemorazione di Padre Pio, protettore
dei volontari di Protezione Civile, il 23/9 a San Benedetto dei Marsi
(locandina allegata), e chiede disponibilità a rappresentare il comitato;
Emanuele conferma la messa (incerto sul corteo) e chiede se partecipare con
la maglietta del comitato, confermato da Emilio. Emanuele (vocale 17:08)
comunica di aver rimandato a giovedì l'appuntamento con il rappresentante
dei materassi, inizialmente previsto domani alle 18, per un contrattempo di
quest'ultimo — Antonio Sabatini aveva notato la sovrapposizione con
l'evento di Padre Pio. Resto rumore (conferme brevi, un messaggio di
sistema, una battuta dialettale su una crostata). Nessuna menzione di
Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-22"

CURATED = {
    ("08:22", "Emanuele Sciarra"): ("decisione",
        "Comunica di aver bloccato la data del 29/9 per l'incontro "
        "pubblicitario dei materassi (il promotore ha chiamato chiedendo "
        "di confermare, essendo la data richiesta anche da altri "
        "gruppi); chiede la lista delle coppie, l'evento si terrà alle "
        "21 come la volta scorsa."),
    ("09:26", "Antonio Aceto"): ("info",
        "Conferma la partecipazione sua e di Jennifer."),
    ("09:37", "Raffaele Di Cesare"): ("info",
        "Conferma la partecipazione sua e della compagna Verdiana."),
    ("09:38", "Valentina D'Arcadia"): ("info",
        "Conferma la partecipazione sua e di Maurizio."),
    ("09:38", "Barbara Rizio"): ("info",
        "Conferma la partecipazione sua e di Silvano."),
    ("09:54", "Tina Giarrante"): ("info",
        "Conferma la propria partecipazione insieme a Ugo Trinchini."),
    ("09:54", "Maikel Montano"): ("info",
        "Conferma la partecipazione sua e della moglie."),
    ("10:01", "Ilenia Piccozzi"): ("info",
        "Comunica che parteciperà senza il compagno Pietro, il cui "
        "turno di lavoro potrebbe non cambiare."),
    ("10:30", "Elvis Ippoliti"): ("info",
        "Conferma la propria partecipazione; per Federica farà sapere "
        "più avanti."),
    ("10:36", "Antonio Aceto"): ("info",
        "Risponde a Emanuele sul nome da usare per l'iscrizione del "
        "comitato: dovrebbe essere \"comitato feste patronali classe "
        "1987\"."),
    ("10:51", "Raffaele Di Cesare"): ("info",
        "Propone che, in mancanza di un partner sicuro per Ilenia ed "
        "Elvis, i due formino insieme la settima coppia."),
    ("10:57", "Elvis Ippoliti"): ("info",
        "Conferma che parteciperà da solo (Federica non ci sarà) e si "
        "rende disponibile a fare coppia."),
    ("12:53", "Alessandro Di Benedetto"): ("info",
        "Conferma la propria partecipazione."),
    ("13:28", "Costantino Mariani"): ("info",
        "Conferma la propria partecipazione salvo imprevisti; crede "
        "sarà presente anche Alexa, ma deve confermare."),
    ("14:45", "Cesare Raglione"): ("info",
        "Conferma la partecipazione sua e di Valentina."),
    ("14:50", "Antonio Sabatini"): ("info",
        "Conferma la partecipazione sua e di Rossella, e dei genitori "
        "Donato e Santina; si rende eventualmente disponibile anche per "
        "un'altra coppia (con Andrea), in attesa di conferma."),
    ("15:13", "Barbara Rizio"): ("info",
        "Comunica la partecipazione dei genitori Donato e Marina."),
    ("16:44", "Alessandro Di Benedetto"): ("info",
        "Chiede a Emilio Caniglia di aggiungere Patrizia D.B. alla "
        "lista coppie."),
    ("16:48", "Emilio Caniglia"): ("domanda",
        "Comunica che il comitato ha ricevuto un invito per l'evento "
        "commemorativo di Padre Pio (protettore dei volontari di "
        "Protezione Civile) di domani, e chiede se c'è qualcuno "
        "disponibile a partecipare in rappresentanza del comitato."),
    ("17:03", "Emanuele Sciarra"): ("info",
        "Conferma che sarà presente almeno alla messa per la "
        "commemorazione di Padre Pio (non è sicuro del corteo) e chiede "
        "se partecipare con la maglietta del comitato."),
    ("17:06", "Antonio Sabatini"): ("domanda",
        "Fa notare che domani alle 18 c'è anche l'appuntamento con il "
        "rappresentante dei materassi, in sovrapposizione con l'evento "
        "di Padre Pio."),
    ("17:10", "Emilio Caniglia"): ("info",
        "Conferma che si parteciperà all'evento di Padre Pio con le "
        "magliette del comitato."),
    ("17:11", "Alessandra Toracchio"): ("info",
        "Comunica che domani non può esserci, ma conferma la propria "
        "disponibilità per l'incontro materassi spostato a giovedì."),
    ("17:12", "Valentina D'Arcadia"): ("info",
        "Comunica che il 29/9 parteciperanno anche i suoi genitori "
        "Tonino e Giovanna; domani invece lei non potrà esserci perché "
        "al lavoro."),
    ("17:18", "Antonio Sabatini"): ("info",
        "Chiarito che l'incontro materassi è stato spostato a giovedì, "
        "conferma che parteciperà anche domani all'evento di Padre Pio."),
}

AUDIO_CURATED = {
    (DATE, "17:08", "Emanuele Sciarra", "PTT-20260922-WA0006.opus"): ("info",
        "Comunica di aver rimandato a giovedì l'appuntamento con il "
        "rappresentante dei materassi, inizialmente previsto domani "
        "alle 18, per un contrattempo di quest'ultimo."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "10:35",
        "anchor_sender": "Emanuele Sciarra",
        "type": "domanda",
        "text": (
            "Chiede come ci si dovrà chiamare in fase di iscrizione come "
            "comitato (\"Comitato Feste 87\" o \"Comitato Feste Classe "
            "1987\"): glielo ha chiesto il rappresentante dei materassi, "
            "pur non essendo necessarie fatture; chiede se qualcuno ne sa "
            "di più."
        ),
        "members": ["PTT-20260922-WA0001.opus", "PTT-20260922-WA0002.opus"],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "12:12", "Emilio Caniglia", "IMG-20260922-WA0003.jpg"):
        "Foto del foglio \"COPPIE\" per l'incontro pubblicitario del "
        "29/9, ripartito da zero rispetto alle liste precedenti: 7 "
        "coppie finora — Antonio A.-Jennifer, Raffaele-Verdiana, "
        "Maurizio-Valentina, Silvano-Barbara, Ugo-Tina, Mike-Lucianny, "
        "Elvis-Ilenia.",
    (DATE, "15:32", "Emilio Caniglia", "IMG-20260922-WA0004.jpg"):
        "Nuovo aggiornamento del foglio \"COPPIE\" per l'incontro del "
        "29/9, ora a 15 righe: Antonio A.-Jennifer, Raffaele-Verdiana, "
        "Maurizio-Valentina, Silvano-Barbara, Ugo-Tina, Mike-Lucianny, "
        "Elvis (senza partner), Ilenia (senza partner), Alessandro "
        "(senza partner), Costantino-Alexa, Cesare-Valentina, Antonio "
        "S. (senza partner), Andrea-Rossella, Donato-Santina, "
        "Donato-Marina.",
    (DATE, "16:49", "Emilio Caniglia", "IMG-20260922-WA0005.jpg"):
        "Locandina della commemorazione di Padre Pio (San Pio da "
        "Pietrelcina), protettore dei volontari di Protezione Civile, "
        "il 23 settembre a San Benedetto dei Marsi: raduno alle 16:45 "
        "in Piazza Risorgimento con corteo verso la statua di San Pio "
        "al cimitero, Santa Messa alle 18:00, benedizione dei mezzi a "
        "cura del parroco Don Enzo.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES)
