#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-13 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 06:50-18:02 (export Dropbox delle 18:03, giornata ancora in corso
al momento dell'export, un giorno prima di San Martino, sabato 14/11).
Alessandra compra i guanti nuovi e organizza il cappello per il costume
con Elvis e Barbara (che mette a disposizione anche una paglietta per lo
spaventapasseri). Costantino mostra in video, da vicino, il campanaccio
recuperato (risolvendo la richiesta del giorno prima). Antonio Aceto
conferma che le padelle gli verranno consegnate a casa. Emilio lancia il
sondaggio sulla pubblicità con "Cannelor", che risulta conveniente
considerati tutti gli eventi dell'anno (inclusa la richiesta della Pro
Loco per l'accensione dell'albero); esce anche l'articolo di stampa
richiesto il giorno prima. Il gruppo discute se vendere l'acqua in
bottiglia ai bambini (Ilenia è contraria, temendo che tolga vendite al
vino) e risolve con la stessa formula del vino: offerta libera, senza
listino esposto. Tina chiede il piano B in caso di pioggia; le previsioni
confermano cielo nuvoloso ma asciutto. Dante nota che il quartiere
Cittadella sta già costruendo il proprio albero di Natale. Nel primo
pomeriggio: le previsioni di weather.com confermano che sabato non piove
di giorno; Valentina mostra l'acqua acquistata e Barbara un secondo
cappello trovato. Emanuele propone palline di Natale con le foto dei
bambini, idea poi accantonata per mancanza di tempo viste le altre cose
da organizzare. Dubbi sul dispositivo per cuocere le castagne (lo sta
finendo "Guerino"), con Emilio che intanto conferma due padelle da un
metro di diametro. Antonio Sabatini rendiconta le spese per gli
ingredienti del vin brulè.

