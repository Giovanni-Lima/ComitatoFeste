#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-12 — solo dati di curatela, logica comune in digest_lib.py.

Giornata parziale (fino alle 21:07 all'atto di questo export). Mattina
dominata dagli auguri di compleanno a MariaLuisa Cianfaglione (decine di
messaggi "buongiorno"/"auguri" da quasi tutto il gruppo, 07:12-10:06) —
rumore, pura cortesia sociale. Emanuele condivide anche un santino/locandina
della "Peregrinatio delle reliquie di San Camillo" (09:18, parrocchia San
Benedetto dei Marsi, 27/9) — fuori tema comitato, rumore.

Punti rilevanti: Emilio Caniglia annuncia che scriverà una sintesi della
riunione di ieri sera (09:33) e più tardi spiega la questione PEC (09:55) —
risposta alla domanda di Emanuele Sciarra (09:41, se serva una PEC per
scrivere al Comune per la sala) — il comitato non è ancora costituito
giuridicamente, quindi userà la propria PEC personale a nome del gruppo;
Emanuele comunica anche di aver scritto alla rappresentante dell'azienda di
materassi per l'incontro sponsorizzato (09:33) e ipotizza la costituzione
formale del comitato da gennaio (09:45). Luca Cicchelli chiede a quanto
ammonta il fondo cassa (11:50) — nessuna cifra reale in risposta nella
finestra, solo battute (Costantino: "1500 euro per te"); la foto che segue
di Alessandra Toracchio (11:54) NON è la risposta al fondo cassa nonostante
la vicinanza nel thread — è in realtà una versione più leggibile della
lista "Coppia" già vista l'11/9 in foto (stesso gioco/attività), pura
coincidenza di argomenti sovrapposti in chat. Costantino Mariani propone
(dubbioso lui stesso, "buona idea o una stronzata") un torneo di calcio
balilla/cabinato per l'inverno, con foto di un allestimento arcade come
riferimento (11:58-12:00). Resto: battute su chi va con chi/cosa portare
per "venerdì" (evento non specificato, contesto insufficiente per capire
se attinente al comitato — non curato, da rivedere se il gruppo ne parla
in modo più esplicito) e il consueto rumore di reazioni/dialetto.

Coda pomeridiana (13:46-16:34): il "venerdì"/le "coppie" di stamattina si
chiariscono retroattivamente — è l'incontro sponsorizzato con l'azienda
materassi, confermato per **venerdì 18 settembre** (Dante/Alessandra
Simonetti/Elvis/Tina/Ugo si organizzano su chi porta chi, rumore/logistica,
non curato singolarmente). Il pezzo grosso della giornata: **Emilio
Caniglia pubblica la sintesi in 9 punti della riunione dell'11/9** (16:16,
come anticipato al mattino) — testo integrale in CURATED data la rilevanza;
Maria Buttari chiede se è stata decisa una quota di partenza (16:20),
Emilio risponde che se n'è discusso ma l'importo resta da determinare,
introducendo l'idea di una "preadesione" informale nel frattempo (16:32).

Coda serale (19:49-21:07): Emanuele Sciarra propone un raduno di auto
d'epoca (sul modello del Circuito di Avezzano, foto di riferimento da una
ricerca Google allegata) abbinato a uno street food, con la disponibilità a
contattare il Comune per i permessi la settimana successiva se il gruppo è
d'accordo — chiede aiuto per trovare gli stand gastronomici; Dante Caniglia
rilancia con un'idea distinta, portare i carri di carnevale di paesi
vicini (Pescina o Luco) a San Benedetto, ricordando che è già successo una
volta in passato (confermato da Martina Del Gizzi). Ugo Trinchini chiede di
aggiungere Donato e Onorina all'incontro con l'azienda dei materassi.
Nessuna menzione di Giovanni Lima da parte di altri membri in questa
finestra (solo suoi messaggi propri).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-12"

