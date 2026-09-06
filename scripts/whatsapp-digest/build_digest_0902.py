#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-02 — solo dati di curatela, logica comune in digest_lib.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-02"

CURATED_SYSTEM = {
    "22:40": ("info",
        "Il gruppo WhatsApp è stato rinominato da \"Comitato feste 87\" a \"Il branco dei pazzi 87\" "
        "(rinominato da Emanuele Sciarra)."),
}

CURATED = {
    ("15:42", "Emilio Caniglia"): ("info",
        "Riepilogo per chi si è perso i messaggi: la maggior parte riguarda idee e proposte per "
        "eventi/iniziative del Comitato (dall'infiorata al prossimo cantante, dalle iniziative di "
        "Natale a quelle di Pasqua). Prossimo impegno: visita a Corinaldo ai primi di ottobre. In "
        "settimana si spera di avere dei preventivi per valutare fattibilità e margini di convenienza."),
    ("15:45", "Emilio Caniglia"): ("decisione",
        "Avviso solo per i ragazzi: domani (3/9) dopo cena, tra le 20:30 e le 20:45, appuntamento in "
        "Piazza per spostare le statue insieme a Osvaldo; si riposizionano entrambe le statue."),
    ("18:15", "Maria Buttari"): ("decisione",
        "Bisogna fare la riunione e vedere chi si candida, con le relative votazioni, per garantire a "
        "tutti il diritto di candidarsi e di votare (cariche del direttivo, incluso il ruolo di "
        "vicepresidente discusso poco prima)."),
    ("19:04", "Ugo Trinchini"): ("info",
        "Per lui va bene l'assetto attuale delle cariche, ma se qualcun altro vuole coprire altri "
        "ruoli va bene lo stesso: l'importante è il bene del gruppo a prescindere dal direttivo."),
    ("19:17", "Costantino Mariani"): ("info",
        "Propone come idea per un evento la \"gita alla Trinità\", con una lotteria organizzata "
        "durante il viaggio di andata."),
    ("19:24", "Luca Cicchelli"): ("domanda",
        "Chiede se organizzare Halloween: è una scelta del gruppo, si può anche non farlo; chiede "
        "idee e suggerimenti per valutare insieme."),
    ("20:35", "Luca Cicchelli"): ("domanda",
        "Chiede come funzionerebbe economicamente un'eventuale auto come primo premio della "
        "lotteria: se ci sono fondi/sconti dedicati o se i soldi per comprarla li deve mettere il "
        "comitato."),
    ("20:44", "Costantino Mariani"): ("info",
        "Propone come premi della lotteria un'auto e una stufa a pellet; si valuta se il rivenditore "
        "(Perinetti) può fare da sponsor."),
    ("21:09", "Dante Caniglia"): ("domanda",
        "Fa notare che vendere 50.000 biglietti in circa 2 mesi significherebbe 830 biglietti al "
        "giorno; chiede di valutare con realismo tempistica e impegno richiesto prima di puntare su "
        "quella cifra."),
    ("21:25", "Dante Caniglia"): ("decisione",
        "Propone di creare una App per il cellulare, da far scaricare in massa, con notifiche per "
        "ogni evento e un elenco di tutti gli enti di San Benedetto; si offre di svilupparla lui "
        "stesso."),
    ("21:30", "Costantino Mariani"): ("domanda",
        "Chiede se non si dovesse organizzare anche una cena del comitato (resta senza una risposta "
        "diretta nel seguito della chat)."),
    ("21:54", "Emanuele Sciarra"): ("info",
        "Preventivo per il bus: circa 1100-1200€ (fornitore indicato: Curzio); da confermare il "
        "giorno preciso."),
    ("21:59", "Luca Cicchelli"): ("domanda",
        "Chiede se serva creare una pagina Facebook dedicata per l'evento."),
    ("22:02", "Alessandra Simonetti"): ("decisione",
        "Propone di puntare su una lotteria a costo zero per il comitato, basata su donazioni."),
    ("22:06", "Alessandra Simonetti"): ("info",
        "Idea per i premi donati: prodotti di farmacia, patate offerte dal sindaco, vino dal Tigre — "
        "premi donati, senza spendere soldi del comitato."),
    ("22:06", "Luca Cicchelli"): ("info",
        "Propone di comprare oggetti economici da Action Avezzano da usare come premi della "
        "lotteria."),
    ("22:16", "Emanuele Sciarra"): ("decisione",
        "Decide di creare una pagina Facebook \"87\" e di pubblicare l'evento anche sul gruppo "
        "Facebook di San Benedetto, per iniziare; poi si amplierà gradualmente."),
    ("22:18", "Dante Caniglia"): ("info",
        "Si offre di sviluppare lui stesso l'app di San Benedetto (ha esperienza/corsi in merito); "
        "tempistica stimata: circa 14 giorni per la pubblicazione più 1 giorno per l'attivazione, "
        "quindi l'app potrebbe essere attiva verso metà novembre."),
    ("22:31", "Antonio Aceto"): ("decisione",
        "Si propone di iniziare lui la pagina Facebook: comincia a chiedere amicizie e a "
        "pubblicizzare la gita, in attesa che siano pronte le locandine."),
    ("22:36", "Costantino Mariani"): ("decisione",
        "Prima di procedere con le locandine bisogna riunirsi di persona: serve parlare con Don Enzo "
        "e mettersi d'accordo con il referente di Corinaldo, che deve organizzarsi a sua volta."),
    ("22:48", "Dante Caniglia"): ("domanda",
        "Chiede il nome definitivo da dare alla pagina Facebook, perché non sarà più modificabile "
        "per un mese; proposte in discussione: \"Comitato Feste San Benedetto classe 87\" (Emanuele) "
        "e \"Comitato Feste Patronali classe '87\" (Antonio) — nome non ancora deciso."),
    ("22:50", "Costantino Mariani"): ("domanda",
        "Richiede di nuovo quando si farà la riunione di persona."),
    ("22:52", "Dante Caniglia"): ("decisione",
        "Come immagine del profilo della pagina si userà il logo della maglietta (già votato come "
        "definitivo); come foto di copertina, per ora una foto del gruppo."),
    ("23:13", "Chiara Gargano"): ("info",
        "Condivide il logo definitivo del comitato in PDF (\"Logo Def 40 Export 2 Mod.pdf\") — file "
        "escluso da WhatsApp dall'export della chat, non recuperabile. La versione di stampa aveva "
        "un problema di pixellatura, risolto insieme a Giacomo."),
    ("23:39", "Chiara Gargano"): ("domanda",
        "Propone di provare a lanciare una campagna di crowdfunding, ma deve ancora riflettere su "
        "come impostarla."),
    ("23:40", "Alessandra Simonetti"): ("domanda",
        "Chiede se il comitato può rientrare nel bando del Consiglio Regionale (L.R. 55/2013, "
        "Abruzzo) che finanzia eventi culturali/tradizionali fino a 10.000€, con scadenza delle "
        "domande il 30 ottobre (dettagli condivisi poco prima in uno screenshot)."),
    ("23:40", "Antonio Aceto"): ("info",
        "Risponde a Chiara: prima serve avere qualche informazione da Don Enzo, poi si potrà "
        "realizzare la locandina con la data precisa."),
}

