#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-08 — solo dati di curatela, logica comune in digest_lib.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-08"

CURATED = {
    ("11:55", "Emilio Caniglia"): ("info",
        "Riepiloga gli aggiornamenti in attesa della riunione con Don Enzo: acquisiti tutti i "
        "preventivi per la visita a Corinaldo (da valutare), in perfezionamento l'incontro con "
        "l'azienda dei materassi per il 18 settembre, nate due nuove app, disponibilità di una "
        "sede segnalata da Elvis Ippoliti (da valutare), acquisiti i dati dei precedenti comitati "
        "(utili per una stima sommaria), e da avviare l'organizzazione di un evento per Halloween."),
    ("12:06", "Emanuele Sciarra"): ("info",
        "Racconta di essere uscito da un colloquio col sindaco, che gli ha dato la PEC per "
        "richiedere la sala comunale e confermato che per venerdì 18 settembre non ci sono "
        "problemi; propone di inviare subito una email formale per assicurarsi la sala, "
        "all'indirizzo PEC: Protocollosdm@pec.it."),
    ("12:08", "Emilio Caniglia"): ("info",
        "Annuncia che il Comitato crescerà ancora, con nuovi ingressi in arrivo."),
    ("13:15", "Emanuele Sciarra"): ("proposta",
        "Propone di chiedere una collaborazione al gestore del locale \"Il Ragno\": lui offre "
        "cocktail e porta gente all'evento, il comitato incassa gli ingressi. L'idea viene però "
        "ritirata subito dopo (13:17, \"Allora come non detto\") quando Elvis Ippoliti fa notare "
        "che il locale resterà aperto fino al 31 e farà una propria festa di chiusura."),
    ("13:19", "Elvis Ippoliti"): ("info",
        "Segnala che da settembre il locale \"Il Ragno\" non sarà più gestito da Gianvito ma da "
        "Pasqualino Caniglia: possibile parlarne per collaborazioni future, oltre che con altre "
        "attività del paese."),
    ("14:31", "Emilio Caniglia"): ("proposta",
        "Apre un sondaggio per scegliere il giorno della prossima riunione della classe (luogo "
        "da definire), con voto aperto a chi è disponibile per entrambe le date: "
        "\"Riunione Classe 1987\" — OPZIONE: Venerdì 11 settembre (15 voti); "
        "OPZIONE: Sabato 12 settembre (8 voti) — snapshot dei voti al momento dell'export, "
        "il sondaggio resta aperto."),
    ("14:51", "Cesare Raglione"): ("domanda",
        "Chiede se, nonostante il 18 settembre ci sia anche un evento organizzato dalla Proloco, "
        "si riuscirà comunque a portare gente all'evento dei materassi."),
    ("15:17", "Antonio Aceto"): ("info",
        "Risponde che dipende da che evento fa la Proloco, ma che per l'evento materassi "
        "servirebbero 10 coppie e che, contando solo i membri della classe, sono già di più."),
    ("15:44", "Ilenia Piccozzi"): ("proposta",
        "Propone di organizzare l'evento di Halloween come si fa di solito per la Befana: in "
        "piazza se il tempo lo permette (altrimenti in palestra), con animazione e un piccolo "
        "contributo economico da parte di ogni bambino partecipante."),
    ("16:22", "Emilio Caniglia"): ("info",
        "Conferma che reperire zucche a basso costo non dovrebbe essere un problema e propone "
        "di pensare anche a un contest a tema."),
    ("16:23", "Elvis Ippoliti"): ("proposta",
        "Propone di creare un villaggio a tema horror (sullo stile di un villaggio di Babbo "
        "Natale ma per Halloween, mai fatto prima), con giochi a tema pensati per i più piccoli "
        "e le famiglie."),
    ("16:33", "Ilenia Piccozzi"): ("info",
        "Chiarisce che Halloween, essendo una festa pagana, è di solito organizzata dalla "
        "Proloco, mentre San Martino (con le zucche) potrebbe essere organizzata dal comitato; "
        "propone comunque di chiedere alla Proloco di poter organizzare anche Halloween."),
    ("16:35", "Elvis Ippoliti"): ("proposta",
        "Propone di dedicare San Martino a un evento pensato per gli adulti (in occasione del "
        "vino novello), dato che i bambini di oggi conoscono poco questa festa mentre Halloween "
        "avrebbe più affluenza; suggerisce di approfondire il tema alla riunione."),
    ("16:43", "Elvis Ippoliti"): ("info",
        "Ricorda al gruppo che, a livello formale, sono ancora una \"classe\" e non un comitato "
        "costituito."),
    ("17:27", "Dante Caniglia"): ("proposta",
        "Propone di affittare una escape room a tema per Halloween."),
    ("18:47", "Dante Caniglia"): ("proposta",
        "Propone di dedicare un evento a Papa Bonifacio VIII, nato a San Benedetto e che istituì "
        "a livello mondiale la festa di Ognissanti/il Giubileo: un evento mai fatto prima, per "
        "\"riprendersi\" qualcosa che appartiene alla città. Condivide un video di riferimento: "
        "https://youtu.be/Ol9qiTMEqqE?is=_g44oU1x57WlqXxT"),
    ("18:55", "Barbara Rizio"): ("proposta",
        "Propone di realizzare una scenografia a tema Famiglia Addams per foto ricordo a "
        "pagamento con i bambini."),
    ("18:57", "Elvis Ippoliti"): ("proposta",
        "Propone un percorso a tappe a tema Halloween, con casette \"paurose\", più punti per "
        "fare foto e bancarelle con gadget o caramelle."),
    ("19:06", "Alessandra Toracchio"): ("proposta",
        "Segnala che il negozio Action sta liquidando a basso prezzo articoli a tema Halloween "
        "e propone di comprarli il prima possibile per approfittare dei prezzi bassi, "
        "condividendo alcune idee semplici ed economiche realizzabili con poco."),
    ("20:24", "Dante Caniglia"): ("proposta",
        "Propone a Emanuele Sciarra di creare una community WhatsApp che riunisca il gruppo "
        "classe ed eventuali gruppi che se ne separeranno in futuro, per non avere gruppi "
        "sparsi; chiede di essere reso amministratore per farlo."),
    ("20:52", "Emanuele Sciarra"): ("decisione",
        "Conferma di aver reso Dante Caniglia amministratore e creato la community WhatsApp, "
        "come da lui proposto poco prima (\"Detto fatto\")."),
    ("20:55", "Emilio Caniglia"): ("info",
        "Riferisce di aver sentito la Proloco: anche loro organizzeranno qualcosa per Halloween, "
        "un evento itinerante a tappe per bambini, e si sono mostrati pienamente disponibili a "
        "una collaborazione. Resta da decidere se inserire qualcosa del comitato nel loro evento "
        "o organizzarsi autonomamente."),
    ("21:01", "Elvis Ippoliti"): ("proposta",
        "Segnala che la Proloco ha avuto la sua stessa idea; propone di valutare se convenga "
        "fare qualcosa insieme a loro o organizzare un evento diverso in autonomia."),
    ("21:28", "Emilio Caniglia"): ("info",
        "Dà il benvenuto a Raffaele Di Cesare, nuovo membro del Comitato entrato tramite la "
        "community WhatsApp appena creata."),
    ("21:59", "Emilio Caniglia"): ("info",
        "Dà il benvenuto anche a MariaLuisa Cianfaglione, nuovo membro del Comitato."),
}

MEDIA_OVERRIDES = {
    (DATE, "15:50", "Emanuele Sciarra", "IMG-20260908-WA0024.jpg"):
        "Foto di un biglietto della lotteria di beneficenza dell'associazione \"Forza e Coraggio "
        "Avezzano\", con l'elenco dei premi (un'automobile, un aspirapolvere, un viaggio, buoni "
        "acquisto) — condivisa come esempio, taggando Costantino Mariani.",
    (DATE, "18:49", "Costantino Mariani", "IMG-20260908-WA0034.jpg"):
        "Foto di una rotonda stradale in fase di costruzione, scattata dall'interno di un'auto "
        "(didascalia \"Altra rotonda\").",
    (DATE, "19:02", "Alessandra Toracchio", "IMG-20260908-WA0040.jpg"):
        "Screenshot di un'idea per Halloween trovata online: un pannello con cappelli da strega "
        "su cui lanciare anelli luminosi, come gioco a premi.",
    (DATE, "19:04", "Alessandra Toracchio", "IMG-20260908-WA0041.jpg"):
        "Screenshot di un'altra idea per Halloween trovata online: il gioco \"Zombie Eyeball "
        "Toss\", bicchieri a tema ragnatela in cui lanciare finti bulbi oculari.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
