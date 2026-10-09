#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-09 — solo dati di curatela, logica comune in digest_lib.py.

Giornata dell'8/10 silenziosa (nessun messaggio). Finestra 07:36-14:35.
Mattina: Emanuele chiede chi gestisce le prenotazioni Corinaldo (gli ha
scritto su Facebook un esterno per 2 posti); Emilio pubblica un messaggio
di aggiornamenti fissato (pullman Corinaldo prenotato/opzionato, 103-104
posti, referenti per le prenotazioni; richiesta sala per l'incontro Bimby
del 16/10, minimo 20 coppie; contatti Pro Loco per Halloween/San Martino,
serve un team di 10-15 persone). Luca (vocale) chiede quanti del comitato
andranno a Corinaldo. Serena propone una futura gita a Nettuno in
primavera. A mezzogiorno arrivano le prime adesioni per l'incontro Bimby
del 16/10 (TEXT_MERGES).

Dalle 13:24 lungo thread sulla castagnata di San Martino (quantità da
procurare, conservazione/congelamento, prezzo, materiali per i cartocci):
diviso in tre blocchi tematici con TEXT_MERGES + AUDIO_MERGES separati per
tenerlo leggibile senza perdere i dettagli operativi concreti (quantità,
prezzi, date). Chiude un sotto-thread su chi debba occuparsi della
pubblicità/locandina di San Martino (Pro Loco o il comitato stesso, visto
che partecipa con vin brulè e castagne). Nessuna menzione di Giovanni Lima
da parte di altri in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-09"

CURATED = {
    ("07:36", "Emanuele Sciarra"): ("domanda",
        "Chiede chi si sta occupando delle prenotazioni per Corinaldo: ieri "
        "sera gli ha scritto su Facebook Simone Odoardi chiedendo di "
        "prenotare per 2 persone."),
    ("08:10", "Emilio Caniglia"): ("decisione",
        "Messaggio di aggiornamenti (fissato in chat). Visita a Corinaldo: "
        "è stato \"prenotato\" un pullman con opzione su un secondo con "
        "Passalacqua, per un totale di 103/104 posti; chi ha già "
        "prenotazioni raccolte col passaparola deve comunicarlo subito ad "
        "Antonio Sabatini, Alessandro Di Benedetto o Serena Di Stefano (la "
        "prenotazione si perfeziona solo col pagamento della quota); a "
        "breve la locandina, che sarà stampata/affissa e pubblicata sui "
        "social. Incontro promozionale del 16 ottobre: oggi si richiede la "
        "sala consiliare del Comune; si comincia a raccogliere in chat i "
        "nomi delle coppie interessate, serve un minimo di 20 coppie. "
        "Halloween e San Martino: nei prossimi giorni contatti con la Pro "
        "Loco per il loro programma; il comitato si organizza per San "
        "Martino, serve un team di almeno 10-15 persone. Altri eventi non "
        "calendarizzati: chiunque può proporre un'iniziativa a beneficio "
        "del comitato, prendendo spunto anche dalle idee di Emanuele "
        "Sciarra."),
    ("10:32", "Serena Di Stefano"): ("proposta",
        "Propone di organizzare, oltre alla gita a Corinaldo, anche una "
        "gita a Nettuno, eventualmente in primavera."),
    ("14:33", "Alessandra Toracchio"): ("info",
        "Risponde che se la Pro Loco organizza la pubblicità si può "
        "chiedere di citare la partecipazione del comitato 87 con le "
        "castagne; propone di farla insieme, ma prima bisogna chiedere."),
}

