#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-25 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 06:07-08:24 (nessun vocale). Mattina quasi solo di saluti (rumore).
Unico punto: Emilio Caniglia (07:13) ricorda l'invito di Don Enzo per la
Messa di domenica 27/9 alle 11:30, in cui la parrocchia accoglierà il corpo
di San Camillo de Lellis, evento che coinvolge tutte le associazioni del
territorio. La locandina rimandata alle 07:14 è lo stesso file
(IMG-20260917-WA0001.jpg) già digest il 17/9 alle 08:05: scartata come
duplicato. Nessuna menzione di Giovanni Lima in questa finestra.

Coda pomeridiana/serale (13:25-20:44, aggiornata con l'export delle 20:44 del
25/9): un breve video di Raffaele Di Cesare (13:25) e' la registrazione di una
storia Instagram non legata al comitato, scartato. Ilenia Piccozzi (13:34)
non puo' esserci martedi'; Emilio Caniglia (16:47) comunica l'invito del
Sindaco per sabato 26/9 alla biblioteca comunale (Giornate Europee del
Patrimonio, scavi archeologici; locandina allegata) e (17:40) posta
l'aggiornamento della lista coppie per il 29/9 (foto, 23 righe). Serata di
conteggio coppie: Alessandra Simonetti (19:31) aggiunge i genitori suoi e di
Costance ("siamo a 20"); Barbara Rizio (19:37) chiede se servono 25 coppie,
Antonio Aceto (vocale 19:38) ricorda la soglia di 24 coppie per i 600 euro
(25 euro a coppia, sotto soglia 20), confermata da Antonio Sabatini ed
Emanuele; Emanuele (vocale 19:43) fa il punto: 22 coppie effettive, mancano
una coppia e due accompagnatrici; Ugo Trinchini (vocale 19:53) propone due
ragazze per Elvis e Antonio senza partner. Tina Giarrante (19:39) anticipa
cosa porta (acqua, bibite, bicchieri), Antonio Sabatini (19:53) si offre per
la spesa e Emanuele (vocali 19:43 e 20:06) riferisce degli avanzi in casa sua
e degli inviti stampati dal promotore con il regolamento dell'estrazione
(Fiat 500 a febbraio) e dell'orologio da parete in regalo. Restano rumore: le
battute su Costantino (19:25 e vocale 19:28), le conferme brevi e le battute
sulle coppie (20:38-20:44, vocale di Elvis compreso). Nessuna menzione di
Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-25"

CURATED = {
    ("07:13", "Emilio Caniglia"): ("info",
        "Ricorda l'invito di Don Enzo per la Messa di domenica 27/9 alle "
        "11:30: la parrocchia accoglierà il corpo di San Camillo de "
        "Lellis, patrono dei malati e degli operatori sanitari, in un "
        "evento eccezionale che coinvolgerà tutte le associazioni del "
        "territorio e tutta la comunità."),
    ("13:34", "Ilenia Piccozzi"): ("info",
        "Comunica che martedì (incontro del 29/9) non potrà esserci."),
    ("16:47", "Emilio Caniglia"): ("info",
        "Comunica l'invito ricevuto dal Sindaco per sabato pomeriggio (26/9) "
        "alla biblioteca comunale, come da locandina: un incontro sul "
        "passato glorioso della città, con novità importanti sui recenti "
        "scavi archeologici."),
    ("19:31", "Alessandra Simonetti"): ("info",
        "Chiede di inserire nella lista coppie i suoi genitori (Ermanno e "
        "Raffaella) e i genitori di Costance (Mario e Patrizia): così crede "
        "di essere arrivati a 20."),
    ("19:37", "Barbara Rizio"): ("domanda",
        "Chiede se bisogna arrivare a 25 coppie; Alessandra Simonetti si "
        "stupisce (\"sono aumentate?\"), Antonio Sabatini ed Emanuele "
        "Sciarra confermano che il numero è 24."),
    ("19:39", "Tina Giarrante"): ("info",
        "Anticipa cosa porterà alla serata del 29/9: un fardello d'acqua, "
        "Coca Cola, tè, aranciata, succo e bicchieri."),
    ("19:53", "Antonio Sabatini"): ("info",
        "Si offre di occuparsi della spesa, se si riesce a fare una piccola "
        "lista di cosa comprare."),
}