CURATED = {
    ("09:33", "Emilio Caniglia"): ("info",
        "Anticipa che scriverà più tardi una breve sintesi della riunione "
        "di ieri sera."),
    ("09:33", "Emanuele Sciarra"): ("info",
        "Comunica di aver scritto alla rappresentante dell'azienda di "
        "materassi per l'incontro sponsorizzato: aggiornerà il gruppo alla "
        "risposta."),
    ("09:41", "Emanuele Sciarra"): ("domanda",
        "Chiede se per inviare una PEC al Comune (per la sala) serva "
        "necessariamente avere una PEC propria o basti una email normale."),
    ("09:45", "Emanuele Sciarra"): ("info",
        "Aggiunge che il comitato potrebbe costituirsi formalmente ed "
        "entrare in vigore da gennaio."),
    ("09:55", "Emilio Caniglia"): ("info",
        "Risponde sulla PEC: userà la propria PEC personale a nome del "
        "gruppo, dato che il comitato non è ancora costituito e "
        "giuridicamente non esiste; dopo la costituzione si potrà usare "
        "una PEC del legale rappresentante o una delegata. Aggiunge che "
        "una PEC della Pubblica Amministrazione difficilmente accetta "
        "risposte da un indirizzo email ordinario (PEO)."),
    ("11:50", "Luca Cicchelli"): ("domanda",
        "Chiede a quanto ammonta il fondo cassa."),
    ("11:58", "Costantino Mariani"): ("proposta",
        "Propone, senza esserne sicuro lui stesso (\"buona idea o una "
        "stronzata\"), un torneo di calcio balilla/cabinato per l'inverno, "
        "allegando la foto di un allestimento arcade come riferimento."),
    ("16:16", "Emilio Caniglia"): ("info",
        "Pubblica la sintesi in 9 punti della riunione dell'11/9: 1) "
        "introduzione di Emidio con consigli e raccomandazioni per il "
        "gruppo; 2) confronto sulla visita a Corinaldo (offerte ricevute, "
        "prenotazioni, proposte per far cassa); 3) incontro sponsorizzato "
        "con l'azienda di materassi confermato per venerdì 18 settembre — "
        "formazione delle coppie, buffet, da lunedì attenzione maggiore "
        "per arrivare pronti; 4) sede del Comitato: convergenza sul locale "
        "offerto da Elvis presso il corso (meno di 50€ per l'attacco alla "
        "corrente, 70€/mese); 5) apprezzamento generale per le "
        "applicazioni a supporto del Comitato; 6) Halloween & San Martino: "
        "incertezza legata alla Proloco, servirà interfacciarsi con loro "
        "prima di decidere; 7) confronto sulle entrate dei Comitati "
        "precedenti; 8) proposte di Raffaele (parete mobile di "
        "arrampicata, traslazione del corpo di Santa Maria Goretti, eventi "
        "con il CAI, altre idee); 9) confronto generale sulle attività del "
        "Comitato (cantante big di agosto, festività patronali di giugno, "
        "confronto tra Comitati precedenti e attuale)."),
    ("16:20", "Maria Buttari"): ("domanda",
        "Chiede se è stata decisa una quota di partenza, per poterla "
        "versare non appena saputo l'importo."),
    ("16:32", "Emilio Caniglia"): ("info",
        "Risponde a Maria: se n'è discusso in riunione ma l'importo resta "
        "da determinare; propone nel frattempo una \"preadesione\" del "
        "tutto informale (iscrizione + versamento quota su un modulo alla "
        "prossima riunione), utile anche per farsi un'idea del numero di "
        "persone del futuro Comitato."),
    ("19:49", "Emanuele Sciarra"): ("proposta",
        "Propone di organizzare un raduno di auto d'epoca (sul modello del "
        "Circuito di Avezzano) abbinato a uno street food nello stesso "
        "evento; ha già verificato cosa serve organizzativamente e, se il "
        "gruppo è d'accordo, si mette in contatto col Comune la settimana "
        "successiva per i permessi — anche il Comune avrebbe già pensato a "
        "un evento simile ma senza tempo per realizzarlo. Chiede aiuto per "
        "trovare gli stand gastronomici."),
    ("20:11", "Ugo Trinchini"): ("info",
        "Chiede di aggiungere Donato e Onorina alla lista per l'incontro "
        "con l'azienda dei materassi."),
    ("21:04", "Dante Caniglia"): ("proposta",
        "Propone, come idea alternativa/aggiuntiva, di accordarsi con i "
        "paesi vicini (Pescina o Luco) che organizzano carri di carnevale "
        "per farli passare anche a San Benedetto — era già successo una "
        "volta in passato, molti anni fa."),
}

MEDIA_OVERRIDES = {
    (DATE, "11:54", "Alessandra Toracchio", "IMG-20260912-WA0005.jpg"):
        "Foto di una pagina di quaderno scritta a mano, titolo \"Coppia\" "
        "— versione più leggibile della stessa lista di coppie vista in "
        "foto l'11/9 (gioco/attività di gruppo), due colonne di nomi "
        "numerate, non un resoconto del fondo cassa nonostante la "
        "posizione nel thread.",
    (DATE, "11:59", "Costantino Mariani", "IMG-20260912-WA0006.jpg"):
        "Foto di un allestimento con cabinati arcade d'epoca (Pac-Man, "
        "Golden Axe, flipper Spider-Man) e sgabelli, presa come "
        "riferimento/ispirazione per la proposta di torneo invernale.",
    (DATE, "19:54", "Emanuele Sciarra", "IMG-20260912-WA0014.jpg"):
        "Screenshot di una ricerca Google (\"auto d'epoca avezzano\") sul "
        "Circuito di Avezzano - Abruzzo Gran Tour, preso come riferimento "
        "per la proposta di raduno di auto d'epoca.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
