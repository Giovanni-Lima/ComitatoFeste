#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-07 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 09:16-20:02. Mattina: thread sulla stampa dei cartellini/badge
(Alessandra Toracchio vorrebbe procedere, Emanuele è d'accordo, Alessandro
Di Benedetto propone di cambiare la scritta, Elvis Ippoliti e Antonio
Sabatini frenano perché il comitato non esiste ancora giuridicamente —
09:16-09:33, TEXT_MERGES). Dante Caniglia (09:39, vocale) chiede un
chiarimento sulla roadmap degli eventi fino a fine 2026. Emanuele condivide
lo screenshot dell'approvazione della pagina Facebook (10:07) e riassume in
due vocali (10:18-10:19, AUDIO_MERGES) quanto deciso nelle riunioni:
Corinaldo, San Martino, Tombolata, Capodanno di massima approvato. Propone
poi (10:33-10:43, tre vocali + screenshot, AUDIO_MERGES) una seconda gita
all'Eurochocolate di Perugia (13-21 novembre), chiedendo referenti che si
impegnino a riempire il pullman; Dante (11:07) concorda sulla gita a Napoli
di fine novembre offrendo disponibilità. Emanuele illustra poi (11:01,
vocale) l'offerta aggiornata Bimby (promozione 4 venduti = 1 omaggio, 6
venduti = 100€ extra) proponendo una dimostrazione culinaria per le coppie
interessate, condivide il link del prodotto (11:09-11:10) e lo screenshot
con i prezzi (11:25). Emilio Caniglia (12:37) decide di aspettare a
stampare i cartellini fino alla costituzione giuridica del comitato, con
nome e cognome del membro ben visibili (anche per quanto accaduto a
Pescina), e conferma che Don Enzo ha dato il programma definitivo per
Corinaldo. Emanuele chiede (13:13) quando si può riusare il programma
della gita dell'85 per fare la locandina.

Pomeriggio (14:59-17:42): Antonio Aceto propone una data per l'Eurochocolate
(22/11) e preventivi pullman (TEXT_MERGES); Antonio Sabatini condivide la
locandina di un'offerta concorrente (Bianchi Tour, già organizzata); segue
un dibattito su opportunità/tempistica delle due gite ravvicinate (Elvis
cauto, Emanuele a favore citando l'esempio dell'85, Antonio Sabatini
preoccupato per il carico di eventi di fine anno). Emilio condivide i
preventivi raccolti per i pullman di Corinaldo (Bianchi/Di Curzio/
Passalacqua) chiedendo pareri sull'affidabilità; Elvis e Emanuele
riferiscono le proprie esperienze. Sera (18:52-19:30): Ugo Trinchini
consegna i primi doni della classe 1986 per la lotteria (buono regalo,
prodotti per capelli, un pacco da 45€, un sacchetto di bomboniere, materiale
di cancelleria). Nessuna menzione di Giovanni Lima da parte di altri in
questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-07"