AUDIO_CURATED = {
    (DATE, "19:38", "Antonio Aceto", "PTT-20260925-WA0009.opus"): ("info",
        "Ricorda che, da quanto sa, bisogna arrivare a 24 coppie per "
        "incassare i 600€ (25€ a coppia); sotto le 24 coppie il compenso "
        "scende a 20€ a coppia."),
    (DATE, "19:43", "Emanuele Sciarra", "PTT-20260925-WA0011.opus"): ("info",
        "Fa il punto sulla lista: attualmente 22 coppie effettive e a due "
        "persone manca la compagna, quindi mancherebbero una coppia "
        "effettiva e due accompagnatrici."),
    (DATE, "19:43", "Emanuele Sciarra", "PTT-20260925-WA0012.opus"): ("info",
        "Comunica che dalla dimostrazione scorsa è avanzato qualcosa che ha "
        "a casa; appena arrivato aggiornerà su cosa c'è."),
    (DATE, "19:53", "Ugo Trinchini", "PTT-20260925-WA0013.opus"): ("proposta",
        "Nota che Elvis e Antonio sono senza partner e propone di inserire "
        "due ragazze: Erika e un'altra (nome poco chiaro nella "
        "trascrizione)."),
    (DATE, "20:06", "Emanuele Sciarra", "PTT-20260925-WA0014.opus"): ("info",
        "Riferisce che il promotore dell'evento di martedì gli ha dato gli "
        "inviti stampati, con luogo/ora dell'evento e il regolamento "
        "dell'estrazione di febbraio: quella sera a ogni coppia verrà dato "
        "un numero, ci si registra gratis sul sito e si può partecipare "
        "all'estrazione di una Fiat 500 (più altri premi). Il promotore lo "
        "ricontatterà il giorno dopo per sapere com'è andata e regalerà al "
        "comitato un orologio da parete (Pierre Cardin) sponsorizzato dalla "
        "sua ditta, usabile come premio per la tombolata."),
    # Vocali di rumore (battute su Costantino, battute sulle coppie): scartati.
    (DATE, "19:28", "Emanuele Sciarra", "PTT-20260925-WA0008.opus"): ("rumore", ""),
    (DATE, "19:41", "Barbara Rizio", "PTT-20260925-WA0010.opus"): ("rumore", ""),
    (DATE, "20:43", "Elvis Ippoliti", "PTT-20260925-WA0019.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {
    (DATE, "16:47", "Emilio Caniglia", "IMG-20260925-WA0006.jpg"):
        "Locandina delle Giornate Europee del Patrimonio (26-27 settembre "
        "2026): sabato 26/9 a San Benedetto dei Marsi, dalle 15:00 alle "
        "19:00 apertura della Domus (corso Vittorio Veneto) e alle 17:30 in "
        "biblioteca comunale \"I secoli di Marruvium, splendidissima "
        "civitas\", presentazione dei risultati degli scavi preventivi in "
        "località Abbazia, con i saluti del Sindaco e gli interventi della "
        "Soprintendenza e della Cooperativa Geoarcheologica Limes; ingresso "
        "gratuito, senza prenotazione.",
    (DATE, "17:40", "Emilio Caniglia", "IMG-20260925-WA0007.jpg"):
        "Aggiornamento del foglio \"COPPIE\" per l'incontro di martedì 29 "
        "settembre, a 23 righe: Antonio A.-Jennifer, Raffaele-Verdiana, "
        "Maurizio-Valentina, Silvano-Barbara, Ugo-Tina, Mike-Lucianny, "
        "Elvis (senza partner), Alessandro-Patrizia, Costantino (senza "
        "partner), Cesare-Valentina, Antonio S. (senza partner), Andrea-"
        "Rossella, Donato-Santina, Donato-Marina, Emilio-Federica, Alessio-"
        "Miriam, Tonino-Giovanna, Alessio-Margherita, Geo-Alice, Gino-"
        "Roberta, Vincenzo-Lara; le righe 6, 9 e 24 sono vuote.",
}

# IMG-20260917-WA0001.jpg (07:14): stessa identica locandina delle reliquie
# di San Camillo già digest il 17/9 alle 08:05, rimandata da Emilio — scartata
# come duplicato per non ripetere lo stesso contenuto in due giorni.
# VID-20260925-WA0005.mp4 (13:25, Raffaele Di Cesare): registrazione di una
# storia Instagram di 3 secondi non legata al comitato, scartata.
_SKIP_FILES = {"IMG-20260917-WA0001.jpg", "VID-20260925-WA0005.mp4"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="forward duplicato locandina + video non legato")
