#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-05 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 12:44-17:15 (coda aggiunta il 5/11 stesso con l'export Dropbox delle
17:31). Emanuele conferma che le castagne per San Martino stanno asciugando e
saranno pronte la settimana prossima (foto). Propone poi di far rivivere la
vecchia tradizione dei barattolini di latta attaccati alle biciclette dei
bambini (Cesare conferma la fattibilità). Ilenia ed Elvis portano concretezza
alla discussione sulle calze della Befana aperta ieri da Emanuele: foto di
esempio, un modello trovato su unigadget.it e un confronto sui prezzi in base
alla quantità. Costantino interviene sulla discussione Capodanno con una
proposta di mediazione (chi non partecipa aiuta con la pubblicità, chi
festeggia di solito altrove fa un piccolo sacrificio), trovando consenso.
Emanuele si informa sui costi dei tagliandini/cartelle della tombola. Segue
logistica sui pagamenti della gita a Corinaldo. Nel tardo pomeriggio: un
chiarimento tra Antonio Aceto ed Elvis sul senso della proposta di
Costantino (risolto con reciproco accordo); l'aggiornamento di Emilio su
Andrea Di Loreto (ora libero da altri impegni) e sulla scadenza di venerdì
6/11 per decidere se procedere col Capodanno; la valutazione di fattibilità
di Emanuele con la voce (non confermata) che la Rupe non faccia il veglione
quest'anno; infine il confronto economico tra Emilio ed Emanuele sui margini
in base al numero di partecipanti. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-05"

CURATED = {
    ("13:50", "Costantino Mariani"): ("proposta",
        "Riallacciandosi alla discussione sul Capodanno, concorda sul "
        "peso economico per le famiglie ma propone che chi non "
        "partecipa al veglione possa comunque aiutare a pubblicizzare "
        "l'evento per portare gente, e che chi di solito festeggia "
        "fuori casa provi comunque a fare un piccolo sacrificio per "
        "stare insieme al comitato quella sera. Ugo ed Elvis si dicono "
        "d'accordo."),
    ("15:23", "Maria Buttari"): ("info",
        "Chiede a chi versare i soldi per la gita a Corinaldo; Antonio "
        "Sabatini risponde che può darli a lui, precisando che non è "
        "urgente (va bene anche il giorno dopo in riunione) e che il "
        "pullman Bianchi Tour è già stato pagato. Confermano insieme 3 "
        "posti: Maria, il marito Cesidio e il figlio Gabriele."),
    ("16:43", "Emilio Caniglia"): ("proposta",
        "Informa che il giorno prima è stato contattato da Andrea Di "
        "Loreto, che ha confermato di non avere più altri impegni per "
        "Capodanno. Sottolinea che venerdì 6/11 bisogna prendere una "
        "decisione se continuare o meno con l'organizzazione — non tanto "
        "per il comitato quanto per correttezza verso il Ragno e verso "
        "Di Loreto — e che, in assenza di sufficiente disponibilità dei "
        "membri, è meglio valutare bene la situazione prima di "
        "proseguire."),
    ("17:09", "Emilio Caniglia"): ("info",
        "Fa notare che è difficile attirare partecipanti con un costo "
        "superiore a 100€ a persona, e che il margine di sicurezza "
        "economico si è avuto solo quando, come l'anno scorso, ha "
        "partecipato anche la classe (30-40-50 persone del comitato su "
        "una percentuale di circa 250 partecipanti). Conferma la voce, "
        "non verificata con certezza, secondo cui la Rupe potrebbe non "
        "organizzare il proprio veglione quest'anno."),
}

AUDIO_CURATED = {
    (DATE, "14:55", "Emanuele Sciarra", "PTT-20261105-WA0015.opus"): ("info",
        "Riferisce di aver chiesto alla moglie dove sono stati fatti i "
        "tagliandini e le cartelle della tombola e quanto sono "
        "costati: la grafica è di Alessia Costanza, ma non sa ancora "
        "se siano stati stampati dove lavora lei o in tipografia, né "
        "il costo esatto; si aggiorna appena ha notizie."),
}

MEDIA_OVERRIDES = {
    (DATE, "12:44", "Emanuele Sciarra", "IMG-20261105-WA0009.jpg"):
        "Foto di grandi quantità di castagne stese ad asciugare a terra "
        "in un locale di deposito, in vista di San Martino; Emanuele "
        "conferma che la settimana prossima saranno pronte e portate a "
        "casa.",
    (DATE, "13:37", "Ilenia Piccozzi", "IMG-20261105-WA0011.jpg"):
        "Foto di una calza di Natale rossa e bianca, semplice, appesa a "
        "una parete, con una spilletta rotonda applicata: esempio delle "
        "calze usate l'anno scorso dal comitato.",
    (DATE, "13:37", "Ilenia Piccozzi", "IMG-20261105-WA0012.jpg"):
        "Screenshot dal sito unigadget.it di una calza di Natale "
        "personalizzabile modello \"Nobo\" (cod. CX1013-05), prezzo a "
        "partire da 0,39€, disponibilità 48.555 pezzi.",
    (DATE, "13:44", "Elvis Ippoliti", "IMG-20261105-WA0014.jpg"):
        "Screenshot della tabella sconti-quantità dello stesso "
        "prodotto: 0,47€ da 1 pezzo, 0,43€ da 250, 0,39€ da 500 (IVA "
        "esclusa).",
}