CURATED = {
    ("10:35", "Raffaele Di Cesare"): ("domanda",
        "Chiede se la serata del 16 è confermata."),
    ("12:37", "Emilio Caniglia"): ("decisione",
        "Sul cartellino identificativo: meglio aspettare, il comitato non "
        "esiste ancora giuridicamente, si potrà procedere solo dopo la sua "
        "registrazione, riportando la denominazione esatta; per il membro "
        "del comitato è meglio indicare nome e cognome, anche per via di "
        "quanto accaduto a Pescina — ne parleranno in riunione. Conferma "
        "inoltre che Don Enzo ha dato il programma definitivo per la visita "
        "a Corinaldo, che sarà riportato nella locandina ufficiale."),
    ("13:13", "Emanuele Sciarra"): ("domanda",
        "Chiede al \"Preside\" quando si può utilizzare il programma della "
        "gita dell'85, per fare la locandina."),
    ("15:09", "Emanuele Sciarra"): ("proposta",
        "Controbatte che a favore delle due gite gioca il fatto dei posti "
        "limitati; riconosce che l'energia da spendere è soprattutto per "
        "trovare le persone da mettere sui pullman, ma ritiene fattibile "
        "dividersi i compiti."),
    ("15:13", "Elvis Ippoliti"): ("proposta",
        "Fa notare che non c'è solo da trovare le persone: bisogna anche "
        "organizzare San Martino, che richiede capire come muoversi per la "
        "cottura e il resto. Consiglia di ragionarci meglio prima di fare "
        "tante iniziative così ravvicinate, rimettendosi comunque al voto "
        "del gruppo."),
    ("15:15", "Antonio Sabatini"): ("proposta",
        "Si dice d'accordo con la cautela di Elvis, viste le tante cose da "
        "fare; per sé, dopo San Martino si concentrerebbe già su Natale e "
        "Befana, che considera già di per sé molto dispendiosi a livello "
        "organizzativo."),
    ("15:17", "Elvis Ippoliti"): ("info",
        "Osserva che bisogna comunque valutare la disponibilità delle "
        "persone, visto che nel giro di circa due mesi ci sono già da "
        "organizzare Natale, tombolata, Capodanno e Befana; si rimette a "
        "quanto si deciderà."),
    ("16:31", "Elvis Ippoliti"): ("info",
        "Riferisce 5 anni di esperienza con l'azienda Arpa: pullman comodo "
        "ma poco affidabile a livello di motore e riscaldamento."),
    ("16:34", "Emanuele Sciarra"): ("info",
        "Dice di conoscere Passalacqua e di aver viaggiato anche con Di "
        "Curzio (sia con l'85 che con amici); li ritiene entrambi "
        "affidabili."),
    ("17:42", "Maria Buttari"): ("info",
        "Riferisce la propria esperienza con un pullman da San Benedetto "
        "per la comunione: i parenti lo trovavano scomodo, ma il servizio "
        "(autista compreso) l'ha soddisfatta."),
}

