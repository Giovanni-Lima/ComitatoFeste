#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-17 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:22-17:02 (export Dropbox delle 17:47, giornata ancora in corso).
Il punto riepilogativo degli auguri di compleanno a Gilda Di Iulio resta in
build_digest_1116.py (primo messaggio della sera prima): i proseguimenti di
auguri che ricadono già nel 17/11 (incluso quello di Giovanni Lima) restano
rumore individuale, non ripetuti qui. La mattina Emanuele riceve un commento
dal tono politico sotto il reel dei ringraziamenti di San Martino: lunga
discussione nel gruppo su come reagire (ignorare o rispondere, se sia un bot
o una persona reale), risolta con cancellazione del commento, segnalazione e
blocco dell'autore, senza alcuna risposta pubblica — tra i pareri anche
quello di Giovanni Lima (ipotesi bot di propaganda), ripreso esplicitamente
da Elvis. Antonio Sabatini rendiconta la vendita delle ultime castagne.
Emanuele propone un cappellino invernale col logo della classe 87 al posto
di felpe/cappotti, accolto bene dal gruppo.

Sera (18:35-21:24, aggiornata con l'export del 18/11 delle 00:28): Emilio
aggiorna sulla banda (Pescina la più conveniente, Celano non ha preventivato,
Capistrello costa 2.000 € in più): si conferma Pescina salvo obiezioni, con
l'ok di Elvis, Luca, Maria, Costantino ed Emidio; resoconto venerdì 20/11.
Emanuele lancia l'idea per l'accensione dell'albero (casetta in legno, Babbo
Natale con Antonio Aceto, elfi, letterine, foto e calendari da vendere):
lunga discussione con Ilenia (il villaggio di Babbo Natale lo fa la Pro
Loco l'8/12 in piazza D'Arpizio, serve evitare di "bruciare" l'idea), il
Grinch che ruba le letterine (Luca), il percorso a ostacoli (Elvis),
Magicabula (Serena), le foto istantanee (Luca). Per le date: la Pro Loco
vorrebbe accendere l'albero con i mercatini il 5 o 6 dicembre (Elvis: il 6
c'è il rosario con Don Enzo). Emanuele anticipa che per la Befana ci sarà il
Comune con Magicabula; Serena chiede di chiarire la voce che il comitato
organizzi il Natale, e Emanuele spiega il calendario degli eventi che si
deciderà venerdì (bozza allegata). Il resto è rumore (battute, sticker).
Nessuna menzione di Giovanni Lima da parte di altri.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-17"

CURATED = {
    ("08:23", "Antonio Sabatini"): ("info",
        "Comunica che le ultime castagne rimaste sono state divise "
        "equamente tra tre membri del comitato: tutto venduto. "
        "Venerdì in riunione verrà esposto, per chiarezza, il "
        "resoconto della giornata di sabato scorso (San Martino)."),
}

MEDIA_OVERRIDES = {
    (DATE, "20:58", "Luca Cicchelli", "IMG-20261117-WA0050.jpg"):
        "Locandina dell'evento dell'anno scorso: \"La Proloco di San "
        "Benedetto dei Marsi presenta Il Villaggio di Babbo Natale\", "
        "8 dicembre dalle ore 15:00, Piazza D'Arpizio (davanti alla "
        "Domus), con casetta e albero gonfiabili e animazione "
        "(Magicabula).",
    (DATE, "21:18", "Emanuele Sciarra", "IMG-20261117-WA0051.jpg"):
        "Bozza di locandina \"Calendario eventi\" (logo 1987, \"Il "
        "Natale è vicino\") con tre esempi segnaposto: 16 dicembre "
        "mercatino in Piazza del Risorgimento (18-23), 20 dicembre Natale "
        "in famiglia (ore 12, Piazza del Risorgimento), 22 dicembre "
        "serata Babbo Natale (ore 18, Santa Sabina); Emanuele: \"idea è "
        "più o meno questa per capire\".",
    (DATE, "07:22", "Emanuele Sciarra", "IMG-20261117-WA0000.jpg"):
        "Screenshot di un commento (di un profilo esterno al "
        "comitato, dai contenuti perlopiù politici) lasciato sotto il "
        "reel di ringraziamento per San Martino pubblicato da "
        "Emanuele: un attacco politico scollegato dal video, "
        "percepito come fuori contesto.",
    (DATE, "11:28", "Costance Rossi", "IMG-20261117-WA0028.jpg"):
        "Locandina di un evento culturale non legato al comitato: "
        "doppio incontro con l'autrice Catena Fiorello Galeano, "
        "domenica 22 novembre 2026, Sala Consiliare del Comune di San "
        "Benedetto dei Marsi (rassegna \"Un autunno da sfogliare\").",
    (DATE, "16:36", "Emanuele Sciarra", "IMG-20261117-WA0031.jpg"):
        "Cosa ne pensate se al posto di felpe o cappotti facciamo un "
        "cappellino con logo e scritta classe 87? Credo che d'inverno "
        "sia comodo per tutti e bene o male tutti lo usiamo... "
        "(immagine di esempio: un berretto personalizzabile con "
        "ricamo di testo/logo, disponibile in molti colori).",
}

AUDIO_CURATED = {
    (DATE, "21:08", "Emanuele Sciarra", "PTT-20261117-WA0046.opus"): ("info",
        "Venerdì in riunione darà un'altra notizia: per la Befana ci "
        "sarà la partecipazione del Comune con Magicabula, bisogna solo "
        "dare la data; spiegherà meglio in riunione."),
    (DATE, "08:02", "Costantino Mariani", "PTT-20261117-WA0020.opus"): ("rumore", ""),
    (DATE, "08:21", "Luca Cicchelli", "PTT-20261117-WA0021.opus"): ("rumore", ""),
    (DATE, "08:21", "Luca Cicchelli", "PTT-20261117-WA0022.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {
        "anchor_time": "20:04", "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Sulle date e sull'idea del Grinch: Emanuele ricorda che Lisa "
            "aveva detto di voler fare l'accensione dell'albero insieme ai "
            "mercatini il 6 dicembre. Elvis obietta che il 6 non si può "
            "fare nulla perché c'è la funzione in chiesa con Don Enzo e "
            "serve la disponibilità delle persone; Emanuele pensa sia il "
            "rosario, circa mezz'ora (non ne è sicuro). Per il Grinch, "
            "aveva visto i costumi in un negozio (circa 15-18 € per "
            "adulti) e l'aveva pensato per la tombolata. Ripete poi "
            "l'idea di partenza: una poltrona nella casetta per le foto "
            "con Babbo Natale (Antonio) e fare qualcosa anche con i "
            "bambini, per non limitarsi alla sola accensione; chiede "
            "altre idee."
        ),
        "members": [
            "PTT-20261117-WA0036.opus", "PTT-20261117-WA0037.opus",
            "PTT-20261117-WA0038.opus", "PTT-20261117-WA0039.opus",
            "PTT-20261117-WA0040.opus", "PTT-20261117-WA0041.opus",
        ],
    },
    {
        "anchor_time": "20:49", "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Emanuele a Luca: l'idea delle foto (con annesso calendario da "
            "vendere) dipende dal capire se la casa/villaggio di Babbo "
            "Natale si fa; se non la fanno si può sfruttare la stessa "
            "cosa con due elfi, un Babbo Natale, letterine portate o "
            "appese all'albero. Per l'accensione dei mercatini la Pro Loco "
            "vorrebbe farla il 5 o 6 dicembre (sabato o domenica, perché "
            "l'8 è un martedì e c'è più affluenza), e ha parlato solo di "
            "mercatini e accensione dell'albero. Concorda che bisogna "
            "chiedere cosa vogliono fare e trarre le conclusioni, magari "
            "approfittando dell'accensione se c'è la casetta."
        ),
        "members": [
            "PTT-20261117-WA0042.opus", "PTT-20261117-WA0043.opus",
            "PTT-20261117-WA0044.opus", "PTT-20261117-WA0045.opus",
        ],
    },
    {
        "anchor_time": "21:16", "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Emanuele: la Pro Loco sta organizzando i mercatini e non sa "
            "se ci sarà anche il villaggio di Babbo Natale con la casetta. "
            "Serena, a voce, dice che circola la voce che il comitato "
            "stia organizzando Natale e Befana, cosa nuova per il gruppo, "
            "e propone di chiarirla (forse con la Pro Loco). Emanuele "
            "risponde che con Chiara stanno preparando un calendario degli "
            "eventi del periodo natalizio: venerdì si decide cosa fare e "
            "poi si lancia la locandina con gli eventi del comitato e "
            "quelli in cui ci si appoggia alla Pro Loco, citata anch'essa."
        ),
        "members": [
            "PTT-20261117-WA0047.opus", "PTT-20261117-WA0048.opus",
            "PTT-20261117-WA0049.opus",
        ],
    },
    {
        "anchor_time": "07:23",
        "anchor_sender": "Emanuele Sciarra",
        "type": "decisione",
        "text": (
            "Dopo aver pubblicato il reel di ringraziamento per San "
            "Martino, Emanuele trova sotto al post un commento dal "
            "tono politico (vedi foto) e, preoccupato di aver "
            "involontariamente dato un'impressione politica, chiede "
            "consiglio al gruppo su come comportarsi, rileggendo più "
            "volte il proprio testo senza trovarvi riferimenti "
            "politici. Alessandra Simonetti consiglia di non "
            "rispondere, facendo notare che il commento è palesemente "
            "fuori luogo; Luca è incerto se rispondere o lasciar "
            "perdere, osservando che anche rispondere potrebbe "
            "insinuare qualcosa. Emanuele valuta anche l'idea di far "
            "intervenire un profilo esterno al comitato per chiedere "
            "chiarimenti, preoccupato per l'immagine del comitato; "
            "Maria lo rassicura di lasciar perdere, spiegando che è "
            "pura provocazione e analizzando il profilo dell'autore "
            "(solo 8 follower contro 5.000 seguiti, tutti post a "
            "sfondo politico, a suo dire \"il solito coglione di "
            "turno\"): non merita risposta. Emanuele propone quindi di "
            "bloccare, e Luca è d'accordo per evitare polemiche senza "
            "fine. Giovanni Lima ipotizza che possano essere bot "
            "automatici di propaganda che attaccano a caso, e invita "
            "a bloccare e andare avanti; Dante pensa invece sia una "
            "persona vera. Elvis concorda sull'approccio "
            "segnalare-bloccare-andare avanti senza rispondere, "
            "riprendendo esplicitamente l'ipotesi di Giovanni sulla "
            "propaganda/incitamento all'odio. Emanuele conferma che "
            "eliminerà il commento, lo segnalerà e bloccherà l'autore. "
            "Costantino concorda sulla pericolosità di esporsi così "
            "apertamente politicamente, scherzando sul rischio di "
            "guai; Elvis ribadisce lo stesso concetto. Valentina pensa "
            "si tratti di commenti generati da intelligenza "
            "artificiale e di aver già bannato lei stessa l'autore; "
            "Elvis dissente, ritenendo dal profilo che si tratti "
            "invece di una persona reale ossessionata di politica. "
            "Emanuele chiude dicendo che, bot o persona reale che "
            "sia, ha comunque già eliminato il commento e bloccato "
            "l'autore. Più tardi Dante ribadisce che si tratta "
            "probabilmente di una persona normale che si è sbagliata "
            "(\"i bot su Facebook non esistono più\"), consigliando di "
            "nascondere il commento; Emanuele conferma di aver già "
            "eliminato tutto e bloccato la persona, nella speranza di "
            "evitare ulteriori attriti."
        ),
        "members": [
            "PTT-20261117-WA0001.opus", "PTT-20261117-WA0002.opus",
            "PTT-20261117-WA0003.opus", "PTT-20261117-WA0004.opus",
            "PTT-20261117-WA0005.opus", "PTT-20261117-WA0006.opus",
            "PTT-20261117-WA0007.opus", "PTT-20261117-WA0008.opus",
            "PTT-20261117-WA0009.opus", "PTT-20261117-WA0010.opus",
            "PTT-20261117-WA0011.opus", "PTT-20261117-WA0012.opus",
            "PTT-20261117-WA0014.opus", "PTT-20261117-WA0015.opus",
            "PTT-20261117-WA0016.opus", "PTT-20261117-WA0017.opus",
            "PTT-20261117-WA0018.opus", "PTT-20261117-WA0019.opus",
            "PTT-20261117-WA0023.opus", "PTT-20261117-WA0024.opus",
            "PTT-20261117-WA0025.opus", "PTT-20261117-WA0026.opus",
            "PTT-20261117-WA0027.opus",
        ],
    },
]

