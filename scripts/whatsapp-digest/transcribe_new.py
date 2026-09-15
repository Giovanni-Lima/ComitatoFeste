#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recupero messaggi nuovi + trascrizione Whisper dei vocali, PRIMA della
curatela (vedi CLAUDE.md, "Trascrizione anticipata dei vocali").

Perché: in curatela serve poter riconoscere vocali "cloni" (stesso
concetto ripetuto da più messaggi vocali) per accorparli in una sola
entry invece di lasciarli come punti distinti — cosa possibile solo se il
testo del vocale è già disponibile PRIMA di scrivere CURATED/AUDIO_CURATED
in build_digest_MMGG.py. Claude non ascolta audio nativamente, ma può
leggere una trascrizione testuale.

Cosa fa, in ordine:
  1. Parsa il .txt estratto (riusa parse_wa.parse_messages).
  2. Filtra solo i messaggi strettamente successivi a
     checkpoint.json -> ultimo_messaggio_letto.
  3. Per ogni audio nuovo chiama Groq Whisper (SOLO trascrizione, niente
     classificazione: quella la fa il curatore leggendo il testo, con
     tutto il contesto della conversazione intorno — vedi CLAUDE.md sul
     perché è meglio che il classificatore isolato del Transcriber).
  4. Scrive un unico file scripts/whatsapp-digest/nuovi_messaggi_<data>.json
     con tutti i messaggi nuovi (testo/media invariati, audio con in più
     il campo "transcript") pronto da leggere in curatela.

Cache/resume: scripts/whatsapp-digest/.transcript_cache.json (gitignored)
mappa nome-file -> testo trascritto, scritta su disco dopo OGNI singola
chiamata (non a fine batch): un crash o un rate-limit a metà non fa
perdere le trascrizioni già pagate, si rilancia lo script e riparte solo
dai file mancanti in cache.

Uso:
    python transcribe_new.py [--delay-ms 3000] [--src <cartella estratta>]

