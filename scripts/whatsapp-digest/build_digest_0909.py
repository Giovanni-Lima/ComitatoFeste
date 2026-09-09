#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-09 — solo dati di curatela, logica comune in digest_lib.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-09"

CURATED = {
    ("14:20", "Costantino Mariani"): ("domanda",
        "Chiede conferma se la riunione si terrà venerdì (data uscita vincitrice dal "
        "sondaggio dell'8/9)."),
    ("14:29", "Emilio Caniglia"): ("info",
        "Condivide i dati storici dei comitati precedenti (classi 1982, 1983 e 1985 — "
        "mancano 1984 e 1986) per una stima sommaria delle entrate: nel tempo sono aumentati "
        "i biglietti venduti (23.000 nel 1982, 26.900 nel 1983, 40.000 nel 1985) ma sono "
        "diminuite le offerte della comunità e degli sponsor. Si chiede se lo sforzo sulla "
        "vendita dei biglietti tolga energie alla ricerca di sponsor/offerte, sperando in una "
        "risposta più chiara quando arriveranno i dati (mancanti) delle classi '84 e '86."),
    ("14:54", "Emilio Caniglia"): ("info",
        "Segnala che il solo cachet dei The Kolors equivale al budget totale dei comitati "
        "precedenti: la classe '86 deve quindi aver avuto entrate aggiuntive oltre al "
        "contributo comunale (10-15mila euro)."),
    ("14:55", "Elvis Ippoliti"): ("info",
        "Ipotizza che le entrate aggiuntive della classe '86 vengano da un mix di contributo "
        "comunale (10-15mila euro), sponsor (altri 10-15mila euro) e circa 10.000 biglietti "
        "venduti in più rispetto al comitato '85."),
    ("14:56", "Antonio Sabatini"): ("info",
        "Segnala che la classe '86 aveva praticamente già assicurato il primo premio della "
        "lotteria (valore stimato 20-25mila euro); Elvis Ippoliti puntualizza (14:57) che "
        "probabilmente lo hanno comunque pagato circa 5-6mila euro, comunque una spesa "
        "minore rispetto ad acquistarlo a prezzo pieno."),
    ("15:04", "Ilenia Piccozzi"): ("info",
        "Segnala che la classe '86 ha speso circa 120.000 euro da gennaio ad agosto."),
    ("15:05", "Elvis Ippoliti"): ("info",
        "Fa notare che per la classe '85 i conti tornano sommando 89mila euro di budget "
        "proprio, i 15mila euro del comune e i 10mila euro di biglietti venduti in più."),
    ("15:06", "Ilenia Piccozzi"): ("info",
        "Precisa che nel mese di giugno la classe '86 non ha organizzato nulla (serate a "
        "costo zero), un fattore da considerare nel confronto dei budget."),
    ("15:07", "Elvis Ippoliti"): ("proposta",
        "Propone di organizzare quante più iniziative possibili mettendoci la manodopera "
        "del gruppo e con materiali a basso costo, per massimizzare gli introiti."),
    ("15:22", "Emanuele Sciarra"): ("proposta",
        "Propone di preparare anche per il comitato un modello prestampato per gli sponsor "
        "(come il tariffario della classe '86 condiviso poco prima da Ugo Trinchini), da "
        "mostrare quando si cercano sponsor."),
    ("15:25", "Emilio Caniglia"): ("decisione",
        "Conferma che il prestampato sponsor sarà preparato, proponendo di integrarlo "
        "pensando anche ad altre forme di pubblicità."),
    ("15:55", "Emilio Caniglia"): ("domanda",
        "Pone una domanda strategica al gruppo: a differenza della classe '86 (che aveva "
        "campo libero, con la Proloco non ancora costituita), il comitato dovrà sempre "
        "mediare con la Proloco per gli eventi (spazi, ripartizione introiti, ecc.). Chiede "
        "se convenga investire energie nel collaborare con la Proloco oppure cercare un "
        "settore senza concorrenza (es. pellegrinaggi religiosi, sponsorizzazioni come "
        "quella dei materassi) — se \"il gioco valga la candela\" nel collaborare con la "
        "Proloco — chiedendo il parere di tutti."),
    ("16:01", "Elvis Ippoliti"): ("info",
        "Risponde che la questione va approfondita, ma ritiene che il comitato debba "
        "comunque avere propri spazi per gli eventi, non pensando che la Proloco occuperà "
        "tutti i mesi."),
    ("16:03", "Ugo Trinchini"): ("info",
        "Concorda sul collaborare con la Proloco, ma cercando comunque uno spazio proprio "
        "senza creare intralcio a nessuno."),
    ("16:33", "Ilenia Piccozzi"): ("info",
        "Concorda: dovrebbe essere la Proloco a essere di supporto al comitato, non il "
        "contrario."),
    ("16:33", "Maria Buttari"): ("info",
        "La collaborazione con la Proloco va bene, ma serve comunque qualcosa di \"tutto "
        "nostro\": meglio puntare su eventi propri."),
    ("17:21", "Raffaele Di Cesare"): ("proposta",
        "Presenta due proposte in vista della riunione: 1) tentare di far venire a San "
        "Benedetto, in concomitanza della festa di agosto, il corpo di Santa Maria Goretti "
        "(oltre alla reliquia dell'ulna già portata da Corinaldo) — un evento inedito che "
        "unirebbe le comunità di San Benedetto, Corinaldo e Nettuno, coinvolgendo Don "
        "Francesco e suo padre (ex sindaco) per i contatti istituzionali (il corpo era già "
        "venuto nel 2012, ma in inverno, mai in agosto); 2) organizzare eventi a costo zero a "
        "tema montagna sfruttando le sue qualifiche CAI: portare per 3-4 giorni la parete "
        "mobile di arrampicata del CAI (con vendita di biglietti), organizzare escursioni e "
        "serate a tema per far conoscere il territorio montano, e proporre incontri nelle "
        "scuole sul tema; propone anche di occuparsi della discesa della Befana dai "
        "campanili."),
    ("17:30", "Emidio Cerasani"): ("info",
        "Appoggia l'idea degli eventi a tema montagna per le nuove generazioni, ma fa "
        "notare (scherzosamente) che San Benedetto è più un paese di campagna che di "
        "montagna. Sul corpo di Santa Maria Goretti, riferisce che il nuovo parroco si sta "
        "già muovendo per valutare un'eventuale \"peregrinatio\"; ricorda inoltre il marzo "
        "2012, quando il vescovo Santoro la proclamò compatrona del paese."),
    ("17:36", "Dante Caniglia"): ("proposta",
        "Alla luce del report di Emilio e del trend emerso, propone come obiettivi la "
        "vendita paritaria dei biglietti e l'aumento delle sponsorizzazioni, puntando a "
        "riportare gli sponsor ai livelli del 1983 per avere più margine."),
    ("18:34", "Emilio Caniglia"): ("decisione",
        "Comunica a tutti che la riunione si terrà presso il rustico di Alessandra "
        "Toracchio, che provvederà a inviare la posizione."),
    ("18:35", "Alessandra Simonetti"): ("domanda",
        "Chiede conferma ad Alessandra Toracchio se il rustico sia quello di nonna Giulia "
        "(risposta affermativa alle 20:19)."),
    ("19:54", "Emanuele Sciarra"): ("info",
        "Ricorda ai partecipanti che chi ha un'attività paga la sponsorizzazione doppia, "
        "trattandosi di beneficenza per il comitato \"87\"; fa i conti a voce alta: il "
        "pacchetto \"massima visibilità\" costa 500€, moltiplicato per 3 fa 1500€, "
        "raddoppiato (quota attività) arriva a 3000€."),
    ("19:55", "Elvis Ippoliti"): ("info",
        "Aggiunge alla lista di chi ha un'attività (e quindi paga la sponsorizzazione "
        "doppia) anche Maikel Montano."),
    ("19:56", "Emanuele Sciarra"): ("info",
        "Commenta che così si parte meglio rispetto al comitato della classe '86."),
    ("19:56", "Dante Caniglia"): ("proposta",
        "Trovando la cifra ancora bassa, propone di chiedere un contributo più alto (circa "
        "10mila euro) a Daniele, da mostrare come esempio agli altri, ricordando che "
        "Cesare quest'anno ha incassato molto bene."),
    ("19:57", "Dante Caniglia"): ("proposta",
        "Suggerisce, in alternativa/aggiunta, di chiedere una donazione pari all'1% del "
        "fatturato."),
    ("20:16", "Elvis Ippoliti"): ("info",
        "A seguito della battuta di Luca Cicchelli sulla SIAE, chiarisce che il relativo "
        "costo dovrebbe essere già compreso nel budget stimato di 100.000 euro; Emanuele "
        "Sciarra conferma che è incluso nel prezzo finale."),
    ("20:19", "Alessandra Toracchio"): ("info",
        "Conferma ad Alessandra Simonetti che il rustico per la riunione è quello di "
        "nonna Giulia."),
}


def _skip_1921_1944(time_, fname):
    """Regola richiesta dall'utente il 9/9/2026: ignorare tutti i messaggi (media inclusi)
    della finestra 19:21-19:44 di questa giornata."""
    return "19:21" <= time_ <= "19:44"

MEDIA_OVERRIDES = {
    (DATE, "14:28", "Emilio Caniglia", "IMG-20260909-WA0006.jpg"):
        "Tabelle e grafici con i dati storici dei comitati classe 1982, 1983 e 1985 (mancano "
        "1984 e 1986): offerte della comunità di giugno e agosto, sponsor, numero di biglietti "
        "venduti e budget totale per ciascun anno.",
    (DATE, "15:16", "Ugo Trinchini", "IMG-20260909-WA0007.jpg"):
        "Foto del tariffario sponsor usato dalla classe 1986 per la festa 2026: quattro "
        "pacchetti (Totem piccolo/grande, logo sul retro o sul fronte dei biglietti della "
        "lotteria, striscione in piazza) con prezzi da 50 a 500 euro, condiviso come esempio "
        "da cui prendere spunto.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, extra_skip_media=_skip_1921_1944,
                 extra_skip_label="messaggi 19:21-19:44 esclusi su richiesta")
