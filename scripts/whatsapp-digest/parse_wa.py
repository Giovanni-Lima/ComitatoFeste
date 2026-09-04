#!/usr/bin/env python3
import json, os, re

BASE = os.path.expanduser("~/mnt/ComitatoFeste/Chat WhatsApp con Il branco dei pazzi 87")
F = os.path.join(BASE, "Chat WhatsApp con Il branco dei pazzi 87.txt")

INVIS = "‎‏"
MSG_START = re.compile(r"^(\d{2})/(\d{2})/(\d{2}), (\d{2}):(\d{2}) - (.*)$")
FILE_RE = re.compile(r"^([A-Za-z0-9_\-]+\.[A-Za-z0-9]+) \(file allegato\)$")
EDIT_MARK = "<Questo messaggio è stato modificato>"

def clean(s):
    for c in INVIS:
        s = s.replace(c, "")
    return s

messages = []
cur = None
with open(F, encoding="utf-8") as f:
    for raw_line in f:
        line = clean(raw_line.rstrip("\n"))
        m = MSG_START.match(line)
        if m:
            dd, mm, yy, hh, mi, rest = m.groups()
            date = f"20{yy}-{mm}-{dd}"; time = f"{hh}:{mi}"
            if ": " in rest:
                sender, text = rest.split(": ", 1)
            else:
                sender, text = None, rest
            cur = {"date": date, "time": time, "sender": sender,
                   "kind": None, "text": text, "file": None, "edited": False}
            messages.append(cur)
        else:
            if cur is None:
                continue
            cur["text"] += "\n" + line

for msg in messages:
    if msg["sender"] is None:
        msg["kind"] = "system"
        continue
    t = msg["text"]
    if EDIT_MARK in t:
        msg["edited"] = True
        t = t.replace(EDIT_MARK, "").rstrip()
    if t.strip() == "<Media omessi>":
        msg["kind"] = "media_omitted"
        msg["text"] = None
    else:
        fm = FILE_RE.match(t.split("\n", 1)[0])
        if fm:
            msg["kind"] = "media"
            msg["file"] = fm.group(1)
            caption = t.split("\n", 1)[1] if "\n" in t else ""
            msg["text"] = caption.strip() or None
        else:
            msg["kind"] = "text"
            msg["text"] = t

out = os.path.expanduser("~/whatsapp_parsed_full.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(messages, f, ensure_ascii=False, indent=2)

from collections import Counter
by_date = Counter(m["date"] for m in messages)
print("totale messaggi:", len(messages))
for d in ["2026-09-01", "2026-09-02", "2026-09-03"]:
    print(d, by_date.get(d, 0))

for d in ["2026-09-02", "2026-09-03"]:
    subset = [m for m in messages if m["date"] == d]
    outp = os.path.expanduser(f"~/whatsapp_parsed_{d}.json")
    with open(outp, "w", encoding="utf-8") as f:
        json.dump(subset, f, ensure_ascii=False, indent=2)
    print(f"scritto {outp} ({len(subset)} messaggi)")

senders02 = Counter(m["sender"] for m in messages if m["date"] == "2026-09-02" and m["sender"])
senders03 = Counter(m["sender"] for m in messages if m["date"] == "2026-09-03" and m["sender"])
print("mittenti 02-09:", dict(senders02))
print("mittenti 03-09:", dict(senders03))
kinds02 = Counter(m["kind"] for m in messages if m["date"] == "2026-09-02")
kinds03 = Counter(m["kind"] for m in messages if m["date"] == "2026-09-03")
print("kind 02-09:", dict(kinds02))
print("kind 03-09:", dict(kinds03))
