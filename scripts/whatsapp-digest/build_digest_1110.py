#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-10 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:38-09:35 (export Dropbox delle 9:38, giornata ancora in corso
al momento dell'export). Emilio posta la sintesi della riunione del 6
novembre e degli sviluppi successivi (squadre San Martino, incontro con
Gianvito, banda "Leoncini d'Abruzzo", calze della Befana), con prossimo
appuntamento venerdì 13/11. Segue un lungo confronto sulla scarsa
comunicazione social del comitato per San Martino/castagnata: Maikel ed
Elvis aprono la discussione, Emanuele spiega i ritardi (in attesa del
materiale della Pro Loco), ma il gruppo — spinto soprattutto da Ilenia —
decide di procedere comunque in autonomia con una locandina propria,
senza aspettare oltre la Pro Loco. In parallelo si raccolgono cassette,
cesti e zucche per l'allestimento. Nessuna menzione di Giovanni Lima.
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
}

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
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES)
