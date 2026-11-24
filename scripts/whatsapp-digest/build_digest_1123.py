#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-23 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:14-22:33. Costantino preferisce il calendario al porta-foto
(più commerciale, lo comprerebbero anche i nonni), propone una "pesca" per
la Befana legata alla lunghezza della sua scopa, e chiede come gestire le
prenotazioni per Capodanno. Emanuele chiarisce che il porta-foto era solo
un'opzione aggiuntiva al calendario, non sostitutiva, e chiede se decidere
subito sul gruppo i numeri di telefono per le prenotazioni di Capodanno o
aspettare la riunione. In mattinata Emanuele propone di ispirarsi a una
locandina vista in un altro gruppo per un mercatino natalizio, pensando a
un format simile (sfruttando "Magicabula" al posto degli artisti di
strada). Emanuele chiede se qualcuno ha contatti con il titolare del bar
"Libero" di Pescina per uno sponsor tramite fattura. In serata Emilio
riporta l'esito della riunione comunale sul calendario natalizio: l'8
dicembre (accensione albero e mercatini, con la castagnata Avis) sono
state prenotate due postazioni del Comitato (vin brulé e spazio foto); per
la Tombolata serve una nuova data, visto che il 27 dicembre è già
occupato da un concerto comunale. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-23"

CURATED = {
    ("08:16", "Costantino Mariani"): ("info",
        "Trova carina l'idea del porta-foto, ma pensa che il "
        "calendario sia la scelta migliore: più \"commerciale\", lo "
        "comprerebbero in quantità maggiori anche i nonni."),
    ("08:17", "Costantino Mariani"): ("proposta",
        "Dopo aver fatto stamattina \"la rotonda\", propone una "
        "\"pesca\" per la Befana legata alla lunghezza della scopa "
        "della Befana."),
    ("08:18", "Costantino Mariani"): ("domanda",
        "Chiede come iniziare a gestire i nominativi per le "
        "prenotazioni di Capodanno."),
    ("09:01", "Emanuele Sciarra"): ("proposta",
        "Condivide (foto) la locandina di un mercatino natalizio "
        "organizzato da un altro gruppo come spunto: se si ha "
        "qualcosa di pronto si potrebbe iniziare a creare una "
        "locandina simile. Non avendo artisti di strada, si "
        "potrebbe sfruttare \"Magicabula\" al loro posto."),
    ("22:33", "Emilio Caniglia"): ("info",
        "Sintesi della riunione promossa dall'amministrazione "
        "comunale per il calendario di Natale. L'8 dicembre: "
        "accensione dell'albero e mercatini di Natale, con anche la "
        "castagnata dell'Avis; come concordato in riunione, Emilio "
        "ha prenotato due postazioni (vin brulé e uno spazio foto) "
        "per non perdere l'occasione — prenotazione sempre "
        "revocabile, da confermare in riunione. Per la Tombolata, "
        "notizie negative: il 27 dicembre è già occupato da un "
        "concerto organizzato dal Comune, quindi andrà decisa "
        "un'altra data in riunione."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "08:18",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Emanuele chiarisce che l'idea del porta-foto con la "
            "pinzetta era solo un'aggiunta: il calendario resta in "
            "ogni caso, e si potrebbe vendere il calendario a 10€ e il "
            "porta-foto a 5€, per dare un'opzione in più. Sul tema "
            "Capodanno, ricorda che si era detto di attivare almeno "
            "due o tre numeri per raccogliere le prenotazioni "
            "(passando poi tramite Chiara per la locandina), e chiede "
            "se decidere la cosa direttamente sul gruppo o aspettare "
            "la riunione."
        ),
        "members": ["PTT-20261123-WA0000.opus", "PTT-20261123-WA0001.opus"],
    },
    {
        "anchor_time": "17:14",
        "anchor_sender": "Emanuele Sciarra",
        "type": "domanda",
        "text": (
            "Chiede se qualcuno ha confidenza con Andrea, il "
            "titolare del bar \"Libero\" a Pescina: quando era "
            "andato a chiedergli lo sponsor per l'85, questi aveva "
            "detto di non poter dare soldi direttamente, ma che gli "
            "avrebbe fatto comodo pagare una fattura (per lo scarico "
            "IVA). Dato che il Comitato deve comunque acquistare "
            "cioccolata per le calze, chiede se qualcuno può riparlargli "
            "con la scusa dello sponsor e verificare se è ancora "
            "interessato a questa soluzione."
        ),
        "members": ["PTT-20261123-WA0005.opus"],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "09:00", "Emanuele Sciarra", "IMG-20261123-WA0003.jpg"):
        "Locandina di un mercatino natalizio (\"Cercasi Partecipanti! "
        "Mercatino di Arte, Ingegno e Cibi Natalizi\", Bagnolo in "
        "Piano, domenica 20 dicembre) presa da un altro gruppo come "
        "spunto grafico: casetta di Babbo Natale, photobooth, "
        "animazioni col Grinch, esibizione di fuoco, laboratori "
        "creativi per bambini.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_merges=AUDIO_MERGES)
