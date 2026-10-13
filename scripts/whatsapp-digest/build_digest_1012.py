#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-12 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:33-15:05. Emilio apre la giornata con un aggiornamento: sabato
17/10 al rustico di Ugo dimostrazione pubblicitaria Bimby (con la proposta
commerciale completa), più il promemoria dell'incontro del 16 ottobre con
l'azienda dei materassi (servono 20 coppie). Tutto il giorno arrivano
adesioni sparse per il 16 (TEXT_MERGES), con due screenshot di Emilio che
riepilogano la tabella coppie aggiornata. In parallelo (09:08-11:21) un
dibattito sulla quota di partecipazione per i bambini alla gita di
Corinaldo: Emilio spiega la composizione della quota attuale (30€, di cui
~10€ di offerta al futuro comitato) e propone di esentare i bambini in
riunione; il gruppo discute se sia sostenibile e converge più su un
ridotto che su una gratuità totale, senza decisione definitiva in questa
finestra. Chiude un breve siparietto: Emilio cancella per errore anche un
messaggio di Ugo insieme al proprio.

Coda serale (19:47, 22:14-22:21): un'ultima adesione per il 16 ottobre, poi
riprende il thread del gira-castagne — Emanuele ha trovato una lavatrice
(cestello da 10 kg) e punta a farne saldare i pezzi la settimana
successiva per i primi test; Maikel conferma la quantità di castagne
concordata. Nessuna menzione di Giovanni Lima da parte di altri in questa
finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-12"

CURATED = {
    ("07:33", "Emilio Caniglia"): ("decisione",
        "Annuncia che sabato 17 ottobre pomeriggio, presso il rustico di "
        "Ugo, ci sarà una dimostrazione pubblicitaria del Bimby con "
        "probabili acquirenti e interessati: con 4 acquisti il comitato "
        "riceverà un Bimby in omaggio. Proposta commerciale: 1.599€ "
        "pagamento unico, 1.638€ a 24 rate a tasso zero, 1.420€ con IVA "
        "agevolata (legge 104) — tutte con kit pane Bimby in omaggio. Chi "
        "è interessato (anche conoscenti/parenti) può contattare lui, "
        "Emanuele o Ugo. Ricorda inoltre l'incontro promozionale del 16 "
        "ottobre con l'azienda dei materassi: serve raggiungere 20 "
        "coppie, chi è disponibile (anche singolarmente) lo scriva in "
        "chat. Ringrazia Emanuele e Ugo per l'organizzazione "
        "dell'evento Bimby."),
    ("07:42", "Emanuele Sciarra"): ("info",
        "Spiega perché serve sapere subito quanti potenziali acquirenti "
        "Bimby ci sono: lui si è già iscritto come rivenditore, e il "
        "bonus di un Bimby omaggio ogni 4 venduti scatta una sola volta "
        "per persona iscritta. Al momento ci sono 6 potenziali "
        "acquirenti: con altri 2 si potrebbe iscrivere anche un secondo "
        "membro e arrivare a 2 Bimby in omaggio; in alternativa, oltre il "
        "4° venduto si guadagnerebbero 100€ a Bimby — chiede se puntare "
        "sul guadagno immediato o sul secondo Bimby omaggio."),
    ("07:48", "Emanuele Sciarra"): ("info",
        "Precisa che chi è interessato all'acquisto non deve per forza "
        "venire sabato: si può organizzare anche un incontro singolo con "
        "la venditrice in un secondo momento."),
    ("09:08", "Alessandra Simonetti"): ("domanda",
        "Chiede se i bambini pagano la stessa quota degli adulti per la "
        "gita, notando che non se n'era ancora discusso: per una famiglia "
        "numerosa, 30€ a testa è una cifra importante."),
    ("09:43", "Emilio Caniglia"): ("info",
        "Risponde che la quota di 30€ è la stessa usata dalle classi 1985 "
        "e 1986: circa 20€ coprono il costo del trasporto a persona, i "
        "restanti ~10€ sono un'offerta al futuro comitato (come già "
        "accaduto negli anni passati). Propone di avanzare alla prossima "
        "riunione l'esenzione dei bambini dal pagamento, rimettendo la "
        "decisione finale al voto del gruppo."),
    ("09:45", "Alessandra Simonetti"): ("proposta",
        "Riferisce di aver già detto che i bambini pagano come gli "
        "adulti (occupano comunque un posto) e nota che non si era "
        "pensato a una riduzione per invogliare le famiglie a "
        "partecipare; propone di vedere come vanno le prenotazioni "
        "intanto. Alessandro chiede se si sa come si sono comportati gli "
        "altri comitati e propone di decidere subito in chat la quota "
        "(anche per fascia d'età), per non farsi trovare impreparati al "
        "momento delle prenotazioni. Maria propone un biglietto ridotto "
        "per i bambini (non gratuito), con eventuale gratuità solo per i "
        "più piccoli (3-4 anni), suggerendo di verificare come hanno "
        "fatto i comitati precedenti. Emanuele propone 20€ per i bambini "
        "fino a 12 anni (età limite usata in molti eventi); ricorda che "
        "per la gita a Napoli non avevano fatto pagare i bambini sotto i "
        "2 anni, ma fa notare che oggi si paga l'intero pullman e non i "
        "singoli posti, quindi un pullman di soli bambini andrebbe in "
        "perdita. Antonio Sabatini avverte che un'esenzione totale "
        "farebbe perdere soldi al comitato: un ridotto è più sostenibile. "
        "Vanessa si informa su come si è comportato il comitato '86 e "
        "conferma che hanno fatto pagare 30€ anche ai bambini, con la "
        "stessa logica \"un posto, un prezzo\". Nessuna decisione "
        "definitiva in questa finestra: se ne riparlerà in riunione, come "
        "anticipato da Emilio."),
    ("10:09", "Costance Rossi"): ("info",
        "Comunica di non potersi rendere disponibile per il 16, ma si "
        "offre come rappresentante del comitato per l'evento di sabato "
        "17, se serve."),
    ("14:42", "Emilio Caniglia"): ("info",
        "Spiega che cancellando un proprio messaggio ha accidentalmente "
        "cancellato anche un messaggio di Ugo Trinchini, scusandosi; "
        "Alessandro Di Benedetto commenta scherzosamente \"c'è aria di "
        "dittatura\"."),
    ("19:47", "Alessandra Simonetti"): ("info",
        "Comunica a Emilio di poter aggiungere altre due persone alla "
        "lista del 16 ottobre: Cristina e Giampiero."),
    ("22:20", "Maikel Montano"): ("domanda",
        "Chiede conferma sulla quantità di castagne concordata (3 "
        "quintali?)."),
}

