#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-11 — solo dati di curatela, logica comune in digest_lib.py.

Giornata COMPLETA (fino alle 23:30, ultimo messaggio del giorno — a
mezzanotte la chat passa al 12/9, curato separatamente). Mattina/primo
pomeriggio dominati dai saluti mattutini e da
un lungo siparietto scherzoso in dialetto tra Elvis/Luca/Raffaele/Maria su
vecchi ricordi (incidente in bicicletta, mongolfiera, "panda verde") — rumore,
niente di attinente al comitato; la stessa vena nostalgica riprende con
Gilda (12:22, mongolfiera), Dante che ricorda vecchie videocassette (asilo,
vendemmia 1991, 13:45/13:53) e la battuta di Raffaele sul vino del '91, poi
ancora con Martina/Costantino nel primo pomeriggio (15:02-15:26, chi stava
"alle stanze"/l'asilo di Pescina) — trattati come rumore/nostalgia, nessun
uso concreto per il comitato dal testo.

Punti rilevanti mattina: Tina Giarrante completa la lista di cosa porta per
la riunione di stasera (vedi anche il thread iniziato il 10/9 da Alessandra
Toracchio/Barbara Rizio); Alessandra Toracchio manda la posizione del
rustico (pin statico via link Maps, non "in tempo reale" — vedi regola
11/9/2026 in CLAUDE.md) con due screenshot di Google Street View come
riferimento visivo; Emanuele Sciarra avvisa che stasera arriva più tardi;
Raffaele Di Cesare chiede a che ora è la riunione, Tina risponde.

Coda pomeridiana/serale (16:13-17:45): Emilio Caniglia manda la foto del
promemoria/ordine del giorno della riunione di stasera (8 punti, trascritti
per intero in MEDIA_OVERRIDES) e lo introduce nel messaggio successivo,
annunciando che porterà il computer per iniziare a verbalizzare; comunica
anche di essere già in contatto con il direttore artistico di Francesco De
Gregori e dei Dire Straits, contatto utile per scegliere un artista
importante senza passare da agenzie locali. **Menzione di Giovanni Lima**
(regola 11/9/2026): il punto 5 dell'ordine del giorno nella foto di Emilio
cita testualmente "app di Giovanni e app di Dante" — segnalato nel recap
finale della sessione, non genera di per sé una entry (l'immagine è comunque
in digest con la trascrizione completa). Resto della coda: due vocali
(Elvis 16:17, Emanuele 16:17), uno sticker di Emanuele (14:28, ignorato) e
un video reale di Dante (17:44, VID-20260911-WA0048.mp4 — verificato con
grep sui box MP4 che ha sia traccia video che audio, "vide"/"avc1" e
"soun"/"mp4a" tutti presenti: non è una GIF di reazione, niente skip),
didascalia in dialetto ("t so truvat la Spa") lasciata al meccanismo
automatico di digest_lib (Didascalia: ...). Chiusura pomeridiana in
rumore/battute sugli orari di arrivo (Alessandra Toracchio, Alessandra
Simonetti, Martina, Tina) — nessun contenuto nuovo rispetto a quanto già
stabilito da Tina alle 14:07.

Coda serale (18:01-21:28): due vocali (Dante 18:05, Emanuele 18:06); Gilda
Di Iulio avvisa che non riesce a venire alla riunione; poi solo rumore
d'arrivo in dialetto (Elvis/Emidio/Barbara/Antonio/Cesare/Costantino, chi
è arrivato, dove si trova il ritrovo — già stabilito, chi sono i presenti)
e un messaggio di Raffaele Di Cesare eliminato da WhatsApp (nessun
contenuto recuperabile, non genera entry). "Quant sa fa….famm sape i
numer" di Emanuele (18:01) resta ambiguo senza poter ascoltare i vocali
adiacenti — trattato come rumore, il Transcriber classificherà i vocali
stessi. Nessuna menzione di Giovanni Lima in questa coda.

Coda notturna (22:04-23:30, durante/dopo la riunione): Alessandra Toracchio
manda la foto di una pagina di quaderno con una lista numerata "Coppia"
(gioco/attività della serata, non decifrabile con certezza nome per nome —
descritta senza indovinare le grafie incerte); Valentina D'Arcadia manda
una foto di gruppo della riunione al rustico (festoni "Happy Birthday" —
lega con gli auguri di Tina a MariaLuisa Cianfaglione il mattino dopo, non
curato qui perché già 12/9); Emidio Cerasani riferisce che Costantino
Mariani offre il primo sponsor (unica notizia sostanziale della serata,
sotto forma di resoconto di un terzo, non conferma diretta — tenuta come
`info`, non `decisione`); 4 vocali (Valentina x2 alle 23:19, Emidio 23:29,
Valentina 23:30). Resto rumore (arrivi, "Dajeee", "Guardate mike").
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-11"

