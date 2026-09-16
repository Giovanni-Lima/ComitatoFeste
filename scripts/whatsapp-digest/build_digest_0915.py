#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-15 — solo dati di curatela, logica comune in digest_lib.py.

Prima giornata curata con la trascrizione anticipata dei vocali
(transcribe_new.py, vedi CLAUDE.md): tutti i vocali di questa finestra sono
già classificati in AUDIO_CURATED, letti col contesto della trascrizione.

Finestra 22:58 del 14/9 - 22:15 del 15/9 (aggiornata con l'export delle
22:15 del 15/9, che estende il giorno oltre le 14:37 della curatela
precedente). Mattina dominata dalla lista coppie/sponsor materassi (vedi
sotto); nel resto della giornata: Dante Caniglia (11:16) risponde alla
proposta del raduno auto d'epoca (10:06) suggerendo il Rotary Club o, in
alternativa, un raduno di auto elaborate tramite un amico di Vezzano;
Emanuele Sciarra (11:33) rilancia con l'idea di Attilio di distribuire
l'evento su più zone del paese coinvolgendo le attività locali. Un thread
sulle maglie del comitato rovinate da lavaggio/stiratura (Giacomo Gentile
12:42, foto di Elvis Ippoliti 12:55) resta un solo punto info + la foto, le
risposte successive (consigli di lavaggio, "ottimo"/conferme) sono rumore.
Tre vocali consecutivi di Emanuele (13:19-13:24) sviluppano un'unica
proposta di street food di 4 giorni prima di Santa Maria Goretti, con le
attività locali, evitando sovrapposizioni con bar/cocktail e specialità già
presenti. Ugo Trinchini (13:27) aggiunge due coppie alla lista (Angela e
Vincenzo di Ortucchio) e (13:42, vocale) comunica due sponsor trovati che
non vogliono comparire su biglietti/totem, chiedendo l'ok del gruppo.
Emanuele (14:31-14:34) condivide un link con contatti street-food e
comunica di aver reperito il numero di chi fa le fregne; Elvis (14:34)
suggerisce un'alternativa per procurarselo. Restano rumore: le varie
conferme brevi ("ottimo", "certo"), due vocali senza contenuto di Dante
(14:25) e uno screenshot di un evento quiz esterno di Costantino, non
legato al comitato.

Sera (19:15-22:15): un video di Elvis (19:17) è una GIF di reazione
mascherata da .mp4 (nessuna traccia audio, ffprobe), scartata in automatico
insieme alle battute testuali/vocali che lo accompagnano (rumore). Ugo
Trinchini (20:07) e Emanuele Sciarra (21:50) aggiungono altre coppie alla
lista del 18/9 (Pasquale e Elena; Christian e Asia), Raffaele Di Cesare
(20:56) ne aggiunge altre due (suo fratello con la moglie; Gino e Martina).
Emanuele (20:10-20:29) comunica altri 2 contatti per le serate materassi e
di essere alla ricerca di aziende di depuratori per serate simili,
stimando ~3000€ raccolti dal comitato con 6 serate totali (i commenti
scherzosi di Dante/Ugo che seguono sono rumore). Barbara Rizio (21:23)
chiede se sono state raggiunte le 20 coppie, Alessandra Simonetti conferma
di sì ricordando che resta da stabilire chi porta cosa; Emanuele (21:51,
con anche Elvis) chiede ad Alessandra Toracchio un resoconto completo, lei
risponde di essersi persa nel conteggio e che lo invierà la mattina dopo.
Un vocale di Emanuele (21:55) propone come ripartire l'acquisto di
bevande/tovaglioli/bicchieri per la prossima serata; una foto di Alessandra
Toracchio (22:01) mostra l'elenco definitivo di chi porta cosa per la
riunione materassi del 18/9, e lei stessa (22:02) comunica cosa è avanzato
dalla serata precedente (patatine, bibite) utile per quel buffet; Emanuele
(22:03) aggiorna il conteggio a 21 coppie. Il lungo scambio (22:07-22:22,
sette vocali) sul nome dialettale di un dolce fritto (nevole/ciarancell/
ferratelle/jarangelle, tra Antonio Aceto, Costantino Mariani, Dante
Caniglia) resta battuta di dialetto, scartato come rumore — coi vocali
tenuti come "rete di sicurezza" (placeholder, classificati poi dal
Transcriber). In coda: Emilio Caniglia (22:19) condivide la foto delle 20
coppie ora al completo; un avviso (22:29) chiede aiuto per recuperare la
sabbia colorata dell'infiorata il giorno dopo; Costantino Mariani (22:32)
chiede se arriverà una sponsorizzazione da un'azienda e suggerisce altri
potenziali sponsor (ristoranti della Marsica, banche); il resto (dolci di
carnevale/Natale, un "ci sto" di Antonio Aceto) è rumore. Un video di
Antonio Aceto (22:38, VID-20260916-WA0005.mp4) è una GIF di reazione
mascherata: niente ffprobe su questa macchina, verificata a mano
analizzando gli atom MP4 (nessun handler "soun"), scartata di conseguenza.
Nessuna menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-15"

