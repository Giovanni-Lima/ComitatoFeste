#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-24 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 09:34-18:16. Emilio chiarisce che Magicabula non ci sarà l'8
dicembre (già un'animazione di Babbo Natale), resta un bonus per altre
occasioni; dettaglia le due postazioni prenotate (foto/calendario e vin
brulé) e la necessità di dividersi in squadre vista la fitta agenda
(8 dicembre, Tombolata, Capodanno, Befana, questua/banchetto di
Sant'Antonio). Si discute la data della Tombolata (ancora da fissare) e
un'idea di vendita di cornetti/ciambelle ai mercatini. Lungo confronto
(spesso acceso) sui tagliandini delle calze della Befana: personalizzarli
o no, prezzo a 5 o 6€ con o senza lotteria, chi ha già venduto cosa;
Emilio richiama che le decisioni si prendono in riunione, non in chat, e
conferma quanto già deciso (5€, niente lotteria); si avvia comunque la
stampa di tagliandini personalizzati tramite Lutech. Accenno finale (poco
chiaro) a un evento del 4 dicembre da organizzare in coppie. In serata è
nato Carlo, figlio di Barbara Rizio: lungo filo di auguri del gruppo, a
cui partecipa anche Giovanni Lima (suo messaggio, nessuna menzione da
parte di altri).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-24"

CURATED = {
    ("09:55", "Emilio Caniglia"): ("info",
        "Risponde a Ilenia che forse non conviene avere Magicabula "
        "l'8 dicembre, dato che ci sarà già un'animazione con un "
        "villaggio/casa di Babbo Natale. Magicabula resta un bonus "
        "per il Comitato, da coinvolgere quando si vuole (dalle "
        "calze della Befana alla Tombolata)."),
    ("09:59", "Emilio Caniglia"): ("info",
        "Per l'8 dicembre ha prenotato (sempre per non perdere "
        "l'opportunità, revocabile) due postazioni: uno stand "
        "foto/calendario nell'area villaggio di Babbo Natale, e "
        "un'altra con vin brulé (e possibilmente altro) vicino alla "
        "castagnata dell'Avis. Entrambe potrebbero servire anche per "
        "pubblicizzare le prevendite delle calze e Capodanno con "
        "locandine; ci si assicurerà di non avere concorrenza interna."),
    ("10:03", "Emilio Caniglia"): ("domanda",
        "Chiede di rivedere la data della Tombolata: 19 o 20 "
        "dicembre? Il 26 dicembre? Oppure nel nuovo anno, il 2 o 3 "
        "gennaio?"),
    ("10:09", "Emilio Caniglia"): ("info",
        "Visto il fitto calendario ravvicinato (8 dicembre, "
        "Tombolata, Capodanno, Befana), invita tutti a iniziare a "
        "dividersi per squadre per la buona riuscita degli eventi, "
        "con un minimo sforzo da parte di ciascuno. Antonio Sabatini "
        "rinnova lo stesso invito, ricordando che fino al 6 gennaio "
        "non ci sarà tregua, e che bisognerà anche iniziare la "
        "questua e il banchetto per Sant'Antonio."),
    ("11:33", "Emilio Caniglia"): ("info",
        "Le calze non sono ancora state ordinate: si sta valutando "
        "come confezionarle con prodotti di qualità a meno di 2,50€ "
        "l'una, confrontando diversi listini per massimizzare il "
        "ricavato. Cercherà di organizzare un incontro in sede "
        "sull'argomento (nel frattempo Antonio ha già venduto una "
        "quindicina di prevendite e anche Ilenia riceve richieste)."),
    ("13:34", "Ugo Trinchini"): ("info",
        "Fa notare che, se si è deciso di prendere calze da "
        "riempire (anziché già pronte), bisogna quantomeno ordinare "
        "la calza stessa; si offre di portare in serata il campione "
        "del materiale già visto, che risulta anche il meno costoso. "
        "Avvisa inoltre che l'indomani verso le 18/18:30 Tomas "
        "Amiconi (fuochi d'artificio) vuole incontrare il Comitato in "
        "sede per un preventivo (conferma il mattino dopo)."),
    ("15:59", "Emilio Caniglia"): ("info",
        "Richiama che le decisioni vengono prese in riunione e non "
        "in chat."),
    ("17:30", "Emilio Caniglia"): ("decisione",
        "Conferma che il prezzo delle calze (e le relative modalità "
        "di vendita) è stato deciso in riunione, dopo confronto e "
        "scambio di opinioni."),
    ("18:43", "Barbara Rizio"): ("info",
        "È nato Carlo, figlio di Barbara Rizio (3,390 kg): il "
        "gruppo si scambia auguri in chat."),
}

TEXT_MERGES = [
    {
        "anchor_time": "10:04",
        "anchor_sender": "Alessandra Toracchio",
        "type": "proposta",
        "text": (
            "Alessandra propone di chiedere a Maria se parteciperà "
            "ai mercatini, e in caso contrario di farle preparare "
            "cornetti e ciambelle da rivendere (non sarebbe un gran "
            "guadagno, ma la gente li prenderebbe volentieri). Luca "
            "propone in alternativa di prepararli loro stessi "
            "(ciambelle fritte e simili); Alessandra fa notare il "
            "problema delle norme HACCP, e Luca scherza che sua "
            "moglie è in possesso del relativo attestato."
        ),
        "members": [
            ["10:04", "Alessandra Toracchio"], ["10:05", "Luca Cicchelli"],
            ["10:05", "Alessandra Toracchio"], ["10:07", "Luca Cicchelli"],
            ["10:09", "Alessandra Toracchio"], ["10:12", "Luca Cicchelli"],
        ],
    },
]

AUDIO_MERGES = [
    {
        "anchor_time": "14:22",
        "anchor_sender": "Antonio Aceto",
        "type": "decisione",
        "text": (
            "Tina condivide come riferimento il tagliandino numerato "
            "del comitato dell'86 (\"Ritira la tua calza\", logo "
            "\"1986 TOP\", n. 122). Si apre un lungo confronto sul "
            "tagliandino delle calze: Antonio sostiene che "
            "risparmiandoci \"è il contenuto che conta\", ma Elvis "
            "ribatte che ne va dell'immagine del Comitato (sembra "
            "una cosa non organizzata) e che andrebbero fatti "
            "personalizzati, cosa possibile se ci si fosse mossi "
            "prima. Antonio spiega di aver finora venduto 18 calze "
            "con un blocchetto preso in sede, timbrando matrice e "
            "tagliandino con un datario impostato al 6 gennaio 2027 "
            "(la Befana); si offre di farsi ridare i tagliandini già "
            "venduti per cambiarli, se si decide di personalizzare. "
            "Ilenia propone di personalizzarli comunque e portare il "
            "prezzo a 6€ con un premio a estrazione come l'anno "
            "scorso (coperto allora da Amaranto); Antonio fa notare "
            "che sarebbe scorretto far pagare 5€ ad alcuni e 6€ ad "
            "altri per via dei tagliandini già in giro. Elvis non "
            "ricorda perché in riunione si fosse scelto 5€ invece di "
            "6€ con lotteria, dato che un euro in più su 900 calze "
            "avrebbe fruttato quasi 900€ gratuitamente; lui e "
            "Antonio, usciti dalla riunione in momenti diversi, "
            "ricostruiscono ricordi leggermente diversi su cosa "
            "fosse stato deciso esattamente. Ilenia chiede una "
            "riunione veloce per fissare calze, giornata dell'8 e "
            "Tombolata. Più tardi Emilio richiama che le decisioni "
            "si prendono in riunione e non in chat, e conferma che "
            "prezzo e modalità di vendita delle calze erano già "
            "stati decisi in riunione. Ugo, intervenuto solo in "
            "serata, segnala di aver già venduto una sessantina di "
            "calze a 5€ e di temere una brutta figura se il prezzo "
            "cambiasse a 6€; Ilenia ed Elvis concordano di restare a "
            "5€ visto quanto già venduto, rinunciando alla lotteria; "
            "Ilenia precisa di aver semplicemente pensato di essere "
            "ancora in tempo per cambiare, ma che va bene restare "
            "alla decisione della riunione senza ripensamenti. Sulla "
            "personalizzazione: Antonio chiede quanto costerebbe "
            "numerare i tagliandini; Dante spiega che con la stampa "
            "i numeri progressivi si generano automaticamente, "
            "mentre scriverli a mano richiederebbe ore di lavoro; "
            "Emanuele riferisce di essere passato da Lutech, che "
            "farebbe un tagliandino bianco col logo del Comitato a "
            "tiratura rapida (consegna scaglionata a blocchi da 50, "
            "tutti i 1000 entro una decina di giorni), lasciando "
            "eventualmente il numero da scrivere a mano per "
            "risparmiare tempo e qualcosa sul costo; chiede un "
            "parere su dove far fare grafica e stampa. Dante si "
            "offre infine di stampare lui stesso i tagliandini, se "
            "gli viene fornito il file."
        ),
        "members": [
            "PTT-20261124-WA0010.opus", "PTT-20261124-WA0011.opus",
            "PTT-20261124-WA0012.opus", "PTT-20261124-WA0013.opus",
            "PTT-20261124-WA0014.opus", "PTT-20261124-WA0015.opus",
            "PTT-20261124-WA0016.opus", "PTT-20261124-WA0017.opus",
            "PTT-20261124-WA0018.opus", "PTT-20261124-WA0022.opus",
            "PTT-20261124-WA0024.opus", "PTT-20261124-WA0025.opus",
            "PTT-20261124-WA0026.opus", "PTT-20261124-WA0027.opus",
            "PTT-20261124-WA0028.opus", "PTT-20261124-WA0029.opus",
            "PTT-20261124-WA0030.opus", "PTT-20261124-WA0031.opus",
        ],
    },
    {
        "anchor_time": "18:12",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Ricorda di dover iniziare a trovare le coppie per il 4 "
            "dicembre, in vista di una serata fra due settimane "
            "(riferimento non del tutto chiaro dalla trascrizione "
            "audio). Dante risponde che se ne occuperà Chiara, già "
            "tutto impostato; Emanuele precisa di volerla lasciare "
            "un po' in pace, visto che è già impegnata con contenuti "
            "social, locandine e altro. Antonio conferma la propria "
            "partecipazione al 4."
        ),
        "members": ["PTT-20261124-WA0032.opus"],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "13:53", "Tina Giarrante", "IMG-20261124-WA0023.jpg"):
        "Tagliandino di riferimento del comitato dell'86: \"Ritira "
        "la tua calza\", logo \"1986 TOP\", illustrazione di una "
        "Befana su scopa, numero progressivo stampato (122).",
    (DATE, "18:43", "Barbara Rizio", "IMG-20261124-WA0035.jpg"):
        "Fiocco nascita azzurro all'uncinetto appeso alla porta, con "
        "nastro ricamato \"È nato Carlo\".",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, text_merges=TEXT_MERGES,
                 audio_merges=AUDIO_MERGES)
