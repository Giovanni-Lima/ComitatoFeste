#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-13 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 06:50-13:31 (export Dropbox delle 13:42, giornata ancora in corso
al momento dell'export, un giorno prima di San Martino, sabato 14/11).
Alessandra compra i guanti nuovi e organizza il cappello per il costume
con Elvis e Barbara (che mette a disposizione anche una paglietta per lo
spaventapasseri). Costantino mostra in video, da vicino, il campanaccio
recuperato (risolvendo la richiesta del giorno prima). Antonio Aceto
conferma che le padelle gli verranno consegnate a casa. Emilio lancia il
sondaggio sulla pubblicità con "Cannelor", che risulta conveniente
considerati tutti gli eventi dell'anno (inclusa la richiesta della Pro
Loco per l'accensione dell'albero); esce anche l'articolo di stampa
richiesto il giorno prima. Il gruppo discute se vendere l'acqua in
bottiglia ai bambini (Ilenia è contraria, temendo che tolga vendite al
vino) e risolve con la stessa formula del vino: offerta libera, senza
listino esposto. Tina chiede il piano B in caso di pioggia; le previsioni
confermano cielo nuvoloso ma asciutto. Dante nota che il quartiere
Cittadella sta già costruendo il proprio albero di Natale. Nessuna
menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-13"

CURATED = {
    ("06:50", "Alessandra Toracchio"): ("info",
        "Buongiorno: ha preso i guantoni nuovi (da lavoro, per "
        "maneggiare le castagne/braceri)."),
    ("09:10", "Antonio Aceto"): ("info",
        "Buongiorno: le padelle per cuocere le castagne gli vengono "
        "consegnate oggi direttamente a casa."),
    ("12:47", "Serena Di Stefano"): ("domanda",
        "Chiede se questa sera c'è la riunione."),
}

MEDIA_OVERRIDES = {
    (DATE, "13:25", "Emanuele Sciarra", "IMG-20261113-WA0021.jpg"):
        "Screenshot delle previsioni meteo orarie per San Benedetto dei "
        "Marsi: cielo nuvoloso, temperature tra 8° e 12°, nessuna "
        "precipitazione prevista — a conferma di quanto detto da "
        "Costantino.",
    (DATE, "13:31", "Dante Caniglia", "IMG-20261113-WA0020.jpg"):
        "Screenshot da un'altra chat (gruppo \"Cittadella\"): il "
        "quartiere Cittadella sta già montando la struttura in legno "
        "del proprio albero di Natale; Dante nota che anche il "
        "Comitato dovrebbe pensare a qualcosa di simile per "
        "partecipare.",
    (DATE, "07:42", "Costantino Mariani", "VID-20261113-WA0000.mp4"):
        "Video (3s) in cui, dopo averlo promesso la sera prima, mostra "
        "da vicino il campanaccio di metallo recuperato, tenendolo in "
        "mano.",
}

AUDIO_CURATED = {
    (DATE, "13:19", "Emanuele Sciarra", "PTT-20261113-WA0012.opus"): ("rumore", ""),
    (DATE, "13:20", "Emanuele Sciarra", "PTT-20261113-WA0013.opus"): ("rumore", ""),
    (DATE, "13:20", "Costantino Mariani", "PTT-20261113-WA0014.opus"): ("rumore", ""),
    (DATE, "13:21", "Emanuele Sciarra", "PTT-20261113-WA0015.opus"): ("rumore", ""),
    (DATE, "13:21", "Emanuele Sciarra", "PTT-20261113-WA0016.opus"): ("rumore", ""),
    (DATE, "13:22", "Emanuele Sciarra", "PTT-20261113-WA0018.opus"): ("rumore", ""),
    (DATE, "13:23", "Emanuele Sciarra", "PTT-20261113-WA0019.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {
        "anchor_time": "13:11",
        "anchor_sender": "Dante Caniglia",
        "type": "decisione",
        "text": (
            "Sul dibattito sull'acqua, Dante rassicura che non si "
            "tratta di fare concorrenza ai bar. Valentina propone "
            "allora di non mettere l'acqua nel listino esposto, "
            "tenendola sotto il banco: chi la chiede ce l'ha, "
            "altrimenti non viene offerta attivamente; chiede a Luca "
            "di verificare se si possa fare. Luca apprezza l'idea, "
            "scherzando di \"acqua di contrabbando\". Costantino "
            "chiarisce che comunque non si tratterebbe di una vera "
            "vendita, ma di un'offerta libera come per il vino: si dà "
            "l'acqua e si lascia a chi la prende un'offerta libera di "
            "un euro a bottiglietta, esattamente come già si fa con il "
            "vino e con le castagne. Luca ed Elvis concordano."
        ),
        "members": [
            "PTT-20261113-WA0003.opus", "PTT-20261113-WA0005.opus",
            "PTT-20261113-WA0006.opus", "PTT-20261113-WA0007.opus",
            "PTT-20261113-WA0008.opus", "PTT-20261113-WA0009.opus",
            "PTT-20261113-WA0010.opus", "PTT-20261113-WA0011.opus",
        ],
    },
]

