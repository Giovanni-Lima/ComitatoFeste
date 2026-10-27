#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-26 — solo dati di curatela, logica comune in digest_lib.py.

Giornata densa (08:04-23:15, aggiornata con l'export delle 08:59 del 27/10).
Mattina: il gruppo raccoglie nominativi di animatori per bambini in vista
del Capodanno (contatti vCard, numeri non riportati per privacy); Emanuele
aggiorna sui contatti delle associazioni vicine per i materassi (vedi
19/10). A pranzo è il compleanno di Emanuele Sciarra: lunga sequenza di
auguri (anche da Giovanni Lima). Nel pomeriggio/sera: richiesta di
preventivi a più bande musicali per le prossime feste (con una divagazione
sulla fattibilità di un Carnevale con carri, giudicata poco praticabile);
un orologio da parete trovato a buon prezzo come possibile premio
lotteria; il gruppo valuta sparatori per i fuochi d'artificio (un contatto
di fiducia di Emanuele a Celano, garantito anche da Dante e Antonio
Aceto), con foto/video di esempio in serata; discussione su calze della
Befana (contenuto, prezzi, quantità) e sui premi della lotteria per i
pullman di Corinaldo (lotteria estesa a entrambi, 4 premi raccolti finora,
un premio riservato per l'evento di agosto). Maria chiede se valutare
anche uno spettacolo con i droni. In tarda serata un numero esterno non
salvato offre un premio alimentare per la lotteria. Nessuna menzione di
Giovanni Lima da parte di altri (lui stesso scrive solo per fare gli
auguri a Emanuele).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-26"

CURATED = {
    ("08:15", "Emanuele Sciarra"): ("info",
        "Aggiorna sui contatti delle associazioni dei paesi vicini "
        "(vedi 19/10): in settimana gli daranno i nominativi da "
        "presentare all'azienda di materassi; se va bene, stima un "
        "guadagno di 700-800€ per il comitato."),
    ("13:12", "Costantino Mariani"): ("info",
        "Oggi è il compleanno di Emanuele Sciarra: il gruppo si scambia "
        "una lunga sequenza di auguri in chat (anche in video), "
        "compreso un messaggio di Giovanni Lima."),
    ("18:17", "Vincenzo Lacasasanta"): ("info",
        "Ha sentito Attilio Raglione per i dolci delle calze della "
        "Befana: l'anno scorso ne sono state fatte 900 (l'anno prima "
        "1000), rivendute a 5€, da 27 cm. Il costo dei prodotti "
        "dipenderà dalla scelta (si aggirerà sui 3€), più circa 1€ per "
        "la calza stessa (consiglia di comprarla a parte); porterà un "
        "catalogo nei prossimi giorni, sperando di avere altre info per "
        "venerdì."),
    ("21:50", "Maria Buttari"): ("domanda",
        "Chiede se anche uno spettacolo con i droni non fosse "
        "un'opzione da valutare, pur trovando valida la proposta dello "
        "sparatore."),
    ("23:15", "+39 327 974 7189"): ("info",
        "Un sostenitore esterno si offre di procurare un premio "
        "alimentare per la lotteria, scusandosi di non poter "
        "partecipare attivamente pur seguendo il lavoro del comitato."),
}

AUDIO_CURATED = {
    (DATE, "13:44", "Dante Caniglia", "PTT-20261026-WA0000.opus"): ("rumore", ""),
    (DATE, "18:28", "Emanuele Sciarra", "PTT-20261026-WA0015.opus"): ("rumore", ""),
    (DATE, "18:29", "Emanuele Sciarra", "PTT-20261026-WA0016.opus"): ("rumore", ""),
    (DATE, "20:08", "Emanuele Sciarra", "PTT-20261026-WA0036.opus"): ("rumore", ""),
    (DATE, "20:16", "Antonio Aceto", "PTT-20261026-WA0037.opus"): ("domanda",
        "Chiede se, prendendo due pullman invece di uno, la lotteria "
        "debba girare su entrambi o solo su uno: in tal caso "
        "servirebbero altri premi, perché quelli già raccolti erano "
        "previsti solo per un pullman."),
}

MEDIA_OVERRIDES = {
    (DATE, "18:29", "Emanuele Sciarra", "IMG-20261026-WA0018.jpg"):
        "Foto di un orologio da parete Pierre Cardin (marchio "
        "Imperial-life) appena ritirato: non eccezionale, ma a questo "
        "prezzo potrebbe essere utile come premio per la lotteria.",
    (DATE, "21:39", "Emanuele Sciarra", "IMG-20261027-WA0020.jpg"):
        "Foto dello sparatore in posa accanto alla \"pupazza\" appena "
        "costruita per gli spettacoli (un fantoccio a tema I Simpson, a "
        "grandezza naturale).",
    (DATE, "21:39", "Emanuele Sciarra", "IMG-20261027-WA0016.jpg"):
        "Foto di uno spettacolo pirotecnico fatto dallo sparatore ai "
        "Santi Martiri, esempio del suo lavoro.",
    (DATE, "21:39", "Emanuele Sciarra", "IMG-20261027-WA0008.jpg"):
        "Foto dell'attrezzatura pirotecnica (postazione con telecomando "
        "e cablaggio) usata dallo sparatore.",
}

TEXT_MERGES = [
    {
        "anchor_time": "08:04",
        "anchor_sender": "Costantino Mariani",
        "type": "proposta",
        "text": (
            "Il gruppo raccoglie nominativi di animatori per bambini in "
            "vista del Capodanno (contatti condivisi come vCard, non "
            "riportati qui per privacy): Costantino segnala Marta "
            "(sentito dire che è brava); Ilenia propone Antonella, "
            "definendola bravissima ed economica, da contattare subito "
            "perché molto richiesta; Serena propone anche \"Magicabula\" "
            "e il nominativo di Anita D'Elia. Emanuele conferma di "
            "conoscere bene Marta (faceva hip hop a sua figlia, la trova "
            "molto brava) ma suggerisce di contattarle tutte per "
            "confrontare disponibilità e proposta economica."
        ),
        "members": [
            ["08:04", "Costantino Mariani"], ["08:09", "Ilenia Piccozzi"],
            ["08:10", "Serena Di Stefano"], ["08:11", "Emanuele Sciarra"],
        ],
    },
    {
        "anchor_time": "20:19",
        "anchor_sender": "Maria Buttari",
        "type": "decisione",
        "text": (
            "Seguito alla domanda di Antonio sui pullman (vedi vocale "
            "20:16): il gruppo conferma che la lotteria si farà su "
            "entrambi i pullman (Barbara concorda). I premi raccolti "
            "finora salgono a 4, incluso quello portato da Selma "
            "(segnalato da Serena); si decide di tenere il premio "
            "\"PUDUE\" come primo premio per l'evento di agosto invece "
            "che per questa lotteria. Restano ancora da fare i giri per "
            "raccogliere altri premi dagli sponsor."
        ),
        "members": [
            ["20:19", "Maria Buttari"], ["20:40", "Barbara Rizio"],
            ["20:41", "Barbara Rizio"], ["20:48", "Serena Di Stefano"],
            ["20:52", "Antonio Aceto"], ["20:53", "Dante Caniglia"],
            ["20:53", "Antonio Aceto"], ["20:54", "Antonio Aceto"],
            ["20:54", "Elvis Ippoliti"],
        ],
    },
]

AUDIO_MERGES = [
    {
        "anchor_time": "17:51",
        "anchor_sender": "Ugo Trinchini",
        "type": "proposta",
        "text": (
            "Ugo ed Emanuele propongono di richiedere preventivi a più "
            "bande musicali per le prossime feste (Sant'Antonio, San "
            "Gabriele, Santa Maria Goretti): Ugo contatterebbe gli "
            "\"Ongini d'Abruzzo\", mentre Dante offre il contatto del "
            "cugino Guido, della banda di Celano (segnala anche una sorta "
            "di cortesia/rispetto tra bande di paesi diversi); Guido "
            "offre inoltre un impresario che potrebbe proporre anche "
            "cantanti e altro intrattenimento, da valutare a una "
            "prossima riunione. Si apre una breve divagazione su un "
            "eventuale Carnevale con carri: giudicato poco praticabile "
            "per le strade strette del paese (già tentato raramente in "
            "passato), un'eventuale ripresa andrebbe comunque valutata "
            "nel piano sicurezza con Mirko."
        ),
        "members": [
            "PTT-20261026-WA0002.opus", "PTT-20261026-WA0003.opus",
            "PTT-20261026-WA0004.opus", "PTT-20261026-WA0005.opus",
            "PTT-20261026-WA0006.opus", "PTT-20261026-WA0010.opus",
            "PTT-20261026-WA0011.opus", "PTT-20261026-WA0012.opus",
            "PTT-20261026-WA0013.opus", "PTT-20261026-WA0014.opus",
        ],
    },
    {
        "anchor_time": "19:09",
        "anchor_sender": "Costantino Mariani",
        "type": "proposta",
        "text": (
            "Costantino propone di muoversi anche su sparatori (fuochi "
            "d'artificio) e luminarie natalizie. Emanuele ha un contatto "
            "di fiducia a Celano (ha sparato anche al suo matrimonio, lo "
            "trova eccezionale) e conosce altri 3-4 sparatori in zona: "
            "si farà fare un video/preventivo, col prezzo che varia in "
            "base al tipo di spari richiesti. Anche Dante e Antonio "
            "Aceto lo conoscono personalmente (tramite la pesca e "
            "tramite il fratello, collega di lavoro di Antonio) e ne "
            "confermano l'affidabilità."
        ),
        "members": [
            "PTT-20261026-WA0024.opus", "PTT-20261026-WA0026.opus",
            "PTT-20261026-WA0029.opus", "PTT-20261026-WA0030.opus",
            "PTT-20261026-WA0031.opus", "PTT-20261026-WA0032.opus",
            "PTT-20261026-WA0033.opus", "PTT-20261026-WA0034.opus",
            "PTT-20261026-WA0035.opus",
        ],
    },
    {
        "anchor_time": "21:41",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "In serata Emanuele condivide foto e video ricevuti dallo "
            "sparatore di Celano: esempi di spettacoli già fatti (Luco, "
            "Santi Martiri, Sacro Cuore, inaugurazione della piazza a "
            "Pescina) e la \"pupazza\" a tema I Simpson appena costruita "
            "per gli spettacoli. Propone di organizzare un incontro con "
            "lui (questa settimana o alla prossima riunione) per "
            "valutare insieme la proposta."
        ),
        "members": [
            "PTT-20261026-WA0038.opus", "PTT-20261026-WA0039.opus",
        ],
    },
]

