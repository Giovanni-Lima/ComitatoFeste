#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-14 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:36-18:13 (export Dropbox delle 18:26, giornata ancora in corso
al momento dell'export): giorno di San Martino, in piazza con lo stand
del comitato. Mattina: Costance chiede il piano B per la pioggia; Costantino
(a voce) rassicura che con i gazebo si va avanti e valuta di chiamare Don
Enzo per anticipare il funerale; Emilio lo sente in mattinata, ritrovo alle
10:30 in sede e operativi da dopo pranzo, funerale permettendo. Emanuele
raccomanda di fare foto anche in carico/scarico (le fa Aceto). Nel primo
pomeriggio logistica di ritrovo, preparazione del vin brulè (ricetta di
Elvis: 2 kg di zucchero ogni 20 litri di vino) e Luca avvisa che hanno
iniziato a cuocere le castagne. Alle 17:28 Emanuele pubblica le foto e i
video dello stand, delle decorazioni, dello spaventapasseri, del braciere
con il tamburo e dei giochi dei bambini. Il resto (saluti, incoraggiamenti,
battute, vocali di scherzo, una GIF mp4, uno sticker) è rumore. Nessuna
menzione di Giovanni Lima da parte di altri (un suo "Grandissimi" alle
17:44, nessun intervento richiesto).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-14"

CURATED = {
    ("07:36", "Costance Rossi"): ("domanda",
        "Buongiorno: a Pescina pioviccicava; chiede quale sia il piano B "
        "in caso di pioggia."),
    ("11:01", "Alessandra Toracchio"): ("domanda",
        "Chiede se ci si è dimenticati di comprare qualcosa di urgente, "
        "visto che sta passando al negozio."),
}

AUDIO_CURATED = {
    (DATE, "09:45", "Dante Caniglia", "PTT-20261114-WA0014.opus"): ("domanda",
        "Chiede a che ora ci si vede oggi."),
    (DATE, "16:01", "Luca Cicchelli", "PTT-20261114-WA0045.opus"): ("domanda",
        "Avvisa che hanno cominciato a cuocere le castagne e chiede a "
        "Alessia a che punto sono gli altri."),
    (DATE, "07:37", "Emanuele Sciarra", "PTT-20261114-WA0004.opus"): ("rumore", ""),
    (DATE, "07:45", "Costantino Mariani", "PTT-20261114-WA0005.opus"): ("rumore", ""),
    (DATE, "10:42", "Luca Cicchelli", "PTT-20261114-WA0018.opus"): ("rumore", ""),
    (DATE, "14:28", "Dante Caniglia", "PTT-20261114-WA0037.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {
        "anchor_time": "07:55",
        "anchor_sender": "Costantino Mariani",
        "type": "info",
        "text": (
            "Costantino commenta il meteo (tempo variabile, in teoria "
            "migliore di quanto sembri) e assicura che, se piove, chi sta "
            "alla casa è coperto dai gazebo e chi cuoce continua a cuocere: "
            "\"le tempeste non ci spaventano\". Pensa di chiamare Don Enzo "
            "per andare prima ed evitare di arrivare durante il funerale."
        ),
        "members": [
            "PTT-20261114-WA0006.opus",
            "PTT-20261114-WA0007.opus",
            "PTT-20261114-WA0008.opus",
            "PTT-20261114-WA0009.opus",
        ],
    },
    {
        "anchor_time": "14:29",
        "anchor_sender": "Cesare Raglione",
        "type": "info",
        "text": (
            "Sul vin brulè: Cesare raccomanda di non farlo troppo dolce "
            "(\"fai buono\"); Elvis dà la ricetta, 2 kg di zucchero ogni 20 "
            "litri di vino; Dante scherza sugli ingredienti segreti di "
            "famiglia, a parte."
        ),
        "members": [
            "PTT-20261114-WA0038.opus",
            "PTT-20261114-WA0039.opus",
            "PTT-20261114-WA0040.opus",
        ],
    },
]

