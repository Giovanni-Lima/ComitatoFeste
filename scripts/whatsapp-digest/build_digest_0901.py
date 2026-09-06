#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-01 — solo dati di curatela, logica comune in digest_lib.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-01"

CURATED = {
    ("05:32", "Dante Caniglia"): ("info",
        "Buongiorno: ora che il comitato è partito, propone di iniziare a pensare alla data di "
        "costituzione del direttivo e di trovare un programma comune (es. Notion o Google Sheet) per "
        "non perdere le idee discusse in chat."),
    ("10:06", "Antonio Aceto"): ("info",
        "Propone un addobbo luminoso davanti alla chiesa di Santa Maria Goretti con colombe bianche "
        "come simbolo di purezza e innocenza (condivide anche un'immagine di esempio)."),
    ("10:09", "Emidio Cerasani"): ("info",
        "Riferisce che Don Enzo vuole che l'addobbo davanti alla chiesa rispetti uno stile adeguato "
        "all'edificio di culto; ne parlerà meglio quando si incontreranno."),
    ("10:26", "Ilenia Piccozzi"): ("info",
        "I fiori per l'addobbo li lascia la classe '86 (riferito da Anna)."),
    ("10:47", "Emidio Cerasani"): ("info",
        "Chiarisce: si sta parlando dell'addobbo del \"cielo\" davanti a Santa Maria Goretti per le "
        "feste di agosto 2027, non di Natale."),
    ("11:11", "Ilenia Piccozzi"): ("info",
        "I fiori dell'addobbo non si tolgono: se non si rovinano si riutilizzano, altrimenti li "
        "ricompra il comitato; a Natale non si usano."),
    ("11:14", "Antonio Aceto"): ("domanda",
        "Chiede a Elvis, in vista delle nuove dime per l'infiorata, di farne una a forma di colomba "
        "per richiamare l'addobbo di Santa Maria Goretti, e propone uno sfondo giallo (richiamo alle "
        "magliette) invece che bianco."),
    ("11:15", "Elvis Ippoliti"): ("info",
        "Risponde che faranno insieme il disegno prima di tagliare le nuove dime."),
    ("11:26", "Maria Buttari"): ("info",
        "Prima di cambiare le dime dell'infiorata, ricorda di sentire Simonetta, che le realizza da "
        "30 anni, per non offenderla e mantenere buoni rapporti con tutti."),
    ("11:27", "Elvis Ippoliti"): ("info",
        "Rassicura: ne ha già parlato con Simonetta all'infiorata ed era d'accordo."),
    ("11:29", "Maria Buttari"): ("domanda",
        "Propone di chiedere al parroco se l'infiorata si può fare colorata, per rispettare tutti i "
        "canoni."),
    ("12:00", "Elvis Ippoliti"): ("info",
        "Mostra una bozza veloce dell'infiorata con le nuove dime, da rifinire tutti insieme in "
        "seguito — immagine esclusa da WhatsApp dall'export, non recuperabile."),
    ("12:07", "Elvis Ippoliti"): ("info",
        "Dettagli tecnici sull'infiorata: si possono usare anche meno fiori visto che il montaggio è "
        "comunque veloce; va rivista la divisione delle dime, perché il rosone centrale verrà "
        "spaccato a metà."),
    ("12:11", "Elvis Ippoliti"): ("info",
        "I fiorellini nella bozza sono sui 30 cm, forse anche più piccoli di quelli usati quest'anno."),
    ("12:16", "Elvis Ippoliti"): ("info",
        "Il problema vero per l'infiorata è colorare tutta la sabbia del fondo di giallo (servirebbero "
        "2-3 metri cubi secondo Emilio Caniglia): da vedere quanto costa."),
    ("12:41", "Tina Giarrante"): ("info",
        "Propone pochi spari/fuochi d'artificio, sia per il costo sia per rispetto degli animali."),
    ("12:47", "Maria Buttari"): ("info",
        "Propone di sostituire i fuochi d'artificio con uno spettacolo di droni: originale, mai fatto "
        "dalle altre classi."),
    ("12:49", "Elvis Ippoliti"): ("info",
        "Fa notare che i droni probabilmente non fanno risparmiare, anzi potrebbero costare di più dei "
        "fuochi."),
    ("12:54", "Luca Cicchelli"): ("decisione",
        "Ricorda ai ragazzi del gruppo di completare entro domenica il \"lavoretto\" a Santa Maria "
        "Goretti."),
    ("13:23", "Maria Buttari"): ("info",
        "Riassunto dei temi della mattinata per chi si è perso i messaggi: addobbo della chiesa con "
        "le colombe, nuove dime per l'infiorata, sabbia gialla e fuochi d'artificio ridotti o "
        "sostituiti con i droni."),
    ("13:40", "Dante Caniglia"): ("decisione",
        "Ribadisce l'idea di creare una struttura su un programma condiviso, così le idee e le "
        "soluzioni restano scritte e salvate per tutti."),
    ("13:51", "Costantino Mariani"): ("info",
        "Valuta i costi di un cantante famoso per l'evento: si aggirerebbero sui 600-700 mila euro "
        "(cachet, palco, luci), servirebbe un palco enorme e comunque non farebbe le piazze piccole — "
        "idea scartata per costi insostenibili."),
    ("13:57", "Dante Caniglia"): ("domanda",
        "Chiede al presidente Emilio se sa creare un Google Calendar condiviso e un progetto aperto "
        "su NotebookLM."),
    ("14:02", "Costantino Mariani"): ("domanda",
        "Chiede quando e dove si farà la riunione di persona."),
    ("14:06", "Costantino Mariani"): ("domanda",
        "Chiede quando si andrà a spostare la statua."),
    ("14:08", "Emilio Caniglia"): ("info",
        "Segnala che il Google Drive condiviso per il discorso non ha ancora ricevuto accessi o "
        "modifiche da parte del gruppo."),
    ("14:09", "Emilio Caniglia"): ("info",
        "Don Enzo non c'è; Emilio è in contatto con Osvaldo e farà sapere a breve."),
    ("16:02", "Emilio Caniglia"): ("decisione",
        "Propone di creare, per ogni iniziativa, delle squadre di 4-5 persone responsabili "
        "dell'organizzazione, con tutto il Comitato a supporto, per evitare confusione e lungaggini "
        "(esempio: come per l'infiorata o per le calze della Befana)."),
    ("16:15", "Elvis Ippoliti"): ("info",
        "Ribadisce che serve una lista/roadmap di tutto ciò che c'è da fare, con un modo semplice per "
        "far interagire tutti senza perdere idee e date degli eventi."),
    ("16:15", "Alessandro Di Benedetto"): ("domanda",
        "Propone di riunirsi per buttare giù idee e programmi: sul gruppo va bene il confronto, ma le "
        "scelte vanno concretizzate in riunione di persona."),
    ("16:19", "Dante Caniglia"): ("decisione",
        "Prima di ogni iniziativa, propone di parlare con il sindaco e con gli enti coinvolti (ex "
        "Misericordia, Pro Loco), prendendo i contatti e capendo come lavorano, così da avere il loro "
        "supporto."),
    ("16:20", "Emilio Caniglia"): ("info",
        "Sta preparando un bilancio di previsione delle entrate basandosi sui dati della classe '82: "
        "farà una media per ogni voce, da usare come stima di budget."),
    ("16:24", "Alessandra Toracchio"): ("info",
        "Segnala che è disponibile il rustico dietro casa di sua nonna per sabato sera, con qualche "
        "limite (bisogna portare da bere, vicini poco discreti)."),
    ("16:27", "Maria Buttari"): ("info",
        "Riepilogo degli eventi principali proposti: gita a Corinaldo (ottobre), Sant'Antonio "
        "(gennaio), San Gabriele (febbraio), feste patronali di giugno (San Vincenzo), feste d'agosto "
        "con cantante e Santa Maria Goretti; più eventi aggiuntivi per raccogliere fondi: Halloween o "
        "San Martino, Casa di Babbo Natale e Befana, Capodanno, Carnevale, caccia alle uova o altro "
        "per Pasqua."),
    ("16:40", "Luca Cicchelli"): ("domanda",
        "Chiede se si può richiedere alla classe '86 il programma di quest'anno (cartaceo o digitale), "
        "da copiare/modificare e poi passare anche all'88."),
    ("16:55", "Dante Caniglia"): ("info",
        "Condivide un esempio (\"almeno per iniziare\") — immagine esclusa da WhatsApp dall'export, "
        "non recuperabile."),
    ("17:39", "Luca Cicchelli"): ("info",
        "Ricorda di non dimenticare Halloween nel programma degli eventi."),
    ("18:18", "Emanuele Sciarra"): ("info",
        "Propone di organizzare la gita a Nettuno, dove morì Santa Maria Goretti, perché quest'anno "
        "si dovrebbe ufficializzare il gemellaggio."),
    ("18:31", "Emanuele Sciarra"): ("info",
        "Indicazioni sui tempi: a gennaio si cercano sponsor, da inizio marzo si potrebbe iniziare a "
        "vendere se tutto è pronto — gli '86 avevano già iniziato a vendere a fine marzo."),
    ("19:08", "Dante Caniglia"): ("info",
        "Si propone di organizzare in autonomia due iniziative: un torneo di braccio di ferro e un "
        "raduno di auto preparate, oppure in alternativa un torneo di powerlifting."),
    ("19:10", "Emanuele Sciarra"): ("domanda",
        "Chiede se qualcuno ha una macchina polaroid, con l'idea di vendere foto istantanee a tema "
        "\"Santa Maria Goretti 2027\" (con cornice fatta a mano) durante l'evento."),
    ("19:26", "Dante Caniglia"): ("domanda",
        "Solleva un dubbio legale: chi dà l'autorizzazione a vendere (foto, magliette, bandane ecc.)? "
        "Nota che gli '86 hanno venduto le bandane senza fare scontrini."),
    ("19:32", "Alessandra Simonetti"): ("decisione",
        "Propone di puntare su eventi a poca spesa e massima resa, come la lotteria di San Gabriele "
        "con premi offerti dalle attività locali (macelleria, pizzerie): il comitato non ci rimette "
        "nulla, entrano solo i soldi dei biglietti."),
    ("19:32", "Emanuele Sciarra"): ("domanda",
        "Chiede a Dante se conosce i vecchi gestori del lago Vetoio (L'Aquila), in vista di un "
        "possibile evento lì."),
    ("19:33", "Dante Caniglia"): ("info",
        "Non li conosce direttamente, ma potrebbe chiedere al suo ex cognato, falconiere, che li "
        "conosce."),
    ("20:35", "Luca Cicchelli"): ("info",
        "Sull'idea delle foto polaroid: è profitto puro, perché chi non vuole la foto non la paga e "
        "viene cancellata — bisogna solo coprire il costo delle cartucce."),
    ("20:54", "Luca Cicchelli"): ("info",
        "Segnala che l'anno prossimo arrivano gli alpini a San Benedetto: un'occasione da sfruttare."),
    ("20:57", "Emidio Cerasani"): ("info",
        "Il gemellaggio con Nettuno nacque grazie alla corale polifonica Marruvium, che purtroppo ora "
        "non esiste più."),
    ("21:46", "Chiara Gargano"): ("info",
        "Sul prezzo delle cartucce polaroid: conferma che il prezzo indicato è corretto (anche se un "
        "po' care), e ritiene l'idea delle foto valida — potrebbero piacere alle persone."),
    ("21:51", "Chiara Gargano"): ("info",
        "Ha lei stessa una polaroid; le cartucce costano dai 50 ai 150€ a seconda di quantità/qualità; "
        "propone di rivendere le foto a 5€ ciascuna, con un selfie incluso e i tag social per farsi "
        "pubblicità."),
    ("21:57", "Luca Cicchelli"): ("domanda",
        "Propone, invece della solita auto, una moto come primo premio della lotteria."),
    ("22:10", "Alessandra Simonetti"): ("info",
        "Riferisce che a Corinaldo si fa la lotteria che \"fa cassa\": bisogna iniziare ad attivarsi "
        "per questo evento, il più imminente."),
    ("22:12", "Alessandra Simonetti"): ("domanda",
        "Chiede se, non chiudendo il conto e non cambiando la P.IVA, ci sono degli incentivi "
        "disponibili."),
    ("22:13", "Costantino Mariani"): ("info",
        "Risponde: bisogna vedere se il comitato precedente appoggia la cosa e se il parroco è "
        "d'accordo; il bilancio si chiude comunque a fine anno; probabile che, come per Pescina, la "
        "P.IVA resti la stessa cambiando solo amministratori e soci."),
    ("22:24", "Costantino Mariani"): ("decisione",
        "Invita il gruppo a informarsi bene sull'aspetto fiscale/legale prima di procedere."),
    ("22:28", "Emanuele Sciarra"): ("decisione",
        "Propone di vedersi sabato sera, se possibile, per spiegare bene cosa gli ha detto Antonio; "
        "altrimenti domani o giovedì per la statua, spiegando tutto a Emilio Caniglia che poi farà da "
        "tramite col gruppo."),
    ("22:34", "Costantino Mariani"): ("info",
        "Condivide informazioni su un possibile finanziamento a fondo perduto: fino al 50% delle "
        "spese ammissibili (massimo 20.000€, quindi fino a 10.000€), con scadenza domande il 30 "
        "ottobre 2026; possibili anche altri fondi regionali per il turismo tramite bandi (con "
        "screenshot allegati)."),
    ("23:13", "Alessandro Di Benedetto"): ("domanda",
        "Chiede di preparare un riassunto per la riunione."),
}