_SKIP_FILES = {
    # vCard di contatti (animatori bambini): nome riportato nel testo del
    # digest, numero di telefono volutamente non incluso (privacy).
    "Marta Animazione.vcf", "Antonella Animazione Bambini.vcf",
    "Anita D Elia.vcf",
    # reazioni video mute (verificate: nessuna traccia audio, niente
    # ffprobe in locale)
    "VID-20261026-WA0001.mp4", "VID-20261027-WA0027.mp4",
    # scatola dell'orologio, ridondante con la foto del prodotto
    "IMG-20261026-WA0019.jpg",
    # materiale promozionale dello sparatore (21:39): foto/video ripetitivi
    # di spettacoli pirotecnici già rappresentati dalle 3 foto tenute
    # (pupazza, Santi Martiri, attrezzatura) — tenute anche per non
    # appesantire inutilmente lo storage con video molto pesanti (fino a
    # ~150 MB l'uno).
    "IMG-20261027-WA0014.jpg", "IMG-20261027-WA0015.jpg",
    "IMG-20261027-WA0019.jpg", "IMG-20261027-WA0018.jpg",
    "IMG-20261027-WA0017.jpg", "IMG-20261027-WA0021.jpg",
    "IMG-20261027-WA0000.jpg", "IMG-20261027-WA0001.jpg",
    "IMG-20261027-WA0003.jpg", "IMG-20261027-WA0004.jpg",
    "IMG-20261027-WA0005.jpg", "IMG-20261027-WA0006.jpg",
    "IMG-20261027-WA0007.jpg", "IMG-20261027-WA0009.jpg",
    "IMG-20261027-WA0010.jpg", "IMG-20261027-WA0012.jpg",
    "VID-20261027-WA0025.mp4", "VID-20261027-WA0026.mp4",
    "VID-20261027-WA0022.mp4", "VID-20261027-WA0024.mp4",
    "VID-20261027-WA0023.mp4", "VID-20261027-WA0013.mp4",
    "VID-20261027-WA0002.mp4", "VID-20261027-WA0011.mp4",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES, audio_merges=AUDIO_MERGES,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="vCard / reazione muta / materiale promozionale ripetitivo")