CURATED = {
    ("07:28", "Ugo Trinchini"): ("info",
        "Chiede ad Alessandra Toracchio di aggiungere alla lista coppie per "
        "l'incontro del 18/9 anche Giovanni (istruttore) e Martina."),
    ("08:06", "Emanuele Sciarra"): ("info",
        "Chiede ad Alessandra Toracchio di aggiungere alla lista coppie anche "
        "il suocero Massimo e la moglie Eugenia; prova a portare oggi stesso "
        "anche i cognati, se riesce."),
    ("10:01", "Emilio Caniglia"): ("info",
        "Risponde a Ugo Trinchini che l'azienda di materassi si chiama "
        "Sanimed Italia, condividendo anche un link Facebook: "
        "https://www.facebook.com/share/1Dif7i9wtn/"),
    ("12:42", "Giacomo Gentile"): ("info",
        "Chiede a Dante Caniglia, Costantino Mariani e Ilenia Piccozzi di "
        "riportare le maglie del comitato: il lavaggio/stiraggio ha "
        "rovinato la stampa, per verificare insieme come risolvere."),
    ("13:27", "Ugo Trinchini"): ("info",
        "Comunica di poter aggiungere alla lista coppie per il 18/9 anche "
        "Angela e Vincenzo (amici di Ortucchio) e annuncia che in serata "
        "darà conferma per altre due coppie."),
    ("14:31", "Emanuele Sciarra"): ("info",
        "Condivide un link con alcuni contatti di attività di street food "
        "da valutare per l'evento (dice di doverlo recuperare perché lo ha "
        "già inviato altrove): https://share.google/jo6H785fmdrE1JAGL"),
    ("14:33", "Emanuele Sciarra"): ("info",
        "Comunica di aver recuperato il numero di telefono della persona "
        "che prepara le fregne, da contattare per lo street food."),
    ("14:34", "Elvis Ippoliti"): ("info",
        "Suggerisce che per procurarsi quel numero si può chiedere anche a "
        "Domenica Paperone, amica della persona in questione."),
    ("20:07", "Ugo Trinchini"): ("info",
        "Chiede a Emilio Caniglia di aggiungere alla lista coppie per il "
        "18/9 anche Pasquale e Elena."),
    ("20:10", "Emanuele Sciarra"): ("info",
        "Comunica di aver trovato altri 2 contatti per le serate materassi "
        "(oltre a quelle già in corso) ed essere alla ricerca di aziende di "
        "depuratori per organizzare serate simili a casa delle coppie (al "
        "momento già 2 disponibili). Stima che con 6 serate totali tra "
        "materassi e depuratori, anche nella peggiore delle ipotesi (500€ a "
        "serata), il comitato potrebbe raccogliere circa 3000€ senza "
        "sforzo, a fronte solo della seccatura di convincere le coppie a "
        "partecipare."),
    ("20:56", "Raffaele Di Cesare"): ("info",
        "Comunica due nuove coppie per l'incontro del 18/9: suo fratello "
        "con la moglie, e Gino con Martina."),
    ("21:23", "Barbara Rizio"): ("domanda",
        "Chiede se sono state raggiunte le 20 coppie per l'incontro del "
        "18/9; Alessandra Simonetti risponde di sì, ricordando che resta "
        "da stabilire chi porta cosa."),
    ("21:50", "Emanuele Sciarra"): ("info",
        "Comunica di aggiungere alla lista coppie per il 18/9 anche "
        "Christian e Asia."),
    ("21:51", "Emanuele Sciarra"): ("domanda",
        "Chiede ad Alessandra Toracchio un resoconto completo delle "
        "coppie; anche Elvis Ippoliti chiede l'elenco di chi porta cosa. "
        "Alessandra risponde di essersi persa nel conteggio e che invierà "
        "tutto la mattina dopo."),
    ("22:02", "Alessandra Toracchio"): ("info",
        "Comunica cosa è avanzato dalla serata precedente, utile per il "
        "buffet del 18/9: 8 buste di patatine, 1 Coca Cola, 1 tè e un "
        "quarto articolo che non ricorda con certezza (probabilmente "
        "aranciata)."),
    ("22:03", "Emanuele Sciarra"): ("info",
        "Aggiorna il conteggio delle coppie per il 18/9 a 21."),
    ("22:29", "Emilio Caniglia"): ("info",
        "Avviso per tutti i ragazzi: il pomeriggio del 16/9, tra le 17 e le "
        "17:30, la classe '86 lascerà la sabbia colorata avanzata per "
        "l'infiorata; Mike si rende disponibile col furgone per andarla a "
        "prendere, appuntamento davanti alla sede della classe '86."),
    ("22:32", "Costantino Mariani"): ("proposta",
        "Chiede se arriverà una sponsorizzazione da \"Kromoss\" e "
        "suggerisce di contattare come potenziali sponsor anche tutti i "
        "ristoranti della Marsica e le banche."),
}

