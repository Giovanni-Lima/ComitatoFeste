#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-15 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:33-19:50 (export Dropbox delle 20:33, giornata ancora in corso):
il giorno dopo San Martino. Mattina: complimenti reciproci; Ugo chiede come
procedere per i fuoconi (smontaggio), si ripiega su domani pomeriggio (manca
un trattore); Costance e Emanuele sul Capodanno (animazione bambini, preventivo
da Marta e da altre animatrici, Andrea per la musica); Emanuele lancia la
bozza del post di ringraziamento (Amministrazione, Don Enzo, Marta Animazione,
Pro Loco). Aceto porta le notizie di Amanda (premi non ritirati dell'anno
scorso donati al comitato) e la disponibilità della pasticceria Paola per la
tombolata; Elvis chiede più presenza sui social e propone i prossimi eventi
(tombolata, accensione dell'albero, Immacolata); Emanuele ripropone il
calendario degli eventi con Chiara. Primo pomeriggio: Sabatini rendiconta
San Martino (incasso 774 €, di cui 116 € di lotteria; spese 400 € più vino e
acqua; attivo circa 374 €) e posta il foglio dei conti; ne nasce una lunga
discussione sui chili di castagne (110 kg acquistati, 105 cartocci e 27 kg
crudi venduti, calo di peso da cotte, avanzo pesato in sede) in cui Elvis e
Dante cercano di far quadrare i numeri e Ilenia, Sabatini, Cesare e Luca
spiegano i sacchetti più abbondanti. Dante invita a scrivere i post con
l'AI per evitare errori. Sera: Emilio gira l'invito di Don Enzo per domenica
22/11 (Messa di Santa Cecilia e concerto del coro Armonia Corale), annuncia
che venerdì Antonio farà un resoconto verificabile dei conti e porta le sue
prove con la bilancia sulle porzioni; considera San Martino un altro
successo dopo Corinaldo. Il resto (cuori, battute, GIF, foto del pranzo,
vocali di scherzo, un contatto telefonico condiviso e non riportato) è
rumore. Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-15"

CURATED = {
    ("11:00", "Costantino Mariani"): ("info",
        "Condivide un video Facebook: "
        "https://www.facebook.com/share/v/1A5nWd9Nfx/"),
    ("12:44", "Emanuele Sciarra"): ("domanda",
        "Propone la bozza del post di ringraziamento per San Martino: "
        "grazie a tutti per la partecipazione alla festa di ieri in "
        "Piazza Risorgimento, culminata con il contest delle zucche "
        "organizzato dalla Pro Loco di San Benedetto; ringraziamento "
        "speciale all'Amministrazione Comunale, al parroco Don Enzo e a "
        "Marta Animazione (Marta Malatesti) per l'animazione di grandi e "
        "piccini, con gli hashtag #SanMartino2026 #Classe1987 e simili. "
        "Chiede se ha dimenticato di citare qualcuno."),
    ("12:50", "Antonio Aceto"): ("info",
        "Riferisce che Andrea ha detto che si può dire tranquillamente "
        "che a Capodanno suonerà lui: per Andrea si può già cominciare a "
        "pubblicizzare; per l'animazione si è invece ancora in attesa."),
    ("12:55", "Antonio Aceto"): ("info",
        "Notizie di Amanda: i premi dell'anno scorso non ritirati "
        "verranno donati al comitato (un iPhone, una notte al rifugio di "
        "Celano, due mesi di abbonamento a una scuola di ballo), insieme "
        "alla parte economica avanzata. Sabato prossimo (21/11) faranno "
        "la loro ultima riunione, dopodiché doneranno queste cose "
        "insieme al POS."),
    ("12:59", "Antonio Aceto"): ("info",
        "Paola della pasticceria fa l'offerta ma non vuole apparire come "
        "sponsor (lo fa tutti gli anni); per la tombolata si può passare "
        "anche da lei, farà un'offerta da usare come premio."),
    ("13:03", "Antonio Aceto"): ("info",
        "Chiunque abbia incontrato stamattina gli ha fatto i complimenti "
        "per San Martino: \"stiamo andando alla grande\"."),
    ("13:27", "Ilenia Piccozzi"): ("info",
        "Propone un'animatrice per i bambini, il cui contatto le è "
        "arrivato da Antonella, e lo condivide al gruppo (contatto "
        "telefonico non riportato qui)."),
    ("13:34", "Dante Caniglia"): ("info",
        "Invita a fare i complimenti a chi ha venduto le castagne: "
        "bellissime e buonissime, zero castagne marce."),
    ("14:20", "Ilenia Piccozzi"): ("info",
        "Avverte che le castagne avanzate vanno rivendute subito, "
        "altrimenti iniziano a fare i vermi."),
    ("14:39", "Cesare Raglione"): ("info",
        "Ricorda di considerare nei conti anche le castagne del cesto e "
        "l'incasso delle pesate del premio, che non gli sembra di vedere."),
    ("19:04", "Emilio Caniglia"): ("info",
        "Si scusa della poca reattività social (è raffreddato) e gira "
        "l'invito di Don Enzo: domenica 22 novembre, Solennità di Cristo "
        "Re e festa di Santa Cecilia, patrona della musica, il Coro "
        "della Piana del Cavaliere \"Armonia Corale\" (circa 40 "
        "elementi) animerà la Messa delle 17:00 e offrirà poi alla "
        "comunità un breve concerto dal titolo \"Cantemus de amore\", "
        "un itinerario musicale dall'amore terreno a quello sacro "
        "(programma in allegato). Don Enzo ringrazia il Comitato Feste "
        "(Classe 1987) e la Pro Loco per l'iniziativa di San Martino."),
    ("19:06", "Emilio Caniglia"): ("info",
        "Annuncia che venerdì in riunione Antonio farà un resoconto "
        "verificabile di tutti i conti."),
    ("19:11", "Emilio Caniglia"): ("info",
        "Per le porzioni di castagne: ieri ha comprato una porzione per "
        "la moglie e il sacchetto avanzato pesa 211 grammi (foto), pur "
        "avendone mangiate alcune lui e la moglie: le porzioni non erano "
        "di circa 250 grammi. Bastano 10 castagne cotte in più per "
        "quasi 70 grammi in più a porzione (foto)."),
}

AUDIO_CURATED = {
    (DATE, "10:50", "Emanuele Sciarra", "PTT-20261115-WA0001.opus"): ("info",
        "Per i fuoconi si rende disponibile domani pomeriggio a "
        "qualsiasi ora (oggi è impegnatissimo al lavoro). Maikel Montano "
        "conferma poco dopo: domani pomeriggio, oggi tutti a riposo."),
    (DATE, "12:10", "Emanuele Sciarra", "PTT-20261115-WA0002.opus"): ("info",
        "Per l'animazione dei bambini a Capodanno aspetta una risposta tra "
        "oggi e domani: Marta, che ha fatto l'animazione di ieri, non ci "
        "sarà perché vuole andare fuori a Capodanno; ha chiesto se "
        "qualche collaboratrice può farla e di avere un preventivo. "
        "Erano stati fatti un paio di nomi, da valutare."),
    (DATE, "13:06", "Emanuele Sciarra", "PTT-20261115-WA0008.opus"): ("proposta",
        "Ripropone l'idea (già detta in riunione e a Chiara) di creare un "
        "calendario degli eventi e ripubblicare tutto data per data. "
        "Chiara è a Parigi in ferie: domani, quando rientra, si "
        "organizzeranno su eventi e cose da fare per costruirlo."),
    (DATE, "13:52", "Costantino Mariani", "PTT-20261115-WA0018.opus"): ("domanda",
        "Chiede com'è andato l'incontro con la banda di Avezzano."),
    (DATE, "13:05", "Costantino Mariani", "PTT-20261115-WA0006.opus"): ("rumore", ""),
    (DATE, "13:10", "Elvis Ippoliti", "PTT-20261115-WA0014.opus"): ("rumore", ""),
}

TEXT_MERGES = [
    {
        "anchor_time": "08:33", "anchor_sender": "Luca Cicchelli",
        "type": "info",
        "text": (
            "Luca: erano anni che non passava una giornata così, si è "
            "proprio divertito, complimenti a tutti. Maria: \"siete stati "
            "fantastici\"."
        ),
        "members": [["08:33", "Luca Cicchelli"], ["08:38", "Maria Buttari"]],
    },
    {
        "anchor_time": "09:12", "anchor_sender": "Ugo Trinchini",
        "type": "domanda",
        "text": (
            "Ugo chiede come procedere per i fuoconi. Emilio non può "
            "partecipare perché è molto raffreddato; Luca propone di farlo "
            "domani pomeriggio, perché a quanto sa non c'è un trattore "
            "disponibile."
        ),
        "members": [["09:12", "Ugo Trinchini"], ["09:23", "Emilio Caniglia"],
                    ["09:31", "Luca Cicchelli"]],
    },
    {
        "anchor_time": "12:09", "anchor_sender": "Costance Rossi",
        "type": "domanda",
        "text": (
            "Costance chiede, per iniziare a presentare il Capodanno, se "
            "animazione e intrattenimento sono ancora da definire, e se si "
            "sta prevedendo l'animazione per bambini; Emanuele conferma di "
            "sì."
        ),
        "members": [["12:09", "Costance Rossi"], ["12:11", "Costance Rossi"],
                    ["12:15", "Emanuele Sciarra"]],
    },
    {
        "anchor_time": "13:01", "anchor_sender": "Elvis Ippoliti",
        "type": "proposta",
        "text": (
            "Elvis chiede di essere più presenti sui social (storie e post "
            "anche mentre l'evento è in corso) per far crescere la pagina, "
            "farsi conoscere e invogliare a partecipare, a partire dal "
            "prossimo evento, così da arrivare al Capodanno \"facendo il "
            "botto\". Aceto pensa che il prossimo evento sia il Capodanno, "
            "poi corregge: la tombolata. Elvis elenca i prossimi appuntamenti: "
            "la tombolata, l'accensione dell'albero (se si vuole fare "
            "qualcosa) e, sempre se si vuole fare qualcosa, la Concetta "
            "(Immacolata)."
        ),
        "members": [["13:01", "Elvis Ippoliti"], ["13:01", "Antonio Aceto"],
                    ["13:02", "Antonio Aceto"], ["13:02", "Emanuele Sciarra"],
                    ["13:02", "Elvis Ippoliti"]],
    },
    {
        "anchor_time": "13:35", "anchor_sender": "Ilenia Piccozzi",
        "type": "domanda",
        "text": (
            "Ilenia e Maria chiedono come è andata la vendita e se sono "
            "avanzate molte castagne; Luca chiede a Emilio di aggiornarli "
            "su come è andata ieri."
        ),
        "members": [["13:35", "Ilenia Piccozzi"], ["13:41", "Maria Buttari"],
                    ["13:43", "Luca Cicchelli"]],
    },
    {
        "anchor_time": "13:53", "anchor_sender": "Antonio Sabatini",
        "type": "info",
        "text": (
            "Dopo una mattinata di riconteggi Antonio Sabatini rendiconta "
            "San Martino: la giornata è andata bene sotto molti aspetti, "
            "senza incassi da capogiro. Il comitato ha incassato in totale "
            "774 € (di cui 116 € dalla lotteria); al netto delle spese "
            "(400 €, più ancora da pagare vino e acqua) l'attivo è di "
            "374 €. Il totale coincide con i tagliandini e con quanto "
            "venduto."
        ),
        "members": [["13:53", "Antonio Sabatini"],
                    ["13:55", "Antonio Sabatini"]],
    },
    {
        "anchor_time": "13:59", "anchor_sender": "Elvis Ippoliti",
        "type": "info",
        "text": (
            "Discussione sui conti delle castagne. Elvis nota che i "
            "cartocci non erano da 240 grammi ma più grandi; di vin "
            "brulè ne sarebbero avanzati 3-4 bicchieri, mentre di "
            "castagne circa una cassetta (Sabatini: 20 kg, tenendo conto "
            "che da cotte perdono circa il 20% del peso). Sabatini: "
            "venduti 105 cartocci e 27 kg di crude (a 5 €). Elvis calcola "
            "che con 80 kg venduti a circa 10 €/kg si sarebbero "
            "incassati 800 € lordi (utile 400 €) e, con cartocci da "
            "270 g, 105 pezzi fanno 28 kg, 37 con il 30% in più, 64 con "
            "le crude: i conti non tornano. Dante stima 50 kg venduti "
            "(52 se tutti da 240 g) e cartocci da circa 270 g."
        ),
        "members": [
            ["13:59", "Elvis Ippoliti"], ["14:01", "Costantino Mariani"],
            ["14:02", "Luca Cicchelli"], ["14:02", "Costantino Mariani"],
            ["14:03", "Luca Cicchelli"], ["14:03", "Antonio Sabatini"],
            ["14:04", "Antonio Sabatini"], ["14:07", "Elvis Ippoliti"],
            ["14:07", "Ilenia Piccozzi"], ["14:07", "Dante Caniglia"],
            ["14:08", "Elvis Ippoliti"], ["14:08", "Antonio Sabatini"],
            ["14:09", "Dante Caniglia"], ["14:10", "Dante Caniglia"],
            ["14:10", "Elvis Ippoliti"], ["14:11", "Elvis Ippoliti"],
            ["14:11", "Dante Caniglia"], ["14:11", "Antonio Sabatini"],
            ["14:13", "Antonio Sabatini"], ["14:13", "Dante Caniglia"],
            ["14:15", "Elvis Ippoliti"],
        ],
    },
    {
        "anchor_time": "16:09", "anchor_sender": "Dante Caniglia",
        "type": "info",
        "text": (
            "Dante consiglia di scrivere i post con l'AI, perché ci sono "
            "sempre errori (e allega due screenshot dei post). Emanuele "
            "risponde che ha ragione ma, tra mille cose da fare, l'errore "
            "ci sta."
        ),
        "members": [["16:09", "Dante Caniglia"], ["16:12", "Emanuele Sciarra"]],
    },
    {
        "anchor_time": "16:22", "anchor_sender": "Elvis Ippoliti",
        "type": "info",
        "text": (
            "Elvis: nel cesto c'erano circa 3,5 kg di castagne, quasi "
            "ininfluenti; si arriverebbe a 68 kg e manca sempre molto, a "
            "meno che nella cassetta avanzata ce ne siano 40. Per Dante, "
            "se i kg acquistati erano 110 (100+10) e ne è stata venduta "
            "circa la metà, qualcosa non quadra: 20 kg in sede ma saranno "
            "al massimo 12, e mancano anche circa 20 € oltre a 4 "
            "bicchieri di vino offerti dalla famiglia Bacarello e "
            "all'offerta di Lino Colucci. Costance ricorda una cassetta "
            "avanzata e una intera sotto (più di 20 kg); Elvis dubita che "
            "le cassette arrivino a 20 kg e propone di pesare quella "
            "rimasta per farne una media. Fa poi il conto dell'utile: "
            "togliendo vino per Mike (50-60 €) e acqua (50 €) restano "
            "274 €."
        ),
        "members": [
            ["16:22", "Elvis Ippoliti"], ["16:37", "Dante Caniglia"],
            ["16:39", "Costance Rossi"], ["16:40", "Dante Caniglia"],
            ["16:41", "Dante Caniglia"], ["16:42", "Costance Rossi"],
            ["16:42", "Dante Caniglia"], ["16:46", "Costance Rossi"],
            ["16:46", "Elvis Ippoliti"], ["16:47", "Elvis Ippoliti"],
        ],
    },
    {
        "anchor_time": "16:26", "anchor_sender": "Ilenia Piccozzi",
        "type": "info",
        "text": (
            "Il fratello di Ilenia vuole comprare 10 kg di castagne: "
            "Antonio Sabatini si offre di passare alla sede entro le 17 "
            "con una bilancia (Ilenia presta la sua); più tardi Ilenia "
            "segnala che Antonio sta andando alla sede insieme a Pietro "
            "per pesare quelle rimaste."
        ),
        "members": [["16:26", "Ilenia Piccozzi"], ["16:32", "Antonio Sabatini"],
                    ["16:33", "Ilenia Piccozzi"], ["16:34", "Antonio Sabatini"],
                    ["16:48", "Ilenia Piccozzi"]],
    },
    {
        "anchor_time": "16:50", "anchor_sender": "Costance Rossi",
        "type": "info",
        "text": (
            "Continua il confronto sui pesi: Dante spiega che le cotte "
            "calano del 25% dopo la cottura e vanno considerate solo "
            "quelle (non quelle vendute); Elvis calcola 105 x 0,270 = "
            "28,35 kg + 30% = 36,85. Costance ipotizza che nei cartocci "
            "entrassero più castagne perché la paletta era tarata sulle "
            "crude e le cotte rimpiccioliscono; Elvis replica che il "
            "volume è lo stesso e il calo è solo d'acqua. Costance e "
            "Dante ricordano che la cassetta avanzata era mezza, poi 3/4."
        ),
        "members": [
            ["16:50", "Costance Rossi"], ["16:51", "Dante Caniglia"],
            ["16:52", "Elvis Ippoliti"], ["16:52", "Dante Caniglia"],
            ["16:53", "Dante Caniglia"], ["16:54", "Costance Rossi"],
            ["16:54", "Elvis Ippoliti"], ["16:58", "Costance Rossi"],
            ["16:58", "Dante Caniglia"], ["17:00", "Elvis Ippoliti"],
            ["17:02", "Costance Rossi"],
        ],
    },
    {
        "anchor_time": "17:17", "anchor_sender": "Luca Cicchelli",
        "type": "info",
        "text": (
            "Luca ricorda che le chiavi della sede le ha Ugo; Ugo "
            "risponde che stamattina sono andati a riprendere i faretti e "
            "le aste di Ilenia e che le chiavi le ha date a Saba. Ilenia "
            "conferma che Antonio e Pietro sono alla sede."
        ),
        "members": [["17:17", "Luca Cicchelli"], ["17:21", "Ugo Trinchini"],
                    ["17:22", "Ilenia Piccozzi"]],
    },
    {
        "anchor_time": "17:28", "anchor_sender": "Dante Caniglia",
        "type": "info",
        "text": (
            "Dante: i pesi (26+25+16 = 67 kg, forse 73) non arrivano a "
            "110. Elvis rifà il conto: 37 kg di cotte, 27 di crude e 4 "
            "del cesto fanno 68, con l'avanzo 84. Sabatini pensa che i "
            "sacchetti fossero più capienti (350-400 g invece di 270, "
            "contando spreco e assaggi). Dante replica che un sacchetto "
            "ne conteneva 240-270 g, mai 400, come provato alla fine; "
            "erano state regalate tre dosi in più. Cesare: verso la fine "
            "i sacchetti li ha fatti più grandi (un paio di kg tra tutti); "
            "Alessandra: l'ultimo l'ha regalato lei. Resta uno sbalzo di "
            "25-30 kg. Ilenia: con sacchetti da circa 300 g i conti "
            "tornano."
        ),
        "members": [
            ["17:28", "Dante Caniglia"], ["17:33", "Elvis Ippoliti"],
            ["17:42", "Antonio Sabatini"], ["17:44", "Dante Caniglia"],
            ["17:49", "Cesare Raglione"], ["17:50", "Dante Caniglia"],
            ["17:50", "Alessandra Toracchio"], ["17:57", "Ilenia Piccozzi"],
        ],
    },
    {
        "anchor_time": "18:12", "anchor_sender": "Dante Caniglia",
        "type": "info",
        "text": (
            "Dante: anche con sacchetti da 400 g, 105 pezzi fanno 42 kg; "
            "con il 25% in più (52) più 27 venduti a parte, 16 avanzati "
            "e 5 regalati si arriva a 90 kg: ne mancano ancora circa 10-20. "
            "Ilenia: 52+27+16+4 del cesto = 99, quindi i conti tornano "
            "(qualcosa è stato spizzicato). Elvis: 20 kg a 4 € sono 80 € "
            "in meno (40 € se ne mancano 10); va bene così ma la prossima "
            "volta bisogna essere più scrupolosi e far quadrare tutto. "
            "Luca: verso la fine i sacchetti erano molto abbondanti "
            "(anche quelli dati a Don Enzo e alla profumeria), quindi "
            "ci sta; per Elvis, se erano da mezzo kg i conti tornano "
            "(da 270 g a quasi il doppio)."
        ),
        "members": [
            ["18:12", "Dante Caniglia"], ["18:16", "Ilenia Piccozzi"],
            ["18:16", "Dante Caniglia"], ["18:17", "Dante Caniglia"],
            ["18:17", "Elvis Ippoliti"], ["18:22", "Ilenia Piccozzi"],
            ["18:23", "Ilenia Piccozzi"], ["18:27", "Luca Cicchelli"],
            ["18:29", "Elvis Ippoliti"],
        ],
    },
    {
        "anchor_time": "19:23", "anchor_sender": "Emilio Caniglia",
        "type": "info",
        "text": (
            "Emilio: siamo stati impeccabili, è un altro successo che "
            "si aggiunge alla visita a Corinaldo; non ha memoria di "
            "castagnate organizzate da comitati né di autobus da 64 "
            "posti. Ugo e Luca concordano."
        ),
        "members": [["19:23", "Emilio Caniglia"], ["19:26", "Ugo Trinchini"],
                    ["19:28", "Luca Cicchelli"]],
    },
    {
        "anchor_time": "19:47", "anchor_sender": "Emilio Caniglia",
        "type": "info",
        "text": (
            "Emilio: anche lui ha porzionato e ha certamente messo più "
            "del dovuto; alla vendita del fresco è arrivato a riempire "
            "una busta con oltre 800 g, ne ha aggiunte altre e erano "
            "1100 g, senza toglierle per fare un kg preciso. Un'altra "
            "considerazione: a parità di volume le castagne cotte "
            "hanno probabilmente un peso specifico maggiore delle crude."
        ),
        "members": [["19:47", "Emilio Caniglia"], ["19:50", "Emilio Caniglia"]],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "13:03", "Serena Di Stefano", "IMG-20261115-WA0010.jpg"):
        "Screenshot della pagina Facebook del Santuario Santa Maria "
        "Goretti di Corinaldo, con il post \"Dedica a Marietta scritta nel "
        "Registro dei visitatori\"; Serena lo condivide con il gruppo.",
    (DATE, "13:06", "Emanuele Sciarra", "IMG-20261115-WA0011.jpg"):
        "Screenshot di un post Facebook di \"Cattolica Welcome\" con il "
        "programma di Natale e Capodanno (\"Cattolica Bosco di Luce\"), "
        "con quattro locandine rosse dell'evento.",
    (DATE, "14:22", "Antonio Sabatini", "IMG-20261115-WA0019.jpg"):
        "Foglio di conti scritto a mano. \"Incasso netto\" 658 € + "
        "entrate da lotteria 116 € = 774 €. \"Riconteggio matrici\": 190 "
        "bibite x 1 € = 190 €; 105 cartocci x 3 € = 315 €; 27 kg "
        "di fresche x 5 € = 135 €; offerta 5 €; totale 645 € (dai "
        "tagliandini; contanti effettivi in cassa 658 €).",
    (DATE, "16:09", "Dante Caniglia", "IMG-20261115-WA0022.jpg"):
        "Screenshot della pagina Facebook \"Classe 1987 San Benedetto dei "
        "Marsi\" con il post su San Martino (\"Noi ci siamo... vi "
        "aspettiamo per vivere un momento di spensieratezza e di allegria "
        "insieme ai nostri bimbi\") e il collage di foto; Dante lo "
        "mostra a proposito degli errori nei post.",
    (DATE, "16:09", "Dante Caniglia", "IMG-20261115-WA0023.jpg"):
        "Screenshot dal post Facebook del gruppo sulla gita a Corinaldo "
        "(\"Come da tradizione anche quest'anno ci stiamo impegnando...\") "
        "con la locandina \"Gita a Corinaldo presso la casa di Santa "
        "Maria Goretti\", altro esempio mostrato da Dante.",
    (DATE, "17:27", "Antonio Sabatini", "IMG-20261115-WA0024.jpg"):
        "Una bilancia digitale con sopra un cesto: una delle pesate "
        "delle castagne avanzate in sede; Antonio scrive che hanno "
        "pesato più volte e in vario modo e il peso corrisponde sempre.",
    (DATE, "19:04", "Emilio Caniglia", "IMG-20261115-WA0025.jpg"):
        "Locandina dell'Armonia Corale Piana del Cavaliere: domenica 22 "
        "novembre, Chiesa di Santa Maria Assunta (Chiesa Grande), ore "
        "17:00, messa in onore di Santa Cecilia, a seguire breve concerto.",
    (DATE, "19:09", "Emilio Caniglia", "IMG-20261115-WA0026.jpg"):
        "Il sacchetto di castagne cotte avanzato, pesato su una bilancia "
        "digitale: 211 grammi.",
    (DATE, "19:13", "Emilio Caniglia", "IMG-20261115-WA0027.jpg"):
        "Dieci castagne cotte sulla bilancia digitale: 69 grammi.",
}

# IMG-0013 (13:10 Aceto, polenta con sugo e salsiccia, "Buon appetito") è
# la foto del pranzo, fuori tema; Elisabettabolle.vcf (13:26 Ilenia) è un
# contatto telefonico personale, non riportato nel digest; VID-0012 (GIF
# senza audio) viene scartato in automatico.
_SKIP_FILES = {"IMG-20261115-WA0013.jpg", "Elisabettabolle.vcf"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 text_merges=TEXT_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="foto pranzo / contatto personale")
