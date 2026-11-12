#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-12 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:55-17:32 (export Dropbox delle 17:35, giornata ancora in corso
al momento dell'export — manca un giorno a San Martino, sabato 14/11).
Emilio gira il preventivo della banda di Pescina "I Leoncini d'Abruzzo"
(date confermate da Don Enzo, manca solo Venerdì Santo) per un totale di
8.000€, invitando chi ha altri contatti a proporre preventivi alternativi;
più tardi Vincenzo riferisce la disponibilità della banda di Avezzano per
un confronto. Luca propone di raccogliere foto/video di tutti gli eventi
dell'anno per un video-ricordo finale, idea che Elvis rilancia proponendo
una serata di chiusura ("La Festa prima delle Feste") per proiettarlo;
Maria chiede di cominciare a raccogliere materiale già da San Martino.
Valentina propone di recuperare le "quartieriadi" di un tempo, un evento
per ciascuno dei 4 quartieri del paese. Il gruppo conferma la scritta del
banchetto ("Da Zio Elvis Vin Brulè", con relativa grafica) tra scherzi sul
vestirsi da Babbo Natale, e Alessandra prepara la scenografia (funghi di
cartone, una targa "bacareje" ancora da correggere, palloncini numerati).
Nel pomeriggio: organizzazione logistica di balle di paglia, prolunghe,
padelle (appuntamento in sede Avis) e bracieri (recuperati tramite Armando
Scalcetto a Gioia, con un momento di confusione su dove si trovassero
risolto da Maikel); Valentina scrive a testate locali per la copertura
stampa; Emilio dettaglia il preventivo di "Cannelor" per la pubblicità sul
bando cittadino e propone un sondaggio; Alessandra censisce i vini per
sabato e mostra le etichette in lavorazione; il gruppo discute il reperire
un campanaccio o, in alternativa, damigiane/conche per l'allestimento.
Condiviso anche l'invito del Comune per la firma di un protocollo a tutela
degli orfani di femminicidio. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-12"

CURATED = {
    ("07:55", "Emilio Caniglia"): ("proposta",
        "Gira il preventivo della banda di Pescina \"I Leoncini "
        "d'Abruzzo\": le date indicate sono già state confermate da Don "
        "Enzo (manca solo Venerdì Santo); chi ha contatti con altre "
        "bande può comunque contattarle o proporle al Comitato per un "
        "preventivo alternativo. Preventivo del Circolo Musicale Banda "
        "\"I Leoncini D'Abruzzo\" (Pescina): domenica 17 gennaio "
        "(Sant'Antonio) 1.000€ per 15/16 elementi; domenica 28 "
        "febbraio (San Gabriele) 1.000€ per 15/16 elementi; 5 e 6 "
        "giugno (feste di Giugno) 1.200€ al giorno per 20/22 elementi; "
        "27, 28 e 29 agosto (feste di Agosto) 1.200€ al giorno per "
        "20/22 elementi — totale 8.000€. Propone di sentirsi al "
        "telefono e incontrarsi appena possibile."),
    ("10:03", "Valentina D'Arcadia"): ("proposta",
        "Ripensando alle quartieriadi degli anni passati, propone di "
        "organizzare un evento per ciascuno dei 4 quartieri del paese, "
        "per coinvolgere ancora di più tutta la cittadinanza."),
    ("10:09", "Emanuele Sciarra"): ("info",
        "Ritiene che si potrebbe fare, ma non è sicuro se per "
        "iniziative di questo tipo serva prima il via libera della Pro "
        "Loco."),
    ("12:09", "Vincenzo Lacasasanta"): ("proposta",
        "Riferisce che domenica mattina la banda di Avezzano è "
        "disponibile a parlare per un preventivo alternativo a quello "
        "dei Leoncini d'Abruzzo, e chiede se qualcuno può "
        "accompagnarlo per intanto sentire cosa propongono."),
    ("13:58", "Elvis Ippoliti"): ("proposta",
        "Chiede di modificare la scritta della targa del banchetto in "
        "\"se magne bon i se bev meje\" (cambiando la \"e\" con la "
        "\"i\" in dialetto), scherzando sul fatto di averla scritta da "
        "ubriaco."),
    ("15:41", "Emanuele Sciarra"): ("domanda",
        "Chiede ad Alessandra se suo marito è riuscito a procurarle i "
        "guanti."),
    ("16:00", "Emilio Caniglia"): ("info",
        "Dice che della questione della corrente elettrica parlerà "
        "domani in riunione."),
    ("16:29", "Alessandra Toracchio"): ("info",
        "Dice che se si riesce a procurarne di nuovi tra oggi e domani "
        "va bene, altrimenti porta i suoi che usa al forno a legna."),
}