AUDIO_CURATED = {
    (DATE, "08:59", "Emanuele Sciarra", "PTT-20260915-WA0003.opus"): ("info",
        "Comunica che restano da trovare quattro coppie per completare la "
        "lista del 18/9; farà sapere più tardi se riesce a rimediare."),
    (DATE, "09:37", "Ugo Trinchini", "PTT-20260915-WA0005.opus"): ("domanda",
        "Chiede conferma del nome della società di materassi (risponde poi "
        "Emilio Caniglia)."),
    (DATE, "10:04", "Emanuele Sciarra", "PTT-20260915-WA0006.opus"): ("info",
        "Conferma a Ugo Trinchini che il presidente lo ha già informato — "
        "era in riunione con Attilio — e che tocca proprio al turno di Ugo "
        "per la visita al materassaio."),
    (DATE, "10:05", "Ugo Trinchini", "PTT-20260915-WA0007.opus"): ("info",
        "Comunica che la coppia che aveva disponibile per la visita al "
        "materassaio è ormai \"bruciata\": ha acquistato lui stesso un "
        "materasso altrove, quindi non la propone."),
    (DATE, "10:06", "Emanuele Sciarra", "PTT-20260915-WA0008.opus"): ("proposta",
        "Propone di organizzare un raduno di macchine d'epoca a San "
        "Benedetto, da concordare col fidanzato di Alessandra Toracchio "
        "(che si occupa di veicoli d'epoca) — anche in ricordo di Mattia, "
        "appassionato di camion — con data ipotizzata in prossimità di "
        "Santa Maria Goretti per il maggior afflusso di pubblico; chiede il "
        "parere del gruppo."),
    (DATE, "10:07", "Emanuele Sciarra", "PTT-20260915-WA0009.opus"): ("info",
        "Rassicura Ugo Trinchini: i rappresentanti che seguono le coppie "
        "cambiano di volta in volta, quindi va bene lo stesso se qualcuno ha "
        "già acquistato — è già capitato l'anno scorso alla manifestazione "
        "materassi ed è anzi un incoraggiamento per gli altri clienti "
        "presenti."),
    (DATE, "11:16", "Dante Caniglia", "PTT-20260915-WA0010.opus"): ("info",
        "Risponde a Emanuele sul raduno di auto d'epoca: suggerisce di "
        "rivolgersi al Rotary Club, che organizza raduni di questo tipo da "
        "anni; in alternativa, se il Comune concede uno spazio, propone un "
        "raduno di auto elaborate tramite un amico di Vezzano."),
    (DATE, "11:33", "Emanuele Sciarra", "PTT-20260915-WA0011.opus"): ("proposta",
        "Risponde a Dante che si può fare, riportando che anche Attilio "
        "aveva pensato a un'idea simile: distribuire l'evento in più zone "
        "del paese (Domus, piazza, sotto la villa) coinvolgendo le attività "
        "locali, così il pubblico si sparge per il paese e ci sono più "
        "possibilità di guadagno."),
    (DATE, "13:19", "Emanuele Sciarra", "PTT-20260915-WA0012.opus"): ("proposta",
        "Propone, su idea nata parlando con la moglie, uno street food di "
        "quattro giorni (giovedì-domenica, prima di Santa Maria Goretti) "
        "coinvolgendo le attività del paese per la richiesta di occupazione "
        "del suolo pubblico: farla durare quattro giorni permette anche a "
        "loro di fare festa e guadagnare di più, a fronte di una quota per "
        "stand richiesta dal comitato più bassa."),
    (DATE, "13:21", "Emanuele Sciarra", "PTT-20260915-WA0013.opus"): ("proposta",
        "Precisa che nello street food andrebbe evitata la parte "
        "cocktail/bar per non danneggiare le attività già presenti (Serena, "
        "Enrico alla villa, il Jolly, il Ragno Su), puntando invece su cibo "
        "come pizza fritta o frittura al cartoccio."),
    (DATE, "13:24", "Emanuele Sciarra", "PTT-20260915-WA0014.opus"): ("proposta",
        "Suggerisce anche opzioni particolari viste ad altri eventi (tacos, "
        "ciambelle fritte con cioccolata), evitando sovrapposizioni con "
        "specialità già offerte da altre attività locali (es. arrosticini), "
        "e chiede il parere del gruppo sull'idea nel complesso."),
    (DATE, "13:42", "Ugo Trinchini", "PTT-20260915-WA0017.opus"): ("proposta",
        "Comunica di aver trovato un paio di aziende disposte a fare da "
        "sponsor per alcune centinaia di euro a testa, ma senza voler "
        "comparire su biglietti o totem; chiede l'ok del gruppo per "
        "procedere lasciando una semplice ricevuta."),
    (DATE, "21:55", "Emanuele Sciarra", "PTT-20260915-WA0030.opus"): ("proposta",
        "Propone che una persona si occupi di acquistare bevande, "
        "tovaglioli, bicchieri e patatine per la prossima serata "
        "(stimando una spesa totale di 50-60€, circa 3€ a testa "
        "considerando che le ragazze portano dolci fatti in casa, o circa "
        "5€ a testa tra i soli uomini) e che il costo venga poi ridiviso "
        "tra tutti i partecipanti; quanto avanza si riusa per le prossime "
        "serate."),
}

