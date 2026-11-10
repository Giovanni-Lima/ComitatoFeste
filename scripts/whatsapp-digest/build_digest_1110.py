#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-10 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:38-14:41 (coda aggiunta il 10/11 stesso con l'export Dropbox
delle 15:38). Emilio posta la sintesi della riunione del 6 novembre e
degli sviluppi successivi (squadre San Martino, incontro con Gianvito,
banda "Leoncini d'Abruzzo", calze della Befana), con prossimo appuntamento
venerdì 13/11. Segue un lungo confronto sulla scarsa comunicazione social
del comitato per San Martino/castagnata: Maikel ed Elvis aprono la
discussione, Emanuele spiega i ritardi (in attesa del materiale della Pro
Loco), ma il gruppo — spinto soprattutto da Ilenia — decide di procedere
comunque in autonomia con una locandina propria, senza aspettare oltre la
Pro Loco. In parallelo si raccolgono cassette, cesti e zucche per
l'allestimento. Prosegue poi la finalizzazione della locandina (bozze
generate con Gemini, un refuso "deduzione"/"degustazione" diventato
scherzosamente il nome del vin brûlé "di zio Elvis"), la ricerca di
materiali per il fuoco, idee a tema per i banchetti, e un lungo confronto
sul rapporto con la Pro Loco (se distanziarsene o mantenere la
collaborazione), con dubbi di Maikel e Luca sulla destinazione dei fondi
raccolti dalla Pro Loco. Chiude la giornata un intervento del presidente
Emilio, che spiega perché il comitato dipenda ancora dalla Pro Loco per
gli aspetti formali di un evento (mancanza di soggettività giuridica
propria) pur potendo pubblicare liberamente contenuti social non
ufficiali, risolvendo i dubbi sollevati da Emanuele. Nessuna menzione di
Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-10"

CURATED = {
    ("07:38", "Emilio Caniglia"): ("info",
        "Posta la sintesi della riunione del 6 novembre e degli "
        "sviluppi successivi. San Martino: definite le disponibilità "
        "del Comitato e il necessario per l'evento (materiale di "
        "consumo, utensili, strutture per le postazioni, scenografia); "
        "nei prossimi giorni si organizzerà la logistica e si "
        "divideranno i membri in squadre per attività, per ottimizzare "
        "ed evitare confusione. Capodanno: dopo il confronto in "
        "riunione, sabato pomeriggio c'è stato un incontro con Gianvito "
        "che ha chiarito alcuni aspetti (numero minimo di partecipanti, "
        "organizzazione dell'evento); serve iniziare subito a "
        "intercettare gruppi e comitive. Ieri pomeriggio incontro con "
        "la banda di Pescina \"I Leoncini d'Abruzzo\": il comitato ha "
        "illustrato le proprie necessità, a breve arriverà un "
        "preventivo da valutare in riunione. Calze della Befana: "
        "Vincenzo ha preso contatti con la Dolfood per consigli e "
        "costi, Maria ha individuato un'azienda con calze già "
        "confezionate a buon prezzo. Prossimo appuntamento: venerdì 13 "
        "novembre, ore 21 in sede."),
    ("09:31", "Elvis Ippoliti"): ("proposta",
        "Conferma che era già da fare da subito il post, ma ora "
        "l'importante è rimediare al più presto. Chiede il punto "
        "sull'approvvigionamento delle castagne, ricordando che restano "
        "da tagliare, da preparare i sacchetti e altro lavoro da "
        "fare."),
    ("09:35", "Emanuele Sciarra"): ("info",
        "Comunica che le castagne gli saranno consegnate domani, tra "
        "tarda mattina e primo pomeriggio; appena saprà l'orario "
        "preciso aggiornerà il gruppo per portarle in sede."),
    ("12:52", "Emilio Caniglia"): ("info",
        "Emilio interviene per chiarire la situazione. Spiega che il "
        "comitato, non avendo ancora una soggettività giuridica propria, "
        "non può gestire autonomamente gli adempimenti necessari per un "
        "evento (comunicazione al SUAP, piano di sicurezza, richiesta "
        "di occupazione di suolo pubblico): finora se ne è occupata la "
        "Pro Loco. Sul ritardo della locandina: la Pro Loco aveva "
        "indetto la riunione organizzativa di San Martino già il 3 "
        "novembre, con accordi presi; nel weekend sono arrivate "
        "indicazioni diverse sull'animazione (equivoco tra Pro Loco e "
        "oratorio, chiarito domenica a Corinaldo parlando con Don Enzo: "
        "la Pro Loco pensava che invitare l'oratorio implicasse che se "
        "ne assumesse anche la responsabilità). Il comitato, tramite "
        "Emanuele, ha quindi contattato autonomamente un'animatrice "
        "senza aspettare i tempi della Pro Loco; il preventivo è "
        "arrivato lunedì mattina, girato subito alla Pro Loco, che ha "
        "confermato solo lunedì sera tra le 20 e le 21 — Emilio ha "
        "girato tutte le informazioni a Chiara per la locandina entro "
        "le 22 dello stesso lunedì. Conclude: più di così, da parte del "
        "comitato, non si poteva fare. Aggiunge poi che le attività "
        "social (foto, video, post, storie) sono comunque cose distinte "
        "dall'organizzazione formale dell'evento."),
}

