#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Libreria comune per generare digest_<data>.json dai messaggi WhatsApp già
parsati (whatsapp_parsed_full.json). Estratta il 6/9/2026 dai 6 script
build_digest_MMGG.py (che fino ad allora duplicavano tutti la stessa
logica) per non dover più propagare bug fix/miglioramenti a mano in ogni
copia — vedi CLAUDE.md, sezione "Generazione di digest_<data>.json".

Ogni build_digest_MMGG.py resta un file "dati": DATE, CURATED,
MEDIA_OVERRIDES, ed eventuali eccezioni specifiche del giorno (es. la
finestra oraria delle bozze del logo del 5/9), passate a build_digest().
"""
import json
import os
import re
import shutil
import subprocess
from collections import defaultdict

HOME = os.path.expanduser("~")
SRC = os.path.join(HOME, "mnt", "ComitatoFeste", "Chat WhatsApp con Il branco dei pazzi 87")
EXPORT = os.path.join(HOME, "mnt", "ComitatoFeste", "Export")
PARSED_FULL = os.path.join(HOME, "whatsapp_parsed_full.json")

EXT_KIND = {
    ".opus": "audio", ".m4a": "audio",
    ".jpg": "foto", ".jpeg": "foto",
    ".mp4": "video",
    ".webp": "sticker",
    ".pdf": "documento",
}


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


def media_text(sender, ext, caption, override):
    """Testo dell'entry per un media. `override` (da MEDIA_OVERRIDES) ha sempre
    la precedenza — ricordati la regola 6/9/2026: niente tratti fisici delle
    persone ritratte, solo azione/contesto."""
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


def build_digest(date, curated, media_overrides, curated_system=None,
                  extra_skip_media=None, extra_skip_label="esclusioni specifiche del giorno",
                  src=None, export=None, parsed_full_path=None,
                  checkpoint_path=None):
    """Genera Export/digest_<date>.json + Export/<date>/ a partire dai messaggi
    già parsati, applicando curatela testo (`curated`/`curated_system`) e
    didascalie media (`media_overrides`).

    extra_skip_media: funzione opzionale (time, fname) -> bool per eccezioni
    specifiche del giorno oltre a sticker/GIF/GIF-mp4 (es. la finestra oraria
    delle bozze del logo del 5/9). Se True, il media viene escluso e contato
    sotto `extra_skip_label`.
    """
    src = src or SRC
    export = export or EXPORT
    parsed_full_path = parsed_full_path or PARSED_FULL
    checkpoint_path = checkpoint_path or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "checkpoint.json")
    curated_system = curated_system or {}

    with open(parsed_full_path, encoding="utf-8") as f:
        all_msgs = json.load(f)
    msgs = [m for m in all_msgs if m["date"] == date]

    entries = []
    seq = defaultdict(int)
    dest_dir = os.path.join(export, date)
    os.makedirs(dest_dir, exist_ok=True)
    existing_before = set(os.listdir(dest_dir))
    kept_filenames = set()

    media_omitted_count = 0
    missing_source_files = []
    skipped_text = []
    skipped_stickers = []
    skipped_reaction_gifs = []
    skipped_extra = []
    used_curated_keys = set()

    for m in msgs:
        time_, sender, kind = m["time"], m["sender"], m["kind"]

        if kind == "system":
            hit = curated_system.get(time_)
            if hit:
                typ, text = hit
                entries.append({"date": date, "time": time_, "author": "Sistema", "type": typ,
                                 "text": text, "file": None})
            continue

        if kind == "media_omitted":
            media_omitted_count += 1
            continue

        if kind == "text":
            key = (time_, sender)
            hit = curated.get(key)
            if hit:
                if key in used_curated_keys:
                    # stesso (time, sender) di un messaggio già curato (es. due messaggi
                    # consecutivi dello stesso minuto): non duplicare l'entry (bug fix 6/9/2026,
                    # visto per la prima volta su build_digest_0906.py).
                    continue
                used_curated_keys.add(key)
                typ, text = hit
                entries.append({"date": date, "time": time_, "author": sender, "type": typ,
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
            if extra_skip_media and extra_skip_media(time_, fname):
                skipped_extra.append((time_, sender, fname))
                continue
            src_path = os.path.join(src, fname)
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
            dest_name = f"{time_.replace(':', '')}_{slug(sender)}{suffix}{ext.lower()}"
            shutil.copy2(src_path, os.path.join(dest_dir, dest_name))
            kept_filenames.add(dest_name)
            override = media_overrides.get((date, time_, sender, fname))
            text = media_text(sender, ext, m.get("text"), override)
            entries.append({"date": date, "time": time_, "author": sender, "type": "media",
                             "text": text, "file": dest_name})
            continue

    stale = existing_before - kept_filenames
    if stale:
        quarantine_dir = os.path.join(export, "_rimossi_" + date)
        os.makedirs(quarantine_dir, exist_ok=True)
        for fn in stale:
            shutil.move(os.path.join(dest_dir, fn), os.path.join(quarantine_dir, fn))

    entries.sort(key=lambda e: e["time"])
    out_path = os.path.join(export, f"digest_{date}.json")
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
    if extra_skip_media:
        print(f"{extra_skip_label}: {len(skipped_extra)}")

    # Checkpoint (regola 6/9/2026): traccia l'ultimo messaggio letto di questa giornata, così da
    # poter ripartire da lì se la curatela viene interrotta a metà. A giornata completata e
    # verificata, riporta l'ultimo messaggio in ordine cronologico del giorno.
    if msgs:
        last = msgs[-1]
        checkpoint = {
            "digest_data": date,
            "ultimo_messaggio_letto": {
                "date": last["date"],
                "time": last["time"],
                "sender": last["sender"],
                "kind": last["kind"],
            },
            "stato": "giornata completata e verificata",
        }
        with open(checkpoint_path, "w", encoding="utf-8") as f:
            json.dump(checkpoint, f, ensure_ascii=False, indent=2)
        print(f"checkpoint aggiornato: {checkpoint_path} -> {checkpoint['ultimo_messaggio_letto']}")

    return {
        "entries": entries,
        "by_type": dict(by_type),
        "media_omitted_count": media_omitted_count,
        "missing_source_files": missing_source_files,
        "skipped_text": skipped_text,
        "skipped_stickers": skipped_stickers,
        "skipped_reaction_gifs": skipped_reaction_gifs,
        "skipped_extra": skipped_extra,
    }