MEDIA_OVERRIDES = {
    (DATE, "22:45", "Chiara Gargano", "IMG-20260902-WA0125.jpg"):
        "Screenshot della vecchia pagina Facebook di classe \"Ragazzi.........FESTA???\", con vecchi "
        "post del gruppo dal 2012 al 2015 (proposte di riunioni, saluti) — la pagina che si sta "
        "valutando di riattivare.",
    (DATE, "22:45", "Chiara Gargano", "IMG-20260902-WA0126.jpg"):
        "Vecchia foto pubblicata sulla pagina Facebook di classe nel 2015 (\"Il diavolo e l'acqua "
        "santa\"), ritrovata riguardando i vecchi post della pagina da riattivare.",
    (DATE, "22:50", "Emanuele Sciarra", "IMG-20260902-WA0138.jpg"):
        "Screenshot di una ricerca Facebook \"comitato feste san benedetto\": pagine esistenti di altri "
        "comitati di classe (1986, 1985, 1983 ecc.), usata come riferimento per il nome/formato della "
        "nuova pagina.",
    (DATE, "23:39", "Alessandra Simonetti", "IMG-20260903-WA0000.jpg"):
        "Screenshot di una ricerca sul bando del Consiglio Regionale (L.R. 55/2013, Abruzzo): finanzia "
        "eventi culturali/tradizionali fino a 10.000€, domande entro il 30 ottobre — riferimento diretto "
        "alla domanda del messaggio successivo sulla scadenza del bando.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, curated_system=CURATED_SYSTEM)