TEXT_MERGES = [
    {
        "anchor_time": "18:35", "anchor_sender": "Emilio Caniglia",
        "type": "decisione",
        "text": (
            "Aggiornamento banda (Emilio): dopo il preventivo della banda "
            "di Pescina c'è stato un contatto con la banda di Celano, che "
            "non ha preventivato perché la proposta sarebbe stata più alta; "
            "domenica mattina Vincenzo Lacasasanta ha incontrato la banda "
            "di Capistrello, il cui preventivo è più alto di 2.000 € "
            "rispetto a Pescina. Entrambe le bande hanno chiesto conferma "
            "entro metà settimana: dato il preventivo più basso e il fatto "
            "che negli ultimi anni ha sempre animato le feste, si procede a "
            "confermare la banda di Pescina (salvo obiezioni), per evitare "
            "che prenda impegni nelle date preventivate. Venerdì 20 "
            "novembre ci sarà un resoconto. Elvis, Luca e Maria approvano."
        ),
        "members": [["18:35", "Emilio Caniglia"], ["18:36", "Elvis Ippoliti"],
                    ["18:38", "Luca Cicchelli"], ["18:44", "Maria Buttari"]],
    },
    {
        "anchor_time": "19:53", "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Idea di Emanuele per l'accensione dell'albero: se ci fosse la "
            "casetta in legno usata a Natale (chiede di chi sia, se "
            "noleggiata o della Pro Loco o del Comune), allestirla con una "
            "poltrona, Antonio Aceto vestito da Babbo Natale e alcuni "
            "elfi (costumi noleggiabili da Fantacarta ad Avezzano), con "
            "consegna delle letterine e foto, agganciandosi ai calendari "
            "da vendere. Ilenia: Babbo Natale deve arrivare con il "
            "villaggio, altrimenti si perde la magia, e fare le foto quel "
            "giorno \"brucerebbe\" l'idea del calendario; il villaggio "
            "di solito lo fanno ogni anno (gonfiabili, vero Babbo Natale, "
            "animazione), da verificare chi se ne occupa e i costi. "
            "Se la Pro Loco non lo facesse, il comitato se ne occuperebbe, "
            "da decidere quando. Ilenia trova simpatica l'idea del Grinch "
            "(Luca: potrebbe rubare le letterine) con foto e magari un "
            "gioco a tema per raccogliere qualche soldo, e propone di "
            "valutare le disponibilità sia per il 6 sia per l'accensione. "
            "Costantino approva."
        ),
        "members": [
            ["19:53", "Emanuele Sciarra"], ["19:55", "Emanuele Sciarra"],
            ["19:56", "Emanuele Sciarra"], ["19:57", "Luca Cicchelli"],
            ["19:58", "Emanuele Sciarra"], ["19:58", "Barbara Rizio"],
            ["19:58", "Ilenia Piccozzi"], ["19:59", "Elvis Ippoliti"],
            ["19:59", "Ilenia Piccozzi"], ["19:59", "Emanuele Sciarra"],
            ["20:00", "Ilenia Piccozzi"], ["20:00", "Emanuele Sciarra"],
            ["20:01", "Emanuele Sciarra"], ["20:01", "Ilenia Piccozzi"],
            ["20:02", "Ilenia Piccozzi"], ["20:02", "Emanuele Sciarra"],
            ["20:03", "Ilenia Piccozzi"], ["20:03", "Elvis Ippoliti"],
            ["20:03", "Luca Cicchelli"], ["20:04", "Ilenia Piccozzi"],
            ["20:05", "Ilenia Piccozzi"], ["20:06", "Ilenia Piccozzi"],
            ["20:06", "Costantino Mariani"],
        ],
    },
    {
        "anchor_time": "20:08", "anchor_sender": "Costantino Mariani",
        "type": "info",
        "text": (
            "Costantino vota per la banda di Pescina; Emidio è d'accordo "
            "(scrive che vengano i \"leoncini\", nei quali suonano anche "
            "alcuni ragazzi di San Benedetto)."
        ),
        "members": [["20:08", "Costantino Mariani"],
                    ["20:19", "Emidio Cerasani"]],
    },
    {
        "anchor_time": "20:29", "anchor_sender": "Luca Cicchelli",
        "type": "proposta",
        "text": (
            "Altre idee per i bambini: Luca propone di staccare le "
            "letterine appese all'albero per portarle a Babbo Natale, con "
            "il Grinch che disturba i bambini e un piccolo premio "
            "(caramelle o leccalecca a tema); Elvis un percorso a "
            "ostacoli molto semplice per imbucare la letterina nella "
            "cassetta di Babbo Natale con il Grinch che li ostacola, "
            "premi in caramelle. Serena segnala che Magicabula ha un "
            "allestimento completo per il villaggio di Babbo Natale. "
            "Emanuele chiede altre idee per fare la differenza; Luca "
            "riprende l'idea di stampare foto istantanee per raccogliere "
            "qualche euro."
        ),
        "members": [["20:29", "Luca Cicchelli"], ["20:32", "Elvis Ippoliti"],
                    ["20:35", "Luca Cicchelli"], ["20:37", "Serena Di Stefano"],
                    ["20:40", "Emanuele Sciarra"], ["20:49", "Luca Cicchelli"]],
    },
    {
        "anchor_time": "20:54", "anchor_sender": "Ilenia Piccozzi",
        "type": "info",
        "text": (
            "Ilenia crede che il villaggio di Babbo Natale lo organizzi la "
            "Pro Loco. Luca condivide la locandina dell'evento dell'anno "
            "scorso (quindi probabilmente si ripeterà) e osserva che, se "
            "la Pro Loco lascia spazio alle idee del comitato, si può fare "
            "qualcosa di più grande: bisogna ritagliarsi uno spazio per un "
            "evento insieme, utile a entrambi (per loro maggiore "
            "partecipazione), saper parlare e trovare un'intesa, perché gli "
            "eventi principali sono tutti loro."
        ),
        "members": [["20:54", "Ilenia Piccozzi"], ["20:58", "Luca Cicchelli"],
                    ["20:59", "Luca Cicchelli"], ["21:06", "Luca Cicchelli"]],
    },
    {
        "anchor_time": "21:13", "anchor_sender": "Serena Di Stefano",
        "type": "domanda",
        "text": (
            "Serena chiede se è già confermato che il comitato stia "
            "organizzando il Natale e non la Befana (è arrivata questa "
            "voce). Ilenia crede che organizzare il Natale non convenga: "
            "non si recupererebbero le spese. Emanuele spiega che se si "
            "decide venerdì quali eventi fare si può pubblicare tutto "
            "(bozza di calendario allegata) e le voci finiranno; Serena "
            "pensa a un malinteso."
        ),
        "members": [["21:13", "Serena Di Stefano"], ["21:15", "Ilenia Piccozzi"],
                    ["21:15", "Emanuele Sciarra"], ["21:18", "Luca Cicchelli"],
                    ["21:19", "Emanuele Sciarra"], ["21:20", "Emanuele Sciarra"],
                    ["21:20", "Serena Di Stefano"]],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES)
