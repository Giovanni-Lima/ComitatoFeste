#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-11-22 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:13-20:05. Antonio e Emilio concordano come comunicare sui
social le prenotazioni per le calze della Befana (senza indicare il
prezzo). Emanuele pubblica un ringraziamento alla Classe 1986 per il
passaggio di testimone. Emilio pubblica la sintesi della riunione di
venerdì 20 (San Martino, calendario natalizio, banda, animatrici per
Capodanno con preventivo) e ricorda l'invito di Don Enzo. Lungo lavoro di
gruppo per completare la lista di potenziali sponsor della Tombolata
(Luca recupera il vecchio elenco del comitato dell'86). Emanuele propone
un'alternativa/aggiunta al calendario natalizio: un porta-foto in stile
segnaposto di matrimonio, chiedendo idee economiche per realizzarlo.
Nessuna menzione di Giovanni Lima.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-11-22"

CURATED = {
    ("08:13", "Antonio Aceto"): ("domanda",
        "Chiede a Emilio se si possa pubblicizzare sui social il "
        "fatto che si stanno dando le prevendite delle calze della "
        "Befana a 5€."),
    ("08:52", "Emilio Caniglia"): ("info",
        "Risponde di sì: Emanuele e Chiara stanno preparando i "
        "contenuti social per i prossimi eventi e per le calze; "
        "meglio però non indicare il prezzo. Dopo un breve scambio "
        "con Antonio, precisa che è meglio scrivere che è possibile "
        "prenotare, piuttosto che parlare di \"prevendita\"."),
    ("12:51", "Emilio Caniglia"): ("info",
        "Sintesi della riunione di venerdì 20 novembre: ampio "
        "confronto sulle prossime attività (calze della Befana, "
        "Tombolata, Capodanno, ecc.) con proposte e idee, oltre a un "
        "resoconto di San Martino. Lunedì 23 novembre alle 21, sala "
        "consiliare, incontro promosso dal Comune per il calendario "
        "natalizio (aperto a chi vuole partecipare). Nei prossimi "
        "giorni contatti con aziende per spari/fuochi d'artificio ed "
        "eventuali incontri in sede, di cui sarà data notizia sul "
        "gruppo. È stata contattata Elisabetta di Collelongo per "
        "l'animazione di Capodanno: 250€ ad animatrice, e (come "
        "l'anno scorso, con 40-50 bambini) ne servono due, quindi "
        "500€ di preventivo. Chi ha conoscenze con altre animatrici o "
        "aziende di fuochi d'artificio può cercare un preventivo "
        "alternativo. Ricorda infine l'invito di Don Enzo per oggi "
        "pomeriggio."),
    ("14:54", "Emanuele Sciarra"): ("proposta",
        "Comunica di aver riscritto tutti i potenziali sponsor per la "
        "Tombolata (vedi foto) su 4 pagine, chiedendo se ce ne siano "
        "altri da aggiungere. Segue una raccolta collettiva di nomi: "
        "Costance segnala Miriana ed Enrico Mascitti (Ortucchio, "
        "parrucchiere); Ilenia aggiunge diverse attività di San "
        "Benedetto e dintorni (parrucchieri, estetiste, Bofrost, "
        "un'edilizia ad Aielli, un negozio a Pescina, un negozio di "
        "vestiti per bambini, una ragazza che fa le unghie, una "
        "bancarella del mercato); Luca recupera un vecchio biglietto "
        "del comitato dell'86 con l'elenco completo degli sponsor di "
        "allora per confronto, e gira anche la lotteria del carnevale "
        "di Pescina come riferimento; Cesare ricorda gli sponsor sul "
        "totem e di controllare al capannone di Montano. Alcuni "
        "(Tina, Ilenia) si offrono di contattare di persona le "
        "attività con cui hanno più confidenza."),
    ("20:00", "Emanuele Sciarra"): ("proposta",
        "Propone, in alternativa/aggiunta al calendario natalizio con "
        "le foto, un porta-foto da tavolo in stile segnaposto (come "
        "quelli fatti per il proprio matrimonio: una base in legno "
        "con una pinzetta per tenere la foto), da vendere a un prezzo "
        "più basso del calendario (es. calendario 10€, porta-foto "
        "5€); al posto della decorazione da sposi userebbe qualcosa "
        "di più pratico. Le pinzette le ha trovate a 8€ per 50 pezzi; "
        "i tronchetti di legno li rifarebbe lui, ma chiede idee "
        "economiche per abbellire il tutto."),
}

MEDIA_OVERRIDES = {
    (DATE, "09:43", "Emanuele Sciarra", "IMG-20261122-WA0001.jpg"):
        "Screenshot di un post pubblicato sulla pagina Facebook "
        "\"Classe 1987 San Benedetto dei Marsi\": un ringraziamento "
        "al Comitato Classe 1986 per l'affetto e l'in bocca al lupo, "
        "con l'impegno a iniziare il proprio percorso con lo stesso "
        "entusiasmo.",
    (DATE, "14:53", "Emanuele Sciarra", "IMG-20261122-WA0006.jpg"):
        "Prima pagina dell'elenco di potenziali sponsor per la "
        "Tombolata.",
    (DATE, "14:53", "Emanuele Sciarra", "IMG-20261122-WA0007.jpg"):
        "Seconda pagina dell'elenco di potenziali sponsor per la "
        "Tombolata.",
    (DATE, "14:53", "Emanuele Sciarra", "IMG-20261122-WA0008.jpg"):
        "Terza pagina dell'elenco di potenziali sponsor per la "
        "Tombolata.",
    (DATE, "14:53", "Emanuele Sciarra", "IMG-20261122-WA0009.jpg"):
        "Quarta pagina dell'elenco di potenziali sponsor per la "
        "Tombolata.",
    (DATE, "15:27", "Luca Cicchelli", "IMG-20261122-WA0010.jpg"):
        "Vecchio biglietto/ricevuta del comitato classe 1986 con "
        "l'elenco completo degli sponsor di allora, tenuto da Luca "
        "come riferimento per confrontare la nuova lista.",
    (DATE, "15:27", "Luca Cicchelli", "IMG-20261122-WA0011.jpg"):
        "Retro o dettaglio dello stesso biglietto/ricevuta del "
        "comitato dell'86.",
    (DATE, "15:33", "Luca Cicchelli", "IMG-20261122-WA0012.jpg"):
        "Biglietto della lotteria del Carnevale di Pescina, girato "
        "come riferimento.",
    (DATE, "15:34", "Luca Cicchelli", "IMG-20261122-WA0013.jpg"):
        "Altro biglietto/dettaglio della lotteria del Carnevale di "
        "Pescina.",
    (DATE, "15:37", "Emanuele Sciarra", "IMG-20261122-WA0014.jpg"):
        "Immagine a corredo della discussione sugli sponsor della "
        "Tombolata.",
    (DATE, "15:56", "Costance Rossi", "IMG-20261122-WA0015.jpg"):
        "Foto/contatto dell'attività di Miriana (Ortucchio), segnalata "
        "come possibile sponsor.",
    (DATE, "20:01", "Emanuele Sciarra", "IMG-20261122-WA0017.jpg"):
        "Il segnaposto creato da Emanuele per il proprio matrimonio: "
        "una base in una fetta di tronchetto di legno con una "
        "pinzetta decorata (tulle bianco) che regge la foto.",
    (DATE, "20:01", "Emanuele Sciarra", "IMG-20261122-WA0018.jpg"):
        "Altra inquadratura dello stesso segnaposto/porta-foto del "
        "matrimonio, preso a modello per l'idea del porta-foto "
        "natalizio.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
