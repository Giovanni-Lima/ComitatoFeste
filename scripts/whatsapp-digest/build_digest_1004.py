#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-04 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 09:02-13:50 (export Dropbox delle 13:51 del 4/10). Mattina dopo la
riunione: Alessandra Toracchio (09:11) ha trovato il frigorifero per la sede
(Tina Giarrante entusiasta). Emilio Caniglia (09:18) riassume la riunione di
ieri sera: visita a Corinaldo l'8 novembre (quota 30€, locandina in arrivo,
passaparola nel frattempo); incontro con l'azienda materassi il 16 ottobre
per 20 coppie, con altri incontri simili nelle prossime settimane; per
Halloween supporto volontario alla Proloco, per San Martino una castagnata
con vin brulé da organizzare in una riunione dedicata; preadesione al
comitato di 20€ a testa, 15 preadesioni per 300€ raccolte, come fondo per le
spese di registrazione; social aperti (Facebook e Instagram) curati da
Emanuele e Antonio A., con Chiara per locandine e contenuti più elaborati;
responsabile delle entrate Antonio Sabatini (che incasserà l'assegno
dell'ultimo incontro), responsabile delle preadesioni Alessandro;
resoconto mensile pubblico per trasparenza. Donato Cerasani (11:41) consegnerà
la sua quota ad Alessandro e Maria Buttari (09:23) quella della madre.
Emanuele Sciarra (09:59) condivide il link della pagina Facebook del comitato,
Antonio Aceto (10:19) quello di Instagram. Per la castagnata dell'11 novembre
Antonio (vocale 10:52) dovrà trovare chi cura le castagne della Tavurà; in
mattinata Costantino Mariani (vocale 10:57) propone una raccolta di indumenti
usati per la Caritas legata a San Martino, e Maria Buttari (11:13) racconta la
leggenda di San Martino proponendo una piccola rappresentazione del gesto
del mantello. Antonio Aceto (11:36, 11:53) condivide due video animati con la
scritta "loading". Elvis Ippoliti (12:21) mostra il pagamento del primo mese
(sembra l'affitto della sede) e Costantino (12:23) risponde che per novembre
tocca a lui. Emanuele (12:27-12:29) presenta le bozze dei badge da mettere nei
portabadge, fatte da Alessandra Toracchio, preferendo quelle verticali; lei
(12:33-12:34) propone di scegliere tra quelle verticali, perché le orizzontali
hanno le scritte troppo ravvicinate. Antonio Aceto (13:21) propone un'immagine
come bozza per pubblicizzare la gita; Dante Caniglia (13:27) fa notare che
non è Corinaldo, e Alessandra Simonetti (13:50) suggerisce di aggiungere la
data. Un video senza audio di Costantino (12:23) è una GIF di reazione,
scartata in automatico con gli sticker. Nessuna menzione di Giovanni Lima in
questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-04"

CURATED = {
    ("09:11", "Alessandra Toracchio"): ("info",
        "Comunica di aver trovato il frigorifero per la sede, se ancora "
        "serve; Elvis Ippoliti dice che forse lo ha trovato Maikel Montano "
        "ieri sera, e che aggiornerà lui."),
    ("09:18", "Emilio Caniglia"): ("decisione",
        "Riassume la riunione di ieri sera. Visita a Corinaldo l'8 novembre: "
        "quota di partecipazione 30€, locandina in arrivo e passaparola "
        "nel frattempo; sarà il primo vero evento del comitato. Incontro "
        "sponsorizzato con l'azienda materassi il 16 ottobre, con 20 coppie "
        "e altri incontri simili nelle prossime settimane. Halloween: solo "
        "supporto volontario alla Proloco, se serve. San Martino: castagnata "
        "e vin brulé, da curare in una riunione dedicata. Preadesione al "
        "comitato: quota simbolica di 20€, 15 preadesioni raccolte per 300€, "
        "fondo per le spese di registrazione e simili. Social: pagine "
        "Facebook e Instagram aperte, curate da Emanuele e Antonio A., con "
        "Chiara per locandine e contenuti. Entrate: responsabile Antonio S. "
        "(incasserà l'assegno dell'ultimo incontro); preadesioni: responsabile "
        "Alessandro. Resoconto mensile pubblico per trasparenza."),
    ("09:23", "Maria Buttari"): ("info",
        "Comunica che farà avere al più presto la quota della madre."),
    ("09:59", "Emanuele Sciarra"): ("info",
        "Condivide il link della pagina Facebook del comitato: "
        "https://www.facebook.com/share/19XwrNFZLY/?mibextid=wwXIfr"),
    ("10:19", "Antonio Aceto"): ("info",
        "Ripropone il link del profilo Instagram della classe 1987: "
        "https://www.instagram.com/classe_1987_sbdm?stkn=MXNpZzI4dm9oM3N2OA%3D%3D&utm_source=qr"),
    ("11:41", "Donato Cerasani"): ("info",
        "Comunica che domani consegnerà la sua quota ad Alessandro."),
    ("12:21", "Elvis Ippoliti"): ("info",
        "Mostra la ricevuta del pagamento del primo mese (sembra l'affitto "
        "della sede); Costantino Mariani si prende il mese di novembre."),
    ("12:28", "Emanuele Sciarra"): ("proposta",
        "Presenta le bozze dei badge da mettere nei portabadge, fatte da "
        "Alessandra Toracchio, e chiede il parere del gruppo; preferisce "
        "quelle verticali."),
    ("12:34", "Alessandra Toracchio"): ("info",
        "Propone di scegliere tra le bozze verticali: le orizzontali hanno le "
        "scritte troppo ravvicinate."),
    ("13:21", "Antonio Aceto"): ("domanda",
        "Chiede se l'immagine condivisa va bene come bozza per cominciare a "
        "pubblicizzare la gita a Corinaldo; Dante Caniglia risponde che è "
        "bella ma non è Corinaldo."),
    ("13:50", "Alessandra Simonetti"): ("proposta",
        "Propone di aggiungere la data sulla locandina della gita."),
    ("14:27", "Alessandra Toracchio"): ("proposta",
        "Sondaggio per scegliere il badge del comitato, con i voti al momento "
        "dell'export: opzione 1 (7 voti), opzione 2 (0 voti), opzione 3 (0 "
        "voti), opzione 4 (3 voti), opzione 5 (14 voti)."),
    ("14:30", "Alessandra Toracchio"): ("info",
        "Propone di scegliere il badge così da farli stampare subito, due "
        "copie a testa per sicurezza; il nome sul badge sarà personalizzabile "
        "da ognuno (esempi: EMILIO, PRESIDENTE, CANIGLIA), basta scriverlo "
        "accanto al numero scelto."),
    ("14:48", "Maria Buttari"): ("domanda",
        "Chiede se la votazione del badge riguarda solo i comitati partecipanti "
        "o anche lei."),
    ("14:49", "Alessandra Toracchio"): ("info",
        "Risponde che i badge si fanno per tutti e invita a votare."),
    ("15:16", "Alessandra Toracchio"): ("info",
        "Chiede di controllare chi manca nell'elenco dei nomi per i badge."),
    ("16:18", "Giovanni Lima"): ("domanda",
        "Chiede se esiste un IBAN del comitato su cui versare la quota."),
    ("16:28", "Antonio Sabatini"): ("info",
        "Mette a disposizione un proprio conto personale per versare la quota "
        "a chi è lontano e non può venire di persona; provvederà poi a girare "
        "le somme ad Alessandro D.B."),
    ("16:32", "Costance Rossi"): ("domanda",
        "Chiede se la quota va versata sul conto di Antonio Sabatini o su "
        "quello di Alessandro, così manda la sua; altrimenti alla prossima "
        "riunione."),
    ("16:32", "Maria Buttari"): ("info",
        "Chiede di ricevere anche lei il codice per la quota, per evitare che "
        "sua madre debba portarla."),
    ("16:37", "Raffaele Di Cesare"): ("info",
        "Si rimette alla maggioranza sulla votazione del badge; per le serate "
        "conferma che ci sono."),
    ("16:55", "Elvis Ippoliti"): ("proposta",
        "Propone di mettere sul badge il nome di battesimo, leggibile, con "
        "eventualmente il soprannome più piccolo sotto: un nome strano o un "
        "soprannome non farebbe fidare chi incontra i volontari fuori da San "
        "Benedetto."),
    ("16:55", "Gilda Di Iulio"): ("info",
        "Chiede il codice IBAN per la quota, o di pagarla alla prossima "
        "riunione."),
    ("17:14", "Domenico Rossi"): ("domanda",
        "Chiede l'IBAN e l'importo della quota per poter pagare subito."),
    ("18:04", "Elvis Ippoliti"): ("domanda",
        "Fa notare che per legge sul badge dovrebbero esserci nome e cognome, "
        "visto che si chiedono offerte per conto della parrocchia e ci sono "
        "soldi di mezzo: meglio informarsi prima per evitare sanzioni."),
    ("18:48", "Alessandra Toracchio"): ("info",
        "Concorda con Elvis sul nome e cognome, soprattutto dopo quello che è "
        "successo quest'anno, quando altre persone hanno chiesto soldi "
        "spacciandosi per il comitato."),
    ("18:49", "Emanuele Sciarra"): ("domanda",
        "Chiede quando si metteranno nome e cognome sul badge."),
    ("18:49", "Elvis Ippoliti"): ("info",
        "Dice di aver cercato velocemente e che dovrebbe esserci una legge in "
        "materia, ma non è il suo campo: meglio chiedere a chi è più esperto."),
    ("19:27", "Tina Giarrante"): ("info",
        "Segnala che sulla maglia di Antonella c'era scritto un soprannome "
        "(\"LELLA\"): probabilmente sul cartellino va come dicono loro."),
    ("20:07", "Alessandra Toracchio"): ("domanda",
        "Chiede a chi bisogna rivolgersi per avere informazioni sul badge."),
    ("20:09", "Emanuele Sciarra"): ("info",
        "Dice che agli 85 ha visto solo il nome sul badge."),
    ("20:10", "Emanuele Sciarra"): ("proposta",
        "Propone di chiedere informazioni al Comune, dove c'è la polizia "
        "municipale che può rispondere."),
}

AUDIO_CURATED = {
    (DATE, "10:34", "Emidio Cerasani", "PTT-20261004-WA0002.opus"): ("rumore", ""),
    (DATE, "10:52", "Antonio Aceto", "AUD-20261004-WA0006.opus"): ("info",
        "Dice che per la castagnata dell'11 novembre (San Martino) va trovato "
        "chi cura le castagne della Tavurà, perché l'11 è tardi; farà sapere "
        "appena possibile."),
    (DATE, "10:57", "Costantino Mariani", "PTT-20261004-WA0003.opus"): ("proposta",
        "Propone, legandola alla festa di San Martino, una raccolta di "
        "indumenti usati da portare alla Caritas, per farsi conoscere."),
    (DATE, "10:57", "Costantino Mariani", "PTT-20261004-WA0004.opus"): ("rumore", ""),
    (DATE, "11:13", "Maria Buttari", "PTT-20261004-WA0005.opus"): ("proposta",
        "Racconta la leggenda di San Martino e propone, per la festa, una "
        "piccola rappresentazione del gesto del mantello diviso con il "
        "mendicante."),
    (DATE, "15:29", "Antonio Aceto", "PTT-20261004-WA0036.opus"): ("proposta",
        "Propone di iniziare a pubblicizzare la gita a Corinaldo con una "
        "locandina con la data dell'8 novembre e la scritta \"seguirai i "
        "dettagli del viaggio\", da pubblicare su Instagram se va bene a "
        "tutti, e di completarla con programma e dettagli quando Don Enzo "
        "confermerà il programma."),
}

MEDIA_OVERRIDES = {
    (DATE, "11:36", "Antonio Aceto", "VID-20261004-WA0007.mp4"):
        "Breve video animato con la scritta \"loading\", condiviso come "
        "battuta nel gruppo.",
    (DATE, "11:53", "Antonio Aceto", "VID-20261004-WA0008.mp4"):
        "Breve video animato con la scritta \"loading\" in rosso, condiviso "
        "come battuta nel gruppo.",
    (DATE, "12:21", "Elvis Ippoliti", "IMG-20261004-WA0012.jpg"):
        "Foto di due banconote da 20€ e 50€ appoggiate su un tavolo di legno: "
        "il pagamento del primo mese (sembra l'affitto della sede).",
    (DATE, "12:27", "Emanuele Sciarra", "IMG-20261004-WA0014.jpg"):
        "Bozza del badge del comitato: cartoncino giallo con \"COMITATO "
        "FESTE - San Benedetto Dei Marsi\", il logo arcade \"1987\" e il "
        "nome \"EMILIO\" in verticale.",
    (DATE, "12:27", "Emanuele Sciarra", "IMG-20261004-WA0015.jpg"):
        "Seconda bozza del badge del comitato in verticale, con il logo "
        "arcade \"1987\" e il nome \"EMILIO\" su sfondo bianco.",
    (DATE, "12:33", "Alessandra Toracchio", "IMG-20261004-WA0017.jpg"):
        "Bozza del badge del comitato con il logo arcade \"1987\" e il nome "
        "\"EMILIO\" su riquadro bianco, scelta tra le proposte.",
    (DATE, "13:21", "Antonio Aceto", "IMG-20261004-WA0018.jpg"):
        "Locandina per la gita della Classe 1987 a Corinaldo: \"Gita a "
        "Corinaldo al Santuario di Santa Maria Goretti\", con la gita che si "
        "terrà a novembre e i dettagli in arrivo (data, prezzo e programma).",
    (DATE, "13:38", "Antonio Aceto", "IMG-20261004-WA0019.jpg"):
        "Seconda versione della locandina per la gita della Classe 1987 a "
        "Corinaldo, \"presso la casa di Santa Maria Goretti\", con la gita a "
        "novembre e i dettagli in arrivo.",
    (DATE, "14:28", "Alessandra Toracchio", "IMG-20261004-WA0034.jpg"):
        "Bozza del badge del comitato (opzione 4 del sondaggio): logo "
        "\"COMITATO FESTA\" in rosa e bianco su sfondo giallo, logo arcade "
        "\"1987\", nome \"EMILIO\" in corsivo su riquadro bianco.",
    (DATE, "14:29", "Alessandra Toracchio", "IMG-20261004-WA0035.jpg"):
        "Bozza del badge del comitato (opzione 5 del sondaggio, la più votata): "
        "logo \"COMITATO FESTA\" in nero e rosa su sfondo giallo, logo arcade "
        "\"1987\", nome \"EMILIO\" in grassetto su riquadro bianco.",
    (DATE, "15:16", "Alessandra Toracchio", "IMG-20261004-WA0039.jpg"):
        "Foto di un foglio con l'elenco scritto a mano dei nomi dei membri per "
        "cui fare il badge, da controllare perché manca qualcuno.",
    (DATE, "15:28", "Antonio Aceto", "IMG-20261004-WA0038.jpg"):
        "Terza versione della locandina della gita della Classe 1987 a "
        "Corinaldo: \"La gita si terrà domenica 8 novembre 2026\", presso la "
        "casa di Santa Maria Goretti, con la scritta \"seguiranno i dettagli "
        "del viaggio\".",
}

# Badge già digeriti alle 12:27-12:33 (stessi file rimandati nel sondaggio delle
# 14:28): duplicati, scartati per non ripetere lo stesso contenuto.
_SKIP_MEDIA = {
    ("14:28", "IMG-20261004-WA0014.jpg"),
    ("14:28", "IMG-20261004-WA0015.jpg"),
    ("14:28", "IMG-20261004-WA0017.jpg"),
}


def _extra_skip(time_, fname):
    return (time_, fname) in _SKIP_MEDIA


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="badge duplicati del sondaggio")