AUDIO_CURATED = {
    (DATE, "09:39", "Dante Caniglia", "PTT-20261007-WA0001.opus"): ("domanda",
        "Non essendo stato alle ultime riunioni per lavoro, chiede: il "
        "briefing di Emilio copre le idee da convalidare fino a fine 2026, "
        "ma di solito un evento si organizza con anticipo (es. Capodanno, "
        "casa di Babbo Natale) — per queste cose non si è ancora iniziato a "
        "chiedere nulla."),
    (DATE, "11:01", "Emanuele Sciarra", "PTT-20261007-WA0008.opus"): ("proposta",
        "Riferisce che il prezzo del Bimby è sceso (circa 1.600-1.640€ con "
        "finanziamento a tasso zero su 24 mesi, incluso il kit per il pane); "
        "vendendo 4 Bimby uno arriva in omaggio, vendendone 6 si ottengono "
        "100€ extra a Bimby venduto più il secondo boccale per chi compra. "
        "Propone, per le 5-6 coppie già interessate, di organizzare una "
        "dimostrazione culinaria pomeridiana in un'unica serata (e "
        "altrettanto per il Folletto con un'altra referente)."),
    (DATE, "11:07", "Dante Caniglia", "PTT-20261007-WA0009.opus"): ("info",
        "Concorda con Emanuele sulla gita a Napoli: essendo tanti, con un "
        "pullman pieno ognuno può portare anche un familiare; si rende "
        "disponibile a dare una mano a organizzare."),
    (DATE, "15:17", "Emanuele Sciarra", "PTT-20261007-WA0015.opus"): ("proposta",
        "Pensa sia più facile organizzare l'Eurochocolate coinvolgendo "
        "anche i paesi limitrofi (potrebbero avere interesse ad "
        "aggregarsi), mentre Corinaldo interessa soprattutto a San "
        "Benedetto; precisa che è solo la sua opinione."),
    (DATE, "16:35", "Emanuele Sciarra", "PTT-20261007-WA0019.opus"): ("info",
        "Riferisce che Di Curzio li ha portati a Pescara per la festa del "
        "Celibato trovandoli in condizioni pietose, ma lo ritiene comunque "
        "molto affidabile come azienda."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "10:18",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Riassume quanto deciso nell'ultima riunione: Capodanno e le "
            "altre iniziative verranno approfondite riunione per riunione "
            "(almeno una al mese) fino a fine mandato; per ora si concentra "
            "la gita a Corinaldo, poi San Martino e l'organizzazione della "
            "tombolata. Il Capodanno risulta già \"tra virgolette\" "
            "approvato — sembra che sia l'ultimo anno che chi lo organizzava "
            "finora lo fa — e ci si può già organizzare anche per quello."
        ),
        "members": ["PTT-20261007-WA0002.opus", "PTT-20261007-WA0003.opus"],
    },
    {
        "anchor_time": "10:33",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Propone, oltre a Corinaldo, una seconda gita all'Eurochocolate "
            "di Perugia (13-21/22 novembre): non tutti vorranno andare a "
            "Corinaldo, e viceversa, quindi le due gite si completerebbero. "
            "Riconosce che organizzare due gite richiede la collaborazione "
            "di tutti; per questa come per le prossime (es. Napoli fine "
            "novembre) propone che due o tre persone si prendano la "
            "responsabilità di cercare partecipanti e riempire ogni "
            "pullman, citando come esempio Emilio e Alessandro per Perugia, "
            "e chiede se tutti sono d'accordo a organizzarsi così."
        ),
        "members": ["PTT-20261007-WA0004.opus", "PTT-20261007-WA0005.opus",
                    "PTT-20261007-WA0006.opus"],
    },
    {
        "anchor_time": "15:14",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Spiega che su 33 persone del gruppo, se solo 8 dicono sì a "
            "un'iniziativa gli altri 25 potrebbero comunque occuparsi "
            "d'altro, quindi gli impegni ravvicinati non sarebbero un "
            "problema reale; cita come esempio che l'85 ha fatto sia "
            "l'Eurochocolate sia una gita a Napoli a distanza di appena 15 "
            "giorni, riuscendo a riempire due pullman. Precisa che è solo "
            "un'idea senza obbligo: se piace al gruppo si fa, altrimenti si "
            "lascia perdere."
        ),
        "members": ["PTT-20261007-WA0013.opus", "PTT-20261007-WA0014.opus"],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "10:07", "Emanuele Sciarra", "IMG-20261007-WA0010.jpg"):
        "Screenshot del post Facebook della pagina del comitato con la "
        "locandina della gita a Corinaldo, finalmente approvato dagli "
        "amministratori del gruppo di San Benedetto.",
    (DATE, "10:34", "Emanuele Sciarra", "IMG-20261007-WA0007.jpg"):
        "Screenshot di una ricerca Google su \"Eurochocolate Perugia 2026\", "
        "che mostra le date dell'evento (13-22 novembre 2026) nel centro "
        "storico di Perugia.",
    (DATE, "11:25", "Emanuele Sciarra", "IMG-20261007-WA0011.jpg"):
        "Foto di un proiettore con il listino prezzi Bimby TM7: con 4 "
        "vendite il Bimby è gratuito completo di accessori più un anno di "
        "abbonamento Cookidoo; prezzo 1.638€ a tasso zero (rata 68,25€ su "
        "24 mesi) oppure 1.599€ pagando in contanti/bonifico/carta, 1.420€ "
        "con IVA agevolata al 4%; vendendone 6 si ottiene anche il secondo "
        "boccale in omaggio.",
    (DATE, "15:07", "Antonio Sabatini", "IMG-20261007-WA0018.jpg"):
        "Locandina pubblicitaria di Bianchi Tour per una gita a "
        "Eurochocolate Perugia 2026 nelle domeniche 15 e 22 novembre, a "
        "39€ (bus + ingresso incluso, posti limitati) — una gita simile è "
        "quindi già organizzata da un'agenzia esterna.",
    (DATE, "16:29", "Emilio Caniglia", "IMG-20260910-WA0068.jpg"):
        "Tabella con i preventivi raccolti per il trasporto a Corinaldo: "
        "Bianchi Tour (54 posti/1.100€, 64 posti/1.250€, 83 posti/1.800€), "
        "Di Curzio (54 posti/1.200€) e Passalacqua (54 posti/1.100€), con "
        "relativo costo a posto.",
    (DATE, "18:52", "Ugo Trinchini", "IMG-20261007-WA0024.jpg"):
        "Scatola con materiale di cancelleria per la lotteria: blocchi "
        "numerati e quaderni da ufficio, parte dei doni della classe 1986.",
    (DATE, "18:52", "Ugo Trinchini", "IMG-20261007-WA0023.jpg"):
        "Sacchetto con fantasia di palline colorate, da un laboratorio di "
        "bomboniere, tra i doni della classe 1986 per la lotteria.",
    (DATE, "18:52", "Ugo Trinchini", "IMG-20261007-WA0022.jpg"):
        "Pacco regalo incartato con fiocco rosso ed etichetta \"Comitato "
        "Feste 1986 — valore commerciale 45€\", tra i doni per la lotteria.",
    (DATE, "18:53", "Ugo Trinchini", "IMG-20261007-WA0020.jpg"):
        "Buono regalo da 50€ del negozio \"A modo tuo\" (abbigliamento "
        "bambino, intimo uomo-donna) di Lecce nei Marsi, tra i doni della "
        "classe 1986 per la lotteria.",
    (DATE, "18:53", "Ugo Trinchini", "IMG-20261007-WA0021.jpg"):
        "Prodotti per capelli Botexpharma (balsamo districante, pasta e "
        "gel naturali), tra i doni della classe 1986 per la lotteria.",
}