AUDIO_CURATED = {
    (DATE, "22:14", "Emanuele Sciarra", "PTT-20261012-WA0017.opus"): ("info",
        "Riferisce di aver trovato la lavatrice per il gira-castagne: la "
        "settimana prossima proverà a far saldare tutti i pezzi "
        "necessari e a fare le prime prove di cottura; chiede aggiornamenti "
        "sulla disponibilità di castagne."),
    (DATE, "22:20", "Emanuele Sciarra", "PTT-20261012-WA0019.opus"): ("info",
        "Conferma la quantità di castagne: la cuoceranno anche in "
        "occasione di Sant'Antonio, il resto lo congeleranno."),
    (DATE, "22:21", "Emanuele Sciarra", "PTT-20261012-WA0020.opus"): ("info",
        "Riferisce di aver trovato fortunosamente una lavatrice da 10 kg, "
        "con un cestello abbastanza grande."),
    (DATE, "22:15", "Emanuele Sciarra", "PTT-20261012-WA0018.opus"): ("rumore", ""),
}

MEDIA_OVERRIDES = {
    (DATE, "09:03", "Emilio Caniglia", "IMG-20261012-WA0002.jpg"):
        "Tabella \"Coppie\" per l'incontro del 16 ottobre, prima versione "
        "(5 coppie su 24 posti): Antonio A.-Jennifer, Raffaele-Verdiana, "
        "Elvis-Tina, Emilio-Federica, Silvano-Barbara.",
    (DATE, "14:41", "Emilio Caniglia", "IMG-20261012-WA0003.jpg"):
        "Tabella \"Coppie\" aggiornata (12 coppie su 20 posti): oltre alle "
        "prime 5, si aggiungono Alessandro-Patrizia, Cesare-Alessandra S., "
        "Maurizio-Valentina, Andrea R.-Rossella, Antonio Sabatini (senza "
        "partner indicato), Ugo-Cassandra, Donato-Onorina.",
}

TEXT_MERGES = [
    {
        "anchor_time": "07:35",
        "anchor_sender": "Antonio Aceto",
        "type": "info",
        "text": (
            "Prosegue la raccolta delle coppie per l'incontro del 16 "
            "ottobre: confermano Antonio Aceto con Jennifer, Tina (ancora "
            "in cerca di un accompagnatore), Elvis, Emanuele (al 90%, "
            "aggiorna più tardi per i turni di lavoro), Barbara con "
            "Silvano, Alessandro Di Benedetto con Patrizia, Cesare, "
            "Alessandra Simonetti (disponibile solo dopo le 21:30 per "
            "impegni di lavoro, abbinata scherzosamente a Cesare), "
            "Valentina D'Arcadia con Maurizio, Antonio Sabatini, e altre "
            "due coppie segnalate da Alessandra Simonetti (Rossella e "
            "\"Ricciolone\")."
        ),
        "members": [
            ["07:35", "Antonio Aceto"], ["07:37", "Tina Giarrante"],
            ["07:37", "Elvis Ippoliti"], ["07:39", "Emanuele Sciarra"],
            ["08:47", "Barbara Rizio"], ["10:41", "Alessandro Di Benedetto"],
            ["11:50", "Cesare Raglione"], ["11:51", "Alessandra Simonetti"],
            ["12:11", "Valentina D'Arcadia"], ["12:12", "Antonio Sabatini"],
            ["12:51", "Alessandra Simonetti"], ["12:53", "Alessandra Simonetti"],
        ],
    },
]

# VID-20261012-WA0013.mp4 (15:05, Elvis): nessuna traccia audio (verificato
# con lo script di supporto, ffprobe non disponibile su questa macchina) —
# è una GIF di reazione mascherata da mp4, non un video vero.
_SKIP_FILES = {"VID-20261012-WA0013.mp4"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="gif di reazione mascherata da mp4")
