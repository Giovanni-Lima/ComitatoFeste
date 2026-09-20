#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-20 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 11:17-16:08 (export Dropbox delle 19:45 del 20/9). Giornata
dell'incontro su San Francesco col Vescovo (16:30, Parrocchia di San
Cipriano, tutti con la maglietta del comitato). Emilio Caniglia (11:17)
ricorda l'appuntamento e spiega le ragioni della nuova sede del Comitato,
poi (11:24) lancia il sondaggio (22 Sì / 0 No al momento dell'export,
curato come proposta, non come decisione). Molti membri rispondono
scrivendo di non poter essere presenti all'incontro (creando un equivoco
col sondaggio, che riguarda la sede): tutti raccolti in una sola entry.
Emanuele Sciarra (14:23) chiede a Emilio se ci si vede prima delle 16:30
(sì, fuori dalle scale della Chiesa) e (14:42, vocale) ricorda i link di
organizzatori di eventi (circo per bambini, artisti di strada) girati tempo
fa, poi condivide 12 immagini del catalogo della ditta "Creatori di
Sorrisi" / GonfiabiliItalia (Antonio Di Luca, Pescara): 10 locandine di
spettacoli/attrazioni, il biglietto da visita e l'elenco dei servizi sul
retro, tutte tenute con didascalia descrittiva. Restano rumore: il
"Bello…." di Emanuele (14:41) e il messaggio vuoto delle 14:45; il
messaggio di sistema delle 11:24 (Emilio fissa un messaggio) non genera
entry. Nessuna menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-20"

CURATED = {
    ("11:17", "Emilio Caniglia"): ("info",
        "Ricorda l'appuntamento di oggi alle 16:30 ai locali della "
        "Parrocchia di San Cipriano per l'incontro su San Francesco: tutti "
        "con le magliette del comitato. Prima del sondaggio spiega le "
        "ragioni della nuova sede: si romperà la prassi della sede storica "
        "consolidata da decenni; non sarà solo una stanza per le feste "
        "patronali ma il punto di riferimento di un anno intero, un ritrovo "
        "(anche settimanale, oltre alle riunioni), un laboratorio di idee e "
        "il luogo dove intavolare trattative mettendo il Comitato in una "
        "posizione diversa."),
    ("11:24", "Emilio Caniglia"): ("proposta",
        "SONDAGGIO: Sei d'accordo per la sede del Comitato presso il Corso "
        "(vicino alla tabaccheria)? — Sì (22 voti), No (0 voti) al momento "
        "dell'export; il sondaggio resta aperto."),
    ("11:28", "Serena Di Stefano"): ("info",
        "Comunica di non poter esserci oggi pomeriggio all'incontro di San "
        "Cipriano; nel corso della giornata lo stesso dicono Costance "
        "Rossi, Barbara Rizio, Alessandra Simonetti, Alessandra Toracchio e "
        "Antonio Aceto, mentre Cesare Raglione non sa se riuscirà. "
        "Alessandra Toracchio e Barbara precisano che nel sondaggio va "
        "risposto Sì/No sulla sede, non sulla presenza."),
    ("14:23", "Emanuele Sciarra"): ("domanda",
        "Chiede a Emilio Caniglia se ci si vede un po' prima delle 16:30; "
        "Emilio risponde di sì, poco prima fuori dalle scale della Chiesa."),
}

AUDIO_CURATED = {
    (DATE, "14:42", "Emanuele Sciarra", "PTT-20260920-WA0008.opus"): ("proposta",
        "Ricorda i link, girati tempo fa, di organizzatori di eventi "
        "(circo per bambini, artisti di strada e altro): volendo si "
        "possono contattare per vedere cosa propongono."),
}

_CONTATTI = "numero verde 800146560, 388 1974808, 331 3576687"

MEDIA_OVERRIDES = {
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0009.jpg"):
        "Locandina \"GonfiabiliItalia\" (Antonio Di Luca, Creatori di "
        "Sorrisi): noleggio di un parco giochi in piazza con oltre 10 "
        "gonfiabili di varie dimensioni, per amministrazioni comunali, Pro "
        "Loco e organizzatori (" + _CONTATTI + ").",
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0010.jpg"):
        "Locandina \"Favolagiocando\": spettacolo con oltre 30 mascotte, "
        "giocolieri, acrobati, equilibristi e illusionisti, 2 ore di "
        "divertimento per famiglie (Creatori di Sorrisi).",
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0011.jpg"):
        "Locandina \"Pinocchio nel magico mondo dei burattini\": spettacolo "
        "interattivo con sorprese, giochi e mascotte (Creatori di Sorrisi).",
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0012.jpg"):
        "Locandina \"Notte Nera 2026\": evento a tema gotico/horror con "
        "spettacoli, performer, animazione e sorprese (Creatori di "
        "Sorrisi).",
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0013.jpg"):
        "Locandina \"Rodeo Show\": toro meccanico, sfide e musica per tutta "
        "la famiglia (Creatori di Sorrisi).",
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0014.jpg"):
        "Locandina \"Surf Meccanico\": simulatore di surf su onda "
        "artificiale, per tutte le età (Creatori di Sorrisi).",
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0015.jpg"):
        "Locandina \"Schiuma Party\": musica, schiuma e divertimento "
        "(Creatori di Sorrisi).",
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0016.jpg"):
        "Locandina \"Calcio Balilla Umano\": sfida a squadre su un gigante "
        "calcio balilla umano, per tutte le età (Creatori di Sorrisi).",
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0017.jpg"):
        "Locandina \"Festival degli Artisti di Strada - Tour 2026\": oltre "
        "10 spettacoli nella stessa sera (acrobati, equilibristi, "
        "giocolieri, fachiri, sputafuoco, lanciatori di coltelli, "
        "funamboli), Creatori di Sorrisi.",
    (DATE, "14:44", "Emanuele Sciarra", "IMG-20260920-WA0018.jpg"):
        "Locandina \"Circo in Piazza - Tour 2026\": 90 minuti di spettacolo "
        "per famiglie con giocolieri, acrobati, clown, lanciatore di "
        "coltelli ed equilibristi (Creatori di Sorrisi).",
    (DATE, "14:45", "Emanuele Sciarra", "IMG-20260920-WA0019.jpg"):
        "Biglietto da visita di Antonio Di Luca, direttore generale e sales "
        "manager di Creatori di Sorrisi (Pescara): WhatsApp +39 388 197 "
        "48 08, Instagram creatoridisorrisi.",
    (DATE, "14:45", "Emanuele Sciarra", "IMG-20260920-WA0020.jpg"):
        "Retro del biglietto da visita, \"I nostri servizi\": attrazioni "
        "gonfiabili, spettacoli musicali e concerti, spettacoli teatrali, "
        "format anni 90, calcio balilla umano, surf meccanico, mascotte, "
        "toro meccanico, mini luna park gonfiabile, spettacoli circensi, "
        "zucchero filato, pop corn, giochi interattivi (numero verde 800 "
        "14 65 60, siti creatoridisorrisi.net e gonfiabilitalia).",
}


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