TEXT_MERGES = [
    {
        "anchor_time": "09:16",
        "anchor_sender": "Alessandra Toracchio",
        "type": "proposta",
        "text": (
            "Riferendosi all'opzione uscita vincente dal sondaggio, chiede "
            "quando può andare a stampare i cartellini/badge, dato che per "
            "lei sono leggibili e chiari. Emanuele Sciarra è d'accordo a "
            "procedere; Alessandro Di Benedetto propone di scrivere "
            "\"comitato feste patronali\" invece dell'immagine. Elvis "
            "Ippoliti e Antonio Sabatini invitano invece ad aspettare e a "
            "informarsi meglio, non essendoci fretta e non essendo chiaro "
            "se il cartellino si possa usare prima della costituzione "
            "ufficiale del comitato."
        ),
        "members": [
            ["09:16", "Alessandra Toracchio"],
            ["09:17", "Alessandra Toracchio"],
            ["09:19", "Emanuele Sciarra"],
            ["09:27", "Alessandra Toracchio"],
            ["09:28", "Alessandro Di Benedetto"],
            ["09:30", "Elvis Ippoliti"],
            ["09:31", "Alessandra Toracchio"],
            ["09:32", "Elvis Ippoliti"],
            ["09:33", "Antonio Sabatini"],
        ],
    },
    {
        "anchor_time": "14:59",
        "anchor_sender": "Antonio Aceto",
        "type": "proposta",
        "text": (
            "Propone di organizzare la gita Eurochocolate per il 22 "
            "novembre, visto che la settimana prima si organizza San "
            "Martino; suggerisce di farsi fare nel frattempo dei preventivi "
            "per i pullman — chi preferisce Eurochocolate a Corinaldo "
            "avrebbe comunque una rappresentanza del comitato in entrambi i "
            "posti."
        ),
        "members": [
            ["14:59", "Antonio Aceto"],
            ["15:01", "Antonio Aceto"],
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES)
