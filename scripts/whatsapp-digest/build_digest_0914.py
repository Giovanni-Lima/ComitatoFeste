#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-14 — solo dati di curatela, logica comune in digest_lib.py.

Giornata parziale (fino alle 15:09 all'atto di questo export), densa: lungo
scambio — molto a colpi di vocali (decine di `PTT-*.opus`, tutti tenuti
come da regola) — sul **cachet del cantante big** e sul budget della festa
di agosto 2027.

Filo principale (13:18-15:09): si riprende il conteggio delle "coppie" per
l'incontro sponsorizzato di venerdì (Emanuele: "siamo arrivati a 20", 13:18);
Emilio Caniglia inquadra i numeri storici (budget 80/90k dei comitati
precedenti all'86, l'unica spesa variabile è il cachet del big che da solo
assorbirebbe tutto il budget, l'unica entrata variabile sono i biglietti
venduti, due entrate "insolite" avute in passato); Giovanni Lima condivide
una lista di cantanti papabili con stima cachet (trascritta per intero,
stesso criterio dei sondaggi — dato tabellare, non va riassunto); Emanuele
allega uno screenshot sul cachet di Achille Lauro. Molto rumore di contorno
(opinioni personali su prezzo/biglietti, tutte esplicitamente presentate
come tali — non curate singolarmente). Il tema scivola poi in una lunga
nostalgia sui cantanti del passato a San Benedetto (Anna Oxa, Venditti, i
Santo California — foto di Elvis di un loro concerto, allegata) — rumore.

Dentro la battuta sulla "mostra di animali" con finti nomi di stand
(Raffaele, 14:53-14:57) c'è un nocciolo vero: Dante Caniglia chiarisce che
le mostre ufficiali sono già regolamentate (Enci/Fci) ma una mostra
amatoriale sarebbe fattibile, e ne stava già parlando col padre per
organizzarla insieme alla benedizione degli animali — curato come proposta.

Chiude la finestra una domanda di Dante sul mandato del comitato (se,
essendo gennaio-dicembre 2027, si possa generare budget anche dopo le
feste estive) con la risposta di Emanuele su un precedente concreto (The
Kolors, tempistiche di ingaggio/pagamento).

Nessuna menzione di Giovanni Lima da parte di altri membri in questa
finestra (solo un suo messaggio proprio, il post con la lista cantanti).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-14"

CURATED = {
    ("13:18", "Emanuele Sciarra"): ("info",
        "Comunica che per l'incontro sponsorizzato di venerdì siamo "
        "arrivati a quota 20 coppie."),
    ("14:07", "Emilio Caniglia"): ("info",
        "Inquadra i numeri storici: il budget dei comitati precedenti "
        "all'86 è stato di 80/90 mila euro, con cui bisognava coprire sia "
        "le feste di giugno che quelle di agosto."),
    ("14:10", "Emilio Caniglia"): ("info",
        "Spiega che le spese sono perlopiù costanti: l'unica voce "
        "davvero variabile è il cachet del cantante big, che a 80/90 "
        "mila euro assorbirebbe da solo l'intero budget."),
    ("14:12", "Giovanni Lima"): ("info",
        "Condivide una lista di cantanti papabili con stima del cachet e "
        "una nota di fattibilità (capienza max 20.000 persone, budget "
        "cachet max 80.000€): Bresh 60-80k (da provare); The Kolors "
        "60-80k (ottima scelta); Coma_Cose 45-65k (molto interessante); "
        "Tananai 60-80k+ (da verificare); Coez 50-70k (molto "
        "interessante); Rose Villain 60-80k (al limite); Rkomi 50-70k "
        "(da valutare); Olly 60-80k+ (probabile sforamento); Capo Plaza "
        "50-70k (interessante); Alex Britti 40-60k (più trasversale); "
        "Achille Lauro >80k (fuori budget, da considerare solo con "
        "budget superiore)."),
    ("14:13", "Emilio Caniglia"): ("info",
        "Spiega che sul fronte entrate l'unica vera variabile è il "
        "numero di biglietti venduti: la classe '85 fu la prima a "
        "passare da 20-25 mila a 40 mila biglietti, ma con questua e "
        "sponsor diminuiti il budget complessivo restò grosso modo "
        "invariato."),
    ("14:23", "Emilio Caniglia"): ("info",
        "Ricorda due entrate \"insolite\" avute in passato: una macchina "
        "non ritirata (differenza di 7-8 mila euro, precisa poi "
        "Costantino Mariani) e un aiuto dell'amministrazione comunale, "
        "oltre alla maggiorazione dei biglietti venduti."),
    ("14:55", "Dante Caniglia"): ("proposta",
        "Dentro la battuta sulla mostra di animali di Raffaele Di "
        "Cesare, chiarisce che le mostre ufficiali sono già "
        "regolamentate da Enci/Fci, ma che una mostra amatoriale "
        "sarebbe fattibile — ne stava già parlando col padre per "
        "organizzarla in concomitanza con la benedizione degli animali."),
    ("15:01", "Dante Caniglia"): ("domanda",
        "Chiede conferma: dato che il comitato è in carica da gennaio a "
        "dicembre 2027, si può generare budget anche dopo le feste "
        "estive? Se così fosse cambierebbe la prospettiva."),
    ("15:03", "Emanuele Sciarra"): ("info",
        "Risponde citando un precedente concreto: i The Kolors furono "
        "ingaggiati definitivamente a fine febbraio con i contatti presi "
        "già a gennaio; i pagamenti sono di solito a 60 giorni dalla "
        "fattura (precisa poi Dante Caniglia)."),
}

MEDIA_OVERRIDES = {
    (DATE, "14:29", "Emanuele Sciarra", "IMG-20260914-WA0018.jpg"):
        "Screenshot di una ricerca sul cachet di Achille Lauro: 40-60mila "
        "euro per una semplice ospitata, 70-100mila+ per un concerto "
        "completo. Didascalia di Emanuele: non lo vede fuori budget se si "
        "riuscisse a un prezzo di 70 mila euro.",
    (DATE, "14:39", "Emanuele Sciarra", "IMG-20260914-WA0025.jpg"):
        "Screenshot di un calendario personale (agosto 2027), condiviso "
        "verosimilmente per valutare disponibilità/date per gli eventi "
        "estivi — impegni personali non trascritti per riservatezza.",
    (DATE, "14:46", "Elvis Ippoliti", "IMG-20260914-WA0040.jpg"):
        "Foto di un concerto dal vivo de \"I Santo California\" (schermo "
        "col nome del gruppo sul palco), condivisa durante la "
        "conversazione nostalgica sui cantanti del passato a San "
        "Benedetto.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
