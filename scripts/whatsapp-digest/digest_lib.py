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

# Normalizzazione del nome autore: il .txt di WhatsApp usa il display name reale
# (es. con apostrofo), ma altrove nella pipeline lo stesso membro compare con una
# forma diversa (tipicamente quella del file foto profilo, es. "Nome-Cognome.jpg").
# Senza allinearli l'Importer — che fa match esatto su DisplayName — crea un membro
# duplicato a ogni import (vedi "Domanda aperta" in CLAUDE.md). La mappa rimappa
# SOLO il nome scritto nelle entry (campo "author", nome file media, testo del
# placeholder vocale); le chiavi di CURATED / MEDIA_OVERRIDES restano il nome
# grezzo del .txt. Aggiungere una riga qui quando emerge un nuovo disallineamento.
AUTHOR_ALIASES = {
    "Valentina D'Arcadia": "Valentina DArcadia",
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


def media_text(sender, ext, caption, override, n=1):
    """Testo dell'entry per un media. `override` (da MEDIA_OVERRIDES) ha sempre
    la precedenza — ricordati la regola 6/9/2026: niente tratti fisici delle
    persone ritratte, solo azione/contesto.

    `n` è la progressione del media nella coppia (minuto, mittente): serve solo
    per il placeholder dei vocali non trascritti. Due (o più) vocali diversi
    dello stesso autore nello stesso minuto avrebbero altrimenti testo identico
    e collasserebbero sul vincolo UNIQUE (GroupId, MemberId, OccurredAt, Text)
    dell'Importer (falso positivo descritto in docs/CONTEXT.md, visto sui dati
    del 10/9/2026). Dal 2° in poi si aggiunge " (n)" per renderli distinti; il
    testo resta un placeholder ("non trascritt" c'è ancora, così l'Importer lo
    continua a escludere dal dedup fuzzy) e il Transcriber lo riscrive comunque.
    """
    if override:
        return override
    kind = EXT_KIND.get(ext.lower(), "file")
    if kind == "audio":
        return (f"Vocale di {sender}, non trascritto. ({n})" if n > 1
                else f"Vocale di {sender}, non trascritto.")
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


TRANSCRIPT_CACHE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".transcript_cache.json")


