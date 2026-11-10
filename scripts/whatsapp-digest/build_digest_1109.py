#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-09 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:41-20:44 (coda aggiunta il 10/11 con l'export Dropbox delle
9:38). Emanuele, dopo la gita di ieri, si attiva per cercare altre
animatrici da proporre a Gianvito per Capodanno, e gira la locandina di
"Christmas World" a Villa Borghese (Roma) come possibile nuova meta di
gita, chiedendo il parere del gruppo. Ilenia mette a disposizione dei
faretti e delle aste del comitato, utili per l'illuminazione di San
Martino. Antonio Sabatini comunica l'incasso di 880€ dalla gita di
Corinaldo. Ugo è in contatto con Paolo degli "Uncini d'Abruzzo" (nome poi
corretto in "Leoncini d'Abruzzo" nella sintesi di Emilio del 10/11),
disponibili a venire in sede in serata per un preventivo. Nel pomeriggio
Emanuele propone una gita libera a Napoli per il 29/11: segue un lungo
confronto con Alessandro Di Benedetto, Elvis e Maria su organizzazione,
responsabilità e calendario già fitto di impegni, che si chiude senza
decisione (rimandato al confronto di persona in sede). In serata Elvis
riporta indicazioni sulle dosi di vin brulé per San Martino. Nessuna
menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-09"

CURATED = {
    ("07:41", "Emanuele Sciarra"): ("proposta",
        "Dopo la bella giornata di ieri, comunica che proverà a sentire "
        "Marta Malatesti per vedere se conosce altre animatrici, in modo "
        "da avere più preventivi da presentare a Gianvito per Capodanno. "
        "Gira poi la locandina di \"Christmas World\", il villaggio di "
        "Natale a Villa Borghese (Roma, dal 28 novembre al 10 gennaio), "
        "come possibile nuova meta di gita; chiede il parere del gruppo "
        "e, se d'accordo, si informerà sul prezzo d'ingresso."),
    ("10:17", "Ilenia Piccozzi"): ("proposta",
        "Comunica di avere 3 faretti (già usati da Pietro per suonare) "
        "e delle aste di supporto, chiedendo se possano servire per "
        "l'illuminazione di San Martino. Barbara ed Elvis confermano "
        "che sarebbero utili; Antonio Aceto nota che potrebbero servire "
        "anche per la cottura delle castagne. Emilio annota la "
        "disponibilità, osservando che i faretti sono comodi perché "
        "direzionabili tramite l'asta."),
    ("10:19", "Ilenia Piccozzi"): ("info",
        "Comunica di aver ricontattato Antonella, che a breve girerà "
        "qualche contatto per l'animazione."),
    ("11:30", "Antonio Sabatini"): ("info",
        "Comunica che dalla giornata di ieri sono entrati nella cassa "
        "del comitato ben 880€, un risultato definito un successo "
        "assoluto che dà energia ed entusiasmo verso il prossimo "
        "obiettivo."),
    ("15:25", "Emanuele Sciarra"): ("proposta",
        "Vista la buona riuscita della gita a Corinaldo, propone di "
        "organizzare una gita libera a Napoli per il 29 novembre "
        "(sfruttando anche i mercatini di Natale), aperta a chiunque "
        "indipendentemente dalla partecipazione a Corinaldo; chiede "
        "aiuto con le prenotazioni. Barbara si offre di mettere a "
        "disposizione il proprio numero per le prenotazioni; Luca "
        "coglie l'occasione per chiedere chi cura la pagina social, "
        "visto che andrebbe sfruttata di più per pubblicizzare gite ed "
        "eventi. Emanuele risponde che se ne occupano lui e Chiara, ma "
        "serve l'aiuto di tutti per poter seguire più fronti insieme "
        "(lui la gita, Emilio San Martino)."),
    ("20:44", "Elvis Ippoliti"): ("info",
        "Riporta il consiglio del padre sulle dosi di vin brulé per San "
        "Martino: 0,2 litri sarebbe troppo, l'anno scorso si serviva "
        "circa mezzo bicchiere per 1€; domani si farà mandare i "
        "bicchieri avanzati per valutare la misura, anche perché il "
        "vino è piuttosto dolce e un bicchiere pieno potrebbe risultare "
        "eccessivo."),
}

MEDIA_OVERRIDES = {
    (DATE, "07:41", "Emanuele Sciarra", "IMG-20261109-WA0000.jpg"):
        "Screenshot di un post Facebook su \"Christmas World\", il "
        "villaggio di Natale a Villa Borghese (Roma), con luna park, "
        "pista di pattinaggio e mercatini, dal 28 novembre 2026 al 10 "
        "gennaio 2027, ingresso a pagamento.",
    (DATE, "10:16", "Ilenia Piccozzi", "IMG-20261109-WA0005.jpg"):
        "Foto di un faretto da lavoro con lungo cavo elettrico e "
        "innesto filettato per il montaggio su un'asta.",
}

