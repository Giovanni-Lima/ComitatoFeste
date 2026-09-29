#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-28 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 17:37-20:14 (export Dropbox delle 20:26 del 28/9; nessun messaggio
prima delle 17:37). Vigilia della serata sponsorizzata del 29/9: Barbara
Rizio (17:37) chiede cosa si porta e se c'è una lista; seguono le adesioni
(Tina Giarrante: acqua e bibite; Barbara: torta salata e rustici;
Alessandro Di Benedetto: vassoio di dolci) mentre Antonio Sabatini (17:45)
fa notare che per il cibo è già tutto a posto (se ne sono occupate 3-4
persone) e servono solo bibite, patatine, vassoi, bicchieri e tovaglioli,
con quello che avanza da lasciare in sede; Alessandra Simonetti ricorda che
sul volantino l'inizio è alle 20:15. Alessandra Simonetti ripubblica anche
la foto dell'invito già digest il 25/9 (stesso file IMG-20260925-WA0023.jpg),
scartata come duplicato. Elvis Ippoliti (vocali 17:48 e 17:52) comunica che
alla nuova sede è stata riattivata la corrente (luci funzionanti,
riduzione di potenza già richiesta da Barbara), che mancano il motorino
dell'acqua e il gas, che darà le chiavi a Emilio, e propone una locandina
"coming soon" grande per la vetrina più riscaldamento e frigorifero;
Emanuele Sciarra (18:18) pensa di avere una stufa a gas a Paternò. Foto
degli interni della sede (Elvis, 18:10). Raffaele Di Cesare (20:01) condivide
un video Facebook come idea per dei giochi; Alessandro Di Benedetto (20:14)
propone di delegare la spesa per i prossimi eventi sponsorizzati a 1-2
persone a rotazione con un fondo cassa. Restano rumore: battute, conferme
brevi e uno scambio di 18:23 di cui manca il contesto (Antonio Sabatini e
Barbara). Nessuna menzione di Giovanni Lima in questa finestra.

Coda serale (20:27-21:15, export del 29/9): Emanuele chiede a chi lasciare
le bevande avanzate dalla dimostrazione scorsa (risponde Antonio Sabatini,
disponibile nel pomeriggio) e trova una soluzione per il riscaldamento
tramite un cannone a gas del suocero, da riempire con una bombola piccola
se qualcuno ne ha una. Una foto di Emanuele (20:38) è lo screenshot di un
fatto di cronaca locale condiviso su Facebook, non legato al comitato,
tenuta con didascalia neutra. Resto rumore ("Grande Lepiss"). Nessuna
menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-28"

CURATED = {
    ("17:37", "Barbara Rizio"): ("domanda",
        "Chiede cosa si porta per domani sera (incontro sponsorizzato del "
        "29/9) e se è stata fatta una lista."),
    ("17:39", "Tina Giarrante"): ("info",
        "Porta un fardello d'acqua, Coca Cola, aranciata, tè e bicchieri; "
        "chiede ad Alessandra Toracchio di organizzare, ma Alessandra "
        "Simonetti fa notare che in questi giorni Alessandra non c'è."),
    ("17:43", "Barbara Rizio"): ("info",
        "Si offre di rifare una torta salata e di preparare dei rustici."),
    ("17:44", "Alessandro Di Benedetto"): ("info",
        "Porta un vassoio di dolci."),
    ("17:45", "Antonio Sabatini"): ("info",
        "Precisa che per il cibo è già tutto a posto (se ne sono occupate "
        "3-4 persone) e che non serve esagerare: essendo a metà settimana "
        "non ci si tratterrà a lungo. Servono solo bibite, patatine, "
        "vassoi, bicchieri e tovaglioli; quello che avanza si potrà "
        "lasciare in sede. Pensa che la serata non comincerà prima delle "
        "21."),
    ("17:45", "Alessandra Simonetti"): ("info",
        "Fa notare che sul volantino l'inizio è alle 20:15, quindi dopo la "
        "gente potrebbe avere fame."),
    ("18:18", "Emanuele Sciarra"): ("info",
        "Pensa di avere una stufa a gas (a bombola) a Paternò: in "
        "settimana passa a controllare."),
    ("20:01", "Raffaele Di Cesare"): ("proposta",
        "Condivide un video Facebook come idea per qualche gioco: "
        "https://www.facebook.com/share/r/1HMK6sswLK/"),
    ("20:14", "Alessandro Di Benedetto"): ("proposta",
        "Per i prossimi eventi sponsorizzati propone di delegare la spesa, "
        "attraverso un fondo cassa, a 1 o 2 persone a rotazione, così da "
        "evitare confusione e malintesi."),
    ("20:27", "Emanuele Sciarra"): ("domanda",
        "Chiede a chi può lasciare domani le bevande avanzate dalla "
        "dimostrazione scorsa."),
    ("20:31", "Emanuele Sciarra"): ("info",
        "Comunica di aver trovato una soluzione per il riscaldamento della "
        "sede: suo suocero ha un cannone a gas, che si può usare "
        "tranquillamente riempiendo una bombola piccola se qualcuno ne ha "
        "una."),
}

AUDIO_CURATED = {
    (DATE, "17:48", "Elvis Ippoliti", "PTT-20260928-WA0006.opus"): ("info",
        "Aggiorna sulla nuova sede: provato il contatore, la corrente è "
        "stata riattivata e le luci funzionano; Barbara aveva già "
        "provveduto ad avvisare per la riduzione della potenza, quindi la "
        "sede è quasi operativa. Il motorino dell'acqua verrà rimesso "
        "domani o dopodomani, quando sarà riparato. Darà le chiavi a "
        "Emilio (presidente) appena lo vede."),
    (DATE, "17:52", "Elvis Ippoliti", "PTT-20260928-WA0007.opus"): ("proposta",
        "Propone di far stampare una locandina grande \"coming soon\" da "
        "appendere alla vetrina o alla porta della sede, e ricorda che "
        "servono un modo per scaldare (Emanuele ha delle stufette "
        "elettriche, il gas non è stato attivato) e un frigorifero per "
        "lasciare qualcosa."),
}

MEDIA_OVERRIDES = {
    (DATE, "18:10", "Elvis Ippoliti", "IMG-20260928-WA0008.jpg"):
        "Foto degli interni della nuova sede del comitato: sala con pareti "
        "arancioni, banco bar in pietra e legno, botti e tavoli alti, sedie "
        "impilate su un lato e archi in mattoni sul fondo.",
    (DATE, "20:38", "Emanuele Sciarra", "IMG-20260928-WA0009.jpg"):
        "Screenshot di un post Facebook della testata locale \"Terre "
        "Marsicane\" su un fatto di cronaca (un arresto dei Carabinieri), "
        "condiviso come chiacchiera di fine serata, non legato al "
        "comitato.",
}

# IMG-20260925-WA0023.jpg (17:46, Alessandra Simonetti): stessa foto
# dell'invito già digest il 25/9 alle 21:11, scartata come duplicato.
_SKIP_FILES = {"IMG-20260925-WA0023.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="foto invito duplicata")
