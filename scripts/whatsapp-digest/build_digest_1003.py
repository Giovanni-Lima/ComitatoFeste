#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-03 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:56-23:57 (export Dropbox delle 13:51 del 4/10; nessun vocale).
Giornata della riunione alla sede (il pub di Elvis) e del transito di San
Francesco. Barbara Rizio (08:20) chiede come ci si organizza per la sera e a
che ora è il transito; Tina Giarrante (08:43) risponde che le hanno detto
dopo le 9, con la locandina della Celebrazione del Transito (sabato 3/10,
ritrovo alle 21:30 presso la Cappellina, fiaccolata verso Santa Sabina).
Antonio Aceto (10:46) chiede se la riunione di stasera è alla nuova sede.
Elvis Ippoliti (12:36, 16:44, 17:43) documenta i lavori nella sede (pavimento
allagato, pulizia finita). Emilio Caniglia (15:25) pubblica il promemoria
dei punti all'ordine del giorno: visita a Corinaldo l'8 novembre, incontro
con l'azienda materassi il 16 ottobre, Halloween e San Martino, preadesione
al comitato, comunicazione e pagine social, varie; con ritrovo alle 9 alla
sede prima dell'evento del Caffè Letterario su San Francesco. In serata
arrivano le conferme di presenza e di orario (Serena Di Stefano 19:45,
Cesare Raglione 19:53, Ilenia Piccozzi 20:14, con risposta di Emilio "9 o chi
riesce un po' prima"); Costantino Mariani porta tre birre; Elvis e Tina
pubblicano foto della serata. Alle 23:43 Emanuele Sciarra condivide due
illustrazioni in stile cartone della foto di gruppo del comitato in
chiesa e sulla piazza (già ripreso da Emidio Cerasani il giorno dopo). Alle
23:57 Antonio Aceto condivide il link del profilo Instagram della classe
1987. Resto rumore (saluti, battute, dialetto). Nessuna menzione di
Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-03"

CURATED = {
    ("08:20", "Barbara Rizio"): ("domanda",
        "Chiede come ci si organizza per la sera e a che ora c'è il transito "
        "di San Francesco; Tina Giarrante risponde che le hanno detto dopo "
        "le 9."),
    ("10:46", "Antonio Aceto"): ("domanda",
        "Chiede se la riunione di stasera si tiene alla nuova sede."),
    ("15:25", "Emilio Caniglia"): ("info",
        "Pubblica il promemoria dei punti all'ordine del giorno della riunione "
        "di stasera: visita a Corinaldo l'8 novembre; incontro sponsorizzato "
        "con l'azienda materassi il 16 ottobre; Halloween e San Martino; "
        "preadesione al comitato; comunicazione e pagine social; varie. "
        "Propone di ritrovarsi alle 9 alla sede del comitato (al pub di "
        "Elvis) e, se si è puntuali, di partecipare all'evento su San "
        "Francesco organizzato dal Caffè Letterario."),
    ("19:45", "Serena Di Stefano"): ("domanda",
        "Chiede se stasera prima ci si vede alla sede per la riunione e poi "
        "in chiesa."),
    ("19:53", "Cesare Raglione"): ("info",
        "Comunica che riuscirà a passare dopo le 22 e chiede di essere "
        "avvisato quando si torna in sede."),
    ("20:14", "Ilenia Piccozzi"): ("domanda",
        "Chiede a che ora ci si vede; Emilio Caniglia risponde alle 9 o "
        "prima per chi riesce."),
    ("21:15", "Barbara Rizio"): ("domanda",
        "Chiede se sono a Santa Sabina; Antonio Aceto risponde di no, sono "
        "alla sede, e Alessandra Simonetti comunica che stanno arrivando."),
    ("22:13", "Costantino Mariani"): ("info",
        "Porta tre birre per la serata; Veronica non verrà."),
    ("23:57", "Antonio Aceto"): ("info",
        "Condivide il link del profilo Instagram della classe 1987: "
        "https://www.instagram.com/classe_1987_sbdm?stkn=MXNpZzI4dm9oM3N2OA%3D%3D&utm_source=qr"),
}

MEDIA_OVERRIDES = {
    (DATE, "08:43", "Tina Giarrante", "IMG-20261003-WA0000.jpg"):
        "Locandina della Celebrazione del Transito di San Francesco, "
        "sabato 3 ottobre 2026 a San Benedetto dei Marsi: ritrovo alle 21:30 "
        "presso la Cappellina di San Francesco, fiaccolata verso il Portale "
        "di Santa Sabina e inizio della celebrazione; in caso di maltempo "
        "l'evento si terrà nella chiesa Maria SS. Assunta. Organizzata dalla "
        "Parrocchia di San Benedetto Abate con il Caffè Letterario Spazio "
        "Cultura.",
    (DATE, "10:43", "Dante Caniglia", "IMG-20261003-WA0003.jpg"):
        "Foto dall'auto in transito, con il cartello \"Corinaldo\" sulla "
        "strada, durante il viaggio di sopralluogo per la gita dell'8 "
        "novembre.",
    (DATE, "12:36", "Elvis Ippoliti", "IMG-20261003-WA0004.jpg"):
        "Foto dell'interno della sede del comitato con il pavimento "
        "allagato: Elvis, al lavoro sulla sede, segnala il problema.",
    (DATE, "16:44", "Elvis Ippoliti", "IMG-20261003-WA0014.jpg"):
        "Foto dell'interno della sede in fase di pulizia, con scopa e "
        "paletta appoggiate sul pavimento.",
    (DATE, "17:43", "Elvis Ippoliti", "IMG-20261003-WA0015.jpg"):
        "Foto dell'ingresso della sede con il pavimento pulito e lo "
        "straccio appoggiato; didascalia \"Finish\" (lavori conclusi).",
    (DATE, "22:14", "Elvis Ippoliti", "IMG-20261003-WA0016.jpg"):
        "Foto di quattro bottiglie di birra su un tavolo nel pub, durante la "
        "riunione.",
    (DATE, "22:54", "Tina Giarrante", "IMG-20261003-WA0017.jpg"):
        "Foto di gruppo scattata in un locale durante la serata, con alcuni "
        "membri del comitato.",
    (DATE, "23:43", "Emanuele Sciarra", "IMG-20261004-WA0000.jpg"):
        "Illustrazione in stile cartone animato di una foto di gruppo del "
        "comitato, con le magliette gialle \"1987\", davanti alla chiesa "
        "accanto al sacerdote che tiene il reliquiario.",
    (DATE, "23:43", "Emanuele Sciarra", "IMG-20261004-WA0001.jpg"):
        "Illustrazione in stile cartone animato di una foto di gruppo del "
        "comitato, con le magliette gialle \"1987\", in piazza, con il "
        "sindaco con la fascia tricolore.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
