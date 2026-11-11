#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-11 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 07:03-13:48 (export Dropbox delle 13:49, giornata ancora in corso
al momento dell'export — la festa di San Martino è sabato 14/11, questa è
la vigilia). Lunga mattinata di prove tecniche per far funzionare la
ricondivisione del post/locandina sui social (Facebook/Instagram) tra i
vari membri, risolta verso le 9:50. Oggi è anche San Martino (onomastico
di Martina Del Gizzi, festeggiata dal gruppo) e Dante coglie l'occasione
per gli auguri di rito. Antonio riferisce una voce incoraggiante per il
veglione di Capodanno: la Rupe non lo farà quest'anno, quindi San
Benedetto resterebbe l'unica opzione in paese — si valuta un incontro con
Andrea Di Loreto per organizzare la comunicazione/sponsorizzazione
dell'evento, con cautela sul rivelarne già il nome. Nel pomeriggio
arrivano le castagne (106-107 kg): si decide di venderle sfuse pesate al
momento in piazza invece che in sacchetti pre-confezionati, e si discute
di quante sgusciare/cuocere in anticipo. Nessuna menzione di Giovanni
Lima.
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
}

MEDIA_OVERRIDES = {}

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
            "(anche solo per abbellimento del banco)."
        ),
        "members": [
            "PTT-20261111-WA0041.opus", "PTT-20261111-WA0042.opus",
            "PTT-20261111-WA0043.opus", "PTT-20261111-WA0044.opus",
        ],
    },
]

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, extra_skip_media=_extra_skip,
                 extra_skip_label="screenshot social ridondanti (ricondivisione)")
