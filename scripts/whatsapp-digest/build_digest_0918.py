#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-18 — solo dati di curatela, logica comune in digest_lib.py.

Giornata dell'incontro sponsorizzato Sanimed Italia (sala consiliare, ore
21). Mattina di soli saluti (rumore), più un video di Raffaele Di Cesare
(08:59, VID-20260918-WA0002.mp4) con traccia audio (verificato a mano,
niente ffprobe su questa macchina) quindi un video vero, ma senza ffmpeg/cv2
non è stato possibile vederne il contenuto: tenuto con didascalia
generica di default, segnalato a parte. Nel pomeriggio (14:21) Emanuele
Sciarra inoltra un vocale della referente Sanimed sul pagamento della
serata (contanti o bonifico) e sul tipo di ricevuta fiscale da emettere
(donazione all'associazione se registrata con timbro, altrimenti
prestazione occasionale sul codice fiscale del presidente); segue lo
scambio con Emilio Caniglia (che deciderà sentendo Antonio Sabatini) e
la conferma dell'orario della serata (21:00, dimostratrice sul posto
verso le 20:30, monta il suo baldacchino). Nessuna menzione di Giovanni
Lima da parte di altri in questa finestra (unico messaggio con il suo nome:
un suo "Buongiorno", rumore).

Sera (18:55-23:40, aggiornata con l'export delle 18:56 del 19/9): Emanuele
chiede chi porta cosa per la serata e segue il thread sul buffet (Tina,
Alessandra Toracchio, pizza rossa di Alessandra Simonetti e Antonella
Profeta); Emilio ricorda orario/luogo (20:50, sala consiliare); Alessandra
Toracchio e Emanuele elencano gli avanzi/le bevande comprate. Lunga catena
di vocali tra Costantino Mariani ed Emanuele (19:03-19:45) per la consegna
della cassa d'acqua, accorpata in un'unica entry (AUDIO_MERGES), più
battute sulle rotonde: tenuto a parte solo il vocale di Costantino delle
19:38 con l'idea del raduno di fuoristrada. Emanuele (19:48, vocale) propone
una serata materassi al mese (una il mese prossimo, una a novembre) più
eventuali depuratori; Costantino (20:24) approva. Foto: screenshot della
card dell'app condiviso da Giovanni Lima ("Trop fort", 18:58), foto di una
rotonda di Costantino, torte salate di Barbara Rizio (20:06). La foto delle
19:17 di Alessandra Toracchio è il ri-inoltro dell'elenco buffet già digest
il 15/9 (stesso file), scartata come duplicato; lo sticker delle 19:18 è
ignorato in automatico. Dopo la serata (23:23) Antonio Aceto chiede com'è
andata: Emanuele risponde "i primi 5 pippi presi", cioè 500 euro.
Restano rumore: gli arrivi/spostamenti (20:32-20:56), le battute
dialettali e il vocale di Costantino delle 20:24 (poco intelligibile).
Nessuna menzione di Giovanni Lima da parte di altri in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-18"

CURATED = {
    ("14:22", "Emanuele Sciarra"): ("info",
        "Comunica che per il pagamento della serata di stasera il comitato "
        "accetterà i contanti."),
    ("14:23", "Emanuele Sciarra"): ("domanda",
        "Chiede a Emilio Caniglia (presidente) il suo codice fiscale per "
        "poter emettere la ricevuta come prestazione occasionale, e se va "
        "bene procedere così per poter rispondere alla referente Sanimed."),
    ("14:28", "Emilio Caniglia"): ("info",
        "Risponde che sentirà più tardi Antonio Sabatini e decideranno "
        "come procedere."),
    ("14:34", "Elvis Ippoliti"): ("domanda",
        "Chiede a che ora inizia la serata di stasera."),
    ("14:35", "Emanuele Sciarra"): ("info",
        "Risponde che la serata inizia alle 21, ma la ragazza che farà la "
        "dimostrazione sarà sul posto verso le 20:30 e intanto monta il "
        "suo baldacchino."),
    ("18:55", "Emanuele Sciarra"): ("domanda",
        "Chiede chi porta cosa per la serata di stasera, per essere sicuri "
        "di avere tutto. Risposte nel thread: Tina Giarrante porta i "
        "vassoi per le patatine e la crostata di Ilenia Piccozzi; "
        "Alessandra Toracchio porta patatine, acqua e aranciata/succo "
        "avanzati da venerdì scorso; Alessandra Simonetti e Antonella "
        "Profeta portano anche la pizza rossa; la cassa d'acqua di "
        "Costantino Mariani viene consegnata a Tina, davanti alla casa del "
        "sindaco."),
    ("19:01", "Emilio Caniglia"): ("info",
        "Ricorda che l'incontro sponsorizzato pubblicitario si terrà "
        "questa sera alle 20:50 nella sala consiliare del Comune, durata "
        "circa un'ora - un'ora e mezza; per il rinfresco vale la lista con "
        "gli incarichi assegnati da Alessandra Toracchio."),
    ("19:22", "Alessandra Toracchio"): ("info",
        "Comunica cosa è avanzato da venerdì scorso per il buffet: 8-9 "
        "pacchi di patatine, 1 Coca Cola, 1 aranciata, 1 tè."),
    ("19:23", "Emanuele Sciarra"): ("info",
        "Comunica di aver comprato 2 aranciate, un tè alla pesca e uno al "
        "limone; quello che avanza si tiene per la prossima serata."),
    ("23:23", "Antonio Aceto"): ("domanda",
        "Chiede com'è andata la serata con Sanimed; Emanuele Sciarra "
        "risponde che sono stati presi i primi \"5 pippi\", cioè 500 euro "
        "(un \"pippo\" vale 100 euro nel gergo del gruppo)."),
}

AUDIO_CURATED = {
    (DATE, "14:21", "Emanuele Sciarra", "AUD-20260918-WA0007.opus"): ("domanda",
        "Inoltra il vocale ricevuto dalla referente Sanimed Italia sui "
        "dettagli del pagamento di stasera: serve sapere se sarà in "
        "contanti o con bonifico, e quale ricevuta fiscale emettere — se "
        "l'associazione è registrata (con timbro) la ricevuta sarà una "
        "donazione all'associazione; altrimenti si può usare il codice "
        "fiscale del presidente con descrizione \"prestazione "
        "occasionale\". Chiede una risposta entro il pomeriggio, prima "
        "dell'arrivo della relatrice."),
    (DATE, "19:38", "Costantino Mariani", "PTT-20260918-WA0026.opus"): ("proposta",
        "Conferma di aver consegnato la cassa d'acqua e, ripassando da una "
        "rotonda, lancia l'idea di organizzare un raduno di fuoristrada "
        "(offroad)."),
    (DATE, "19:48", "Emanuele Sciarra", "PTT-20260918-WA0029.opus"): ("proposta",
        "Ha altri due contatti per serate materassi e propone di "
        "organizzarne una al mese (la prossima il mese prossimo, un'altra "
        "a novembre), cercando poi di inserire anche qualche serata con i "
        "depuratori; chiede il parere del gruppo (Costantino Mariani "
        "approva)."),
    (DATE, "20:24", "Costantino Mariani", "PTT-20260918-WA0031.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {"anchor_time": "19:03", "anchor_sender": "Costantino Mariani",
     "type": "info",
     "text": "Accordi a voce tra Costantino Mariani ed Emanuele Sciarra per "
             "il passaggio della cassa d'acqua per la serata: Costantino, "
             "fuori tutto il giorno, non sa a che ora rientra e chiede a "
             "chi consegnarla; dopo vari scambi la consegna avviene (19:38).",
     "members": ["PTT-20260918-WA0010.opus", "PTT-20260918-WA0011.opus",
                 "PTT-20260918-WA0016.opus", "PTT-20260918-WA0017.opus",
                 "PTT-20260918-WA0018.opus", "PTT-20260918-WA0019.opus",
                 "PTT-20260918-WA0020.opus", "PTT-20260918-WA0021.opus",
                 "PTT-20260918-WA0022.opus", "PTT-20260918-WA0023.opus",
                 "PTT-20260918-WA0024.opus", "PTT-20260918-WA0025.opus",
                 "PTT-20260918-WA0027.opus", "PTT-20260918-WA0028.opus"]},
]

MEDIA_OVERRIDES = {
    (DATE, "18:58", "Giovanni Lima", "IMG-20260918-WA0009.jpg"):
        "Screenshot dell'app Comitato feste 87 (vista Agenda) con la card "
        "di Emanuele Sciarra delle 16:55 sul buffet del 18/9 (contributi di "
        "Ilenia, Tina, Antonella e Alessandra), condiviso con il commento "
        "\"Trop fort\".",
    (DATE, "19:05", "Costantino Mariani", "IMG-20260918-WA0012.jpg"):
        "Foto scattata dall'auto di una rotonda in campagna, con le "
        "montagne sullo sfondo al tramonto, condivisa per scherzo nel "
        "thread sulla consegna dell'acqua.",
    (DATE, "20:06", "Barbara Rizio", "IMG-20260918-WA0030.jpg"):
        "Foto di due vassoi di torte salate già tagliate a quadrati, "
        "pronte per il buffet della serata (didascalia: \"Torte salate "
        "pronte\").",
}

# Video di Raffaele (08:59) escluso su richiesta di Giovanni: contenuto non
# visibile (niente ffmpeg/cv2 su questa macchina), non vale tenerlo con
# didascalia generica.
# IMG-20260915-WA0031.jpg (19:17, Alessandra Toracchio): ri-inoltro
# dell'elenco buffet già digest il 15/9 alle 22:01, stesso file, scartato.
_SKIP_FILES = {"VID-20260918-WA0002.mp4", "IMG-20260915-WA0031.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="video escluso su richiesta + forward duplicato")
