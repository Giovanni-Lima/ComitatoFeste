#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-21 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 10:14-19:38, dominata dal filone delle serate dimostrative a
pagamento. Emanuele Sciarra riferisce di aver contattato i promotori dei
materassi (lo richiameranno i responsabili di zona) e la referente del
Bimby (screenshot 11:05: si dice disponibile a ripetere l'evento fatto con
la classe '85, lo richiamerà a fine settimana), e chiede il contatto di un
rappresentante Kirby (Alessandra Toracchio ne ha uno). Un rappresentante dei
materassi vuole incontrare almeno tre persone del comitato prima della
serata (Emanuele dice "mercoledì 18", ma il 18/9 era venerdì: quasi
certamente mercoledì 23/9, alle 18); disponibilità raccolte a seguire
(Alessandra T., Antonio Sabatini, Raffaele, Ugo si rendono disponibili,
Antonio Aceto no per questa settimana). Le condizioni proposte dall'azienda
(vocale 11:13): fino a 25 euro a coppia con 24 coppie, in date 29/9 e
6-7-8/10; Emanuele resta tiepido sulla resa (vocale 10:58) e non può
partecipare a quelle date. Antonio Sabatini propone un sondaggio flash sulle
date. Resto rumore: battute sul comprare un materasso, dialetto, "ottimo",
due vocali scherzosi di Emanuele (10:51 e 11:17, scartati come rumore). Foto
delle 10:41 di Raffaele: immagine promozionale/scherzosa a tema
elettrodomestici, tenuta con didascalia neutra. Nessuna menzione di Giovanni
Lima in questa finestra.

Estensione 12:34-19:38 (export delle 20:43): alle 12:34 Emanuele Sciarra
apre un sondaggio per la data della serata promozionale materassi (29/9
10 voti, 6/10 8, 7/10 5, 8/10 8 al momento dell'export) e alle 12:42
sollecita a rispondere in fretta per bloccare una data; Costantino Mariani
non c'e' prima delle 19 e dice sì a tutte le date per sé (per la coppia
dipende), Alessandro Di Benedetto si rende disponibile per l'incontro di
mercoledi' alle 18. In serata (19:33) Emanuele condivide un video Facebook
in cui compare Emidio Cerasani (che risponde alle 19:38: SMG2017). Nessun
vocale, nessun media e nessuna menzione di Giovanni Lima in questa finestra;
il messaggio di sistema delle 12:35 (messaggio fissato) e il resto (saluti,
battute) sono rumore.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-21"

CURATED = {
    ("10:14", "Emanuele Sciarra"): ("info",
        "Comunica di aver contattato i promotori dei materassi (a breve "
        "lo contatteranno i responsabili di zona) e che a breve lo "
        "contatterà anche la referente del Bimby, per vedere se se ne "
        "ricava qualcosa. Aggiunge che all'evento di ieri erano in pochi "
        "ma i presenti si sono complimentati per la presenza e perché il "
        "comitato è già operativo, il che lo rende più fiducioso."),
    ("10:26", "Emanuele Sciarra"): ("domanda",
        "Chiede se qualcuno può reperire il numero di un rappresentante "
        "Kirby, per contattarlo e vedere se fa serate dimostrative con "
        "compenso."),
    ("10:47", "Alessandra Toracchio"): ("info",
        "Comunica di avere un contatto per il Kirby e di far sapere "
        "qualcosa prima di sera."),
    ("10:54", "Antonio Aceto"): ("info",
        "Comunica che questa settimana lavora di pomeriggio e sarà "
        "assente all'incontro con i rappresentanti dei materassi."),
    ("10:56", "Raffaele Di Cesare"): ("info",
        "Dice che si sentirà mercoledì mattina per confermare se riesce "
        "ad esserci all'incontro delle 18."),
    ("11:01", "Alessandra Toracchio"): ("info",
        "Si rende disponibile per l'incontro con i rappresentanti dei "
        "materassi."),
    ("11:04", "Antonio Sabatini"): ("info",
        "Si rende disponibile, eventualmente, per l'incontro con i "
        "rappresentanti dei materassi."),
    ("11:32", "Raffaele Di Cesare"): ("info",
        "Comunica che lui e la sua compagna sono disponibili dal lunedì "
        "al venerdì sera, quindi per lui la serata materassi va bene in "
        "qualunque delle date proposte."),
    ("11:55", "Ugo Trinchini"): ("info",
        "Conferma la propria disponibilità per la serata materassi e "
        "dice che proverà a coinvolgere qualche coppia."),
    ("12:03", "Emanuele Sciarra"): ("domanda",
        "Chiede al gruppo di decidere la data della serata materassi, "
        "così da poterla confermare."),
    ("12:09", "Antonio Aceto"): ("info",
        "Comunica che il 29/9 lavora di mattina, quindi per quella data "
        "è disponibile."),
    ("12:10", "Antonio Sabatini"): ("proposta",
        "Propone un sondaggio flash per capire in quale delle tre date "
        "disponibili c'è più disponibilità nel gruppo; per lui ogni "
        "giorno va bene."),
    ("12:34", "Emanuele Sciarra"): ("proposta",
        "Apre un sondaggio: \"Incontro per serata promozionale "
        "materassi\". Opzioni, con i voti al momento dell'export: 29 "
        "settembre (10 voti), 6 ottobre (8 voti), 7 ottobre (5 voti), "
        "8 ottobre (8 voti)."),
    ("12:42", "Emanuele Sciarra"): ("info",
        "Chiede di rispondere al sondaggio il prima possibile: il "
        "rappresentante gli ha detto che, se le date dovessero essere "
        "occupate, lo avviserebbe, e per garantirsi una data in cui il "
        "comitato incassa qualcosa in più bisogna bloccarla al più "
        "presto."),
    ("13:43", "Costantino Mariani"): ("info",
        "Comunica che per un orario prima delle 19 non può esserci."),
    ("13:46", "Costantino Mariani"): ("info",
        "Dice che per sé vota sì a tutte le date del sondaggio, mentre "
        "per la sua coppia dipende da orari e giorni."),
    ("14:30", "Alessandro Di Benedetto"): ("info",
        "Si rende disponibile per l'incontro di mercoledì alle 18 con "
        "i rappresentanti dei materassi."),
    ("19:33", "Emanuele Sciarra"): ("info",
        "Condivide un video Facebook: "
        "https://www.facebook.com/share/v/1DYEYE5vbj/?mibextid=wwXIfr "
        "e fa notare a Emidio Cerasani che compare anche lui nel video; "
        "Emidio conferma (19:38) che è del SMG2017, il suo primo anno di "
        "sacerdozio."),
}

AUDIO_CURATED = {
    (DATE, "10:50", "Emanuele Sciarra", "PTT-20260921-WA0002.opus"): ("domanda",
        "Riferisce che uno dei rappresentanti dei materassi vuole "
        "incontrarli prima della serata, per spiegare a voce come "
        "funziona (in sintesi: 20 coppie che pagano circa 25 euro a "
        "coppia); servono almeno tre persone del comitato per l'incontro "
        "di mercoledì (dice \"mercoledì 18\", ma presumibilmente intende "
        "il 23/9). Lui ci sarà, perché questa settimana lavora di mattina; "
        "chiede la disponibilità di altre due persone."),
    (DATE, "10:51", "Emanuele Sciarra", "PTT-20260921-WA0003.opus"): ("rumore", ""),
    (DATE, "10:53", "Dante Caniglia", "PTT-20260921-WA0004.opus"): ("domanda",
        "Chiede se, tra le circa 40 persone del gruppo, nessuno conosca "
        "qualcuno che lavora con i materassi (nel vocale trascritto come "
        "\"Matarazzo\", probabilmente \"materasso\") per agganciare un "
        "contatto utile."),
    (DATE, "10:58", "Emanuele Sciarra", "PTT-20260921-WA0005.opus"): ("info",
        "Esprime perplessità sulla resa delle serate materassi: nella "
        "serata precedente, se la venditrice avesse venduto due materassi "
        "il comitato avrebbe avuto 100 euro in più, con il 20% in fattura "
        "riconosciuto ai venditori; a suo parere non vale la pena mettere "
        "in difficoltà qualcuno per una cifra così, ma se qualcuno vuole "
        "davvero comprare perché reputa buono il prodotto ben venga."),
    (DATE, "10:59", "Emanuele Sciarra", "PTT-20260921-WA0006.opus"): ("info",
        "Riporta che l'incontro con il rappresentante dei materassi è "
        "fissato per mercoledì alle 18: spiegherà per sommi capi come "
        "funziona e, se qualcuno mette a disposizione una sala o una casa, "
        "si potrà parlare anche della serata."),
    (DATE, "11:13", "Emanuele Sciarra", "PTT-20260921-WA0007.opus"): ("proposta",
        "Riferisce le condizioni proposte dall'azienda di materassi "
        "(Imperial Life, come trascritto) per queste ultime date: con 24 "
        "coppie pagano 25 euro a coppia, cioè 600 euro; passate queste "
        "date chiedono da 15 a 25 coppie e riconoscono 20 euro a coppia "
        "(con 25 coppie, 500 euro). Le date disponibili sono 29 settembre "
        "e 6, 7 e 8 ottobre. Se in serata si vende un materasso, alla "
        "consegna il comitato riceve 100 euro di bonus; nessun obbligo di "
        "acquisto; si offre un piccolo buffet come già fatto. Chiede il "
        "parere del gruppo per iniziare a fare domanda per la sala "
        "comunale."),
    (DATE, "11:17", "Emanuele Sciarra", "PTT-20260921-WA0008.opus"): ("rumore", ""),
    (DATE, "12:04", "Emanuele Sciarra", "PTT-20260921-WA0011.opus"): ("info",
        "Comunica che non potrà partecipare né il 29/9 (lavora di notte) "
        "né il 6, 7 e 8/10 (lavora di pomeriggio e stacca alle 22)."),
}

MEDIA_OVERRIDES = {
    (DATE, "10:41", "Raffaele Di Cesare", "IMG-20260921-WA0009.jpg"):
        "Immagine promozionale a tema elettrodomestici: un addetto di "
        "negozio circondato da elettrodomestici e da un materasso in "
        "memory foam distribuisce volantini a un banco, accanto a un "
        "banner con la scritta \"Richiedi una dimostrazione! Portiamo il "
        "negozio a casa tua\" (materassi, caffè, cooking), condivisa nel "
        "thread sulle serate dimostrative.",
    (DATE, "11:05", "Emanuele Sciarra", "IMG-20260921-WA0010.jpg"):
        "Screenshot di una chat tra Emanuele Sciarra (che si presenta come "
        "vicepresidente del comitato feste) e la referente Bimby: lui "
        "chiede come ha funzionato l'evento dimostrativo organizzato con "
        "la classe '85 e se il comitato avrebbe avuto un ricavo a "
        "prescindere dalle vendite; lei risponde che l'evento è stato "
        "organizzato con la classe '85 e che lo ripeterebbe volentieri, "
        "ma è in vacanza e chiamerà a fine settimana.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
