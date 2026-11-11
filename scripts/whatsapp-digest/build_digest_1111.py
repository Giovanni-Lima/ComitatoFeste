#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-11 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:03-21:15 (coda aggiunta l'11/11 con l'export Dropbox delle
21:48 — la festa di San Martino è sabato 14/11, questa è la vigilia).
Lunga mattinata di prove tecniche per far funzionare la ricondivisione del
post/locandina sui social (Facebook/Instagram) tra i vari membri, risolta
verso le 9:50. Oggi è anche San Martino (onomastico di Martina Del Gizzi,
festeggiata dal gruppo) e Dante coglie l'occasione per gli auguri di rito.
Antonio riferisce una voce incoraggiante per il veglione di Capodanno: la
Rupe non lo farà quest'anno, quindi San Benedetto resterebbe l'unica
opzione in paese — si valuta un incontro con Andrea Di Loreto per
organizzare la comunicazione/sponsorizzazione dell'evento, con cautela sul
rivelarne già il nome (nel pomeriggio/sera Maikel aggiorna che l'incontro
non si è ancora concretizzato, rimandato forse a domani). Nel pomeriggio
arrivano le castagne (106-107 kg): si decide di venderle sfuse pesate al
momento in piazza invece che in sacchetti pre-confezionati, si discute di
quante sgusciare/cuocere in anticipo (si converge su una ventina di kg, il
resto intero anche per la lotteria) e Emanuele spiega la prova di cottura
a piccoli lotti con l'attrezzo nuovo. Nel tardo pomeriggio si organizza
anche l'apertura della sede per portare castagne, tovaglie e la
scenografia (ricci e foglie di castagne). Emilio annuncia che venerdì
preparerà uno schema dei gruppi/attività e un recap del materiale, e che
si è già assicurata la presenza della Protezione Civile; valuta anche
(dopo il suggerimento di Cesare) un annuncio a pagamento dell'evento, da
sottoporre a sondaggio. In serata il gruppo spinge sulla visibilità social
del reel di Chiara e propone di farsi scrivere un articolo da una pagina
locale. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-11"

CURATED = {
    ("09:04", "Maria Buttari"): ("info",
        "Oggi è San Martino, onomastico di Martina Del Gizzi: il gruppo "
        "si scambia auguri in chat."),
    ("14:00", "Elvis Ippoliti"): ("info",
        "Ricorda che venerdì si farà una prova con i sacchetti per "
        "valutare le quantità, e che i sacchetti vanno anche piegati."),
    ("14:43", "Antonio Sabatini"): ("info",
        "Comunica di essere stato delegato dal presidente ad aprire la "
        "sede: chi può si trovi lì per le 15:30 al massimo."),
    ("15:43", "Alessandra Toracchio"): ("domanda",
        "Chiede se la Protezione Civile viene chiamata a questi eventi "
        "e chi se ne occupa."),
    ("16:05", "Emilio Caniglia"): ("info",
        "Risponde che ha già chiesto la presenza della Protezione "
        "Civile, anche di poche unità, munita di estintori e con "
        "l'autobotte."),
    ("16:14", "Emilio Caniglia"): ("info",
        "Annuncia che per venerdì preparerà uno schema con gruppi in "
        "base a disponibilità e attività (allestimento, cottura, vin "
        "brulé, ecc.) per organizzarsi meglio ed evitare confusione, "
        "oltre a un recap del materiale necessario (bancali, utensili, "
        "ecc.) per organizzare il trasporto."),
    ("16:20", "Emilio Caniglia"): ("info",
        "Riferisce che Cesare ha suggerito di pubblicizzare l'evento "
        "con \"Cannelor\", proposta che giudica valida: si informerà sul "
        "costo e, vista l'imminenza dell'evento, si procederà con un "
        "sondaggio per autorizzare la spesa."),
    ("19:08", "Emanuele Sciarra"): ("info",
        "Condivide un reel Instagram fatto da Chiara Gargano "
        "(https://www.instagram.com/reel/DfnEyXWKvlG/?cplk=MXRqYm55Y3dsdjlmaw==) "
        "e invita tutti a condividerlo."),
}

