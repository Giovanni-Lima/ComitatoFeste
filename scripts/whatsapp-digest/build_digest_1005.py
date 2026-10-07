#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Digest del 2026-10-05 — solo dati di curatela, logica comune in digest_lib.py.

Finestra 08:03-14:19 (export Dropbox delle 17:02 del 5/10). Mattina: Antonio
Sabatini (08:03) precisa che i primi eventi promozionali hanno già fatto
incassare e che ci saranno altre occasioni fino a dicembre, chiedendo di
mantenere riservate le informazioni su alcuni ruoli del comitato fino
all'apertura di un conto corrente; Emanuele Sciarra (08:35) chiede di
ripubblicare i post di Facebook e Instagram. Il grosso della mattinata e del
primo pomeriggio riguarda la gita a Corinaldo dell'8 novembre: Elvis
Ippoliti chiede se la visita è al santuario di Santa Maria Goretti (la
locandina dice "presso la casa"), Serena Di Stefano spiega che si va sia alla
casa natale sia al santuario, Emanuele sente Don Enzo per il programma
(partenza verso le 6:30, arrivo verso le 10:30-11, messa, poi libertà) e
si parla di una locandina definitiva con il programma. Antonio Aceto e
Martina Del Gizzi chiariscono che il santuario di Santa Maria Goretti è a
Nettuno (più un santuario a Corinaldo, dove c'è la casa natale). Emanuele
e Raffaele condividono la locandina sui gruppi Facebook del comitato: la
pagina del comitato è in attesa di approvazione e non è facile trovare il
gruppo "San Benedetto No Censure Inside", su cui Emanuele non riesce a
cercare (vocali 13:07-14:19). Dante Caniglia (13:52) consiglia di
pubblicare con la pagina dentro i gruppi e di ricondividere sui profili
personali per farla crescere. Nessuna menzione di Giovanni Lima da parte di
altri in questa finestra.

Coda serale (17:30-18:21, export del 7/10): Dante (vocale) ribadisce la regola
di pubblicare le cose ufficiali con la pagina del comitato; Emanuele condivide
un video di calcio non legato al comitato.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from digest_lib import build_digest

DATE = "2026-10-05"

CURATED = {
    ("08:03", "Antonio Sabatini"): ("info",
        "Precisa che i primi eventi promozionali hanno già fatto incassare "
        "qualcosa e che fino a dicembre ci saranno altre occasioni di "
        "guadagno; chiede di mantenere riservate le informazioni su alcuni "
        "\"ruoli\" del comitato fino all'apertura di un conto corrente."),
    ("08:35", "Emanuele Sciarra"): ("info",
        "Invita tutti a ripubblicare i post che verranno pubblicati su "
        "Facebook e Instagram, per avere più visibilità sugli eventi."),
    ("11:14", "Elvis Ippoliti"): ("info",
        "Fa notare che il santuario sta a Nettuno ma c'è anche un santuario a "
        "Corinaldo; basta fare la locandina aggiornata con il programma."),
    ("13:06", "Raffaele Di Cesare"): ("info",
        "Segnala che la locandina è già stata condivisa nei gruppi di San "
        "Benedetto."),
    ("13:22", "Emanuele Sciarra"): ("domanda",
        "Chiede quali case o chiese ci siano a Corinaldo: dice di conoscerne "
        "solo una."),
    ("13:22", "Raffaele Di Cesare"): ("info",
        "Condivide due link di gruppi Facebook: "
        "https://www.facebook.com/share/g/14uHvS139nn/ e "
        "https://www.facebook.com/share/g/18SR9gLAHN/"),
    ("13:23", "Elvis Ippoliti"): ("info",
        "Segnala che il santuario Santa Maria Goretti è diventato un "
        "santuario nella versione della locandina che ha pubblicato."),
    ("13:23", "Emanuele Sciarra"): ("info",
        "Dice di essere in attesa di approvazione per uno dei due gruppi."),
    ("13:23", "Raffaele Di Cesare"): ("info",
        "Dice che sull'altro gruppo si può caricare senza attese."),
    ("13:30", "Emanuele Sciarra"): ("info",
        "Dice che non riesce a trovare il gruppo indicato da Raffaele."),
    ("13:31", "Raffaele Di Cesare"): ("info",
        "Suggerisce di cercare \"San Benedetto no censura inside\" e il "
        "risultato dovrebbe comparire."),
    ("13:31", "Elvis Ippoliti"): ("info",
        "Dice di aver pubblicato lui la locandina in questo gruppo."),
}

AUDIO_CURATED = {
    (DATE, "08:56", "Emanuele Sciarra", "PTT-20261005-WA0000.opus"): ("info",
        "Riferisce di aver sentito Emilio, che chiede di confermare il "
        "programma con don Enzo: l'85 ha un programma praticamente uguale; "
        "oggi si prova a sentire don Enzo su partenza (verso le 6:30), arrivo "
        "(verso le 10:30-11), messa e tempo libero, poi si fa subito la "
        "locandina e il viaggio."),
    (DATE, "11:08", "Antonio Aceto", "PTT-20261005-WA0002.opus"): ("info",
        "Spiega che ha scritto \"casa di Santa Maria Goretti\" perché su Google "
        "il santuario risultava a Nettuno, e lui era sicuro che a Corinaldo ci "
        "sia la casa."),
    (DATE, "13:52", "Dante Caniglia", "PTT-20261005-WA0014.opus"): ("info",
        "Ribadisce che non è la stessa cosa pubblicare nei gruppi con la pagina "
        "rispetto a farlo con il profilo personale."),
    (DATE, "14:19", "Emanuele Sciarra", "PTT-20261005-WA0016.opus"): ("info",
        "Dice di aver provato con la pagina, ma non riesce a ritrovare il link "
        "di Raffaele; nel gruppo di San Benedetto ha inviato la richiesta sia "
        "dal profilo personale sia da quello della pagina, in attesa di "
        "valutazione."),
    (DATE, "17:30", "Dante Caniglia", "PTT-20261005-WA0021.opus"): ("proposta",
        "Ribadisce la regola sulla pubblicazione: le cose ufficiali, nei "
        "gruppi ufficiali, vanno pubblicate sempre con la pagina del "
        "comitato, poi tutti ricondividono per la popolarità."),
}

TEXT_MERGES = [
    {
        "anchor_time": "08:37",
        "anchor_sender": "Elvis Ippoliti",
        "type": "info",
        "text": (
            "Chiede se la visita a Corinaldo non sia al santuario di Santa Maria "
            "Goretti, visto che la locandina dice \"presso la casa\". Serena "
            "Di Stefano risponde che a Corinaldo c'è anche la casa natale e che "
            "durante la giornata si andrà sia lì sia al santuario (la \"casa\" "
            "è la struttura, non un'abitazione). Elvis propone di indicare anche "
            "il santuario sulla locandina, perché la gita è con la chiesa; "
            "Emanuele Sciarra dice che il programma sarà nella locandina definitiva "
            "e propone di contattare subito don Enzo per il punto di partenza e "
            "il programma."
        ),
        "members": [
            ["08:37", "Elvis Ippoliti"],
            ["08:44", "Serena Di Stefano"],
            ["08:46", "Elvis Ippoliti"],
            ["08:47", "Emanuele Sciarra"],
            ["08:47", "Serena Di Stefano"],
            ["08:48", "Emanuele Sciarra"],
            ["08:51", "Elvis Ippoliti"],
        ],
    },
]

AUDIO_MERGES = [
    {
        "anchor_time": "12:55",
        "anchor_sender": "Martina Del Gizzi",
        "type": "info",
        "text": "Precisa che il santuario di Santa Maria Goretti sta a Nettuno; "
                "Costantino Mariani aggiunge che a Corinaldo ci sono la casa natale "
                "e la chiesa.",
        "members": ["PTT-20261005-WA0003.opus", "PTT-20261005-WA0007.opus"],
    },
    {
        "anchor_time": "13:07",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": "Dice che la pagina del comitato è in attesa di approvazione "
                "da parte degli amministratori del gruppo di San Benedetto.",
        "members": ["PTT-20261005-WA0005.opus", "PTT-20261005-WA0006.opus"],
    },
    {
        "anchor_time": "13:37",
        "anchor_sender": "Emanuele Sciarra",
        "type": "info",
        "text": "Riferisce di non riuscire a trovare il gruppo \"San Benedetto No "
                "Censure Inside\" né tramite il link di Raffaele né cercando tra "
                "gruppi e persone, né col profilo personale né con quello del "
                "comitato; dice che si fida di chi lo dice.",
        "members": ["PTT-20261005-WA0010.opus", "PTT-20261005-WA0011.opus",
                    "PTT-20261005-WA0012.opus"],
    },
    {
        "anchor_time": "13:52",
        "anchor_sender": "Dante Caniglia",
        "type": "proposta",
        "text": "Consiglia di pubblicare con la pagina dentro i gruppi e di "
                "ricondividere sui propri profili, così la pagina cresce.",
        "members": ["PTT-20261005-WA0013.opus"],
    },
]

MEDIA_OVERRIDES = {
    (DATE, "13:23", "Elvis Ippoliti", "IMG-20261005-WA0008.jpg"):
        "Screenshot della pagina del santuario di Santa Maria Goretti, con "
        "la foto della chiesa in mattoni: la chiesa di San Nicolò, detta di "
        "Sant'Agostino, ora Santuario Diocesano.",
    (DATE, "13:35", "Emanuele Sciarra", "IMG-20261005-WA0009.jpg"):
        "Screenshot di un link di gruppo Facebook che risulta non disponibile "
        "al momento.",
    (DATE, "13:38", "Elvis Ippoliti", "IMG-20261005-WA0015.jpg"):
        "Screenshot di un post della pagina \"San Benedetto dei Marsi - NO "
        "censure inside\" che condivide la locandina della gita della Classe "
        "1987 a Corinaldo.",
    (DATE, "13:40", "Antonio Aceto", "IMG-20261005-WA0020.jpg"):
        "Screenshot del post della Classe 1987 di San Benedetto dei Marsi con "
        "la locandina della gita a Corinaldo, dove si ricorda il gemellaggio "
        "con il comune di Corinaldo e la santa nata e vissuta lì.",
    (DATE, "18:21", "Emanuele Sciarra", "VID-20261005-WA0022.mp4"):
        "Video di una partita di calcio dell'Under 21 dell'Italia, condiviso "
        "senza commenti legati al comitato.",
}

# IMG-20261005-WA0009.jpg (13:35, Emanuele): screenshot "contenuto non disponibile",
# già rimosso dall'app dopo l'import del 5/10 — escluso per non reinserirlo.
_SKIP_FILES = {"IMG-20261005-WA0009.jpg"}


def _extra_skip(time_, fname):
    return fname in _SKIP_FILES


if __name__ == "__main__":
    build_digest(DATE, CURATED, MEDIA_OVERRIDES, audio_curated=AUDIO_CURATED,
                 audio_merges=AUDIO_MERGES, text_merges=TEXT_MERGES,
                 extra_skip_media=_extra_skip,
                 extra_skip_label="screenshot rimosso in app")
