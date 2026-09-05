#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re, shutil, subprocess
from collections import defaultdict

HOME = os.path.expanduser("~")
SRC = os.path.join(HOME, "mnt", "ComitatoFeste", "Chat WhatsApp con Il branco dei pazzi 87")
EXPORT = os.path.join(HOME, "mnt", "ComitatoFeste", "Export")
DATE = "2026-09-04"

def slug(name):
    s = name.replace("'", "").replace("'", "")
    s = re.sub(r"\s+", "-", s.strip())
    return s

def is_reaction_gif(path):
    """Regola 4/9/2026: WhatsApp salva le GIF di reazione come .mp4 muti e brevi.
    Un .mp4 senza traccia audio è quindi una GIF, non un video vero: si ignora."""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "a",
             "-show_entries", "stream=codec_type", "-of", "csv=p=0", path],
            capture_output=True, text=True, timeout=15)
        return out.stdout.strip() == ""
    except Exception:
        return False  # in dubbio, non escludere

CURATED = {
    ("08:10", "Costantino Mariani"): ("info",
        "Riferisce (sentito da Luca Trinchini) che tutti i totem sono stati tolti."),
    ("15:50", "Alessandra Toracchio"): ("domanda",
        "Chiede cosa è stato deciso per la riunione."),
    ("15:50", "Emilio Caniglia"): ("info",
        "Riepilogo dopo il riposizionamento delle statue di ieri sera: incontro breve con Don Enzo "
        "con novità importanti, e rimozione di tutti i totem (saranno riutilizzati il prossimo anno, "
        "piccola spesa risparmiata per il Comitato). Novità: invito da parte di Don Enzo alla messa "
        "delle 11:30 del 27 settembre con le magliette del Comitato (sarà esposto il corpo di San "
        "Camillo de Lellis); la visita a Corinaldo è posticipata all'8 novembre per impegni di Don "
        "Enzo e accordi con Don Luigi di Corinaldo; probabile un nuovo incontro con Don Enzo in "
        "settimana per definire l'impegno per le Feste Patronali."),
    ("15:57", "Alessandra Simonetti"): ("info",
        "Il 27 settembre, oltre alla messa, ci sarà anche la benedizione degli operatori sanitari."),
    ("16:06", "Costance Rossi"): ("domanda",
        "Propone di fare una riunione prima di vedere Don Enzo, per arrivare con idee comuni tra "
        "tutti."),
    ("16:10", "Elvis Ippoliti"): ("info",
        "Conferma che se ne era già parlato la sera prima con Emidio e altri (di persona), anche per "
        "decidere le cariche finali e scegliere la sede."),
    ("16:17", "Luca Cicchelli"): ("info",
        "Propone una piccola quota di partecipazione da parte di tutti per gli incontri/eventi, da "
        "definire in base alle esigenze e al consenso del gruppo."),
    ("16:19", "Costance Rossi"): ("decisione",
        "Propone di provare a organizzare l'incontro entro fine settembre."),
    ("16:19", "Emidio Cerasani"): ("info",
        "Riferisce che Costantino Mariani (imprenditore) ha detto di mettere una quota alta di "
        "partecipazione."),
    ("16:20", "Costance Rossi"): ("domanda",
        "Visto che il 27 settembre ci sarà molta partecipazione per la benedizione, chiede se si può "
        "organizzare qualcosa in quell'occasione."),
    ("16:21", "Emilio Caniglia"): ("decisione",
        "Per lui va bene organizzare l'incontro prima di quello con Don Enzo (la prossima settimana, "
        "infrasettimanale): bisogna decidere se farlo stasera, domani sera o domenica sera."),
    ("16:22", "Elvis Ippoliti"): ("info",
        "Pensa si possa fare l'incontro lunedì o martedì, dato che con Don Enzo ci si vedrà mercoledì "
        "o giovedì."),
    ("16:24", "Emanuele Sciarra"): ("info",
        "La \"ragazza dei materassi\" (sponsor per la lotteria) aspetta solo che le venga data una "
        "data."),
    ("16:25", "Emanuele Sciarra"): ("decisione",
        "Bisogna chiedere la sala al Comune per l'incontro; propone di organizzare un piccolo buffet "
        "per l'occasione."),
    ("16:26", "Emanuele Sciarra"): ("info",
        "Con 5€ a testa si compra da mangiare e da bere per il buffet, oppure chi vuole e sa fare "
        "porta dolci fatti in casa."),
    ("18:30", "Dante Caniglia"): ("info",
        "Sta seguendo in diretta un evento per bambini e genitori (gruppo \"Snack club\") ad "
        "Avezzano: nota stupito quanta gente porti, a suo dire più del concerto dei The Kolors "
        "(condivide diversi video dall'evento)."),
    ("18:38", "Maria Buttari"): ("info",
        "Osserva che gli eventi che attirano i bambini fanno soldi — spunto per la pianificazione di "
        "futuri eventi del comitato."),
    ("18:42", "Emanuele Sciarra"): ("info",
        "Condivide un link a un video Facebook, relativo allo stesso evento per bambini di cui si "
        "stava parlando: https://www.facebook.com/share/r/1EUmPSTZqM/?mibextid=wwXIfr"),
}