MEDIA_OVERRIDES = {
    (DATE, "15:36", "Emanuele Sciarra", "IMG-20261111-WA0064.jpg"):
        "Le castagne in cassette di plastica nel bagagliaio dell'auto, "
        "pronte per essere portate in sede.",
    (DATE, "21:14", "Emanuele Sciarra", "IMG-20261111-WA0070.jpg"):
        "Screenshot delle statistiche Instagram della storia con le "
        "cassette di castagne appena pubblicata (65 contatti raggiunti, "
        "85 visualizzazioni).",
    (DATE, "21:15", "Emanuele Sciarra", "IMG-20261111-WA0071.jpg"):
        "Screenshot delle statistiche Instagram della storia con la "
        "locandina di San Martino (125 contatti raggiunti, 486 "
        "visualizzazioni, 8 interazioni).",
}

# Mattinata di prove tecniche sulla ricondivisione social: gli screenshot
# delle schermate Facebook/Instagram non aggiungono nulla al racconto già
# completo nel testo, quindi vengono esclusi (stesso criterio delle foto
# ridondanti dell'8/11).
_SKIP_SOCIAL_SCREENSHOTS_1111 = {
    "IMG-20261111-WA0010.jpg", "IMG-20261111-WA0011.jpg",
    "IMG-20261111-WA0024.jpg", "IMG-20261111-WA0025.jpg",
    "IMG-20261111-WA0026.jpg",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_SOCIAL_SCREENSHOTS_1111


AUDIO_CURATED = {
    (DATE, "08:55", "Dante Caniglia", "PTT-20261111-WA0012.opus"): ("info",
        "Ricorda che oggi è San Martino, con gli auguri di rito a chi "
        "porta questo nome."),
    (DATE, "09:52", "Emanuele Sciarra", "PTT-20261111-WA0020.opus"): ("info",
        "Anticipa che oggi pomeriggio gli consegneranno le castagne, e "
        "che poi pubblicheranno un reel."),
    (DATE, "13:00", "Emanuele Sciarra", "PTT-20261111-WA0033.opus"): ("info",
        "Comunica che le castagne sono state scaricate (circa 106-107 "
        "kg secondo la pesatura del nipote, con qualche chilo in più "
        "per compensare eventuali scarti) e sono momentaneamente sotto "
        "casa sua; nel primo pomeriggio chi è disponibile le porterà in "
        "sede."),
    (DATE, "13:52", "Luca Cicchelli", "PTT-20261111-WA0046.opus"): ("rumore", ""),
    (DATE, "15:40", "Emanuele Sciarra", "PTT-20261111-WA0060.opus"): ("rumore", ""),
    (DATE, "15:42", "Antonio Aceto", "PTT-20261111-WA0061.opus"): ("rumore", ""),
    (DATE, "19:43", "Elvis Ippoliti", "PTT-20261111-WA0067.opus"): ("info",
        "Commenta che il bancone del pub, con quel dipinto sullo "
        "sfondo, si presta benissimo per fare reel/contenuti video; si "
        "complimenta anche con Chiara per il reel che ha pubblicato."),
}

AUDIO_MERGES = [
    {
        "anchor_time": "07:14",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Lunga sessione di prove per far funzionare la "
            "ricondivisione del post/locandina sui social del comitato: "
            "Elvis segnala di non riuscire a ricondividere il post come "
            "post su Facebook (solo come storia), né il video "
            "d'Instagram una volta aperto. Emanuele verifica le "
            "impostazioni della pagina (risultavano già aperte alla "
            "ricondivisione) e spiega che per ricondividere nelle "
            "proprie storie serve taggare i membri nel contenuto "
            "originale; promette di farlo per le prossime storie. Dopo "
            "vari tentativi — con Antonio (amministratore della pagina) "
            "che riesce, Maria che inizialmente ricondivide solo il "
            "repost di un gruppo locale invece dell'originale, ed Elvis "
            "che fatica a trovare il pulsante giusto — è MariaLuisa a "
            "individuare il procedimento corretto (il tasto in basso a "
            "sinistra) e la condivisione riesce per tutti verso le "
            "9:50. Elvis coglie l'occasione per proporre di rendere "
            "amministratori della pagina più membri, ritenendo i social "
            "una leva fondamentale da gestire meglio per far crescere "
            "la visibilità del comitato."
        ),
        "members": [
            "PTT-20261111-WA0000.opus", "PTT-20261111-WA0001.opus",
            "PTT-20261111-WA0002.opus", "PTT-20261111-WA0003.opus",
            "PTT-20261111-WA0004.opus", "PTT-20261111-WA0005.opus",
            "PTT-20261111-WA0006.opus", "PTT-20261111-WA0007.opus",
            "PTT-20261111-WA0008.opus", "PTT-20261111-WA0009.opus",
            "PTT-20261111-WA0014.opus", "PTT-20261111-WA0015.opus",
            "PTT-20261111-WA0016.opus", "PTT-20261111-WA0017.opus",
            "PTT-20261111-WA0018.opus", "PTT-20261111-WA0019.opus",
        ],
    },
    {
        "anchor_time": "10:30",
        "anchor_sender": "Maikel Montano",
        "type": "domanda",
        "text": (
            "Maikel, già in cantina, chiede con urgenza chi ha "
            "l'ordine del vino e quante bottiglie/quanto vino prendere, "
            "non avendo questa informazione."
        ),
        "members": ["PTT-20261111-WA0021.opus"],
    },
    {
        "anchor_time": "11:16",
        "anchor_sender": "Antonio Aceto",
        "type": "proposta",
        "text": (
            "Antonio riferisce una chiacchierata avuta con un "
            "conoscente (\"il Vigno\"): quest'anno la Rupe non "
            "farebbe il veglione di Capodanno ma punterebbe su un "
            "evento di Natale con un altro artista, lasciando San "
            "Benedetto come unica opzione di veglione in paese — "
            "Antonio è stato invitato a spingere forte sull'evento. "
            "Emanuele "
            "propone un incontro con Andrea Di Loreto per organizzare "
            "insieme la comunicazione/sponsorizzazione, oltre a un "
            "confronto con Gianvito su un mezzo menu dell'evento; "
            "pensa che la locandina vera e propria arriverà solo a "
            "fine novembre/inizio dicembre, ma nel frattempo si "
            "potrebbe pubblicare — se Andrea è d'accordo — una "
            "\"pre-locandina\" generica. Elvis raccomanda cautela: "
            "Andrea ha chiesto esplicitamente di gestire lui la propria "
            "immagine, quindi meglio non fare il suo nome in giro e "
            "parlare solo genericamente di una \"sorpresa\"; Antonio "
            "conferma che si atterrà a questo d'ora in poi (avendo già "
            "accennato musica/animazione, senza nomi, a chi gliene "
            "aveva chiesto). Emanuele si offre di sentire Andrea nel "
            "pomeriggio, proponendo di coordinarsi su come e quanto "
            "comunicare in base a cosa preferisce lui (effetto sorpresa "
            "o anticipazioni); suggerisce inoltre di risentire Marta "
            "(l'animatrice, presente sabato a San Martino) per altri "
            "contatti/preventivi da sottoporre a Gianvito, che resta "
            "comunque l'unico a decidere chi ingaggiare, pagando lui. "
            "Maikel conferma che Andrea non farà marcia indietro "
            "(sono parenti) e si offre come punto di contatto "
            "alternativo per dividersi i compiti. Emanuele, impegnato "
            "in una visita in fabbrica (Bofrost) con poco accesso al "
            "telefono, lascia che chiunque sia disponibile (oggi, "
            "domani o dopodomani, escluso sabato per San Martino) vada "
            "a parlare con Andrea."
        ),
        "members": [
            "PTT-20261111-WA0022.opus", "PTT-20261111-WA0023.opus",
            "PTT-20261111-WA0027.opus", "PTT-20261111-WA0028.opus",
            "PTT-20261111-WA0029.opus", "PTT-20261111-WA0030.opus",
            "PTT-20261111-WA0031.opus", "PTT-20261111-WA0032.opus",
        ],
    },
    {
        "anchor_time": "13:02",
        "anchor_sender": "Emanuele Sciarra",
        "type": "decisione",
        "text": (
            "Emanuele chiede se confezionare le castagne in sacchetti "
            "da uno o tre chili per la vendita, e chi ha una bilancia. "
            "Maikel conferma di averne una disponibile. Cesare propone "
            "però di evitare le confezioni pre-fatte e portare "
            "direttamente la bilancia in piazza, vendendo le castagne "
            "sfuse pesate al momento in base al prezzo al chilo. "
            "Emanuele e Maria trovano l'idea valida (fa risparmiare "
            "tempo e non richiede di indovinare i pesi in anticipo); "
            "Elvis conferma che è proprio quanto deciso in riunione "
            "(mucchio sul banco, pesatura al momento), a differenza di "
            "quanto Emanuele ricordava (sacchetti pronti)."
        ),
        "members": [
            "PTT-20261111-WA0034.opus", "PTT-20261111-WA0035.opus",
            "PTT-20261111-WA0036.opus", "PTT-20261111-WA0037.opus",
            "PTT-20261111-WA0038.opus", "PTT-20261111-WA0039.opus",
            "PTT-20261111-WA0040.opus",
        ],
    },
    {
        "anchor_time": "13:35",
        "anchor_sender": "Luca Cicchelli",
        "type": "proposta",
        "text": (
            "Luca chiede conferma che le castagne si vendano sia cotte "
            "che crude, e quante prepararne per la cottura. Elvis "
            "risponde che va valutato con attenzione: meglio tenerle "
            "integre il più possibile e sgusciarle mano a mano che "
            "servono, perché una volta sgusciate andrebbero congelate "
            "se non cotte subito. Emanuele conferma che una ventina di "
            "chili sono già stati sgusciati, porterà degli "
            "spaccanoci per sgusciarne altre sul momento secondo "
            "necessità ed evitare sprechi, tenendo il resto intero "
            "(anche solo per abbellimento del banco). Poco dopo Luca ed "
            "Elvis tornano sull'argomento per fissare una base di "
            "partenza: concordano sulle 20-25 kg già individuate, da "
            "tagliare subito per farsi un'idea di quanti sacchetti ne "
            "escono, aggiustando poi il tiro con l'esperienza sul "
            "campo (per Elvis conviene comunque sprecare il meno "
            "possibile, ritenendo indifferente tagliarne 25 o 30 kg); "
            "avendo gli attrezzi giusti sul posto, tagliarne altre al "
            "momento non sarebbe comunque un problema. Antonio Aceto "
            "chiude il discorso confermando l'impostazione: tagliarne "
            "una ventina abbondante, lasciando le altre intere da "
            "tagliare all'occorrenza; le castagne già tagliate si "
            "possono anche congelare senza problemi — anzi risultano "
            "più buone, perché l'umidità trattenuta dal congelamento le "
            "rende più morbide in cottura (vanno però cotte "
            "direttamente da congelate); il resto, intere, servirà "
            "anche per la lotteria."
        ),
        "members": [
            "PTT-20261111-WA0041.opus", "PTT-20261111-WA0042.opus",
            "PTT-20261111-WA0043.opus", "PTT-20261111-WA0044.opus",
            "PTT-20261111-WA0045.opus", "PTT-20261111-WA0047.opus",
            "PTT-20261111-WA0048.opus", "PTT-20261111-WA0049.opus",
            "PTT-20261111-WA0050.opus", "PTT-20261111-WA0059.opus",
        ],
    },
    {
        "anchor_time": "14:12",
        "anchor_sender": "Maikel Montano",
        "type": "info",
        "text": (
            "Maikel aggiorna che ha parlato con Andrea Di Loreto, il "
            "quale lo richiamerà per capire se incontrarsi oggi (Maikel "
            "rientra da Pescara verso le 17-18) o un altro giorno. In "
            "serata, non essendo arrivata nessuna chiamata, Emanuele "
            "chiede aggiornamenti e Maikel spiega di non sapere ancora "
            "nulla di più: Andrea aveva impegni e si sarebbe liberato "
            "oggi, altrimenti si rimanda a domani o dopodomani, e lo "
            "risentirà lui stesso. Emanuele rassicura che non è "
            "urgente, era solo un seguito al discorso della mattinata: "
            "ci si organizzerà comunque con chi è più vicino alla cosa."
        ),
        "members": [
            "PTT-20261111-WA0052.opus", "PTT-20261111-WA0068.opus",
            "PTT-20261111-WA0069.opus",
        ],
    },
    {
        "anchor_time": "14:17",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Emanuele annuncia che oggi porta anche il gazebo in sede "
            "(un 3x3 pieghevole, veloce da montare), lasciandolo lì in "
            "anticipo perché sabato lavora fino alle 14; sul fronte "
            "castagne spiega che non si potranno cuocere tutte insieme "
            "ma a piccoli lotti (5-6 kg alla volta) con l'attrezzo "
            "nuovo appena ricevuto, che nessuno ha ancora usato — sarà "
            "una prova sul campo. Quelle già cotte andranno tenute "
            "nelle cassette di plastica già fornite e portate una alla "
            "volta, vendendole sia semplici sia con le gocce. Chiede "
            "anche se, una volta cotte, vadano messe in un telo o se "
            "servano degli stracci vecchi, non ricordando bene quel "
            "passaggio della riunione."
        ),
        "members": [
            "PTT-20261111-WA0053.opus", "PTT-20261111-WA0054.opus",
            "PTT-20261111-WA0055.opus",
        ],
    },
    {
        "anchor_time": "14:55",
        "anchor_sender": "Maikel Montano",
        "type": "domanda",
        "text": (
            "Maikel ricorda di avere a casa ricci e foglie di castagne "
            "per la scenografia e chiede chi se ne debba occupare, e se "
            "portarli in anticipo o direttamente sabato in piazza; Tina "
            "risponde che se ne occupano Barbara e Alessandra. Emanuele "
            "propone di lasciarli pure già in sede (sentendo anche "
            "Elvis), oppure di portarli direttamente sabato; Maikel "
            "chiarisce che per lui non cambia nulla tenerli a casa, "
            "voleva solo sapere se servivano prima — la questione si "
            "chiude con Alessandra Toracchio che conferma di non "
            "doverli portare in anticipo."
        ),
        "members": [
            "PTT-20261111-WA0056.opus", "PTT-20261111-WA0057.opus",
            "PTT-20261111-WA0058.opus",
        ],
    },
    {
        "anchor_time": "19:07",
        "anchor_sender": "Antonio Aceto",
        "type": "proposta",
        "text": (
            "Antonio concorda con la proposta di Valentina e suggerisce "
            "di contattare, se qualcuno li conosce, Terre Marsicane o "
            "Marsica Live per farsi scrivere un articolo (che "
            "raggiungerebbe tutta la zona); in alternativa si offre di "
            "provare lui stesso tramite una sua conoscenza, se nessuno "
            "ha un contatto più diretto."
        ),
        "members": ["PTT-20261111-WA0065.opus", "PTT-20261111-WA0066.opus"],
    },
]

TEXT_MERGES = [
    {
        "anchor_time": "14:37",
        "anchor_sender": "Barbara Rizio",
        "type": "info",
        "text": (
            "Barbara chiede a che ora si va in sede a portare le "
            "castagne e il resto; Tina ricorda che le tovaglie vecchie "
            "le porta Alessandra Toracchio, e Barbara si offre di "
            "iniziare a portare anche lei qualcosa."
        ),
        "members": [["14:37", "Barbara Rizio"], ["14:48", "Tina Giarrante"],
                    ["14:53", "Barbara Rizio"]],
    },
    {
        "anchor_time": "17:43",
        "anchor_sender": "Valentina D'Arcadia",
        "type": "proposta",
        "text": (
            "Valentina condivide un link Facebook "
            "(https://www.facebook.com/share/18uZbWejGh/) e propone di "
            "farsi scrivere/pubblicare anche loro in modo simile; Maria "
            "si dice d'accordo."
        ),
        "members": [["17:43", "Valentina D'Arcadia"], ["17:54", "Maria Buttari"]],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="screenshot social ridondanti (ricondivisione)")