TEXT_MERGES = [
    {
        "anchor_time": "08:17",
        "anchor_sender": "Emilio Caniglia",
        "type": "info",
        "text": (
            "Emilio dice che sentirà Don Enzo in mattinata. Luca chiede a "
            "che ora si inizierà a preparare; Emilio risponde alle 10:30, "
            "chi può alla sede."
        ),
        "members": [
            ["08:17", "Emilio Caniglia"], ["08:20", "Luca Cicchelli"],
            ["08:55", "Emilio Caniglia"],
        ],
    },
    {
        "anchor_time": "09:46",
        "anchor_sender": "Alessandra Toracchio",
        "type": "info",
        "text": (
            "Alessandra chiede se hanno sentito Don Enzo; Emilio risponde "
            "che saranno operativi da dopo pranzo, funerale permettendo, e "
            "che scriverà a breve."
        ),
        "members": [
            ["09:46", "Alessandra Toracchio"], ["10:02", "Emilio Caniglia"],
            ["10:03", "Emilio Caniglia"],
        ],
    },
    {
        "anchor_time": "10:33",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Emanuele raccomanda di fare foto anche durante il carico e lo "
            "scarico; Tina risponde che le foto le fa Antonio Aceto."
        ),
        "members": [
            ["10:33", "Emanuele Sciarra"], ["10:44", "Tina Giarrante"],
        ],
    },
    {
        "anchor_time": "13:37",
        "anchor_sender": "Cesare Raglione",
        "type": "info",
        "text": (
            "Cesare chiede a che ora ci si vede nel pomeriggio. Luca, Ugo "
            "e Antonio alle 14 fanno altri giri per la legna e il resto, "
            "poi ci si vede quando si vuole dopo le due; Emanuele è "
            "appena rientrato e dopo una doccia e un boccone sarà alla "
            "sede; Dante parte da Az in cinque minuti."
        ),
        "members": [
            ["13:37", "Cesare Raglione"], ["13:39", "Luca Cicchelli"],
            ["13:59", "Emanuele Sciarra"], ["14:06", "Dante Caniglia"],
        ],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "09:11", "Maria Buttari", "IMG-20261114-WA0013.jpg"):
        "Screenshot delle previsioni meteo per San Benedetto dei Marsi: "
        "9°, nuvoloso, nuvolosità al mattino con schiarite nel "
        "pomeriggio, massime tra 11° e 13°.",
    (DATE, "14:16", "Elvis Ippoliti", "IMG-20261114-WA0041.jpg"):
        "La grande pentola di alluminio con il vin brulè in "
        "preparazione, mentre una persona vi tiene sopra un involucro di "
        "alluminio con le spezie.",
    (DATE, "14:23", "Elvis Ippoliti", "VID-20261114-WA0042.mp4"):
        "Video del vin brulè che viene mescolato nella pentola, con "
        "l'aggiunta di una bustina di ingredienti.",
    (DATE, "16:02", "Valentina D'Arcadia", "IMG-20261114-WA0046.jpg"):
        "Selfie di quattro membri del comitato sotto il gazebo dello "
        "stand, con un grosso fiocco arancione sul tavolo.",
    (DATE, "17:28", "Emanuele Sciarra", "IMG-20261114-WA0054.jpg"):
        "Lo stand del comitato in piazza decorato a tema autunnale: "
        "funghi, zucche, una botte con foglie e frutta, tovaglie "
        "arancioni.",
    (DATE, "17:28", "Emanuele Sciarra", "IMG-20261114-WA0056.jpg"):
        "Espositore in legno rosso con zucche decorate in vari modi "
        "(facce, una strega, fiori), in piazza davanti alla chiesa.",
    (DATE, "17:28", "Emanuele Sciarra", "IMG-20261114-WA0058.jpg"):
        "Lo spaventapasseri seduto su balle di fieno con zucche, in "
        "piazza.",
    (DATE, "17:28", "Emanuele Sciarra", "IMG-20261114-WA0059.jpg"):
        "Due partecipanti reggono il cesto con il fiocco arancione, "
        "forse quello della lotteria, davanti allo stand.",
    (DATE, "17:28", "Emanuele Sciarra", "IMG-20261114-WA0064.jpg"):
        "Selfie di gruppo di alcuni membri del comitato in piazza, "
        "davanti alla chiesa.",
    (DATE, "17:28", "Emanuele Sciarra", "IMG-20261114-WA0065.jpg"):
        "Il cartello appeso allo stand del vin brulè: \"Da Zio Elvis "
        "Bacareje, se magne bon i se bev meje\".",
    (DATE, "17:28", "Emanuele Sciarra", "IMG-20261114-WA0076.jpg"):
        "Il braciere con le castagne in cottura in piazza, delimitato da "
        "un nastro bianco e rosso, con lo stand sullo sfondo.",
    (DATE, "17:28", "Emanuele Sciarra", "IMG-20261114-WA0078.jpg"):
        "Primo piano del braciere con il tamburo rotante per cuocere le "
        "castagne sul fuoco, in piazza.",
    (DATE, "17:28", "Emanuele Sciarra", "VID-20261114-WA0052.mp4"):
        "Video serale della piazza durante la festa: una persona in "
        "costume passeggia con un bastone, con una bambina vicina.",
    (DATE, "17:28", "Emanuele Sciarra", "VID-20261114-WA0073.mp4"):
        "Video dei bambini disposti in fila in piazza per un gioco.",
}

# Esclusioni di media ridondanti o poco significativi (scelta di curatela):
# - 10:00 Ugo VID-0016: video di un uomo che cammina su una strada (battuta);
# - 10:32 Aceto IMG-0022: selfie allo specchio ("ecc è chiuso");
# - 15:08 Dante IMG-0043 (scherzo "mi faccio il bagno") e VID-0044/0047:
#   altri video della pentola, già coperti da IMG-0041 e VID-0042;
# - 17:28 Emanuele: ritratti singoli (0049, 0055, 0060, 0069), seconde
#   copie degli stessi scatti (0061, 0066, 0070 = foto già inviata alle
#   16:02, 0068, 0071), scatti di dettaglio poco significativi (0050,
#   0051, 0067, 0072, 0074, 0075, 0077) e video ripetitivi (0053, 0057,
#   0062, 0063).
_SKIP_FILES = {
    "VID-20261114-WA0016.mp4", "IMG-20261114-WA0022.jpg",
    "IMG-20261114-WA0043.jpg", "VID-20261114-WA0044.mp4",
    "VID-20261114-WA0047.mp4",
    "IMG-20261114-WA0049.jpg", "IMG-20261114-WA0050.jpg",
    "IMG-20261114-WA0051.jpg", "IMG-20261114-WA0055.jpg",
    "IMG-20261114-WA0060.jpg", "IMG-20261114-WA0061.jpg",
    "IMG-20261114-WA0066.jpg", "IMG-20261114-WA0067.jpg",
    "IMG-20261114-WA0068.jpg", "IMG-20261114-WA0069.jpg",
    "IMG-20261114-WA0070.jpg", "IMG-20261114-WA0071.jpg",
    "IMG-20261114-WA0072.jpg", "IMG-20261114-WA0074.jpg",
    "IMG-20261114-WA0075.jpg", "IMG-20261114-WA0077.jpg",
    "VID-20261114-WA0053.mp4", "VID-20261114-WA0057.mp4",
    "VID-20261114-WA0062.mp4", "VID-20261114-WA0063.mp4",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="media ridondanti/poco significativi")
