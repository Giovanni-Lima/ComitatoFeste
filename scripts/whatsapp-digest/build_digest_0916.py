#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-16 — solo dati di curatela, logica comune in digest_lib.py.

Giornata dominata da due thread: il conto su cui incassare l'offerta della
serata materassi (mattina presto, 05:50-07:56 — Antonio Aceto chiede se va
rilasciata una ricevuta e su che IBAN, Dante Caniglia e Ugo Trinchini
rispondono con la loro esperienza di IBAN personali usati in passato,
Antonio Sabatini si offre di usare un conto Poste che non utilizza, accolto
con conferme brevi da più persone) e il conteggio finale delle coppie per
l'incontro del 18/9 (13:12-14:09 — Elvis Ippoliti chiede il totale,
Costantino Mariani chiede a chi passare un compito perché non può venire,
Ugo Trinchini propone coppie di riserva, Emanuele Sciarra aggiunge i
cognati portando il teorico a 21, Elvis spiega di aver perso la sua
compagna Federica e di cercarne una nuova per non scendere sotto 20; Emilio
Caniglia chiude con la foto aggiornata delle coppie, ora a 22 righe con due
posizioni ancora incomplete). Resto della giornata: saluti/battute
dialettali (rumore) e due foto scherzose di Luca Cicchelli (un cartello
stradale, un paesaggio di montagna) tenute con didascalia neutra. Un video
di Dante Caniglia (05:50, VID-20260916-WA0006.mp4) è una GIF di reazione
mascherata (nessun handler audio negli atom MP4, verificato a mano — niente
ffprobe su questa macchina); una foto di Alessandra Toracchio (13:30) è il
forward della stessa immagine già digest il 15/9 alle 22:19 (aggiornamento
coppie), scartata come duplicato. Nessuna menzione di Giovanni Lima in
questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-16"

CURATED = {
    ("07:44", "Antonio Sabatini"): ("proposta",
        "Si offre di mettere a disposizione un conto Poste che non "
        "utilizza per raccogliere l'incasso del bonifico della serata."),
    ("13:12", "Elvis Ippoliti"): ("domanda",
        "Chiede ad Alessandra Toracchio a quante coppie si è arrivati per "
        "l'incontro del 18/9."),
    ("13:41", "Ugo Trinchini"): ("domanda",
        "Chiede se conviene aggiungere qualche coppia in più alla lista "
        "come riserva, nel caso qualcuno desse buca."),
    ("14:09", "Ugo Trinchini"): ("info",
        "Conclude che, se si trova una ragazza da affiancare a Elvis, si "
        "arriva comunque a 21 coppie e si è al sicuro sul numero."),
}

AUDIO_CURATED = {
    (DATE, "05:50", "Antonio Aceto", "PTT-20260916-WA0000.opus"): ("domanda",
        "Chiede come funzionerà l'incasso dell'offerta di circa 500€ della "
        "serata materassi di venerdì: se va rilasciata una ricevuta a chi "
        "la fa, o se è tutto informale, dato che si era detto di non poter "
        "rilasciare ricevute agli sponsor."),
    (DATE, "05:51", "Dante Caniglia", "PTT-20260916-WA0001.opus"): ("info",
        "Risponde che di solito, in casi simili, ha ricevuto o un'email o "
        "i soldi direttamente su un e-bank; non sa come funzioni per "
        "questi organizzatori specifici."),
    (DATE, "06:02", "Antonio Aceto", "PTT-20260916-WA0002.opus"): ("domanda",
        "Chiede se l'IBAN da fornire debba essere intestato a "
        "un'associazione o possa essere un IBAN personale."),
    (DATE, "06:35", "Dante Caniglia", "PTT-20260916-WA0003.opus"): ("info",
        "Risponde che a lui, quando organizzò lui stesso una serata "
        "simile, i soldi arrivarono sul suo IBAN personale."),
    (DATE, "06:39", "Ugo Trinchini", "PTT-20260916-WA0004.opus"): ("info",
        "Comunica che anche l'anno scorso il bonifico fu fatto su un IBAN "
        "personale."),
    (DATE, "13:24", "Costantino Mariani", "PTT-20260916-WA0014.opus"): ("domanda",
        "Chiede a chi può passare il compito di portare l'acqua per la "
        "serata materassi, perché lui non potrà venire."),
    (DATE, "13:42", "Emanuele Sciarra", "PTT-20260916-WA0015.opus"): ("info",
        "Comunica di essersi scordato di aggiungere una coppia: anche i "
        "cognati Daniele e Alessia partecipano, portando il totale "
        "teorico a 21 coppie."),
    (DATE, "13:42", "Elvis Ippoliti", "PTT-20260916-WA0016.opus"): ("info",
        "Spiega il motivo della domanda sul conteggio: ha avuto un "
        "imprevisto con Federica, che venerdì non ci sarà; se non si "
        "trova un'altra ragazza che faccia coppia con lui si resta a 20, "
        "altrimenti serve un'altra coppia di riserva."),
}

MEDIA_OVERRIDES = {
    (DATE, "07:37", "Luca Cicchelli", "IMG-20260916-WA0009.jpg"):
        "Foto di un cartello stradale con le indicazioni per le località "
        "\"Bastardo\" e \"Massa Martana\", condivisa per scherzo sul nome "
        "del primo paese.",
    (DATE, "11:36", "Luca Cicchelli", "IMG-20260916-WA0011.jpg"):
        "Foto di un paesaggio di montagna, scattata durante un tragitto "
        "in auto.",
    (DATE, "15:15", "Emilio Caniglia", "IMG-20260916-WA0020.jpg"):
        "Aggiornamento del foglio \"COPPIE\" per l'incontro del 18/9, ora "
        "a 22 righe: aggiunge Daniele-Alessia (i cognati di Emanuele) e "
        "due posizioni ancora incomplete in attesa di partner, Elvis (in "
        "cerca di una nuova compagna dopo l'imprevisto con Federica) e "
        "Alessandro Di Benedetto.",
}

# .mp4 senza ffprobe su questa macchina (16/9/2026): VID-20260916-WA0006.mp4
# verificato a mano (nessun handler "soun" negli atom MP4) -> GIF di
# reazione mascherata. IMG-20260915-WA0039.jpg è il forward della stessa
# foto già digest il 15/9 alle 22:19: stesso identico file, scartato come
# duplicato per non ripetere lo stesso contenuto in due giorni.
_SKIP_FILES = {"VID-20260916-WA0006.mp4", "IMG-20260915-WA0039.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="GIF mp4 + forward duplicato coppie")