AUDIO_CURATED = {
    (DATE, "08:31", "Luca Cicchelli", "PTT-20261009-WA0000.opus"): ("domanda",
        "Si scusa per le assenze e chiede quanti membri del comitato "
        "andranno alla gita a Corinaldo."),
    (DATE, "09:24", "Maikel Montano", "PTT-20261009-WA0002.opus"): ("domanda",
        "Riferisce che la signora contattata per le castagne è malata e "
        "quest'anno ne ha pochissime; lo mette in contatto con un'altra "
        "persona, probabilmente a un prezzo meno conveniente. Chiede se "
        "qualcun altro conosce un fornitore con un prezzo migliore, e "
        "quante castagne servano, perché la settimana successiva a "
        "Civitella c'è una festa che rischia di esaurirle."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "13:38",
        "anchor_sender": "Maikel Montano",
        "type": "info",
        "text": (
            "Maikel conferma che quest'anno le castagne scarseggiano nella "
            "zona (i castagneti si sono ammalati), è in attesa di un altro "
            "contatto; Cesare conferma di avere già un fornitore, anche se "
            "la qualità è da verificare. Emanuele, oltre alla quantità, "
            "pensa anche a una piccola scenografia con cestini di vimini, "
            "ricci e foglie di castagno, e ricorda che ci sarà pure il vin "
            "brulè, utile anche per i bambini. Antonio Aceto riferisce di "
            "aver già chiesto 25 kg a un collega di Civitella, che "
            "risponderà entro la settimana successiva."
        ),
        "members": ["PTT-20261009-WA0003.opus", "PTT-20261009-WA0004.opus",
                    "PTT-20261009-WA0005.opus", "PTT-20261009-WA0006.opus",
                    "PTT-20261009-WA0007.opus", "PTT-20261009-WA0008.opus",
                    "PTT-20261009-WA0009.opus", "PTT-20261009-WA0010.opus",
                    "PTT-20261009-WA0011.opus", "PTT-20261009-WA0012.opus"],
    },
    {
        "anchor_time": "14:04",
        "anchor_sender": "Antonio Aceto",
        "type": "info",
        "text": (
            "Antonio Aceto spiega perché il collega di Civitella non può "
            "dargli subito le castagne: le deve prima raccogliere e "
            "curare, e gliele consegnerà solo a ridosso dell'evento "
            "(intorno a 5€/kg) per evitare che si rovinino; precisa anche "
            "che, una volta scongelate, vanno poi cotte tutte insieme."
        ),
        "members": ["PTT-20261009-WA0013.opus", "PTT-20261009-WA0014.opus",
                    "PTT-20261009-WA0015.opus", "PTT-20261009-WA0016.opus",
                    "PTT-20261009-WA0017.opus", "PTT-20261009-WA0018.opus",
                    "PTT-20261009-WA0019.opus", "PTT-20261009-WA0020.opus"],
    },
    {
        "anchor_time": "14:13",
        "anchor_sender": "Antonio Aceto",
        "type": "info",
        "text": (
            "Antonio Aceto propone, in alternativa alle porzioni singole "
            "già pesate, di congelare le castagne in blocchi da 4-5 kg; "
            "per i guantoni da forno pesanti servirà un contatto di "
            "Alessandra."
        ),
        "members": ["PTT-20261009-WA0021.opus", "PTT-20261009-WA0022.opus",
                    "PTT-20261009-WA0023.opus", "PTT-20261009-WA0024.opus",
                    "PTT-20261009-WA0025.opus"],
    },
    {
        "anchor_time": "14:27",
        "anchor_sender": "Emanuele Sciarra",
        "type": "domanda",
        "text": (
            "Chiede se della pubblicità/locandina per San Martino se ne "
            "occuperà la Pro Loco o se deve pensarci il comitato, dato che "
            "quest'anno partecipa anche con vin brulè e castagne — in tal "
            "caso conviene farlo sapere alla gente; chiede se negli anni "
            "precedenti la Pro Loco si è già occupata di una locandina, "
            "altrimenti bisogna sentirli."
        ),
        "members": ["PTT-20261009-WA0026.opus", "PTT-20261009-WA0027.opus"],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "13:37", "Elvis Ippoliti", "IMG-20261009-WA0030.jpg"):
        "Screenshot di una ricerca online su quante castagne ci sono in un "
        "classico cartoccio da strada (tra le 7 e le 10, circa 100g), a "
        "supporto del calcolo delle quantità da procurare.",
    (DATE, "13:37", "Elvis Ippoliti", "IMG-20261009-WA0031.jpg"):
        "Screenshot di una ricerca online su quante castagne ci sono in un "
        "chilo (tra le 60 e le 80 di media, a seconda della pezzatura), a "
        "supporto dello stesso calcolo.",
    (DATE, "14:00", "Alessandra Toracchio", "IMG-20261009-WA0029.jpg"):
        "Foto di alcune castagne comprate al supermercato Eurospin, di "
        "buona pezzatura.",
    (DATE, "14:26", "Raffaele Di Cesare", "IMG-20261009-WA0028.jpg"):
        "Screenshot di una guida organizzativa \"Festa di San Martino — "
        "Castagne & Vin Brulè\" (San Benedetto dei Marsi) con tabelle sul "
        "dimensionamento dei cartocci (10-12 castagne, 150-200g) e sul "
        "fabbisogno di castagne crude in base all'affluenza prevista (es. "
        "500 persone ≈ 110-120 kg), più consigli su proporzioni del vin "
        "brulè e preparazione; Raffaele commenta scherzosamente \"Siamo "
        "sempre nel 2026 giusto?\".",
}