Sera (18:10-22:14, aggiornata con l'export delle 18:26 del 14/11): Antonio
Aceto mostra le due padelle forate per le castagne; Elvis chiede com'è il
bicchiere e Sabatini mostra quelli da 0,2 bianchi; Emanuele mostra il
dispositivo per le castagne, a cui manca ancora la catena (si monta
domani), e condivide un video Facebook. Alle 21 la riunione; Elvis, che
non può venire, chiede a voce un secondo termos con rubinetto, un fuocone
e una bombola di gas per il vin brulè, e Emanuele risponde che Emilio ha
parlato con la Pro Loco: il contest parte alle 15, forse con qualche
minuto di ritardo per un funerale alle 14:30. Foto della serata di
lavorazione delle castagne in sede. Aceto raccomanda il cesto della
lotteria "indovina quanti chili di castagne". Il resto (battute,
vocali di scherzo, due GIF mp4) è rumore. Nessuna menzione di Giovanni
Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-13"

CURATED = {
    ("06:50", "Alessandra Toracchio"): ("info",
        "Buongiorno: ha preso i guantoni nuovi (da lavoro, per "
        "maneggiare le castagne/braceri)."),
    ("09:10", "Antonio Aceto"): ("info",
        "Buongiorno: le padelle per cuocere le castagne gli vengono "
        "consegnate oggi direttamente a casa."),
    ("12:47", "Serena Di Stefano"): ("domanda",
        "Chiede se questa sera c'è la riunione."),
    ("19:42", "Emanuele Sciarra"): ("info",
        "Segnala che al dispositivo per cuocere le castagne manca la "
        "catena, che domani verrà montata."),
    ("19:59", "Emanuele Sciarra"): ("info",
        "Condivide un video Facebook: "
        "https://www.facebook.com/share/r/19xRmsfiE7/?mibextid=wwXIfr"),
    ("22:14", "Antonio Aceto"): ("info",
        "Raccomanda di preparare il cesto per la lotteria con il gioco "
        "\"indovina quanti chili di castagne ci sono\" (scritto in "
        "dialetto)."),
}

MEDIA_OVERRIDES = {
    (DATE, "13:25", "Emanuele Sciarra", "IMG-20261113-WA0021.jpg"):
        "Screenshot delle previsioni meteo orarie per San Benedetto dei "
        "Marsi: cielo nuvoloso, temperature tra 8° e 12°, nessuna "
        "precipitazione prevista — a conferma di quanto detto da "
        "Costantino.",
    (DATE, "13:31", "Dante Caniglia", "IMG-20261113-WA0020.jpg"):
        "Screenshot da un'altra chat (gruppo \"Cittadella\"): il "
        "quartiere Cittadella sta già montando la struttura in legno "
        "del proprio albero di Natale; Dante nota che anche il "
        "Comitato dovrebbe pensare a qualcosa di simile per "
        "partecipare.",
    (DATE, "07:42", "Costantino Mariani", "VID-20261113-WA0000.mp4"):
        "Video (3s) in cui, dopo averlo promesso la sera prima, mostra "
        "da vicino il campanaccio di metallo recuperato, tenendolo in "
        "mano.",
    (DATE, "13:44", "Maria Buttari", "IMG-20261113-WA0022.jpg"):
        "Screenshot delle previsioni per sabato (giorno di San "
        "Martino) da weather.com: di giorno 12°, molto nuvoloso, 12% "
        "di probabilità di pioggia; di notte 8°, con rischio di "
        "acquazzoni (50%) solo a tarda notte. Commento di Maria: \"Non "
        "piove...dai\".",
    (DATE, "15:05", "Valentina D'Arcadia", "IMG-20261113-WA0033.jpg"):
        "La sua auto carica di fardelli d'acqua (naturale e "
        "frizzante, marca Santa Croce) appena acquistati per sabato; "
        "sul retro si intravede anche un cappello di paglia. Commento "
        "di Valentina: \"Mo basta a piove che di acqua ne abbiamo "
        "abbastanza\".",
    (DATE, "15:06", "Barbara Rizio", "IMG-20261113-WA0032.jpg"):
        "Secondo cappello trovato: un fedora di paglia crema con "
        "fascia beige.",
    (DATE, "18:10", "Antonio Aceto", "IMG-20261113-WA0034.jpg"):
        "Le due padelle forate, appoggiate su un tavolino all'aperto, "
        "per cuocere le castagne.",
    (DATE, "18:15", "Antonio Sabatini", "IMG-20261113-WA0036.jpg"):
        "I bicchieri di carta da 0,2 l, nelle confezioni, per servire "
        "il vino.",
    (DATE, "19:42", "Emanuele Sciarra", "VID-20261113-WA0048.mp4"):
        "Video del dispositivo per cuocere le castagne: un tamburo "
        "metallico con motore, ancora in lavorazione.",
    (DATE, "21:42", "Tina Giarrante", "IMG-20261114-WA0000.jpg"):
        "Foto dall'alto di alcuni membri nella sede che lavorano le "
        "castagne, con le cassette piene sul tavolo.",
    (DATE, "21:56", "Emanuele Sciarra", "IMG-20261114-WA0001.jpg"):
        "Foto di gruppo di alcuni membri seduti attorno al tavolo nella "
        "sede dopo il lavoro sulle castagne; uno mostra un cestello.",
    (DATE, "21:56", "Emanuele Sciarra", "IMG-20261114-WA0002.jpg"):
        "Due membri con il pollice alzato nella sede, tra scatole di "
        "decorazioni e il cartello giallo \"Classe 1987\".",
}

AUDIO_CURATED = {
    (DATE, "13:19", "Emanuele Sciarra", "PTT-20261113-WA0012.opus"): ("rumore", ""),
    (DATE, "13:20", "Emanuele Sciarra", "PTT-20261113-WA0013.opus"): ("rumore", ""),
    (DATE, "13:20", "Costantino Mariani", "PTT-20261113-WA0014.opus"): ("rumore", ""),
    (DATE, "13:21", "Emanuele Sciarra", "PTT-20261113-WA0015.opus"): ("rumore", ""),
    (DATE, "13:21", "Emanuele Sciarra", "PTT-20261113-WA0016.opus"): ("rumore", ""),
    (DATE, "13:22", "Emanuele Sciarra", "PTT-20261113-WA0018.opus"): ("rumore", ""),
    (DATE, "13:23", "Emanuele Sciarra", "PTT-20261113-WA0019.opus"): ("rumore", ""),
    (DATE, "18:45", "Dante Caniglia", "PTT-20261113-WA0037.opus"): ("rumore", ""),
    (DATE, "19:05", "Costantino Mariani", "PTT-20261113-WA0038.opus"): ("rumore", ""),
    (DATE, "19:25", "Costantino Mariani", "PTT-20261113-WA0039.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {
        "anchor_time": "13:11",
        "anchor_sender": "Dante Caniglia",
        "type": "decisione",
        "text": (
            "Sul dibattito sull'acqua, Dante rassicura che non si "
            "tratta di fare concorrenza ai bar. Valentina propone "
            "allora di non mettere l'acqua nel listino esposto, "
            "tenendola sotto il banco: chi la chiede ce l'ha, "
            "altrimenti non viene offerta attivamente; chiede a Luca "
            "di verificare se si possa fare. Luca apprezza l'idea, "
            "scherzando di \"acqua di contrabbando\". Costantino "
            "chiarisce che comunque non si tratterebbe di una vera "
            "vendita, ma di un'offerta libera come per il vino: si dà "
            "l'acqua e si lascia a chi la prende un'offerta libera di "
            "un euro a bottiglietta, esattamente come già si fa con il "
            "vino e con le castagne. Luca ed Elvis concordano."
        ),
        "members": [
            "PTT-20261113-WA0003.opus", "PTT-20261113-WA0005.opus",
            "PTT-20261113-WA0006.opus", "PTT-20261113-WA0007.opus",
            "PTT-20261113-WA0008.opus", "PTT-20261113-WA0009.opus",
            "PTT-20261113-WA0010.opus", "PTT-20261113-WA0011.opus",
        ],
    },
    {
        "anchor_time": "15:22",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Emanuele propone, come idea per l'albero di Natale, delle "
            "palline da riempire con foto (dei bambini), con tanto di "
            "aggancio per sigillarle e appenderle; dice di averne a "
            "casa di simili coi suoi bambini, in polistirolo, ma "
            "ammette che richiederebbe parecchio tempo e chiede "
            "pareri, specificando di averla \"buttata lì\" come idea. "
            "Alessandra risponde che l'idea è bella ma troppo "
            "dispendiosa di tempo, viste le altre cose già in "
            "programma (mercatino, Babbo Natale, Tombolata, capodanno, "
            "calze della Befana), e propone di concentrarsi prima su "
            "quelle; Emanuele conferma di aver solo buttato lì "
            "l'idea e si trova d'accordo."
        ),
        "members": [
            "PTT-20261113-WA0023.opus", "PTT-20261113-WA0024.opus",
            "PTT-20261113-WA0025.opus",
        ],
    },
    {
        "anchor_time": "16:51",
        "anchor_sender": "Elvis Ippoliti",
        "type": "domanda",
        "text": (
            "Elvis chiede cosa si abbia per cuocere le castagne "
            "domani, se solo il \"riflettore\", e se il dispositivo "
            "(un bruciatore) che doveva servire allo scopo sia stato "
            "completato. Emanuele risponde che se ne sta occupando "
            "\"Guerino\", a cui aveva portato un pezzo che gli serviva "
            "per finirlo di assemblare; gli aveva garantito che "
            "sarebbe stato pronto per oggi ma c'è stato qualche "
            "piccolo intoppo (non si sentiva bene), lo richiamerà per "
            "aggiornamenti. Emilio intanto comunica di avere comunque "
            "due padelle da un metro di diametro; Elvis conferma che "
            "la domanda era solo per organizzarsi, e che quelle due "
            "padelle grandi dovrebbero bastare comunque."
        ),
        "members": [
            "PTT-20261113-WA0026.opus", "PTT-20261113-WA0027.opus",
            "PTT-20261113-WA0028.opus", "PTT-20261113-WA0029.opus",
            "PTT-20261113-WA0030.opus",
        ],
    },
    {
        "anchor_time": "21:15",
        "anchor_sender": "Elvis Ippoliti",
        "type": "info",
        "text": (
            "Elvis, che non riesce a venire alla riunione per contrattempi "
            "a casa, dice di aver già avvisato Mike: per domani servono un "
            "altro termos da circa 5 litri con rubinetto (per servire il "
            "vin brulè caldo, prelevandolo dal pentolone), un fuocone e "
            "una bombola di gas (la fiamma deve restare bassa per tenerlo "
            "in temperatura); chiede di sapere a che ora saranno "
            "operativi per regolarsi sull'inizio della preparazione. "
            "Emanuele risponde che Emilio è andato a parlare con la Pro "
            "Loco: da quanto ha capito il contest parte alle 15, con "
            "possibile slittamento di qualche minuto perché alle 14:30 c'è "
            "un funerale in chiesa; aggiornerà appena torna il presidente. "
            "Elvis ribadisce di ricordarsi di fuocone, bombola e termos, "
            "e che per i tempi si aggiornerà dopo."
        ),
        "members": [
            "PTT-20261113-WA0045.opus",
            "PTT-20261113-WA0049.opus",
            "PTT-20261113-WA0050.opus",
        ],
    },
]