MEDIA_OVERRIDES = {
    (DATE, "10:46", "Valentina D'Arcadia", "IMG-20261112-WA0013.jpg"):
        "Grafica scelta per il banchetto: \"Da Zio Elvis Vin Brulè\", "
        "scritta su sfondo bordeaux con decorazioni di uva, ulivi e "
        "calici di vino.",
    (DATE, "11:03", "Alessandra Toracchio", "IMG-20261112-WA0012.jpg"):
        "Decorazioni a tema bosco (funghi di cartone e cespugli, ceste "
        "di vimini) caricate in auto, parte della scenografia che sta "
        "preparando.",
    (DATE, "13:53", "Alessandra Toracchio", "IMG-20261112-WA0020.jpg"):
        "Bozza della targa per il banchetto: \"DA ZIO ELVIS BACAREJE, "
        "SE MAGNE BON E SE BEV MEJE\", su sfondo bordeaux con "
        "decorazioni di uva, funghi e zucca — testo ancora da "
        "correggere (vedi messaggio successivo di Elvis).",
    (DATE, "13:53", "Alessandra Toracchio", "IMG-20261112-WA0021.jpg"):
        "Festone a tema zucche con la scritta \"W SAN MARTINO\", già "
        "allestito.",
    (DATE, "13:53", "Alessandra Toracchio", "IMG-20261112-WA0022.jpg"):
        "Palloncino giallo con il numero \"1987\", parte della "
        "composizione numerata a cui sta lavorando.",
    (DATE, "15:58", "Emilio Caniglia", "IMG-20261112-WA0032.jpg"):
        "Gira l'invito dell'Amministrazione Comunale di San Benedetto "
        "dei Marsi, in collaborazione con \"Il Giardino Segreto\" e il "
        "Progetto Airone: firma del Protocollo d'Intesa per la tutela "
        "degli orfani di femminicidio e violenza domestica, venerdì 13 "
        "novembre 2026 alle 15:00 in Sala Consiliare.",
    (DATE, "15:59", "Antonio Aceto", "IMG-20261112-WA0031.jpg"):
        "I due fuconi (bracieri) caricati su un rimorchio, pronti per "
        "essere portati in piazza.",
    (DATE, "17:09", "Alessandra Toracchio", "IMG-20261112-WA0037.jpg"):
        "Screenshot di un programma di grafica con la bozza delle "
        "etichette per i vini: \"vino rosso\", \"vino bianco\" (due "
        "varianti), \"vin brulè\".",
}

