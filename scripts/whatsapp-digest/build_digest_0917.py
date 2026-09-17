#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-09-17 — solo dati di curatela, logica comune in digest_lib.py.

Giornata breve (07:46-15:31), nessun vocale. Punti principali: Costance
Rossi (08:02) chiede se si trova una coppia sostitutiva per lei e il
marito Cesare, che non parteciperanno al 18/9; Emilio Caniglia (08:05)
annuncia i prossimi appuntamenti parrocchiali/comunitari (Sanimed Italia
il 18/9, l'incontro su San Francesco col Vescovo il 20/9, la peregrinatio
delle reliquie di San Camillo il 27/9), con le due locandine dei due
eventi di terzi; Raffaele Di Cesare (11:15) aggiorna sulle sue due
proposte (parete di arrampicata in iter, possibile problema procedurale;
escursioni approvate per il programma 2027 come "settimana verde");
Costantino Mariani (11:53) segnala un potenziale nuovo sponsor
(concessionario Perinetti, nuovi marchi auto); il thread sulla coppia
mancante si chiude nel pomeriggio (Emilio chiede conferma, Costance
confirma che mancheranno entrambi) e viene sostituita da Piero e Luisa,
proposti da Alessandro Di Benedetto (14:38) e già nell'aggiornamento
coppie delle 15:30. Barbara Rizio (15:15) comunica i costi di
riattivazione delle utenze (energia/gas). Resto rumore (saluti,
"buongiorno", un "Ottimo", due messaggi di sistema "ha fissato un
messaggio").

Coda pomeridiana/serale (aggiornata con l'export delle 23:19 del 17/9, che
estende il giorno oltre le 15:31): Dante Caniglia (17:20, vocale) rilancia
un'idea della sorella, presidente della Pro Loco — una festa in maschera
per Halloween, magari in collaborazione — e chiede se Emilio ne ha già
parlato con loro; comunica anche (17:58) che "Manuel" ha dato disponibilità
a fornire premi per le lotterie del comitato. Un video di Dante (17:56,
VID-20260917-WA0013.mp4) ha traccia audio (verificato a mano, niente
ffprobe su questa macchina) quindi è un video vero, non una GIF — ma senza
ffmpeg/cv2/altre librerie per estrarne un frame non è stato possibile
vederne il contenuto: tenuto con la didascalia generica di default,
segnalato a parte. In serata Emilio (21:07) riferisce di aver sentito la
Pro Loco (non hanno ancora programmazione chiara, ma sono aperti a
collaborare, con l'avvertenza che sarebbe laborioso e col ritorno
economico incerto); Dante (21:16) controbatte che collaborare comunque
converrebbe. Emilio (21:52) chiede idee concrete per un ritorno economico
da una festa di bambini in maschera: seguono proposte di Antonio Aceto
(vendita di dolciumi — ciambelle zuccherate, zucchero filato, mele
caramellate) ed Emanuele Sciarra (vendita di foto a tema, con Antonio che
rilancia un tema "Famiglia Addams" e l'idea di un calendario invece della
foto singola, che Emanuele giudica più adatto a Natale). Resto rumore
(commenti/battute brevi, l'assegnazione scherzosa "tu fai Mercoledì" a
Tina Giarrante). Nessuna menzione di Giovanni Lima in questa finestra.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-09-17"

CURATED = {
    ("08:02", "Costance Rossi"): ("domanda",
        "Chiede se si riesce a trovare una coppia sostitutiva per lei e "
        "suo marito Cesare, che non potranno partecipare all'incontro "
        "del 18/9."),
    ("11:15", "Raffaele Di Cesare"): ("info",
        "Aggiorna sulle sue proposte: per la parete di arrampicata ha "
        "avviato l'iter di richiesta, con un possibile problema "
        "procedurale dato che il richiedente sarebbe la sezione CAI di "
        "Teramo di cui è socio (i concedenti potrebbero obiettare che "
        "verrebbe usata lontano dalla sede) — problema da verificare, se "
        "emergesse proverà a risolverlo diplomaticamente; per le "
        "escursioni, la proposta è stata approvata e verrà inserita nel "
        "programma 2027 come \"settimana verde\", durante la quale si "
        "potranno organizzare eventi di qualsiasi difficoltà (trekking, "
        "arrampicata, sci) chiedendo ai partecipanti un'offerta per il "
        "comitato."),
    ("11:53", "Costantino Mariani"): ("info",
        "Comunica che da questa settimana il concessionario \"Perinetti\" "
        "vende anche i marchi Suzuki, Isuzu e Mitsubishi (potenziale "
        "nuovo sponsor)."),
    ("13:55", "Emilio Caniglia"): ("domanda",
        "Chiede a Costance Rossi se mancheranno entrambi lei e il "
        "marito, o solo uno dei due, all'incontro del 18/9."),
    ("14:14", "Costance Rossi"): ("info",
        "Conferma a Emilio Caniglia che mancheranno entrambi, lei e il "
        "marito Cesare."),
    ("14:38", "Alessandro Di Benedetto"): ("info",
        "Comunica di poter aggiungere alla serata di venerdì 18/9 suo "
        "fratello Piero e la cognata Luisa."),
    ("15:15", "Barbara Rizio"): ("info",
        "Aggiorna sui costi di riattivazione delle utenze: energia circa "
        "25€, gas circa 55€, la diminuzione di potenza è gratuita."),
    ("17:58", "Dante Caniglia"): ("info",
        "Comunica che \"Manuel\" ha dato disponibilità a fornire premi "
        "per qualunque lotteria organizzi il comitato."),
    ("21:07", "Emilio Caniglia"): ("info",
        "Riferisce di aver sentito la Pro Loco: non hanno ancora una "
        "programmazione chiara sugli eventi perché impegnati con altro "
        "di più immediato; per lui si può valutare una collaborazione se "
        "si trovano disponibilità, ma sarebbe qualcosa di laborioso e "
        "dispendioso, con un ritorno economico incerto per il comitato."),
    ("21:16", "Dante Caniglia"): ("info",
        "Controbatte a Emilio: pur avendo obiettivi diversi dalla Pro "
        "Loco, organizzare insieme porterebbe comunque un introito — se "
        "Halloween non lo fa nessuno non si guadagna nulla, farlo insieme "
        "a loro porterebbe qualcosa; ritiene la collaborazione "
        "necessaria in questo caso."),
    ("21:52", "Emilio Caniglia"): ("domanda",
        "Chiede idee concrete su come ottenere un ritorno economico da "
        "una festa di bambini in maschera per Halloween."),
    ("22:06", "Antonio Aceto"): ("proposta",
        "Propone di vendere dolciumi durante l'evento: ciambelle "
        "zuccherate, zucchero filato, mele caramellate."),
    ("22:08", "Emanuele Sciarra"): ("proposta",
        "Ribadisce l'idea, già proposta in passato, di vendere foto a "
        "tema scattate durante l'evento."),
    ("22:09", "Antonio Aceto"): ("proposta",
        "Rilancia sull'idea delle foto proponendo un tema \"Famiglia "
        "Addams\", offrendosi lui stesso per il ruolo di Zio Fester."),
    ("22:10", "Antonio Aceto"): ("proposta",
        "Propone di realizzare un calendario con le foto a tema, invece "
        "di vendere la semplice foto singola."),
    ("22:12", "Emanuele Sciarra"): ("info",
        "Conferma che si può comunque fare anche il calendario, ma "
        "ritiene che sotto Natale sarebbe più facile venderlo."),
}

AUDIO_CURATED = {
    (DATE, "17:20", "Dante Caniglia", "PTT-20260917-WA0012.opus"): ("proposta",
        "Rilancia un'idea di sua sorella, presidente della Pro Loco: "
        "organizzare una festa in maschera per Halloween, magari in "
        "collaborazione tra le due associazioni; chiede se Emilio ne ha "
        "già parlato con loro nella riunione con la Pro Loco."),
}

MEDIA_OVERRIDES = {
    (DATE, "08:05", "Emilio Caniglia", "IMG-20260917-WA0000.jpg"):
        "Locandina della Parrocchia San Benedetto Abate: evento \"San "
        "Francesco e il Vescovo dei Marsi\" domenica 20/9 alle 16:30 al "
        "Centro Pastorale San Cipriano, con la partecipazione del "
        "Vescovo di Avezzano Mons. Giovanni Massaro e altri relatori "
        "(organizzato dagli Amici Francesco di Assisi SBM). Condivisa "
        "insieme all'annuncio dei prossimi appuntamenti comunitari: "
        "l'incontro con Sanimed Italia del 18/9, questo evento del 20/9, "
        "e la peregrinatio delle reliquie di San Camillo del 27/9.",
    (DATE, "08:05", "Emilio Caniglia", "IMG-20260917-WA0001.jpg"):
        "Locandina della Diocesi di Avezzano - Parrocchia San Benedetto "
        "Abate: \"Peregrinatio delle reliquie del corpo di San Camillo\" "
        "domenica 27/9, con il programma della giornata (arrivo reliquie "
        "alle 9:30, messe alle 10:00 e alle 11:30, saluto finale alle "
        "15:30).",
    (DATE, "15:30", "Emilio Caniglia", "IMG-20260917-WA0011.jpg"):
        "Aggiornamento del foglio \"COPPIE\" per l'incontro del 18/9: la "
        "coppia Cesare-Costance viene sostituita da Piero-Luisa "
        "(fratello e cognata di Alessandro Di Benedetto); per il resto "
        "invariato, con le posizioni di Elvis e di Alessandro Di "
        "Benedetto stesso ancora incomplete.",
}

if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED)