def _load_transcript_cache(path):
    if path and os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def build_digest(date, curated, media_overrides, curated_system=None,
                  extra_skip_media=None, extra_skip_label="esclusioni specifiche del giorno",
                  src=None, export=None, parsed_full_path=None,
                  checkpoint_path=None, audio_curated=None, audio_merges=None,
                  transcript_cache_path=None):
    """Genera Export/digest_<date>.json + Export/<date>/ a partire dai messaggi
    già parsati, applicando curatela testo (`curated`/`curated_system`) e
    didascalie media (`media_overrides`).

    extra_skip_media: funzione opzionale (time, fname) -> bool per eccezioni
    specifiche del giorno oltre a sticker/GIF/GIF-mp4 (es. la finestra oraria
    delle bozze del logo del 5/9). Se True, il media viene escluso e contato
    sotto `extra_skip_label`.

    audio_curated: dict (date, time, sender, filename) -> (type, text) per un
    vocale ATOMICO già classificato in curatela (usando la trascrizione
    prodotta da transcribe_new.py) — il file resta comunque tenuto/copiato,
    ma l'entry esce con type/text reali invece del placeholder "non
    trascritto", e porta anche `transcript` (dalla cache) così l'Importer può
    valorizzare MediaAsset.TranscriptionText/TranscribedAt e il Transcriber lo
    salta in automatico (vedi CLAUDE.md, "Trascrizione anticipata dei vocali").

    Un vocale con type "rumore" in audio_curated viene scartato del tutto (regola
    19/9/2026): nessuna entry, file non copiato (il testo del secondo elemento è ignorato).

    audio_merges: lista di gruppi di vocali "cloni" da accorpare in
    un'unica entry di sintesi, scartandone i file:
        {"anchor_time": "HH:MM", "anchor_sender": "Nome", "type": ...,
         "text": ..., "members": ["file1.opus", "file2.opus", ...]}
    Un vocale non coperto né da `audio_curated` né da `audio_merges` mantiene
    il comportamento di sempre (placeholder, file tenuto, type "media") — è
    la rete di sicurezza in caso la curatela non arrivi a classificare tutto.
    """
    src = src or SRC
    export = export or EXPORT
    parsed_full_path = parsed_full_path or PARSED_FULL
    checkpoint_path = checkpoint_path or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "checkpoint.json")
    curated_system = curated_system or {}
    audio_curated = audio_curated or {}
    audio_merges = audio_merges or []
    transcript_cache = _load_transcript_cache(transcript_cache_path or TRANSCRIPT_CACHE_PATH)

    merged_filenames = {fn for group in audio_merges for fn in group["members"]}

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
    skipped_audio_merged = []
    skipped_audio_noise = []
    used_curated_keys = set()

    for m in msgs:
        time_, sender, kind = m["time"], m["sender"], m["kind"]
        # nome grezzo del .txt -> chiavi CURATED/MEDIA_OVERRIDES e log diagnostici;
        # `author` (rimappato) -> campo "author" delle entry, nome file media, placeholder vocale.
        author = AUTHOR_ALIASES.get(sender, sender)

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
                entries.append({"date": date, "time": time_, "author": author, "type": typ,
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
            if fname in merged_filenames:
                # Vocale "clone" accorpato con altri in un'unica entry di
                # sintesi (regola aggiunta il 15/9/2026): il file si scarta,
                # non genera una entry propria. La entry di sintesi viene
                # emessa una sola volta, dopo il loop principale.
                skipped_audio_merged.append((time_, sender, fname))
                continue
            audio_hit = audio_curated.get((date, time_, sender, fname))
            if audio_hit and audio_hit[0] == "rumore":
                # Vocale classificato "rumore" in curatela (regola 19/9/2026): si butta,
                # niente entry, niente copia del file — né Importer né Transcriber lo vedranno.
                skipped_audio_noise.append((time_, sender, fname))
                continue
            src_path = os.path.join(src, fname)
            if not os.path.isfile(src_path):
                missing_source_files.append((time_, sender, fname))
                continue
            if ext.lower() == ".mp4" and is_reaction_gif(src_path):
                skipped_reaction_gifs.append((time_, sender, fname))
                continue
            k = (time_.replace(":", ""), author)
            seq[k] += 1
            n = seq[k]
            suffix = f"-{n}" if n > 1 else ""
            dest_name = f"{time_.replace(':', '')}_{slug(author)}{suffix}{ext.lower()}"
            shutil.copy2(src_path, os.path.join(dest_dir, dest_name))
            kept_filenames.add(dest_name)

            entry = {"date": date, "time": time_, "author": author, "file": dest_name}
            if audio_hit:
                typ, text = audio_hit
                entry["type"] = typ
                entry["text"] = text
            else:
                override = media_overrides.get((date, time_, sender, fname))
                entry["type"] = "media"
                entry["text"] = media_text(author, ext, m.get("text"), override, n=n)
            transcript = transcript_cache.get(fname)
            if transcript:
                entry["transcript"] = transcript
            entries.append(entry)
            continue

    for group in audio_merges:
        entries.append({"date": date, "time": group["anchor_time"], "author": group["anchor_sender"],
                         "type": group["type"], "text": group["text"], "file": None})

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
    if audio_merges:
        print(f"vocali accorpati in {len(audio_merges)} entry di sintesi (file scartati): {len(skipped_audio_merged)}")
    if audio_curated:
        print(f"vocali atomici pre-classificati in curatela: {len(audio_curated) - len(skipped_audio_noise)}")
    if skipped_audio_noise:
        print(f"vocali classificati rumore in curatela, scartati: {len(skipped_audio_noise)}")
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
        "skipped_audio_merged": skipped_audio_merged,
        "skipped_audio_noise": skipped_audio_noise,
    }