# Foto-ricordo/scherzo personale (selfie legato alla battuta su Costantino
# e la curia) e un duplicato dell'invito già condiviso da Emilio: nessun
# contenuto organizzativo aggiuntivo, escluse come le foto ridondanti già
# scartate in altre giornate.
_SKIP_EXTRA_1112 = {"IMG-20261112-WA0011.jpg", "IMG-20261112-WA0036.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_EXTRA_1112


AUDIO_CURATED = {
    (DATE, "09:28", "Emanuele Sciarra", "PTT-20261112-WA0004.opus"): ("rumore", ""),
    (DATE, "11:47", "Emidio Cerasani", "PTT-20261112-WA0009.opus"): ("rumore", ""),
    (DATE, "11:47", "Emanuele Sciarra", "PTT-20261112-WA0010.opus"): ("rumore", ""),
    (DATE, "12:00", "Luca Cicchelli", "PTT-20261112-WA0014.opus"): ("rumore", ""),
    (DATE, "13:48", "Antonio Aceto", "PTT-20261112-WA0017.opus"): ("info",
        "Comunica che oggi alle 15:00 c'è un appuntamento alla sede "
        "dell'Avis per andare a prendere le padelle per cuocere le "
        "castagne, chiedendo se qualcuno vuole accompagnarlo o se ha "
        "le chiavi della sede per aprirgli e sistemarle lì. Antonio "
        "Sabatini risponde di avere sempre lui le chiavi e di essere "
        "disponibile ad aprire al volo appena saputo l'orario."),
    (DATE, "13:54", "Alessandra Toracchio", "PTT-20261112-WA0023.opus"): ("info",
        "Mostra alcuni palloncini gialli su cui vuole scrivere un "
        "numero per ciascuno (come quello con \"1987\"), per provare a "
        "comporre qualcosa da disporre in giro una volta gonfiati "
        "tutti; sta preparando il materiale, partendo dal colore "
        "giallo già scelto."),
    (DATE, "13:57", "Emanuele Sciarra", "PTT-20261112-WA0024.opus"): ("info",
        "Conferma di avere lui le prolunghe con le ciabatte da "
        "cantiere; controllerà in magazzino domani, non riuscendo "
        "oggi perché stacca tardi dal lavoro."),
    (DATE, "13:57", "Emanuele Sciarra", "PTT-20261112-WA0025.opus"): ("info",
        "Riporta che anche il Comitato Classe '85 si è complimentato "
        "per l'iniziativa di San Martino, tramite un messaggio di "
        "Maria Laura."),
    (DATE, "14:06", "Ugo Trinchini", "PTT-20261112-WA0026.opus"): ("info",
        "È a Letre e si offre di accompagnare chi passa dalla "
        "Dolciaria Vecchia, vicino alla braceria della Muletta."),
    (DATE, "15:53", "Emanuele Sciarra", "PTT-20261112-WA0029.opus"): ("rumore", ""),
    (DATE, "16:45", "Emanuele Sciarra", "PTT-20261112-WA0030.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {
        "anchor_time": "09:15",
        "anchor_sender": "Luca Cicchelli",
        "type": "proposta",
        "text": (
            "Luca propone di raccogliere foto e video di tutti gli "
            "eventi dell'anno per montare, a fine percorso, un "
            "video-ricordo che ciascuno potrà tenersi; fa notare che "
            "del materiale esiste già (l'infiorata con la classe '86 "
            "dell'anno scorso, la gita a Corinaldo). Antonio chiede "
            "conferma che non sia una battuta; Luca risponde che era "
            "serio. Elvis trova l'idea bella e rilancia: si potrebbe "
            "proiettare il video in una serata di chiusura dedicata a "
            "ringraziare tutti per l'anno appena trascorso, con "
            "intrattenimento e atmosfera, da studiare se tutti sono "
            "d'accordo. Luca cita come precedente la festa di fine "
            "estate con cui la classe 1986 aveva concluso il proprio "
            "percorso, proponendo di fare qualcosa di simile per "
            "chiudere."
        ),
        "members": [
            "PTT-20261112-WA0000.opus", "PTT-20261112-WA0001.opus",
            "PTT-20261112-WA0002.opus", "PTT-20261112-WA0003.opus",
            "PTT-20261112-WA0005.opus", "PTT-20261112-WA0006.opus",
        ],
    },
    {
        "anchor_time": "10:30",
        "anchor_sender": "Alessandra Toracchio",
        "type": "decisione",
        "text": (
            "Alessandra propone di scrivere sul banchetto \"VIN BRULÈ "
            "DI ZIO ELVIS\"; il gruppo approva tra le risate (Emanuele "
            "la trova simpatica, Elvis è d'accordo e scherza sul "
            "vestirsi da Babbo Natale con dei sacchi di iuta, di cui "
            "Barbara ha la disponibilità). Emanuele fa sapere di non "
            "avere una barba da Babbo Natale — verificherà a casa nel "
            "pomeriggio — e chiede se si siano trovate le due balle di "
            "paglia o se restino solo i rotoloni; Alessandra conferma "
            "che si sta procurando qualcosa anche per quello. Valentina "
            "condivide poi la grafica della scritta, che il gruppo "
            "conferma come versione definitiva (Alessandra: "
            "\"decidetevi prima che inizio la scritta\"; Maria ed "
            "Elvis: \"questa è la migliore\"; Alessandra: \"andata\"). "
            "Emanuele chiede infine di fare qualche foto del risultato, "
            "da allegare a quelle dell'allestimento di sabato per "
            "risparmiare un reel a parte."
        ),
        "members": ["PTT-20261112-WA0007.opus", "PTT-20261112-WA0008.opus"],
    },
    {
        "anchor_time": "13:29",
        "anchor_sender": "Costantino Mariani",
        "type": "info",
        "text": (
            "Costantino si scusa per l'assenza, dice di essere "
            "comunque aggiornato (ha letto e ascoltato tutti i "
            "messaggi), e comunica di aver trovato lui le balle di "
            "paglia: le deve andare a caricare, non sa se stasera o "
            "domani sera con l'auto o se dovrà usare il furgoncino. "
            "Offre anche un po' di prolunghe e ciabatte per le "
            "correnti alternate."
        ),
        "members": ["PTT-20261112-WA0015.opus", "PTT-20261112-WA0016.opus"],
    },
    {
        "anchor_time": "13:53",
        "anchor_sender": "Luca Cicchelli",
        "type": "domanda",
        "text": (
            "Luca chiede quando si debba andare a prendere il braciere "
            "e come verrà trasportato, facendo notare che è grosso e "
            "pesante."
        ),
        "members": ["PTT-20261112-WA0018.opus", "PTT-20261112-WA0019.opus"],
    },
    {
        "anchor_time": "14:48",
        "anchor_sender": "Cesare Raglione",
        "type": "info",
        "text": (
            "Cesare spiega che i braceri di Armando Scalcetto si "
            "trovano a Gioia, dal Prologo, che glieli riporterà oggi "
            "pomeriggio al suo negozio; lui li scaricherà con il "
            "muletto, andranno poi trasportati con un rimorchio, e lui "
            "stesso li scaricherà di nuovo in piazza con il muletto. "
            "Antonio fa però notare che, secondo quanto gli ha "
            "riferito Salvatore, i braceri starebbero nel cortile di "
            "Sergio, e dice che quando andrà a prendere le padelle "
            "farà un salto a controllare; Maikel chiarisce di aver "
            "parlato il giorno prima con Sergio, che prima sembrava "
            "non saperne nulla, poi è risultato che li aveva prestati "
            "alla Pro Loco di Gioia."
        ),
        "members": ["PTT-20261112-WA0027.opus", "PTT-20261112-WA0028.opus"],
    },
    {
        "anchor_time": "17:12",
        "anchor_sender": "Elvis Ippoliti",
        "type": "proposta",
        "text": (
            "Elvis chiede se si riesce a procurare un campanaccio di "
            "quelli usati al collo delle mucche, di quelli grossi; "
            "Tina chiede se ce l'ha Dante. Barbara aggiunge che "
            "servirebbero anche delle fiaschette o damigiane di una "
            "volta, o qualche conca di rame, per l'allestimento, se "
            "qualcuno le ha; Elvis trova l'idea delle damigiane con la "
            "paglia intorno molto bella per l'allestimento, e dice che "
            "controllerà a casa. Dante risponde di non avere "
            "campanacci, ma propone in alternativa un acchiappasogni "
            "fatto con le lattine; chiede conferma al padre, mentre "
            "Tina ricorda di ricordarselo appeso tra vecchi collari "
            "(pur dicendosi poco attendibile); Dante conferma che non "
            "ci sono, solo dei \"vreccali\" (sassi), purtroppo. "
            "Emanuele si offre di chiedere a una collega che ha "
            "un'azienda di vitelli se ne ha uno da prestare."
        ),
        "members": [
            "PTT-20261112-WA0033.opus", "PTT-20261112-WA0034.opus",
            "PTT-20261112-WA0035.opus",
        ],
    },
]

TEXT_MERGES = [
    {
        "anchor_time": "09:27",
        "anchor_sender": "Maria Buttari",
        "type": "proposta",
        "text": (
            "Sulla stessa idea, Maria chiede di raccogliere già da San "
            "Martino qualche foto in più per il video di Chiara; Elvis "
            "propone di chiamare la serata di proiezione \"La Festa "
            "prima delle Feste\"."
        ),
        "members": [["09:27", "Maria Buttari"], ["09:31", "Elvis Ippoliti"]],
    },
    {
        "anchor_time": "14:08",
        "anchor_sender": "Dante Caniglia",
        "type": "info",
        "text": (
            "Alla proposta delle quartieriadi, Dante risponde \"5\"; "
            "Martina chiede perché 5, visto che oltre al quartiere "
            "migliore (la Cittadella) ce ne sono altri; Dante elenca, "
            "in dialetto: \"La cord, I pajarej, l casett gnov I la "
            "garbatell\"."
        ),
        "members": [
            ["14:08", "Dante Caniglia"], ["14:10", "Martina Del Gizzi"],
            ["14:11", "Dante Caniglia"],
        ],
    },
    {
        "anchor_time": "15:32",
        "anchor_sender": "Valentina D'Arcadia",
        "type": "info",
        "text": (
            "Valentina scrive sia a Marsica Live sia a Terre Marsicane "
            "segnalando che, oltre alle castagnate di venerdì al "
            "Cerchio, ce n'è una anche a San Benedetto, allegando la "
            "locandina, per vedere se rispondono; scrive anche ad AZ "
            "Informa, sperando che non venga chiesto un contributo per "
            "l'articolo."
        ),
        "members": [
            ["15:32", "Valentina D'Arcadia"], ["15:40", "Valentina D'Arcadia"],
            ["15:41", "Valentina D'Arcadia"],
        ],
    },
    {
        "anchor_time": "16:15",
        "anchor_sender": "Emilio Caniglia",
        "type": "proposta",
        "text": (
            "Alla domanda di Elvis su come si fosse rimasti con "
            "\"Cannelor\" per la pubblicità, Emilio risponde di aver "
            "contattato Daniele \"Cannelor\" per il bando cittadino, "
            "riportando i costi: 250€ per il pacchetto completo "
            "(indipendentemente dal numero di eventi, dall'inizio alla "
            "fine del mandato del Comitato, comprensivo di San "
            "Martino, pagamento a fine mandato) oppure 25€ a chiamata "
            "(per ogni giro di macchina). Ricorda che dal Comitato "
            "Classe 1981 in poi si è sempre scelto il pacchetto "
            "completo, tranne l'ultimo Comitato (classe 1986) che ha "
            "preferito pagare a chiamata. Visto l'impegno di spesa, "
            "propone per la sera stessa un sondaggio per scegliere tra "
            "le due opzioni, ricordando che la decisione sarà comunque "
            "riportata in riunione per la conferma ufficiale."
        ),
        "members": [["16:07", "Elvis Ippoliti"], ["16:15", "Emilio Caniglia"]],
    },
    {
        "anchor_time": "16:44",
        "anchor_sender": "Alessandra Toracchio",
        "type": "domanda",
        "text": (
            "Alessandra chiede quanti vini servano per sabato (rosso, "
            "bianco, vin brulè) e se si sta dimenticando qualcosa; "
            "Antonio risponde elencando vino rosso, bianco, rosato e "
            "vin brulè, escludendo il novello. Alessandra condivide "
            "poi (foto) la bozza delle etichette che sta preparando "
            "per i vini."
        ),
        "members": [
            ["16:44", "Alessandra Toracchio"], ["16:45", "Alessandra Toracchio"],
            ["17:07", "Alessandra Toracchio"], ["17:08", "Alessandra Toracchio"],
            ["17:08", "Antonio Aceto"], ["17:09", "Alessandra Toracchio"],
            ["17:10", "Alessandra Toracchio"], ["17:10", "Antonio Aceto"],
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="foto personale o duplicato di una già condivisa")