TEXT_MERGES = [
    {
        "anchor_time": "06:51",
        "anchor_sender": "Alessandra Toracchio",
        "type": "proposta",
        "text": (
            "Alessandra chiede a Elvis come vuole il cappello (per il "
            "costume), così lo procurano e stasera porta tutto in "
            "sede. Barbara dice di avere una paglietta; Elvis pensa "
            "possa andare bene, e se ce n'è un'altra disponibile una "
            "la userebbe lui e l'altra per lo spaventapasseri. Il "
            "gruppo conferma, lasciando comunque aperta la possibilità "
            "di trovare qualcosa di più adatto."
        ),
        "members": [
            ["06:51", "Alessandra Toracchio"], ["06:53", "Barbara Rizio"],
            ["06:53", "Elvis Ippoliti"], ["06:54", "Emanuele Sciarra"],
            ["06:54", "Maria Buttari"], ["06:54", "Barbara Rizio"],
            ["06:55", "Luca Cicchelli"], ["06:55", "Elvis Ippoliti"],
            ["06:55", "Barbara Rizio"], ["06:56", "Barbara Rizio"],
            ["06:57", "Elvis Ippoliti"], ["06:58", "Barbara Rizio"],
        ],
    },
    {
        "anchor_time": "10:09",
        "anchor_sender": "Emilio Caniglia",
        "type": "proposta",
        "text": (
            "Emilio, considerato l'impegno di spesa, propone un "
            "sondaggio per decidere sulla pubblicità con il bando "
            "cittadino tramite Daniele \"Cannelor\", precisando che "
            "l'argomento sarà comunque riportato in riunione e che la "
            "proposta serve solo ad accelerare i tempi vista "
            "l'imminenza di San Martino. Lancia quindi il sondaggio:\n\n"
            "SONDAGGIO: Bando cittadino con Daniele \"Cannelor\"\n"
            "OPZIONE: Sì al pacchetto completo (250 euro da saldare a "
            "fine mandato) (15 voti)\n"
            "OPZIONE: Sì, solo a chiamata (25 euro per ogni giro di "
            "macchina) (1 voto)\n"
            "OPZIONE: No (sia per il pacchetto completo che per "
            "singola chiamata) (0 voti)\n\n"
            "Spiega poi che il pacchetto completo copre tutti gli "
            "eventi e le feste a prescindere dal numero di giri di "
            "macchina (San Martino compreso, con un giro stasera e uno "
            "domani mattina). Alla domanda di Valentina se convenga "
            "solo con più di 10 eventi da sponsorizzare, Emilio elenca "
            "gli eventi in programma (San Martino, Tombolata, l'evento "
            "delle calze, più la richiesta della Pro Loco di una "
            "presenza all'accensione dell'albero in coincidenza con i "
            "mercatini di Natale, e tutte le feste da Sant'Antonio ad "
            "Agosto), oltre all'aiuto del bando per annunciare questua "
            "e banchetto; fissa poi il messaggio del sondaggio. "
            "Valentina conclude che allora conviene."
        ),
        "members": [
            ["10:09", "Emilio Caniglia"], ["10:14", "Emilio Caniglia"],
            ["10:16", "Emilio Caniglia"], ["10:16", "Valentina D'Arcadia"],
            ["10:19", "Emilio Caniglia"], ["10:21", "Valentina D'Arcadia"],
        ],
    },
    {
        "anchor_time": "10:21",
        "anchor_sender": "Alessandra Toracchio",
        "type": "info",
        "text": (
            "Alessandra condivide un link Facebook "
            "(https://www.facebook.com/share/1FVaVS4N34/): è uscito "
            "l'articolo su San Benedetto richiesto il giorno prima a "
            "Marsica Live/Terre Marsicane/AZ Informa. Valentina esulta "
            "di essere stata ascoltata; Elvis scherza chiedendo se "
            "basti dire che si è visto un asino volante per avere un "
            "articolo, e Valentina risponde che, viste le circostanze, "
            "potrebbe anche provarci."
        ),
        "members": [
            ["10:21", "Alessandra Toracchio"], ["10:21", "Valentina D'Arcadia"],
            ["10:23", "Elvis Ippoliti"], ["10:24", "Valentina D'Arcadia"],
            ["10:24", "Elvis Ippoliti"],
        ],
    },
    {
        "anchor_time": "11:42",
        "anchor_sender": "Valentina D'Arcadia",
        "type": "proposta",
        "text": (
            "Valentina fa notare che si è pensato al vino ma non "
            "all'acqua, dopo una battuta ricevuta in merito; Emanuele "
            "chiede se piova, Valentina osserva che con tanti bambini "
            "presenti le bottigliette d'acqua converrebbe venderle, "
            "proponendo una decina di fardelli da 24 (miste "
            "naturale/frizzante) per circa 42,50€, poi rivista a 10 "
            "fardelli (misti). Luca si offre di portarne un paio di "
            "suo. Emanuele scherza sul far bere subito vino ai "
            "bambini. Antonio Sabatini consiglia di ridurre a 240 "
            "bottigliette circa, con un 60% naturale e 40% leggermente "
            "frizzante, per contenere la spesa; Valentina si assesta "
            "su 6 fardelli naturali (144 bottigliette) e 4 leggermente "
            "frizzanti (96), evitando le frizzanti pure. Ilenia "
            "dissente: ricorda che agli eventi a cui ha partecipato "
            "con bambini l'acqua si compra sempre al bar, che il "
            "comitato deve puntare a vendere il vino (se i bambini "
            "bevono acqua non comprano vino), che ai bambini deve "
            "pensarci la Pro Loco e non il comitato, che il comitato "
            "ai bambini offre già i dolcetti. Alessandra precisa che "
            "si parlava comunque di acqua per i bambini, mica per far "
            "bere vino a loro. Valentina ribatte che comunque vendendo "
            "le bottigliette a 1€ sono soldi che rientrano; Ilenia si "
            "dice d'accordo se vengono vendute (pensava si dovessero "
            "offrire gratis)."
        ),
        "members": [
            ["11:42", "Valentina D'Arcadia"], ["11:42", "Emanuele Sciarra"],
            ["11:43", "Valentina D'Arcadia"], ["11:44", "Valentina D'Arcadia"],
            ["11:45", "Antonio Aceto"], ["11:46", "Barbara Rizio"],
            ["11:46", "Luca Cicchelli"], ["11:47", "Valentina D'Arcadia"],
            ["11:47", "Emanuele Sciarra"], ["11:49", "Elvis Ippoliti"],
            ["11:50", "Valentina D'Arcadia"], ["11:52", "Luca Cicchelli"],
            ["11:53", "Maria Buttari"], ["11:53", "Valentina D'Arcadia"],
            ["11:58", "Antonio Sabatini"], ["12:00", "Valentina D'Arcadia"],
            ["12:50", "Ilenia Piccozzi"], ["12:52", "Ilenia Piccozzi"],
            ["12:54", "Alessandra Toracchio"], ["12:54", "Ilenia Piccozzi"],
            ["12:55", "Ilenia Piccozzi"], ["13:00", "Valentina D'Arcadia"],
            ["13:01", "Ilenia Piccozzi"],
        ],
    },
    {
        "anchor_time": "13:22",
        "anchor_sender": "Tina Giarrante",
        "type": "domanda",
        "text": (
            "Tina chiede come sia previsto il meteo per domani e quale "
            "fosse il piano B; Costantino risponde che si farebbe "
            "dentro la chiesa, e che secondo le previsioni domani "
            "dovrebbe essere nuvoloso ma non piovoso."
        ),
        "members": [
            ["13:22", "Tina Giarrante"], ["13:22", "Costantino Mariani"],
            ["13:24", "Costantino Mariani"],
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES)