MEDIA_OVERRIDES = {
    (DATE, "08:55", "Emilio Caniglia", "IMG-20260915-WA0004.jpg"):
        "Foto aggiornata del foglio \"COPPIE\" per l'incontro del 18/9: 16 "
        "coppie compilate su 20 posti (nuove rispetto alla versione del "
        "14/9): Elvis-Federica, Raffaele-Verdiana, Ugo-Tina, Cesare-"
        "Alessandra S., Emanuele-Liberata, Maikel-Lucianny, Roberto-Dalila, "
        "Cesare-Costance, Antonio S.-Alessandra T., Silvano-Barbara, "
        "Vincenzo-Lara, Emilio-Antonella, Daniele-Jessica, Giovanni-Martina, "
        "Massimo-Eugenia, Donato-Onorina.",
    (DATE, "12:55", "Elvis Ippoliti", "IMG-20260915-WA0015.jpg"):
        "Foto della stampa su una maglia gialla del comitato (grafica di "
        "un cabinato arcade con la scritta \"INSERT COIN\"): la texture "
        "risulta leggermente sporca/opaca dopo il lavaggio, il problema "
        "segnalato nel thread sulle maglie rovinate.",
    (DATE, "22:01", "Alessandra Toracchio", "IMG-20260915-WA0031.jpg"):
        "Foto di un documento a schermo con l'elenco di chi porta cosa per "
        "la riunione materassi di venerdì 18/9 (buffet): Ugo vassoio "
        "dolci, Ale T bicchieri, Costantino 1 cassa d'acqua, Raffaele 2 "
        "Coca Cola, Barbara 2 torte salate, Tina vassoio per patatine, "
        "Emanuele 1 aranciata e 1 tè, Emilio tovaglioli, Costance nevole.",
    (DATE, "22:19", "Emilio Caniglia", "IMG-20260915-WA0039.jpg"):
        "Foto aggiornata del foglio \"COPPIE\" per l'incontro del 18/9: "
        "tutte le 20 coppie compilate (elenco completo, rispetto alla "
        "versione da 16/20 delle 8:55): Elvis-Federica, Raffaele-Verdiana, "
        "Ugo-Tina, Cesare-Alessandra S., Emanuele-Liberata, Maikel-"
        "Lucianny, Roberto-Dalila, Cesare-Costance, Antonio S.-Alessandra "
        "T., Silvano-Barbara, Vincenzo-Lara, Emilio-Antonella, Daniele-"
        "Jessica, Giovanni-Martina, Massimo-Eugenia, Donato-Onorina, "
        "Vincenzo-Angela, Pasquale-Elena, Gino-Martina, Christian-Asia.",
}

# .mp4 senza ffprobe su questa macchina (16/9/2026): verificato a mano che
# VID-20260916-WA0005.mp4 (22:38, Antonio Aceto) non ha traccia audio
# (nessun handler "soun" negli atom MP4) -> GIF di reazione mascherata,
# stesso trattamento di is_reaction_gif() ma deciso fuori da digest_lib
# perché qui ffprobe manca e la funzione, in sua assenza, non esclude nulla
# di default (fail-open).
_SKIP_FILES = {"VID-20260916-WA0005.mp4"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="GIF mp4 verificate a mano (niente ffprobe)")
