#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re, shutil, subprocess
from collections import defaultdict

HOME = os.path.expanduser("~")
SRC = os.path.join(HOME, "mnt", "ComitatoFeste", "Chat WhatsApp con Il branco dei pazzi 87")
EXPORT = os.path.join(HOME, "mnt", "ComitatoFeste", "Export")
DATE = "2026-09-02"

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
        hit = CURATED_SYSTEM.get(time_)
        if hit:
            typ, text = hit
            entries.append({"date": DATE, "time": time_, "author": "Sistema", "type": typ,
                             "text": text, "file": None})
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