MEDIA_OVERRIDES = {
    (DATE, "07:07", "Serena Di Stefano", "IMG-20260904-WA0007.jpg"):
        "Foto di un cervo in un prato nella nebbia mattutina, condivisa insieme al saluto \"sono in "
        "compagnia\".",
    (DATE, "14:08", "Elvis Ippoliti", "IMG-20260904-WA0046.jpg"):
        "Meme: fotogramma da \"Il Signore degli Anelli - Il Ritorno del Re\" con la scritta scherzosa "
        "\"PER COSTANTINO!\" al posto di \"per Frodo\" — battuta rivolta a Costantino Mariani.",
    (DATE, "18:33", "Elvis Ippoliti", "IMG-20260904-WA0054.jpg"):
        "Selfie con un bicchiere di birra in mano e occhiali da sole — foto conviviale della serata.",
    (DATE, "19:21", "Elvis Ippoliti", "IMG-20260904-WA0064.jpg"):
        "Foto all'aperto in un locale/bar, momento conviviale della serata.",
    (DATE, "19:35", "Ugo Trinchini", "IMG-20260904-WA0065.jpg"):
        "Selfie di due persone con da bere in mano, sorridenti — foto conviviale della serata.",
}

EXT_KIND = {
    ".opus": "audio", ".m4a": "audio",
    ".jpg": "foto", ".jpeg": "foto",
    ".mp4": "video",
    ".webp": "sticker",
    ".pdf": "documento",
}

def media_text(sender, ext, caption, override):
    if override:
        return override
    kind = EXT_KIND.get(ext.lower(), "file")
    if kind == "audio":
        return f"Vocale di {sender}, non trascritto."
    if kind == "foto":
        t = f"Foto condivisa da {sender}."
        if caption:
            t += f" Didascalia: {caption}"
        return t
    if kind == "video":
        t = f"Video condiviso da {sender}."
        if caption:
            t += f" Didascalia: {caption}"
        return t
    if kind == "sticker":
        return f"Sticker condiviso da {sender}."
    if kind == "documento":
        t = f"Documento condiviso da {sender}."
        if caption:
            t += f" Didascalia: {caption}"
        return t
    t = f"File condiviso da {sender} ({ext})."
    if caption:
        t += f" Didascalia: {caption}"
    return t

with open(os.path.join(HOME, "whatsapp_parsed_full.json"), encoding="utf-8") as f:
    all_msgs = json.load(f)
msgs = [m for m in all_msgs if m["date"] == DATE]

entries = []
seq = defaultdict(int)
dest_dir = os.path.join(EXPORT, DATE)
os.makedirs(dest_dir, exist_ok=True)
existing_before = set(os.listdir(dest_dir))
kept_filenames = set()

media_omitted_count = 0
missing_source_files = []
skipped_text = []
skipped_stickers = []
skipped_reaction_gifs = []

for m in msgs:
    time_, sender, kind = m["time"], m["sender"], m["kind"]

    if kind == "system":
        continue

    if kind == "media_omitted":
        media_omitted_count += 1
        continue

    if kind == "text":
        key = (time_, sender)
        hit = CURATED.get(key)
        if hit:
            typ, text = hit
            entries.append({"date": DATE, "time": time_, "author": sender, "type": typ,
                             "text": text, "file": None})
        else:
            skipped_text.append((time_, sender))
        continue

    if kind == "media":
        fname = m["file"]
        ext = os.path.splitext(fname)[1]
        if ext.lower() in (".webp", ".gif"):
            skipped_stickers.append((time_, sender, fname))
            continue
        src_path = os.path.join(SRC, fname)
        if not os.path.isfile(src_path):
            missing_source_files.append((time_, sender, fname))
            continue
        if ext.lower() == ".mp4" and is_reaction_gif(src_path):
            skipped_reaction_gifs.append((time_, sender, fname))
            continue
        k = (time_.replace(":", ""), sender)
        seq[k] += 1
        n = seq[k]
        suffix = f"-{n}" if n > 1 else ""
        dest_name = f"{time_.replace(':','')}_{slug(sender)}{suffix}{ext.lower()}"
        shutil.copy2(src_path, os.path.join(dest_dir, dest_name))
        kept_filenames.add(dest_name)
        override = MEDIA_OVERRIDES.get((DATE, time_, sender, fname))
        text = media_text(sender, ext, m.get("text"), override)
        entries.append({"date": DATE, "time": time_, "author": sender, "type": "media",
                         "text": text, "file": dest_name})
        continue

stale = existing_before - kept_filenames
if stale:
    quarantine_dir = os.path.join(EXPORT, "_rimossi_" + DATE)
    os.makedirs(quarantine_dir, exist_ok=True)
    for fn in stale:
        shutil.move(os.path.join(dest_dir, fn), os.path.join(quarantine_dir, fn))

entries.sort(key=lambda e: e["time"])
out_path = os.path.join(EXPORT, f"digest_{DATE}.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"scritto {out_path} ({len(entries)} entry)")
by_type = defaultdict(int)
for e in entries:
    by_type[e["type"]] += 1
print("per tipo:", dict(by_type))
print("media_omessi (esclusi da WhatsApp, non recuperabili):", media_omitted_count)
print("file sorgente mancanti:", missing_source_files)
print(f"messaggi di testo NON curati/scartati come rumore: {len(skipped_text)}")
print(f"sticker/gif ignorati: {len(skipped_stickers)}")
print(f"gif di reazione travestite da mp4, ignorate: {skipped_reaction_gifs}")