TEXT_MERGES = [
    {
        "anchor_time": "12:11",
        "anchor_sender": "Antonio Aceto",
        "type": "info",
        "text": (
            "Si raccolgono le prime adesioni per l'incontro promozionale "
            "Bimby del 16 ottobre: Antonio Aceto con Jennifer, Tina "
            "Giarrante (in coppia), Raffaele Di Cesare con Verdy."
        ),
        "members": [
            ["12:11", "Antonio Aceto"],
            ["12:13", "Tina Giarrante"],
            ["12:22", "Raffaele Di Cesare"],
        ],
    },
    {
        "anchor_time": "13:28",
        "anchor_sender": "Dante Caniglia",
        "type": "proposta",
        "text": (
            "Si apre il thread sulla quantità di castagne da procurare per "
            "la castagnata di San Martino. Dante suggerisce di chiamare "
            "contatti nel Carsolano (zona Poggio Cinolfo e dintorni, che "
            "hanno sempre roscette e marroni); Costance si offre di "
            "chiedere, una volta saputa la quantità. Emanuele chiede un "
            "parere al gruppo e propone 50 kg come base di partenza. Luca "
            "chiede quante castagne ci siano in un chilo e segnala che "
            "serve procurare un rullo per la cottura. Cesare chiede a "
            "Valentina D'Arcadia di verificare disponibilità e prezzo. "
            "Elvis calcola che con 50 kg si ottengono 40-50 cartocci; nel "
            "gruppo si arriva a discutere (anche scherzosamente, tra "
            "Vincenzo e Dante) se il numero di cartocci totali desiderato "
            "sia più vicino a 500."
        ),
        "members": [
            ["13:28", "Dante Caniglia"], ["13:28", "Costance Rossi"],
            ["13:29", "Emanuele Sciarra"], ["13:30", "Emanuele Sciarra"],
            ["13:31", "Emanuele Sciarra"], ["13:34", "Luca Cicchelli"],
            ["13:36", "Luca Cicchelli"], ["13:41", "Cesare Raglione"],
            ["13:45", "Elvis Ippoliti"], ["13:52", "Vincenzo Lacasasanta"],
            ["13:52", "Dante Caniglia"], ["13:53", "Dante Caniglia"],
            ["13:54", "Elvis Ippoliti"], ["13:54", "Dante Caniglia"],
        ],
    },
    {
        "anchor_time": "14:00",
        "anchor_sender": "Alessandra Toracchio",
        "type": "info",
        "text": (
            "Alessandra riferisce di aver già preso delle castagne da "
            "Eurospin (belle grosse, circa 120g/8 pezzi: servono 10-11 per "
            "riempire un cartoccio) e che si rovinano comunque entro l'11 "
            "novembre, ma propone come soluzione il congelamento. Martina "
            "segnala un possibile contatto in Valle Roveto (visto su "
            "Instagram) e suggerisce di congelare le castagne a porzioni "
            "già pesate, indicando un prezzo orientativo della roscetta "
            "intorno ai 15€/kg. Si discute del prezzo (5€/kg dal collega "
            "di Civitella contro il prezzo da supermercato) e Barbara fa "
            "notare che la scarsità generale potrebbe far salire i prezzi; "
            "Alessandra mette a disposizione il proprio congelatore."
        ),
        "members": [
            ["14:00", "Alessandra Toracchio"], ["14:00", "Costance Rossi"],
            ["14:02", "Martina Del Gizzi"], ["14:03", "Alessandra Toracchio"],
            ["14:03", "Martina Del Gizzi"], ["14:04", "Alessandra Toracchio"],
            ["14:05", "Martina Del Gizzi"], ["14:05", "Alessandra Toracchio"],
            ["14:06", "Martina Del Gizzi"], ["14:07", "Alessandra Toracchio"],
            ["14:07", "Martina Del Gizzi"], ["14:09", "Martina Del Gizzi"],
            ["14:09", "Alessandra Toracchio"], ["14:10", "Martina Del Gizzi"],
            ["14:10", "Alessandra Toracchio"], ["14:10", "Luca Cicchelli"],
            ["14:11", "Antonio Aceto"], ["14:11", "Martina Del Gizzi"],
            ["14:11", "Alessandra Toracchio"], ["14:11", "Barbara Rizio"],
        ],
    },
    {
        "anchor_time": "14:12",
        "anchor_sender": "Martina Del Gizzi",
        "type": "info",
        "text": (
            "Prosegue il confronto su come preparare i cartocci: Martina "
            "propone di congelare porzioni già pesate, Elvis preferisce "
            "contare a occhio il numero di castagne (10-12 circa) senza "
            "pesare ogni porzione; si concorda che la castagnata dovrebbe "
            "tenersi il 14 o 15 novembre. Per i cartocci si valuta il "
            "giornale riciclato al posto dei bicchieri di plastica; "
            "Alessandra mette a disposizione buste da congelatore e "
            "propone di stampare due etichette col logo del comitato da "
            "attaccare ai cartocci, idea approvata da Elvis."
        ),
        "members": [
            ["14:12", "Alessandra Toracchio"], ["14:12", "Martina Del Gizzi"],
            ["14:13", "Elvis Ippoliti"], ["14:13", "Martina Del Gizzi"],
            ["14:14", "Martina Del Gizzi"], ["14:14", "Elvis Ippoliti"],
            ["14:15", "Martina Del Gizzi"], ["14:16", "Martina Del Gizzi"],
            ["14:16", "Antonio Aceto"], ["14:16", "Elvis Ippoliti"],
            ["14:17", "Martina Del Gizzi"], ["14:18", "Antonio Aceto"],
            ["14:18", "Martina Del Gizzi"], ["14:18", "Alessandra Toracchio"],
            ["14:19", "Martina Del Gizzi"], ["14:19", "Elvis Ippoliti"],
            ["14:19", "Alessandra Toracchio"], ["14:20", "Alessandra Toracchio"],
            ["14:20", "Martina Del Gizzi"], ["14:21", "Alessandra Toracchio"],
            ["14:21", "Martina Del Gizzi"], ["14:22", "Alessandra Toracchio"],
            ["14:23", "Alessandra Toracchio"], ["14:26", "Elvis Ippoliti"],
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES)