CURATED = {
    ("08:53", "Tina Giarrante"): ("info",
        "Per la riunione di stasera comunica cosa ha preso: varie patatine, 2 "
        "bottiglie di acqua frizzante, un succo e un tè; il resto lo portano "
        "gli altri. Chiede comunque ad Alessandra Toracchio di mandare la "
        "posizione."),
    ("11:55", "Alessandra Toracchio"): ("info",
        "Condivide la posizione del rustico per la riunione di stasera: "
        "https://maps.google.com/?q=42.0035863,13.6262866"),
    ("13:36", "Emanuele Sciarra"): ("info",
        "Avvisa che stasera arriva più tardi: stacca dal lavoro alle 22 e poi "
        "raggiunge il gruppo."),
    ("13:54", "Raffaele Di Cesare"): ("domanda",
        "Scherza con Dante sul portare il vino del '91, poi chiede a che ora "
        "è la riunione di stasera."),
    ("14:07", "Tina Giarrante"): ("info",
        "Risponde a Raffaele: la riunione di stasera è dopo le 21, o "
        "comunque sarà Alessandra ad avvisare quando è pronta."),
    ("16:14", "Emilio Caniglia"): ("info",
        "Introduce la foto del promemoria appena inviata: promemoria per la "
        "riunione di stasera con i punti sintetici emersi dalle discussioni "
        "dei giorni scorsi; porterà il computer per iniziare a verbalizzare "
        "la riunione."),
    ("16:16", "Emilio Caniglia"): ("info",
        "Comunica di essere già in contatto con il direttore artistico di "
        "Francesco De Gregori, anche membro dei Dire Straits: un contatto "
        "utile per scegliere un artista importante evitando le agenzie "
        "locali."),
    ("20:42", "Gilda Di Iulio"): ("info",
        "Avvisa che non riesce a venire alla riunione di stasera."),
    ("22:58", "Emidio Cerasani"): ("info",
        "Riferisce che Costantino Mariani offre il primo sponsor."),
}

MEDIA_OVERRIDES = {
    (DATE, "12:02", "Alessandra Toracchio", "IMG-20260911-WA0039.jpg"):
        "Screenshot di Google Street View che inquadra un incrocio con una "
        "casa color pesca a due piani con balcone e persiane verdi, per "
        "mostrare com'è la zona sul retro del palazzo del ritrovo.",
    (DATE, "12:02", "Alessandra Toracchio", "IMG-20260911-WA0040.jpg"):
        "Screenshot di Google Street View su Via Italia con una freccia rossa "
        "disegnata a mano che indica l'ingresso esatto (una porta con tenda) "
        "tra due edifici rustici, per indicare dove trovare il punto di "
        "ritrovo.",
    (DATE, "16:13", "Emilio Caniglia", "IMG-20260911-WA0045.jpg"):
        "Foto del promemoria per la riunione dell'11/9/2026 (intestazione "
        "\"Classe 1987\"), ordine del giorno in 8 punti: 1) Introduzione di "
        "Emidio; 2) Visita Corinaldo (valutazione preventivi ed altro); 3) "
        "\"Incontro sponsorizzato\" - azienda materassi; 4) Sede Comitato; "
        "5) Applicazioni a supporto del Comitato: app di Giovanni e app di "
        "Dante; 6) Halloween & San Martino (valutazione collaborazione con "
        "la Proloco); 7) Report entrate Comitati precedenti; 8) Varie ed "
        "eventuali.",
    (DATE, "22:39", "Alessandra Toracchio", "IMG-20260911-WA0051.jpg"):
        "Foto di una pagina di quaderno scritta a mano, titolo \"Coppia\" e "
        "una lista numerata da 1 a 12 di nomi (gioco/attività della serata) "
        "— grafia poco leggibile in alcuni punti, nomi non trascritti con "
        "certezza.",
    (DATE, "22:53", "Valentina D'Arcadia", "IMG-20260911-WA0053.jpg"):
        "Foto di gruppo della riunione al rustico: i presenti seduti "
        "attorno a un lungo tavolo con snack e bevande, festoni dorati "
        "\"Happy Birthday\" appesi al soffitto.",
}

# VID-20260911-WA0042.mp4 (giorno precedente, già gestito): nessuna traccia
# audio (ispezionati i box MP4 — 'vide'/'avc1' presenti, 'soun'/'mp4a'
# assenti). VID-20260911-WA0048.mp4 (17:44, Dante) invece ha ENTRAMBE le
# tracce ('vide'/'avc1' e 'soun'/'mp4a' tutte presenti, verificato via grep
# sui box binari — ffprobe non disponibile in questa sessione): è un video
# vero, non va scartato.
_REACTION_GIF_MP4 = {
    "VID-20260911-WA0042.mp4",
}


def _skip_reaction_gif_mp4(time_, fname):
    return fname in _REACTION_GIF_MP4


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES,
                 extra_skip_media=_skip_reaction_gif_mp4,
                 extra_skip_label="GIF di reazione .mp4 senza audio, escluse")