MEDIA_OVERRIDES = {
    (DATE, "08:18", "Alessandra Toracchio", "IMG-20261110-WA0030.jpg"):
        "Foto di cassette di legno decorative: chiede se qualcuno può "
        "procurarne di simili per l'allestimento di San Martino. Ugo si "
        "offre di chiedere a Pasquale il fruttivendolo; anche Alessandra "
        "e Ilenia offrono dei cesti.",
    (DATE, "08:26", "Emanuele Sciarra", "IMG-20261110-WA0014.jpg"):
        "Screenshot della pagina Facebook del comitato \"Classe 1986\": "
        "il primo post pubblico della pagina, una foto di gruppo del "
        "12/11/2025.",
    (DATE, "08:26", "Emanuele Sciarra", "IMG-20261110-WA0011.jpg"):
        "Screenshot della stessa pagina: un post del 17/11/2025 (\"Ci "
        "stiamo preparando...\") e, in alto, la locandina dell'evento "
        "di dicembre con panini e vin brulé a cura del Comitato 1986.",
    (DATE, "08:26", "Emanuele Sciarra", "IMG-20261110-WA0013.jpg"):
        "Screenshot della stessa pagina: la locandina completa "
        "dell'evento \"Accensione dell'Albero di Natale\" (8/12/2025, "
        "Piazza Risorgimento), con castagnata a cura di AVIS e panini/"
        "vin brulé a cura del Comitato 1986 — esempi citati da Emanuele "
        "per spiegare come la pagina social degli \"86\" sia stata "
        "alimentata nel tempo.",
    (DATE, "08:28", "Barbara Rizio", "IMG-20261110-WA0016.jpg"):
        "Foto dell'allestimento che Barbara mette a disposizione: una "
        "giacca rossa e un cappello su un'asta (da contadino/"
        "spaventapasseri), due cesti di vimini e due cassette di legno "
        "bianche.",
    (DATE, "09:19", "Elvis Ippoliti", "IMG-20261110-WA0028.jpg"):
        "Screenshot di un post Facebook della Pro Loco sulla festa di "
        "Halloween (22 ottobre), che menziona l'esposizione delle "
        "zucche decorate il 14 novembre \"in occasione della festa di "
        "San Martino\" senza però nominare il comitato: Elvis nota di "
        "averlo già segnalato il 25 ottobre.",
    (DATE, "09:44", "Costance Rossi", "IMG-20261110-WA0031.jpg"):
        "Locandina (non legata al comitato) della presentazione del "
        "libro \"Io e Pepè\" di Catena Fiorello Galeano, domenica 22 "
        "novembre ore 16 in Sala Consiliare, a cura del Caffè Letterario "
        "Spazio Cultura.",
    (DATE, "11:15", "Emanuele Sciarra", "IMG-20261110-WA0075.jpg"):
        "Versione corretta e definitiva della locandina di \"Festa di "
        "San Martino e delle Castagne\" (sabato 14 novembre, ore 16, "
        "Piazza Risorgimento, organizzata dalla Classe '87 con il "
        "patrocinio della Giunta comunale): degustazione di castagne "
        "arrosto, vino novello e prodotti tipici, degustazione di vin "
        "brûlé caldo \"di zio Elvis\", animazione per bambini. Generata "
        "con l'aiuto di Gemini (link condiviso: "
        "https://share.gemini.google/tM7CdLZ86aHi).",
}

# Bozze intermedie della locandina (refuso "deduzione"/anno sbagliato),
# scartate come le iterazioni di un logo: si tiene solo la versione
# definitiva (IMG-20261110-WA0075.jpg sopra).
_SKIP_DRAFTS_1110 = {
    "IMG-20261110-WA0032.jpg", "IMG-20261110-WA0038.jpg",
    "IMG-20261110-WA0052.jpg",
}