AUDIO_MERGES = [
    {
        "anchor_time": "13:35",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Emanuele propone di far rivivere una vecchia tradizione "
            "del paese: decorare le biciclette dei bambini con "
            "barattolini di latta attaccati dietro (spunto venuto dalla "
            "moglie, per il figlio), per poi regalarne anche agli altri "
            "bambini del comitato — pensando inizialmente ai propri "
            "figli e a quelli di Antonio Aceto, in modo che gli altri "
            "si aggreghino di conseguenza. Cesare conferma che si può "
            "fare, servono solo i barattoli."
        ),
        "members": [
            "PTT-20261105-WA0007.opus", "PTT-20261105-WA0008.opus",
        ],
    },
    {
        "anchor_time": "13:37",
        "anchor_sender": "Ilenia Piccozzi",
        "type": "proposta",
        "text": (
            "Ilenia posta due foto come esempio per le calze della "
            "Befana (idea aperta il giorno prima da Emanuele): la calza "
            "semplice usata l'anno scorso e lo screenshot di una calza "
            "personalizzabile \"Nobo\" trovata su unigadget.it, a "
            "partire da 0,39€. Il gruppo apprezza ed Emanuele, "
            "scherzosamente, ne sottolinea la convenienza visto il "
            "prezzo (\"aggiudicate!\"). Segue un confronto sui prezzi in "
            "base alla quantità: Elvis calcola 0,47€ per 200 pezzi, "
            "0,43€ per 250; Barbara segnala che anche Ugo aveva trovato "
            "lo stesso sito allo stesso prezzo. Elvis posta anche lo "
            "screenshot della tabella sconti del prodotto e, con almeno "
            "800 pezzi (quantità minima indicata da Ilenia), calcola un "
            "prezzo di 0,39€ a pezzo; condivide infine il link del "
            "prodotto: https://www.unigadget.it/it/calza-di-natale-"
            "nobo---PP9484"
        ),
        "members": [
            "PTT-20261105-WA0013.opus",
        ],
    },
    {
        "anchor_time": "16:12",
        "anchor_sender": "Elvis Ippoliti",
        "type": "info",
        "text": (
            "Prosegue la discussione sul Capodanno: ad alcuni messaggi di "
            "Antonio Aceto, che ribadisce di non poter \"fare i conti in "
            "tasca\" a chi non ha la disponibilità economica per il "
            "veglione e di non condividere la posizione di Costantino, "
            "Elvis risponde spiegando il senso del messaggio di "
            "Costantino: chi festeggia comunque altrove farebbe meglio a "
            "venire al veglione del comitato per stare insieme, non per "
            "obbligo ma perché la spesa, tanto, la farebbe comunque; "
            "ritiene inoltre che si sarebbe dovuto chiarire fin "
            "dall'inizio chi fosse davvero disponibile, prima di "
            "contattare Di Loreto, ma che con una decina di persone si "
            "possa comunque procedere. Antonio Aceto si scusa, dicendo "
            "di aver fraintenso e di essere ora d'accordo col "
            "ragionamento di Costantino. Elvis ribadisce la stessa "
            "lettura: è giusto che chi di solito festeggia fuori casa "
            "faccia un piccolo sacrificio per stare insieme, senza che "
            "nessuno sia costretto."
        ),
        "members": [
            "PTT-20261105-WA0016.opus", "PTT-20261105-WA0017.opus",
            "PTT-20261105-WA0018.opus", "PTT-20261105-WA0019.opus",
        ],
    },
    {
        "anchor_time": "16:45",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Dopo l'aggiornamento di Emilio su Di Loreto e sulla scadenza "
            "di venerdì, Emanuele valuta fattibile organizzare il "
            "Capodanno con le circa dieci persone attualmente "
            "disponibili, sottolineando che aiutare il gruppo a portare "
            "gente e a pubblicizzare l'evento conta indipendentemente "
            "dalla partecipazione personale di ciascuno; si rimette "
            "comunque alla volontà della maggioranza. Segnala poi una "
            "voce di corridoio, non confermata, secondo cui la Rupe "
            "potrebbe non fare il veglione quest'anno, il che "
            "aumenterebbe le possibilità di attirare i loro ragazzi; "
            "Antonio Aceto commenta scherzosamente che, se fosse vero, "
            "\"sbancherebbero\"."
        ),
        "members": [
            "PTT-20261105-WA0020.opus", "PTT-20261105-WA0021.opus",
        ],
    },
    {
        "anchor_time": "17:13",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Rispondendo al punto economico di Emilio, Emanuele sostiene "
            "che il margine di guadagno resterebbe simile anche portando "
            "150-180 persone invece di 250 (stima 1.000-2.000€), e "
            "propone di chiedere sostegno anche al gruppo \"gli anni "
            "86\", come già fatto per Corinaldo con alcuni dei suoi "
            "membri. Conclude con una riflessione più ampia: un veglione "
            "capace di attirare anche i più giovani (come succedeva "
            "quando, da ragazzo, al veglione si mescolavano generazioni "
            "diverse) toglierebbe loro la tentazione di spendere gli "
            "stessi soldi per una serata a Pescara; ribadisce comunque "
            "di rimettersi, come sempre, alla volontà della "
            "maggioranza."
        ),
        "members": [
            "PTT-20261105-WA0022.opus", "PTT-20261105-WA0023.opus",
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES)
