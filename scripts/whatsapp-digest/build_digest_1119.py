#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-19 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:07-19:44 (export Dropbox delle 20:48, giornata ancora in corso).
Cappellino col logo 1987: pareri del gruppo (troppo nero, meglio un po' di
giallo), Emanuele precisa che si tratta solo di bozze di Giacomo Gentile e
che il prototipo sarà fatto dopo averne verificato la fattibilità; girano
altre alternative (giallo, nero con patch gialla, bordi gialli). Mattina:
Maikel scarica dal furgone il materiale (tamburo per le castagne) e si
organizza con Barbara (sedia da portare in sede) e Emanuele (gazebo suo, da
lasciare in sede; la macchina gira-castagne va ripresa per cambiare i
riduttori). Elvis chiede di eliminare la pagina Facebook "Classe 1987" usata
per le pubblicità: Emanuele la elimina, Dante avrebbe preferito renderla
privata (pagina di 20 anni) e ne segue un chiarimento a voce. Sera: Emanuele
ripropone il sondaggio sui badge (cinque proposte) per il banchetto delle
offerte di Sant'Antonio del mese prossimo. Il resto è rumore (battute, una
GIF). In tarda serata Alessandra mostra un esempio del badge vincitore
(opzione 5) con un nome reale, chiedendo conferma; si aspetta la fine del
sondaggio per preparare la lista nome/cognome. Antonio Aceto solleva il
dubbio se includere "patronali" nella dicitura (come faceva il comitato
dell'86); Elvis chiede di informarsi bene prima di procedere — questione
che si risolverà il giorno dopo. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-19"

CURATED = {}

AUDIO_CURATED = {}

AUDIO_MERGES = [
    {
        "anchor_time": "08:56", "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Emanuele precisa che il cappellino mostrato è solo un "
            "prototipo/bozza fatto da Giacomo Gentile per dare l'idea, non "
            "il colore scelto. Si danno più opzioni: Giacomo legge i "
            "messaggi e dirà se è fattibile; intanto, se ognuno dice la "
            "sua, si trova l'incontro per farlo (se lo si vuole). Ha "
            "girato le bozze di Giacomo e se ne decide venerdì in "
            "riunione."
        ),
        "members": ["PTT-20261119-WA0001.opus", "PTT-20261119-WA0002.opus"],
    },
    {
        "anchor_time": "09:50", "anchor_sender": "Maikel Montano",
        "type": "info",
        "text": (
            "Logistica del materiale: Maikel ha il materiale sul furgone "
            "(che deve portare dal meccanico) e chiede di chi sia e dove "
            "lasciarlo, altrimenti lo scarica al magazzino. Barbara dice "
            "che la sedia si può tenere e portare alla sede; poi spiega che "
            "non è nemmeno sua: stava dall'agosto alla fermata dell'autobus "
            "vicino a Gianvito e nessuno l'ha mai ripresa, e pensava potesse "
            "servire per la scenografia. Maikel la porterà alla sede. "
            "Emanuele: il gazebo è suo e si può lasciare in sede per "
            "riutilizzarlo; la macchina gira-castagne va invece ripresa "
            "per cambiare i riduttori di velocità."
        ),
        "members": [
            "PTT-20261119-WA0005.opus", "PTT-20261119-WA0006.opus",
            "PTT-20261119-WA0007.opus", "PTT-20261119-WA0008.opus",
            "PTT-20261119-WA0010.opus", "PTT-20261119-WA0011.opus",
        ],
    },
    {
        "anchor_time": "18:39", "anchor_sender": "Elvis Ippoliti",
        "type": "info",
        "text": (
            "Chiarimenti a voce sulla pagina Facebook eliminata (la "
            "ricostruzione dai vocali non è del tutto chiara): Elvis dice "
            "che quella pagina era stata creata ai tempi della pagina del "
            "comitato, invece di un taccuino, e che l'aveva creata Emanuele "
            "con Antonio in riunione; Dante ricorda che all'inizio si era "
            "detto di modificare la pagina della classe; Emanuele spiega "
            "che anziché creare la pagina aveva creato il gruppo la sera "
            "della riunione e poi l'ha eliminato perché non serviva."
        ),
        "members": [
            "PTT-20261119-WA0058.opus", "PTT-20261119-WA0062.opus",
            "PTT-20261119-WA0066.opus",
        ],
    },
    {
        "anchor_time": "22:24",
        "anchor_sender": "Antonio Aceto",
        "type": "domanda",
        "text": (
            "Alessandra mostra un esempio del badge scelto con un nome "
            "reale, chiedendo conferma che sia la versione definitiva; "
            "Emanuele conferma, dicendo che aspetteranno la fine del "
            "sondaggio per poi fare la lista con nome e cognome di "
            "tutti e prepararli. Alessandra chiede a Maikel nome e "
            "cognome per non sbagliare (Maikel lo fornisce). Antonio "
            "Aceto chiede se non si debba inserire anche la dicitura "
            "\"patronali\", ricordando che il comitato dell'86 "
            "scriveva sempre \"Comitato Feste Patronali, San Benedetto "
            "dei Marsi\", visto che si tratta appunto del comitato "
            "delle feste patronali e non di un comitato generico per "
            "qualsiasi evento. Elvis ribadisce che secondo lui bisogna "
            "prima informarsi bene su cosa vada scritto, prima di "
            "procedere con i badge."
        ),
        "members": ["PTT-20261119-WA0072.opus", "PTT-20261119-WA0073.opus"],
    },
]