MEDIA_OVERRIDES = {
    (DATE, "10:06", "Antonio Aceto", "IMG-20260901-WA0037.jpg"):
        "Immagine di esempio (mockup) dell'addobbo proposto: la chiesa di Santa Maria Goretti di "
        "notte, con luci, drappi bianchi, colombe e una croce luminosa sospesi sulla strada davanti "
        "all'ingresso.",
    (DATE, "11:17", "Antonio Aceto", "IMG-20260901-WA0042.jpg"):
        "Foto di riferimento di un'infiorata già esistente (tappeto di fiori giallo con motivo a "
        "grappoli d'uva, in un vicolo), condivisa come esempio di stile/colori per la nuova infiorata.",
    (DATE, "18:01", "Dante Caniglia", "IMG-20260901-WA0091.jpg"):
        "Schema/mappa mentale \"Calendario Eventi 2026-2027 Comitato Classe 1987\": elenco mese per "
        "mese di tutti gli eventi proposti (da ottobre 2026 ad agosto 2027: gita a Corinaldo, "
        "Halloween, San Martino, Natale, Capodanno, Befana, Sant'Antonio, Carnevale, San Gabriele, "
        "Pasqua, feste patronali di giugno, feste d'agosto con cantante e Santa Maria Goretti) più le "
        "collaborazioni strategiche da attivare (Don Renzo, Pro Loco, Misericordia) — bozza di "
        "roadmap complessiva.",
    (DATE, "18:51", "Dante Caniglia", "IMG-20260901-WA0125.jpg"):
        "Screenshot di un post Facebook del Comitato Classe 1986 su un concerto (\"The Kolors\") con "
        "foto aeree della piazza gremita, condiviso come esempio del tipo di evento/comunicazione "
        "social di un'altra classe.",
    (DATE, "22:20", "Costantino Mariani", "IMG-20260901-WA0180.jpg"):
        "Screenshot di una ricerca su bandi regionali (Abruzzo compresa) per la valorizzazione delle "
        "tradizioni locali: contributi a fondo perduto fino al 50% delle spese ammissibili per "
        "concerti, spettacoli e manifestazioni, più eventuali contributi comunali — a supporto del "
        "punto successivo sul finanziamento.",
    (DATE, "22:24", "Costantino Mariani", "IMG-20260901-WA0179.jpg"):
        "Screenshot con i dettagli del bando regionale: copertura fino al 50% delle spese ammissibili "
        "nel bilancio preventivo della festa, scadenza domande 30 ottobre 2026, modalità di "
        "partecipazione tramite la FIRA (Finanziaria Regionale Abruzzese).",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES)