AUDIO_CURATED = {
    (DATE, "11:41", "Ugo Trinchini", "PTT-20261109-WA0008.opus"): ("proposta",
        "Comunica di essere in contatto con Paolo degli \"Uncini "
        "d'Abruzzo\", disponibili a venire in sede stasera per "
        "illustrare un preventivo; invita chi può a essere presente per "
        "ascoltare la proposta. Più tardi conferma che l'incontro è "
        "fissato per le 20 circa."),
    (DATE, "11:50", "Emanuele Sciarra", "PTT-20261109-WA0009.opus"): ("info",
        "Risponde a Ugo confermando la propria disponibilità per "
        "l'incontro con Paolo degli \"Uncini d'Abruzzo\", chiedendo solo "
        "l'orario."),
    (DATE, "19:04", "Elvis Ippoliti", "PTT-20261109-WA0027.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {
        "anchor_time": "16:25",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Continua il confronto sulla gita a Napoli. Emanuele "
            "chiarisce che non si tratterebbe di una gita guidata e "
            "programmata come quella di Corinaldo, ma di una \"gita "
            "libera\" sul modello già sperimentato con il comitato "
            "\"gli 85\": il pullman lascia e ricarica il gruppo a un "
            "orario fissato (vicino a Piazza Plebiscito), e ognuno è "
            "libero di visitare quel che preferisce (Cristo velato, "
            "San Gregorio Armeno, Spaccanapoli, ecc.), senza bisogno di "
            "un itinerario organizzato; chiedere aiuto al gruppo serve "
            "solo a dividersi i fronti (lui si occuperebbe della gita, "
            "Emilio di San Martino, altri di Capodanno), non per "
            "mancanza di volontà di fare da solo. Alessandro Di "
            "Benedetto apprezza l'iniziativa ma invita alla cautela: un "
            "evento di questa portata andrebbe organizzato con un "
            "itinerario e discusso prima in riunione, vista anche la "
            "scarsa esperienza pregressa del comitato. Elvis è dello "
            "stesso parere: prima di fare locandine o pubblicità "
            "bisogna verificare la disponibilità reale delle persone, e "
            "chi organizza si assume comunque una responsabilità "
            "(anche se, chiarisce poi Emanuele, il contratto e "
            "l'assicurazione del pullman restano in capo alla ditta/"
            "agenzia noleggiatrice); ricorda inoltre che il calendario "
            "è già fitto di impegni ravvicinati (San Martino, "
            "l'appuntamento del 6 dicembre con Don Enzo, poi Natale, "
            "Tombolata, Capodanno e le calze della Befana) e che le "
            "decisioni vanno sempre prese e votate in riunione. Maria "
            "aggiunge che, se i più giovani possono preferire una gita "
            "libera, le persone più grandi vorrebbero piuttosto un "
            "itinerario guidato da seguire insieme. Emanuele, pur "
            "condividendo in buona parte le obiezioni, fa notare che "
            "aspettare la riunione di venerdì lascerebbe solo 13 giorni "
            "per organizzare tutto (vista la data del 29), e porta a "
            "sostegno della fattibilità gli esempi dei comitati \"gli "
            "85\" e \"gli 84\", che in passato hanno organizzato gite "
            "anche con meno di due settimane di preavviso riempiendo il "
            "pullman; Luca nota che invece le gite \"degli 86\" sono "
            "andate meno bene per scarsa partecipazione (30 persone "
            "alla loro gita a Corinaldo). Nel frattempo Luca segnala "
            "che \"gli 86\" starebbero valutando un tavolo proprio a "
            "Capodanno, con una decina/quindicina di partecipanti già "
            "confermati tramite Antonella. Visto il perdurare del "
            "confronto, Emanuele decide di non insistere oltre "
            "(\"abolita la questione gita a Napoli\") e invita chi può "
            "a vedersi quella sera stessa in sede per parlarne di "
            "persona."
        ),
        "members": [
            "PTT-20261109-WA0012.opus", "PTT-20261109-WA0013.opus",
            "PTT-20261109-WA0014.opus", "PTT-20261109-WA0015.opus",
            "PTT-20261109-WA0016.opus", "PTT-20261109-WA0017.opus",
            "PTT-20261109-WA0018.opus", "PTT-20261109-WA0020.opus",
            "PTT-20261109-WA0021.opus", "PTT-20261109-WA0022.opus",
            "PTT-20261109-WA0023.opus", "PTT-20261109-WA0024.opus",
            "PTT-20261109-WA0025.opus", "PTT-20261109-WA0026.opus",
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES)
