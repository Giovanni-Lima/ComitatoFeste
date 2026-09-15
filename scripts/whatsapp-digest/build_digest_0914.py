#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-14 — solo dati di curatela, logica comune in digest_lib.py.

Giornata parziale (fino alle 22:33 all'atto di questo export), densa: lungo
scambio — molto a colpi di vocali (decine di `PTT-*.opus`, tutti tenuti
come da regola) — sul **cachet del cantante big** e sul budget della festa
di agosto 2027.

Filo principale (13:18-15:09): si riprende il conteggio delle "coppie" per
l'incontro sponsorizzato di venerdì (Emanuele: "siamo arrivati a 20", 13:18);
Emilio Caniglia inquadra i numeri storici (budget 80/90k dei comitati
precedenti all'86, l'unica spesa variabile è il cachet del big che da solo
assorbirebbe tutto il budget, l'unica entrata variabile sono i biglietti
venduti, due entrate "insolite" avute in passato); Giovanni Lima condivide
una lista di cantanti papabili con stima cachet (trascritta per intero,
stesso criterio dei sondaggi — dato tabellare, non va riassunto); Emanuele
allega uno screenshot sul cachet di Achille Lauro. Molto rumore di contorno
(opinioni personali su prezzo/biglietti, tutte esplicitamente presentate
come tali — non curate singolarmente). Il tema scivola poi in una lunga
nostalgia sui cantanti del passato a San Benedetto (Anna Oxa, Venditti, i
Santo California — foto di Elvis di un loro concerto, allegata) — rumore.

Dentro la battuta sulla "mostra di animali" con finti nomi di stand
(Raffaele, 14:53-14:57) c'è un nocciolo vero: Dante Caniglia chiarisce che
le mostre ufficiali sono già regolamentate (Enci/Fci) ma una mostra
amatoriale sarebbe fattibile, e ne stava già parlando col padre per
organizzarla insieme alla benedizione degli animali — curato come proposta.

Segue una domanda di Dante sul mandato del comitato (se, essendo
gennaio-dicembre 2027, si possa generare budget anche dopo le feste estive)
con la risposta di Emanuele su un precedente concreto (The Kolors,
tempistiche di ingaggio/pagamento).

Coda pomeridiana/serale (16:34-20:25), ancora più densa di vocali:
autorizzata la sala consiliare del Comune per l'incontro sponsorizzato del
18/9 (Emilio, 16:34); prosegue il confronto budget/cachet (Dante chiede
cosa permise all'86 di "osare", Emilio risponde sulle entrate aggiuntive,
Ilenia e Antonio Aceto notano che l'aiuto comunale scala col nome
dell'artista, Emanuele porta il benchmark dell'85 — 15mila € per le 3
serate di giugno); Raffaele sintetizza la scelta di fondo (cantante
costoso + impegno massimo, o approccio sobrio) proponendo di deciderla per
alzata di mano in riunione; Dante rilancia proponendo di ripartire dal
file di Emilio puntando sulla maggiorazione della quota sponsor, poi di
mettere già la lista sponsor sui totem e farsi carico ciascuno di almeno
uno sponsor (sono in 38); Emilio conferma una lista di 250+ nominativi già
esistente, Costance allega il PDF con l'elenco aziende. Alessandra
Toracchio manda la lista coppie aggiornata (13 coppie, foto trascritta per
intero). Emilio condivide anche una tabella storica dettagliata
(questua/sponsor/biglietti/budget totale per classe 1982-1985, foto
trascritta per intero) e nota che il contributo sponsor è in calo negli
anni, probabilmente per la maggiore pressione sulla vendita biglietti —
da cui nasce una discussione etica sull'acquisto di blocchetti di
biglietti da parte di membri del comitato come forma di finanziamento
informale (Emilio la giudica discutibile e da evitare, Luca ricorda che è
sempre successo — fino a 1000€ a testa nell'86 — e la difende come prassi
comune); foto di alcuni biglietti di una lotteria della Proloco comprati
per gioco da Tina Giarrante. **Menzione di Giovanni Lima**
(regola 11/9/2026): Dante condivide la foto di un post Facebook di uno
sconosciuto influencer somigliante a Giovanni ("Sosia di Giovanni Lima",
20:15), Giovanni stesso risponde per le rime (20:25) — puro scherzo, non
genera un punto a parte oltre alla foto stessa.

Terza finestra (20:29-22:33): Alessandro Di Benedetto interviene con una
lunga argomentazione (20:35, ripresa poi alle 20:47/20:51/20:59/21:06/21:08)
sui criteri di scelta degli artisti — propone di definire tramite votazione
se puntare su valore artistico, popolarità o cachet, invitando a valutare
con lucidità senza confronti con altri comitati — curata come proposta
unica di sintesi. **Nota di trasparenza**: nella stessa finestra (20:41-20:53)
la discussione sull'etica dei biglietti del giorno prima degenera in un
confronto più acceso sul vincitore della lotteria della Proloco (Costance
si difende, Antonio Sabatini ed Elvis chiedono conferme sull'identità del
vincitore) — coerentemente con la richiesta dell'utente di rimuovere dal
digest il tema dell'estrazione della lotteria, questo scambio è stato
lasciato come rumore, non curato. Segue: Costantino Mariani propone di
iniziare già a contattare sponsor (21:32), Dante concorda e propone di
dividersi i compiti (21:34) — curato come proposta unica. Più tardi
Costantino chiarisce la logistica dei pagamenti sponsor: ricevuta semplice
ora, quella fiscale a gennaio, anche senza data per chi preferisce, oppure
bonifico (21:57-21:58) — curato come info, illustrato dalla foto di un
blocco ricevute generico allegata poco dopo (22:14). Chiude la finestra una
domanda di Costantino sulla sede (22:28). Elvis allega uno screenshot
dell'app Agenda del comitato con la didascalia (in dialetto) che il
problema dell'app è risolto (22:19) — nessuna nuova menzione di Giovanni
Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-14"

CURATED = {
    ("13:18", "Emanuele Sciarra"): ("info",
        "Comunica che per l'incontro sponsorizzato di venerdì siamo "
        "arrivati a quota 20 coppie."),
    ("14:07", "Emilio Caniglia"): ("info",
        "Inquadra i numeri storici: il budget dei comitati precedenti "
        "all'86 è stato di 80/90 mila euro, con cui bisognava coprire sia "
        "le feste di giugno che quelle di agosto."),
    ("14:10", "Emilio Caniglia"): ("info",
        "Spiega che le spese sono perlopiù costanti: l'unica voce "
        "davvero variabile è il cachet del cantante big, che a 80/90 "
        "mila euro assorbirebbe da solo l'intero budget."),
    ("14:12", "Giovanni Lima"): ("info",
        "Condivide una lista di cantanti papabili con stima del cachet e "
        "una nota di fattibilità (capienza max 20.000 persone, budget "
        "cachet max 80.000€): Bresh 60-80k (da provare); The Kolors "
        "60-80k (ottima scelta); Coma_Cose 45-65k (molto interessante); "
        "Tananai 60-80k+ (da verificare); Coez 50-70k (molto "
        "interessante); Rose Villain 60-80k (al limite); Rkomi 50-70k "
        "(da valutare); Olly 60-80k+ (probabile sforamento); Capo Plaza "
        "50-70k (interessante); Alex Britti 40-60k (più trasversale); "
        "Achille Lauro >80k (fuori budget, da considerare solo con "
        "budget superiore)."),
    ("14:13", "Emilio Caniglia"): ("info",
        "Spiega che sul fronte entrate l'unica vera variabile è il "
        "numero di biglietti venduti: la classe '85 fu la prima a "
        "passare da 20-25 mila a 40 mila biglietti, ma con questua e "
        "sponsor diminuiti il budget complessivo restò grosso modo "
        "invariato."),
    ("14:23", "Emilio Caniglia"): ("info",
        "Ricorda due entrate \"insolite\" avute in passato: una macchina "
        "non ritirata (differenza di 7-8 mila euro, precisa poi "
        "Costantino Mariani) e un aiuto dell'amministrazione comunale, "
        "oltre alla maggiorazione dei biglietti venduti."),
    ("14:55", "Dante Caniglia"): ("proposta",
        "Dentro la battuta sulla mostra di animali di Raffaele Di "
        "Cesare, chiarisce che le mostre ufficiali sono già "
        "regolamentate da Enci/Fci, ma che una mostra amatoriale "
        "sarebbe fattibile — ne stava già parlando col padre per "
        "organizzarla in concomitanza con la benedizione degli animali."),
    ("15:01", "Dante Caniglia"): ("domanda",
        "Chiede conferma: dato che il comitato è in carica da gennaio a "
        "dicembre 2027, si può generare budget anche dopo le feste "
        "estive? Se così fosse cambierebbe la prospettiva."),
    ("15:03", "Emanuele Sciarra"): ("info",
        "Risponde citando un precedente concreto: i The Kolors furono "
        "ingaggiati definitivamente a fine febbraio con i contatti presi "
        "già a gennaio; i pagamenti sono di solito a 60 giorni dalla "
        "fattura (precisa poi Dante Caniglia)."),
    ("16:34", "Emilio Caniglia"): ("info",
        "Comunica che sono stati autorizzati all'uso della sala "
        "consiliare del Comune per l'incontro sponsorizzato di venerdì 18 "
        "settembre; se riesce in serata prepara l'elenco delle coppie."),
    ("17:20", "Dante Caniglia"): ("domanda",
        "Chiede quali fossero i motivi/le certezze che permisero alla "
        "classe '86 di \"osare\" con un budget più alto."),
    ("17:20", "Emilio Caniglia"): ("info",
        "Risponde: alla media si può aggiungere un 20-30 mila euro tra "
        "aiuto del Comune e maggiorazione biglietti, ma anche così "
        "difficilmente si coprirebbe tutto."),
    ("17:22", "Ilenia Piccozzi"): ("info",
        "Avverte che il Comune dà il contributo solo se l'artista è di "
        "un certo livello: non correrebbe rischi altrimenti."),
    ("17:26", "Antonio Aceto"): ("info",
        "Conferma: l'aiuto comunale è proporzionale al nome dell'artista "
        "proposto — non è lo stesso proporre un nome locale o, per "
        "esempio, Achille Lauro."),
    ("17:29", "Emanuele Sciarra"): ("info",
        "Ricorda un benchmark storico: l'85 spese circa 15.000€ per le 3 "
        "serate di giugno, e a detta loro anche quello fu troppo."),
    ("17:48", "Raffaele Di Cesare"): ("proposta",
        "Sintetizza la scelta di fondo in due opzioni e propone di "
        "deciderla democraticamente per alzata di mano in riunione: "
        "rischiare un cantante costoso puntando a superare i 100mila con "
        "l'impegno massimo di tutti, oppure restare su un approccio più "
        "sobrio con l'impegno normale per organizzare l'evento."),
    ("17:54", "Dante Caniglia"): ("proposta",
        "Propone di ripartire dal file di Emilio come base, spostando "
        "l'attenzione su una maggiorazione della quota sponsor come leva "
        "per garantire il risultato."),
    ("17:58", "Dante Caniglia"): ("proposta",
        "Propone di mettere già la lista sponsor sui totem e iniziare a "
        "contattarli organizzando squadre o singoli, con l'obiettivo che "
        "ognuno dei 38 membri porti almeno uno sponsor a testa."),
    ("18:02", "Emilio Caniglia"): ("info",
        "Comunica che esiste già una lista sponsor di oltre 250 "
        "nominativi."),
    ("18:06", "Dante Caniglia"): ("info",
        "Ricorda che sarà disponibile anche l'app per caricare i loghi "
        "degli sponsor, pubblicità aggiuntiva per loro."),
    ("18:17", "Emilio Caniglia"): ("info",
        "Nota che il confronto dei dati storici mostra una diminuzione "
        "non trascurabile del contributo sponsor negli anni, "
        "probabilmente per la maggiore pressione sulle attività e "
        "l'aumento della vendita di biglietti."),
    ("18:20", "Emilio Caniglia"): ("info",
        "Solleva una questione etica: l'acquisto di biglietti in blocco "
        "da parte di membri del Comitato come forma di finanziamento è, "
        "a suo parere, una pratica discutibile da evitare — una "
        "considerazione personale e generale, precisa più tardi, non "
        "riferita al comitato attuale né a quelli passati."),
    ("18:29", "Luca Cicchelli"): ("info",
        "Riferisce, senza fare nomi, che membri e famiglie del Comitato "
        "'86 arrivarono a comprare fino a 1000€ di biglietti a testa; "
        "difende la prassi (\"l'unione fa la forza\") quando Emilio "
        "torna sul tema più tardi."),
    ("20:35", "Alessandro Di Benedetto"): ("proposta",
        "Propone di definire tramite votazione gli obiettivi e i criteri "
        "di scelta degli artisti da chiamare (valore artistico, "
        "popolarità o cachet), invitando a valutare con lucidità e senza "
        "confronti impliciti con altri comitati; sottolinea che non "
        "prenderebbero comunque in considerazione artisti di livello "
        "inferiore agli ultimi comitati, ma questo non implica investire "
        "le stesse somme, e che spesso cachet e popolarità non sono "
        "proporzionati al valore reale dell'artista."),
    ("21:32", "Costantino Mariani"): ("proposta",
        "Propone di iniziare già a bussare a qualche porta per gli "
        "sponsor; Dante Caniglia concorda (sentito prima il parere di "
        "Emilio) e propone di dividersi i compiti."),
    ("21:57", "Costantino Mariani"): ("info",
        "Chiarisce la logistica dei pagamenti sponsor: per ora si può "
        "procedere con una ricevuta semplice (anche senza data, per chi "
        "preferisce restare più tranquillo) e a gennaio si rilascia "
        "quella fiscale definitiva; in alternativa c'è chi farà un "
        "bonifico."),
    ("22:28", "Costantino Mariani"): ("domanda",
        "Chiede, in conclusione, come intendano muoversi riguardo alla "
        "sede."),
}

MEDIA_OVERRIDES = {
    (DATE, "14:29", "Emanuele Sciarra", "IMG-20260914-WA0018.jpg"):
        "Screenshot di una ricerca sul cachet di Achille Lauro: 40-60mila "
        "euro per una semplice ospitata, 70-100mila+ per un concerto "
        "completo. Didascalia di Emanuele: non lo vede fuori budget se si "
        "riuscisse a un prezzo di 70 mila euro.",
    (DATE, "14:39", "Emanuele Sciarra", "IMG-20260914-WA0025.jpg"):
        "Screenshot di un calendario personale (agosto 2027), condiviso "
        "verosimilmente per valutare disponibilità/date per gli eventi "
        "estivi — impegni personali non trascritti per riservatezza.",
    (DATE, "14:46", "Elvis Ippoliti", "IMG-20260914-WA0040.jpg"):
        "Foto di un concerto dal vivo de \"I Santo California\" (schermo "
        "col nome del gruppo sul palco), condivisa durante la "
        "conversazione nostalgica sui cantanti del passato a San "
        "Benedetto.",
    (DATE, "17:27", "Alessandra Toracchio", "IMG-20260914-WA0063.jpg"):
        "Foto di un foglio stampato \"LISTA COPPIE X IL 18\", 13 coppie "
        "compilate su 20 posti: Elvis-Federica, Raffaele-Verdiana, "
        "Tina-Ugo, Ale S-Cesare, Emanuele-Liberata, Micke-Lucianny, "
        "Costance-Cesare, Roberto-Dalila, Ale T-Antonio S, Barbara "
        "(senza coppia indicata), Vincenzo-Lara, Emilio-Antonella, "
        "Daniele-Gessica.",
    (DATE, "18:14", "Emilio Caniglia", "IMG-20260914-WA0079.jpg"):
        "Foto di cinque tabelle con relativi grafici, dati storici per "
        "classe (1982-1985): Offerte Comunità Giugno (15000 / 10567 / — "
        "/ 10000), Offerte Comunità Agosto (20000 / 18000 / — / 17000), "
        "Sponsor (24000 / 26330 / — / 22000), N. Biglietti (23000 / "
        "26900 / — / 40000), Totale Budget (82000 / 81797 / — / 89000) "
        "— dato aggregato delle entrate menzionato nel testo.",
    (DATE, "18:15", "Costance Rossi", "elenco aziende per contributo feste.pdf"):
        "Documento PDF: elenco aziende per il contributo alle feste "
        "(l'elenco sponsor già esistente citato nel testo).",
    (DATE, "18:49", "Tina Giarrante", "IMG-20260914-WA0112.jpg"):
        "Foto di alcuni biglietti di una lotteria della Proloco (\"Estate "
        "Lecco\", 1€ l'uno, primo premio un viaggio in Lapponia) — Tina "
        "scherza dicendo che se vince qualcosa lo offre al gruppo.",
    (DATE, "20:15", "Dante Caniglia", "IMG-20260914-WA0143.jpg"):
        "Foto di un post social di uno sconosciuto content creator, "
        "condivisa per scherzo perché somiglia a Giovanni Lima.",
    (DATE, "22:14", "Costantino Mariani", "IMG-20260914-WA0209.jpg"):
        "Screenshot di un'inserzione Amazon per un blocco di ricevute "
        "generiche (confezione da 5), a illustrazione della discussione "
        "in corso sulla logistica dei pagamenti sponsor.",
    (DATE, "22:19", "Elvis Ippoliti", "IMG-20260914-WA0208.jpg"):
        "Screenshot dell'app Agenda del comitato, allegato con la "
        "didascalia (in dialetto) che il problema dell'app è stato "
        "risolto.",
}

# VID-20260914-WA0210.mp4: nessuna traccia audio (ispezionati i box MP4 —
# 'vide'/'avc1' presenti, 'soun'/'mp4a' assenti, ffprobe non disponibile in
# questa sessione). GIF di reazione travestita da video, va scartata.
_REACTION_GIF_MP4 = {
    "VID-20260914-WA0210.mp4",
}


def _skip_reaction_gif_mp4(time_, fname):
    return fname in _REACTION_GIF_MP4


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES,
                 extra_skip_media=_skip_reaction_gif_mp4,
                 extra_skip_label="GIF di reazione .mp4 senza audio, escluse")