def _extra_skip(time_, fname):
    return fname in _SKIP_DRAFTS_1110


AUDIO_CURATED = {
    (DATE, "09:05", "Luca Cicchelli", "PTT-20261110-WA0026.opus"): ("rumore", ""),
}

AUDIO_MERGES = [
    {
        "anchor_time": "08:03",
        "anchor_sender": "Maikel Montano",
        "type": "domanda",
        "text": (
            "Maikel chiede perché sui social del comitato non ci sia "
            "ancora nulla (locandina, foto) su San Martino/castagnata. "
            "Elvis concorda: non basta pubblicare solo a evento fatto, i "
            "social vanno tenuti attivi di continuo, scrivendo e "
            "coinvolgendo (consiglio dato anche da Antonella). Maikel "
            "ribadisce il punto: chi non fa parte del gruppo, anche "
            "dello stesso paese, non ha modo di sapere cosa succederà "
            "sabato."
        ),
        "members": [
            "PTT-20261110-WA0000.opus", "PTT-20261110-WA0001.opus",
            "PTT-20261110-WA0002.opus",
        ],
    },
    {
        "anchor_time": "08:24",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Emanuele spiega che il ritardo è dovuto al fatto che la "
            "locandina doveva uscire già due settimane fa, quando in "
            "riunione la Pro Loco si era impegnata a girare il "
            "vettoriale/logo necessario; nel frattempo si aspettava "
            "anche la conferma sull'animazione, arrivata solo ieri sera "
            "alle 22 (sarà Marta). Mostra come esempio lo storico della "
            "pagina Facebook del comitato \"gli 86\": i primi post, "
            "generici, sono arrivati prima di avere materiale "
            "fotografico vero e proprio, poi la pagina è stata "
            "rafforzata via via con le immagini degli eventi "
            "organizzati. Maria ribadisce che, visti i ritardi (è già "
            "martedì), bisogna comunque pubblicare subito qualcosa di "
            "generico per avvisare la popolazione che sabato ci sarà la "
            "castagnata, anche senza tutti i dettagli definitivi; "
            "Emanuele concorda sul principio ma nota che si era "
            "preferito aspettare la Pro Loco perché l'evento è anche "
            "loro, e non si voleva \"bruciare\" la loro comunicazione; "
            "riferisce che Emilio è in contatto con Giorgio (Pro Loco) "
            "proprio su questo da ieri mattina."
        ),
        "members": [
            "PTT-20261110-WA0003.opus", "PTT-20261110-WA0004.opus",
            "PTT-20261110-WA0005.opus", "PTT-20261110-WA0006.opus",
            "PTT-20261110-WA0007.opus", "PTT-20261110-WA0008.opus",
            "PTT-20261110-WA0009.opus", "PTT-20261110-WA0010.opus",
        ],
    },
    {
        "anchor_time": "08:48",
        "anchor_sender": "Ilenia Piccozzi",
        "type": "decisione",
        "text": (
            "Ilenia interviene con decisione: a suo parere il comitato "
            "non deve aspettare la Pro Loco, perché loro hanno già "
            "ottenuto il proprio ritorno dalla vendita delle zucche (i "
            "cui acquirenti sanno già della premiazione di sabato) e "
            "non hanno interesse a spingere sulla castagnata; propone "
            "quindi di procedere autonomamente con la locandina, visto "
            "che altrimenti ci rimette solo il comitato. Luca suggerisce "
            "di sentire subito Daniele per il bando di occupazione "
            "suolo pubblico (circa 20€); Emanuele conferma che serve "
            "comunque mantenere buoni rapporti con la Pro Loco per "
            "altri aspetti, come l'autorizzazione a cuocere le castagne "
            "con il fuoco, dato che il comitato non è ancora formalmente "
            "costituito con permessi propri, e riporta la richiesta di "
            "Lisa (Pro Loco/comune) di scrivere obbligatoriamente \"con "
            "patrocinio del Comune\" sulla locandina per evitare "
            "problemi di occupazione del suolo pubblico. Elvis distingue "
            "comunque tra la locandina vera e propria (che richiede "
            "l'iter completo) e un semplice post sui social per "
            "annunciare subito l'evento, fattibile nel frattempo. Luca "
            "insiste che un evento non si pubblicizza 3-4 giorni prima, "
            "citando l'esempio di un torneo di biliardino pubblicizzato "
            "con un mese di anticipo; Elvis precisa che la Pro Loco in "
            "realtà si era già tutelata (la locandina di Halloween "
            "citava il contest delle zucche a San Martino), quindi è il "
            "comitato a essere rimasto indietro con la propria "
            "comunicazione. Maria e Ilenia concordano che alla Pro Loco, "
            "avendo già incassato con le zucche, non interessi la "
            "\"perdita\" del comitato. Maria chiude: visto che le "
            "autorizzazioni del Comune ci sono già, si fa la locandina e "
            "basta, senza più aspettare — la pubblicità è già in "
            "ritardo. Antonio Aceto si allinea: dato che la Pro Loco si "
            "è già pubblicizzata per conto suo, il comitato può "
            "procedere per la propria strada senza remore; Ilenia e "
            "Maria confermano. Luca sollecita a muoversi subito, "
            "offrendosi di occuparsene lui stesso da domani se qualcuno "
            "prepara il materiale."
        ),
        "members": [
            "PTT-20261110-WA0017.opus", "PTT-20261110-WA0019.opus",
            "PTT-20261110-WA0020.opus", "PTT-20261110-WA0021.opus",
            "PTT-20261110-WA0022.opus", "PTT-20261110-WA0023.opus",
            "PTT-20261110-WA0025.opus", "PTT-20261110-WA0027.opus",
            "PTT-20261110-WA0029.opus",
        ],
    },
    {
        "anchor_time": "10:04",
        "anchor_sender": "Luca Cicchelli",
        "type": "proposta",
        "text": (
            "Luca chiede chi si occupa del fuoco per cuocere le "
            "castagne, offrendosi di chiedere ad Andrea eventuali "
            "bancali rotti da buttare. Emanuele conferma di avere tre "
            "grandi contenitori di legno adatti e chiede a Cesare "
            "Raglione delle vasche/bacinelle grandi di alluminio (di "
            "quelle usate per il mangime); Cesare risponde di averne "
            "solo di plastica, ma Maria ricorda che Cesare aveva "
            "comunque già detto di avere dei bancali. Luca nota che "
            "serviranno comunque anche per Sant'Antonio; Emanuele "
            "aggiunge che può chiedere bancali e materiale di scarto "
            "anche al lavoro (SAC), utili per entrambi gli eventi. Più "
            "tardi Cesare suggerisce di far girare la notizia anche "
            "tramite passaparola (\"Cannelloro\"), a suo dire più "
            "efficace dei social."
        ),
        "members": [
            "PTT-20261110-WA0034.opus", "PTT-20261110-WA0035.opus",
            "PTT-20261110-WA0036.opus", "PTT-20261110-WA0037.opus",
        ],
    },
    {
        "anchor_time": "10:03",
        "anchor_sender": "Luca Cicchelli",
        "type": "proposta",
        "text": (
            "Emanuele condivide una prima bozza di locandina generata "
            "con l'aiuto di Gemini e chiede pareri. Il gruppo accoglie "
            "con entusiasmo (Luca: \"bomba, bomba!\"), ma segnala "
            "alcune correzioni: manca la menzione del vin brulé (Elvis) "
            "e la voce \"animazione per bambini\" andrebbe messa più in "
            "risalto, trattandosi di un'iniziativa portata avanti "
            "direttamente dal comitato e non dalla Pro Loco (Maria, "
            "Ilenia) — tanto che, nota Emanuele, l'animatrice è stata "
            "contattata direttamente dal comitato, quindi la Pro Loco "
            "non ha titolo per lamentarsi. Emanuele aggiorna la "
            "grafica aggiungendo il vin brulé, ma per un refuso "
            "dell'IA la voce esce come \"deduzione speciale\" invece "
            "di \"degustazione speciale\": Elvis se ne accorge e "
            "scherza sul fatto che suoni come un'offerta \"di zio "
            "Elvis\"; il gruppo si diverte all'idea e, una volta "
            "corretto il refuso, la voce resta scherzosamente "
            "intestata al \"vin brûlé di zio Elvis\". Si concorda "
            "inoltre di non indicare prezzi sulla locandina (si "
            "useranno cartelli scritti a mano sul posto, come per la "
            "vendita delle castagne a crudo). Prima di procedere con "
            "la pubblicazione, Emanuele preferisce attendere il "
            "benestare di Emilio per rispetto del suo ruolo di "
            "presidente, non sapendo se avesse preso accordi diversi "
            "con la Pro Loco; Emilio, raggiunto brevemente al lavoro, "
            "risponde di aspettare che la Pro Loco (tramite Chiara) "
            "fornisca la propria locandina ufficiale, per poi "
            "eventualmente procedere con quella preparata da Emanuele. "
            "Il gruppo nel frattempo scherza sulla propria impazienza "
            "(\"c'era troppo silenzio\")."
        ),
        "members": [
            "PTT-20261110-WA0033.opus", "PTT-20261110-WA0039.opus",
            "PTT-20261110-WA0040.opus", "PTT-20261110-WA0041.opus",
            "PTT-20261110-WA0042.opus", "PTT-20261110-WA0043.opus",
            "PTT-20261110-WA0044.opus", "PTT-20261110-WA0045.opus",
            "PTT-20261110-WA0046.opus", "PTT-20261110-WA0047.opus",
            "PTT-20261110-WA0048.opus", "PTT-20261110-WA0049.opus",
            "PTT-20261110-WA0050.opus", "PTT-20261110-WA0051.opus",
            "PTT-20261110-WA0053.opus", "PTT-20261110-WA0054.opus",
            "PTT-20261110-WA0055.opus", "PTT-20261110-WA0056.opus",
            "PTT-20261110-WA0057.opus", "PTT-20261110-WA0058.opus",
            "PTT-20261110-WA0059.opus", "PTT-20261110-WA0060.opus",
            "PTT-20261110-WA0064.opus",
        ],
    },
    {
        "anchor_time": "10:31",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Si apre un confronto più ampio sul rapporto con la Pro "
            "Loco. Emanuele pone il nodo: proseguire per conto proprio "
            "incuranti della Pro Loco, come fanno altri comitati, "
            "oppure mantenere una collaborazione utile ad ottenere "
            "agevolazioni senza troppi attriti. Antonio Aceto propende "
            "per andare per la propria strada, non sentendosi in debito "
            "con nessuno. Emanuele concorda ma vuole che la decisione "
            "sia presa tutti insieme, votata alla riunione di venerdì, "
            "valutando pro e contro; coglie l'occasione per correggere "
            "una voce circolata in paese secondo cui il comitato non "
            "avrebbe voluto fare nulla per Halloween: chiarisce che, "
            "quando ne avevano parlato con la Pro Loco, avevano solo "
            "detto di non sentirsela di organizzare da soli un veglione "
            "a stretto giro senza certezze sulla riuscita, ma che non "
            "si erano affatto tirati indietro da un'eventuale "
            "collaborazione. Maria, anche alla luce di questa voce "
            "scorretta, è favorevole a smarcarsi e portare avanti gli "
            "eventi del comitato per conto proprio, chiedendo i debiti "
            "permessi direttamente al Comune, ma ribadisce che la "
            "decisione finale andrà presa tutti insieme, a votazione, "
            "in riunione. Emanuele si dice sostanzialmente d'accordo, "
            "ma vuole prima avere il quadro preciso della situazione, "
            "dato che Emilio è il più in contatto con Giorgio della Pro "
            "Loco. Luca aggiunge un argomento pratico: il calendario "
            "estivo della Pro Loco cresce ogni anno e lascia sempre "
            "meno spazio ai comitati (l'anno scorso \"gli 86\" sono "
            "riusciti a fare un solo evento, a luglio); meglio quindi "
            "prepararsi in anticipo un proprio programma estivo "
            "autonomo. Emanuele conferma che nessuno vieta comunque di "
            "organizzare un evento lo stesso giorno della Pro Loco "
            "(salvo il caso delle feste patronali, dove serve comunque "
            "un minimo di raccordo col Comune). Emanuele, scrivendo "
            "mentre è al lavoro, chiede di poter girare tutto al "
            "gruppo prima di pubblicare alcunché, perché \"20.000 "
            "occhi sono meglio di due\"."
        ),
        "members": [
            "PTT-20261110-WA0061.opus", "PTT-20261110-WA0062.opus",
            "PTT-20261110-WA0063.opus", "PTT-20261110-WA0065.opus",
            "PTT-20261110-WA0066.opus", "PTT-20261110-WA0067.opus",
            "PTT-20261110-WA0068.opus", "PTT-20261110-WA0069.opus",
            "PTT-20261110-WA0070.opus", "PTT-20261110-WA0071.opus",
            "PTT-20261110-WA0072.opus", "PTT-20261110-WA0073.opus",
            "PTT-20261110-WA0074.opus",
        ],
    },
    {
        "anchor_time": "11:22",
        "anchor_sender": "Emanuele Sciarra",
        "type": "proposta",
        "text": (
            "Elvis propone di vestirsi a tema per chi starà dietro al "
            "banco (per esempio con sacchi di tela/ardichella) e che "
            "qualcuno giri vestito da San Martino tra la gente, anche "
            "per gestire una lotteria sul numero di castagne. Emanuele "
            "coglie l'occasione per riferire di aver già trovato — per "
            "la tombolata, non per San Martino — un vestito da Grinch a "
            "17-18€ in un negozio cinese; si dice inoltre favorevole, "
            "se si farà, all'idea delle \"chitarre di Ghello\" per San "
            "Martino. Dante rilancia scherzosamente proponendo un "
            "vestito a tema \"aceto\" per Antonio Aceto (\"fa più "
            "effetto\"); Alessandra si offre di occuparsene."
        ),
        "members": ["PTT-20261110-WA0076.opus", "PTT-20261110-WA0077.opus"],
    },
    {
        "anchor_time": "11:44",
        "anchor_sender": "Maikel Montano",
        "type": "domanda",
        "text": (
            "Maikel, in collegamento da Roma, si dice d'accordo nel "
            "proseguire per la propria strada, ma solleva un dubbio da "
            "\"profano\": che fine fanno i soldi raccolti dalla Pro "
            "Loco con i suoi eventi? Non gli sembra normale dover quasi "
            "litigare con le attività e la Pro Loco solo per organizzare "
            "le feste patronali. Luca risponde che, per quel poco che "
            "sa, i soldi tornano in parte alla comunità o rifinanziano "
            "altri eventi, in un circolo continuo. Maikel ribatte che un "
            "minimo di utile da un evento resta sempre, mentre il "
            "comitato almeno ha un obiettivo chiaro e noto a tutti. Luca "
            "precisa che non tutti gli eventi vanno bene: anche il "
            "torneo di biliardino organizzato da loro, ad esempio, è "
            "arrivato quasi in pareggio una volta sottratti i costi di "
            "noleggio; Cesare conferma che anche l'evento degli "
            "arrosticini è andato quasi in pari."
        ),
        "members": [
            "PTT-20261110-WA0078.opus", "PTT-20261110-WA0079.opus",
            "PTT-20261110-WA0080.opus", "PTT-20261110-WA0081.opus",
            "PTT-20261110-WA0082.opus",
        ],
    },
    {
        "anchor_time": "12:34",
        "anchor_sender": "Cesare Raglione",
        "type": "info",
        "text": (
            "Cesare chiede quando bisognerà tagliare le castagne; "
            "Antonio Aceto risponde tra venerdì sera e sabato mattina. "
            "Luca scherza proponendo di tagliarle direttamente durante "
            "la riunione di venerdì invece di stare solo a parlare; "
            "Antonio concorda che servirà davvero, visto il tempo "
            "necessario per preparare la grande quantità di castagne."
        ),
        "members": ["PTT-20261110-WA0083.opus", "PTT-20261110-WA0084.opus"],
    },
    {
        "anchor_time": "13:27",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": (
            "Emanuele chiede chiarimenti a Emilio: se il comitato "
            "avesse voluto pubblicizzare San Martino per conto proprio, "
            "poteva farlo senza aspettare la Pro Loco? Emilio risponde "
            "che, al di là della locandina ufficiale (che richiede "
            "tempo per i vari aspetti da valutare), tutto il resto — "
            "post, foto, video, storie — è assolutamente libero, come "
            "già fatto all'apertura delle pagine social: più contenuti "
            "ci sono, più il comitato cresce sui social. Emanuele chiede "
            "ulteriore conferma se la \"mezza locandina\" già preparata "
            "da lui si potesse pubblicare senza citare la Pro Loco; "
            "chiede anche se, vista la locandina di Halloween che "
            "menzionava le zucche ma non il comitato, sarebbe scorretto "
            "pubblicare prima una locandina propria e poi una "
            "collettiva. Emilio preferisce una sola locandina per non "
            "creare confusione, rimandando il tema a un confronto "
            "diretto in riunione; conferma che la dicitura finale sarà "
            "\"evento organizzato dalla Pro Loco con la partecipazione "
            "della classe 1987\". Emanuele si dice d'accordo e annuncia "
            "che domani, allo scarico delle castagne, pubblicheranno "
            "comunque un reel."
        ),
        "members": [
            "PTT-20261110-WA0087.opus", "PTT-20261110-WA0088.opus",
            "PTT-20261110-WA0089.opus",
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="bozze intermedie della locandina (refuso corretto)")