TEXT_MERGES = [
    {
        "anchor_time": "08:07", "anchor_sender": "Ilenia Piccozzi",
        "type": "info",
        "text": (
            "Pareri sul cappellino col logo 1987: Ilenia lo trova carino ma "
            "non lo indosserebbe (le piace di più il secondo modello); "
            "Alessandra lo trova troppo nero e suggerisce un po' di giallo "
            "per spezzare; Tina lo metterebbe, forse meglio con il logo su "
            "sfondo giallo; Emidio, Barbara e Valentina approvano "
            "(Valentina: nero con il logo giallo, se si può)."
        ),
        "members": [["08:07", "Ilenia Piccozzi"], ["08:09", "Alessandra Toracchio"],
                    ["09:21", "Tina Giarrante"], ["09:23", "Emidio Cerasani"],
                    ["09:26", "Barbara Rizio"], ["09:28", "Valentina D'Arcadia"]],
    },
    {
        "anchor_time": "12:43", "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Altre alternative per il cappellino: Emanuele gira una "
            "versione gialla (Alessandra: no grazie, Tina concorda) e "
            "Antonio Aceto un'altra proposta; Emanuele riferisce che "
            "Giacomo, prima di fare un prototipo, vuole verificare la "
            "fattibilità. Antonella trova bella l'idea ma non lo "
            "indosserebbe (non ha mai usato cappelli), Alessandra dice che "
            "è bello e lo vuole; Emanuele gira un'altra prova con i bordi "
            "gialli."
        ),
        "members": [["12:43", "Emanuele Sciarra"], ["14:23", "Alessandra Toracchio"],
                    ["14:42", "Emanuele Sciarra"], ["14:42", "Antonio Aceto"],
                    ["14:45", "Tina Giarrante"], ["14:48", "Antonella Profeta"],
                    ["14:55", "Alessandra Toracchio"], ["14:56", "Emanuele Sciarra"]],
    },
    {
        "anchor_time": "16:41", "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Elvis ha chiesto di cancellare la pagina Facebook (usata solo "
            "per le pubblicità, \"non ci fa bene\"): Emanuele provvede. "
            "Dante avrebbe preferito che non fosse cancellata ma resa "
            "privata, come prima; Emanuele risponde che ormai l'ha "
            "eliminata e Dante commenta che era una pagina di 20 anni."
        ),
        "members": [["16:41", "Emanuele Sciarra"], ["17:43", "Dante Caniglia"],
                    ["17:44", "Emanuele Sciarra"], ["18:34", "Dante Caniglia"]],
    },
    {
        "anchor_time": "19:43", "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Emanuele ripropone il sondaggio sui badge (cinque proposte "
            "allegate) per potersi organizzare in vista del mese prossimo, "
            "quando inizierà il banchetto per le offerte di Sant'Antonio. "
            "SONDAGGIO \"Bedge\": opzione 1 (3 voti), opzione 2 (1 voto), "
            "opzione 3 (0 voti), opzione 4 (1 voto), opzione 5 (7 voti). "
            "Sul badge andranno scritti nome e cognome."
        ),
        "members": [["19:42", "Emanuele Sciarra"], ["19:43", "Emanuele Sciarra"],
                    ["19:44", "Emanuele Sciarra"]],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "08:57", "Emanuele Sciarra", "IMG-20261119-WA0003.jpg"):
        "Screenshot della scheda di un modello di cappellino di lana a "
        "risvolto da personalizzare con una toppa, con la tavolozza dei "
        "colori disponibili (nero, verde, blu, rosso, grigio, bianco, "
        "giallo fluo, rosa...).",
    (DATE, "08:57", "Emanuele Sciarra", "IMG-20261119-WA0004.jpg"):
        "Screenshot della scheda di un altro modello di cappellino a "
        "risvolto, taglia unica, con i colori disponibili.",
    (DATE, "09:50", "Maikel Montano", "IMG-20261119-WA0014.jpg"):
        "L'interno del furgone di Maikel con il tamburo metallico con "
        "motore per cuocere le castagne e altro materiale da scaricare.",
    (DATE, "12:43", "Emanuele Sciarra", "IMG-20261119-WA0039.jpg"):
        "Alternativa per il cappellino: cappellino di lana giallo chiaro "
        "con la toppa rettangolare \"1987\" a cifre composte da scene di "
        "videogiochi.",
    (DATE, "14:38", "Antonio Aceto", "IMG-20261119-WA0047.jpg"):
        "Proposta di Antonio Aceto: cappellino nero con toppa gialla "
        "rettangolare con \"1987\" a cifre di videogiochi.",
    (DATE, "14:56", "Emanuele Sciarra", "IMG-20261119-WA0046.jpg"):
        "Altra prova con i bordi gialli: cappellino nero con toppa nera e "
        "\"1987\" contornato di giallo.",
    (DATE, "15:53", "Elvis Ippoliti", "IMG-20261119-WA0045.jpg"):
        "Screenshot del gruppo Facebook \"Classe 1987 San Benedetto dei "
        "Marsi\" (gruppo pubblico, 89 membri) con in evidenza un post "
        "pubblicitario; didascalia di Elvis: \"Cancellate questa pagina che "
        "la usano solo per le pubblicità e non ci fa bene\".",
    (DATE, "19:42", "Emanuele Sciarra", "IMG-20261119-WA0067.jpg"):
        "Badge, opzione 1: grafica gialla \"Comitato Feste - San Benedetto "
        "dei Marsi\" con cabinato arcade, \"1987\" e il campo del nome "
        "(esempio \"Emilio\").",
    (DATE, "19:42", "Emanuele Sciarra", "IMG-20261119-WA0068.jpg"):
        "Badge, opzione 2: stessa grafica gialla con cabinato arcade e "
        "\"1987\", scritte in blu scuro.",
    (DATE, "19:42", "Emanuele Sciarra", "IMG-20261119-WA0069.jpg"):
        "Badge, opzione 3: variante della grafica gialla con cabinato "
        "arcade, \"1987\" e nome, con un'altra resa delle scritte.",
    (DATE, "19:42", "Emanuele Sciarra", "IMG-20261119-WA0070.jpg"):
        "Badge, opzione 4: versione orizzontale \"Comitato Festa - San "
        "Benedetto dei Marsi\" con scritte cromate, cabinato arcade, "
        "\"1987\" e nome.",
    (DATE, "19:42", "Emanuele Sciarra", "IMG-20261119-WA0071.jpg"):
        "Badge, opzione 5: versione orizzontale \"Comitato Festa - San "
        "Benedetto dei Marsi\" con scritte rosa, cabinato arcade, "
        "\"1987\" e nome.",
    (DATE, "21:25", "Alessandra Toracchio", "IMG-20261120-WA0000.jpg"):
        "Esempio del badge scelto (opzione 5) applicato con un nome "
        "reale: grafica gialla con cabinato arcade, \"1987\", "
        "\"Comitato Feste San Benedetto dei Marsi\" ed \"Emilio "
        "Caniglia\"; Alessandra chiede conferma che sia la versione "
        "definitiva.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES)