Stessa chiave Groq usata dal Transcriber .NET (vedi GroqKey.cs): env
GROQ_API_KEY, altrimenti key.txt risalendo le cartelle fino alla radice
del repo.
"""
import argparse
import json
import os
import sys
import time

import requests

from parse_wa import parse_messages, BASE as DEFAULT_SRC

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH = os.path.join(SCRIPT_DIR, ".transcript_cache.json")
CHECKPOINT_PATH = os.path.join(SCRIPT_DIR, "checkpoint.json")

TRANSCRIPTIONS_URL = "https://api.groq.com/openai/v1/audio/transcriptions"
WHISPER_MODEL = "whisper-large-v3"

# Stesso elenco di Src/backend/ComitatoFeste.Importer/MediaKind.cs.
AUDIO_EXT = {".opus", ".m4a", ".ogg", ".mp3", ".wav", ".aac"}

CONTENT_TYPES = {
    ".opus": "audio/ogg", ".ogg": "audio/ogg",
    ".m4a": "audio/mp4", ".mp3": "audio/mpeg",
    ".wav": "audio/wav", ".aac": "audio/aac",
}


def resolve_groq_key():
    env = os.environ.get("GROQ_API_KEY")
    if env and env.strip():
        return env.strip()
    d = SCRIPT_DIR
    for _ in range(8):
        path = os.path.join(d, "key.txt")
        if os.path.isfile(path):
            text = open(path, encoding="utf-8").read().strip()
            if text:
                return text
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    return None


def load_cache():
    if os.path.isfile(CACHE_PATH):
        with open(CACHE_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    tmp = CACHE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    os.replace(tmp, CACHE_PATH)


def load_checkpoint():
    with open(CHECKPOINT_PATH, encoding="utf-8") as f:
        return json.load(f)


def after_checkpoint(messages, last):
    """Messaggi strettamente successivi a checkpoint['ultimo_messaggio_letto']
    (stesso confronto (date, time, sender) usato manualmente finora)."""
    boundary = (last["date"], last["time"], last["sender"])
    idx = None
    for i, m in enumerate(messages):
        if (m["date"], m["time"], m["sender"]) == boundary:
            idx = i
    if idx is None:
        # Nessun match esatto (raro: es. mittente rimappato) - meglio non
        # tagliare nulla che perdere messaggi, il chiamante lo segnala.
        print(f"ATTENZIONE: checkpoint {boundary} non trovato nei messaggi parsati, "
              f"nessun filtro applicato.", file=sys.stderr)
        return messages
    return messages[idx + 1:]


def transcribe_one(session, api_key, src_dir, fname, delay_ms, max_retries=3):
    ext = os.path.splitext(fname)[1].lower()
    path = os.path.join(src_dir, fname)
    if not os.path.isfile(path):
        print(f"  [{fname}] SALTATO: file non trovato in {src_dir}")
        return None

    send_name = fname
    if ext == ".opus":
        send_name = os.path.splitext(fname)[0] + ".ogg"

    with open(path, "rb") as f:
        content = f.read()

    for attempt in range(1, max_retries + 1):
        resp = session.post(
            TRANSCRIPTIONS_URL,
            headers={"Authorization": f"Bearer {api_key}"},
            files={"file": (send_name, content, CONTENT_TYPES.get(ext, "application/octet-stream"))},
            data={"model": WHISPER_MODEL, "language": "it", "response_format": "json"},
            timeout=180,
        )
        if resp.status_code == 200:
            text = resp.json().get("text", "").strip()
            time.sleep(delay_ms / 1000)
            return text
        if resp.status_code == 429 or resp.status_code >= 500:
            wait = int(resp.headers.get("Retry-After", 2 * attempt))
            print(f"  [{fname}] HTTP {resp.status_code}, ritento tra {wait}s (tentativo {attempt}/{max_retries})")
            time.sleep(wait)
            continue
        raise RuntimeError(f"Groq Whisper HTTP {resp.status_code}: {resp.text[:300]}")

    raise RuntimeError(f"Groq Whisper: esauriti i tentativi per {fname}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--delay-ms", type=int, default=3000,
                     help="pausa tra un vocale e il successivo (default: 3000, limite Whisper 20 req/min)")
    ap.add_argument("--src", default=DEFAULT_SRC,
                     help="cartella con il .txt e i media estratti dallo zip")
    ap.add_argument("--date", default=None,
                     help="ignora il checkpoint e trascrivi tutti i vocali di questa "
                          "data (yyyy-MM-dd) — per backfill/test su un giorno storico")
    args = ap.parse_args()

    api_key = resolve_groq_key()
    if not api_key:
        print("Chiave Groq assente: imposta GROQ_API_KEY oppure crea key.txt nella radice del repo.", file=sys.stderr)
        return 2

    txt_path = os.path.join(args.src, "Chat WhatsApp con Il branco dei pazzi 87.txt")
    if not os.path.isfile(txt_path):
        print(f"Non trovo il .txt in {txt_path} (usa --src per un percorso diverso).", file=sys.stderr)
        return 2

    all_messages = parse_messages(txt_path)
    if args.date:
        new_messages = [m for m in all_messages if m["date"] == args.date]
        print(f"messaggi del {args.date} (modalità backfill/test, checkpoint ignorato): {len(new_messages)}")
    else:
        checkpoint = load_checkpoint()
        new_messages = after_checkpoint(all_messages, checkpoint["ultimo_messaggio_letto"])
        print(f"messaggi nuovi (dopo checkpoint {checkpoint['ultimo_messaggio_letto']}): {len(new_messages)}")

    audio_new = [m for m in new_messages
                 if m["kind"] == "media" and os.path.splitext(m["file"])[1].lower() in AUDIO_EXT]
    print(f"di cui vocali da trascrivere: {len(audio_new)}")

    cache = load_cache()
    session = requests.Session()
    done, reused, errors = 0, 0, 0

    for m in audio_new:
        fname = m["file"]
        if fname in cache:
            reused += 1
            continue
        print(f"[{m['time']}] {m['sender']} ({fname}) ... trascrivo")
        try:
            text = transcribe_one(session, api_key, args.src, fname, args.delay_ms)
        except Exception as e:
            errors += 1
            print(f"  ERRORE: {e}")
            continue
        if text is None:
            continue
        cache[fname] = text
        save_cache(cache)  # flush immediato: resume sicuro dopo un crash
        done += 1
        print(f"  -> \"{text[:70]}\"")

    print(f"\n== trascritti ora: {done}, già in cache: {reused}, errori: {errors} ==")

    for m in new_messages:
        if m["kind"] == "media" and os.path.splitext(m["file"])[1].lower() in AUDIO_EXT:
            m["transcript"] = cache.get(m["file"])

    if not new_messages:
        print("Nessun messaggio nuovo, nessun file di output scritto.")
        return 0

    out_date = new_messages[-1]["date"]
    out_path = os.path.join(SCRIPT_DIR, f"nuovi_messaggi_{out_date}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(new_messages, f, ensure_ascii=False, indent=2)
    print(f"scritto {out_path} ({len(new_messages)} messaggi, pronto per la curatela)")

    if errors > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