TEXT_MERGES = [
    {
        "anchor_time": "06:51",
        "anchor_sender": "Alessandra Toracchio",
        "type": "proposta",
        "text": (
            "Alessandra chiede a Elvis come vuole il cappello (per il "
            "costume), così lo procurano e stasera porta tutto in "
            "sede. Barbara dice di avere una paglietta; Elvis pensa "
            "possa andare bene, e se ce n'è un'altra disponibile una "
            "la userebbe lui e l'altra per lo spaventapasseri. Il "
            "gruppo conferma, lasciando comunque aperta la possibilità "
            "di trovare qualcosa di più adatto."
        ),
        "members": [
            ["06:51", "Alessandra Toracchio"], ["06:53", "Barbara Rizio"],
            ["06:53", "Elvis Ippoliti"], ["06:54", "Emanuele Sciarra"],
            ["06:54", "Maria Buttari"], ["06:54", "Barbara Rizio"],
            ["06:55", "Luca Cicchelli"], ["06:55", "Elvis Ippoliti"],
            ["06:55", "Barbara Rizio"], ["06:56", "Barbara Rizio"],
            ["06:57", "Elvis Ippoliti"], ["06:58", "Barbara Rizio"],
        ],
    },
    {
        "anchor_time": "10:09",
        "anchor_sender": "Emilio Caniglia",
        "type": "proposta",
        "text": (
            "Emilio, considerato l'impegno di spesa, propone un "
            "sondaggio per decidere sulla pubblicità con il bando "
            "cittadino tramite Daniele \"Cannelor\", precisando che "
            "l'argomento sarà comunque riportato in riunione e che la "
            "proposta serve solo ad accelerare i tempi vista "
            "l'imminenza di San Martino. Lancia quindi il sondaggio:\n\n"
            "SONDAGGIO: Bando cittadino con Daniele \"Cannelor\"\n"
            "OPZIONE: Sì al pacchetto completo (250 euro da saldare a "
            "fine mandato) (15 voti)\n"
            "OPZIONE: Sì, solo a chiamata (25 euro per ogni giro di "
            "macchina) (1 voto)\n"
            "OPZIONE: No (sia per il pacchetto completo che per "
            "singola chiamata) (0 voti)\n\n"
            "Spiega poi che il pacchetto completo copre tutti gli "
            "eventi e le feste a prescindere dal numero di giri di "
            "macchina (San Martino compreso, con un giro stasera e uno "
            "domani mattina). Alla domanda di Valentina se convenga "
            "solo con più di 10 eventi da sponsorizzare, Emilio elenca "
            "gli eventi in programma (San Martino, Tombolata, l'evento "
            "delle calze, più la richiesta della Pro Loco di una "
            "presenza all'accensione dell'albero in coincidenza con i "
            "mercatini di Natale, e tutte le feste da Sant'Antonio ad "
            "Agosto), oltre all'aiuto del bando per annunciare questua "
            "e banchetto; fissa poi il messaggio del sondaggio. "
            "Valentina conclude che allora conviene."
        ),
        "members": [
            ["10:09", "Emilio Caniglia"], ["10:14", "Emilio Caniglia"],
            ["10:16", "Emilio Caniglia"], ["10:16", "Valentina D'Arcadia"],
            ["10:19", "Emilio Caniglia"], ["10:21", "Valentina D'Arcadia"],
        ],
    },
    {
        "anchor_time": "10:21",
        "anchor_sender": "Alessandra Toracchio",
        "type": "info",
        "text": (
            "Alessandra condivide un link Facebook "
            "(https://www.facebook.com/share/1FVaVS4N34/): è uscito "
            "l'articolo su San Benedetto richiesto il giorno prima a "
            "Marsica Live/Terre Marsicane/AZ Informa. Valentina esulta "
            "di essere stata ascoltata; Elvis scherza chiedendo se "
            "basti dire che si è visto un asino volante per avere un "
            "articolo, e Valentina risponde che, viste le circostanze, "
            "potrebbe anche provarci."
        ),
        "members": [
            ["10:21", "Alessandra Toracchio"], ["10:21", "Valentina D'Arcadia"],
            ["10:23", "Elvis Ippoliti"], ["10:24", "Valentina D'Arcadia"],
            ["10:24", "Elvis Ippoliti"],
        ],
    },
    {
        "anchor_time": "11:42",
        "anchor_sender": "Valentina D'Arcadia",
        "type": "proposta",
        "text": (
            "Valentina fa notare che si è pensato al vino ma non "
            "all'acqua, dopo una battuta ricevuta in merito; Emanuele "
            "chiede se piova, Valentina osserva che con tanti bambini "
            "presenti le bottigliette d'acqua converrebbe venderle, "
            "proponendo una decina di fardelli da 24 (miste "
            "naturale/frizzante) per circa 42,50€, poi rivista a 10 "
            "fardelli (misti). Luca si offre di portarne un paio di "
            "suo. Emanuele scherza sul far bere subito vino ai "
            "bambini. Antonio Sabatini consiglia di ridurre a 240 "
            "bottigliette circa, con un 60% naturale e 40% leggermente "
            "frizzante, per contenere la spesa; Valentina si assesta "
            "su 6 fardelli naturali (144 bottigliette) e 4 leggermente "
            "frizzanti (96), evitando le frizzanti pure. Ilenia "
            "dissente: ricorda che agli eventi a cui ha partecipato "
            "con bambini l'acqua si compra sempre al bar, che il "
            "comitato deve puntare a vendere il vino (se i bambini "
            "bevono acqua non comprano vino), che ai bambini deve "
            "pensarci la Pro Loco e non il comitato, che il comitato "
            "ai bambini offre già i dolcetti. Alessandra precisa che "
            "si parlava comunque di acqua per i bambini, mica per far "
            "bere vino a loro. Valentina ribatte che comunque vendendo "
            "le bottigliette a 1€ sono soldi che rientrano; Ilenia si "
            "dice d'accordo se vengono vendute (pensava si dovessero "
            "offrire gratis)."
        ),
        "members": [
            ["11:42", "Valentina D'Arcadia"], ["11:42", "Emanuele Sciarra"],
            ["11:43", "Valentina D'Arcadia"], ["11:44", "Valentina D'Arcadia"],
            ["11:45", "Antonio Aceto"], ["11:46", "Barbara Rizio"],
            ["11:46", "Luca Cicchelli"], ["11:47", "Valentina D'Arcadia"],
            ["11:47", "Emanuele Sciarra"], ["11:49", "Elvis Ippoliti"],
            ["11:50", "Valentina D'Arcadia"], ["11:52", "Luca Cicchelli"],
            ["11:53", "Maria Buttari"], ["11:53", "Valentina D'Arcadia"],
            ["11:58", "Antonio Sabatini"], ["12:00", "Valentina D'Arcadia"],
            ["12:50", "Ilenia Piccozzi"], ["12:52", "Ilenia Piccozzi"],
            ["12:54", "Alessandra Toracchio"], ["12:54", "Ilenia Piccozzi"],
            ["12:55", "Ilenia Piccozzi"], ["13:00", "Valentina D'Arcadia"],
            ["13:01", "Ilenia Piccozzi"],
        ],
    },
    {
        "anchor_time": "13:22",
        "anchor_sender": "Tina Giarrante",
        "type": "domanda",
        "text": (
            "Tina chiede come sia previsto il meteo per domani e quale "
            "fosse il piano B; Costantino risponde che si farebbe "
            "dentro la chiesa, e che secondo le previsioni domani "
            "dovrebbe essere nuvoloso ma non piovoso."
        ),
        "members": [
            ["13:22", "Tina Giarrante"], ["13:22", "Costantino Mariani"],
            ["13:24", "Costantino Mariani"],
        ],
    },
    {
        "anchor_time": "18:13",
        "anchor_sender": "Elvis Ippoliti",
        "type": "info",
        "text": (
            "Elvis chiede com'è il bicchiere; Antonio Sabatini risponde "
            "che sono da 0,2 l, bianchi (e ne mostra la confezione); "
            "Elvis approva."
        ),
        "members": [
            ["18:13", "Elvis Ippoliti"], ["18:14", "Antonio Sabatini"],
            ["18:15", "Elvis Ippoliti"],
        ],
    },
    {
        "anchor_time": "19:49",
        "anchor_sender": "Costantino Mariani",
        "type": "info",
        "text": (
            "Costantino chiede a che ora è l'appuntamento di stasera; "
            "Emanuele risponde alle 21:00."
        ),
        "members": [
            ["19:49", "Costantino Mariani"], ["19:49", "Emanuele Sciarra"],
        ],
    },
]

# IMG-20261114-WA0003.jpg (21:56, Emanuele): quasi identica a WA0001 (stessa
# foto di gruppo, secondo scatto), scartata come ridondante.
_SKIP_FILES = {"IMG-20261114-WA0003.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES,
                 extra_skip_media=_extra_skip, extra_skip_label="foto ridondante")
