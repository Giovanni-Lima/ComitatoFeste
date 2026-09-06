#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re, shutil, subprocess
from collections import defaultdict

HOME = os.path.expanduser("~")
SRC = os.path.join(HOME, "mnt", "ComitatoFeste", "Chat WhatsApp con Il branco dei pazzi 87")
EXPORT = os.path.join(HOME, "mnt", "ComitatoFeste", "Export")
DATE = "2026-09-05"

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

# --- Regola "iterazioni di design" (aggiunta 4/9/2026, applicata qui per la prima volta) ---
# Il 5/9 il gruppo ha passato l'intero pomeriggio (13:37-19:26) a discutere e rifare il
# logo/maglietta del comitato, producendo decine di bozze intermedie in jpg. L'utente ha
# indicato esplicitamente le uniche due immagini definitive da tenere:
#   IMG-20260905-WA0123.jpg ("Maglietta") e IMG-20260905-WA0124.jpg ("Logo"),
#   entrambe inviate da Antonio Aceto alle 18:54.
# Tutte le altre .jpg cadute in quella finestra oraria sono bozze intermedie e vengono
# escluse automaticamente, TRANNE due immagini che sono finite nella stessa finestra ma
# non c'entrano nulla con il logo (una pubblicità e uno screenshot della chat), esplicitamente
# tenute fuori dall'esclusione.
LOGO_WINDOW_START = "13:37"
LOGO_WINDOW_END = "19:26"
LOGO_FINAL_FILES = {"IMG-20260905-WA0123.jpg", "IMG-20260905-WA0124.jpg"}
LOGO_WINDOW_UNRELATED = {"IMG-20260905-WA0117.jpg", "IMG-20260905-WA0118.jpg"}

def is_logo_draft(time_, fname):
    if not fname.lower().endswith(".jpg"):
        return False
    if fname in LOGO_FINAL_FILES or fname in LOGO_WINDOW_UNRELATED:
        return False
    return LOGO_WINDOW_START <= time_ <= LOGO_WINDOW_END

CURATED_SYSTEM = {
    "19:06": ("info",
        "Dante Caniglia cambia l'immagine del gruppo (presumibilmente con il nuovo logo appena "
        "definito)."),
}

CURATED = {
    ("11:04", "Alessandra Toracchio"): ("domanda",
        "Chiede cosa è stato deciso riguardo alla riunione."),
    ("12:24", "Emilio Caniglia"): ("info",
        "Saluto a tutti: oggi è il compleanno di Don Enzo, ha scritto gli auguri a nome di tutta la "
        "classe 1987."),
    ("12:26", "Emilio Caniglia"): ("decisione",
        "Per la riunione, va bene organizzarsi con un sondaggio per scegliere il giorno."),
    ("12:37", "Dante Caniglia"): ("info",
        "Condivide un link a un video Facebook come spunto per un'idea che potrebbe far guadagnare "
        "soldi al comitato: https://www.facebook.com/share/r/18oo8erFaj/"),
    ("13:34", "Chiara Gargano"): ("decisione",
        "Propone di modificare il logo attuale, che non convince del tutto, per renderlo adatto a "
        "tutte le stampe (locandine, manifesti ecc.) e idoneo anche per le copertine social e app."),
    ("13:47", "Chiara Gargano"): ("info",
        "Ribadisce le regole di base del logo: va sempre senza sfondo, con \"Comitato Feste\" "
        "scritto sotto \"1987\"; colori di riferimento rosa per le donne e blu per i maschi."),
    ("13:55", "Elvis Ippoliti"): ("info",
        "Ricorda che sulle magliette va comunque scritto in modo leggibile \"Comitato Feste San "
        "Benedetto\" o \"1987\" (non ricorda quale dei due)."),
    ("16:51", "Chiara Gargano"): ("decisione",
        "Dichiara chiusa la fase di modifica: il logo è solo quello appena mostrato, non ci saranno "
        "altre modifiche."),
    ("17:43", "Emanuele Sciarra"): ("domanda",
        "Chiede conferma: è stato modificato solo il LOGO, e le magliette del comitato sono ancora "
        "da progettare a parte?"),
    ("19:01", "Maria Buttari"): ("info",
        "Conferma ad Antonio Aceto che il logo (appena postato nella sua versione definitiva) era "
        "già stato scelto in precedenza."),
    ("19:10", "Elvis Ippoliti"): ("info",
        "Fa notare che, se online si è mostrato il logo per intero, poi sulle magliette non ci si "
        "può presentare con un logo tagliato/mozzato: serve coerenza tra le due versioni."),
    ("19:14", "Antonio Sabatini"): ("info",
        "Chiarisce che è stata solo una modifica minima, non sull'immagine: la scritta in "
        "orizzontale è più leggibile e d'impatto. D'accordo nell'usare entrambe le versioni (lunga e "
        "corta) a seconda delle esigenze."),
    ("19:53", "Emanuele Sciarra"): ("info",
        "Fa notare, senza offesa per nessuno, che si stanno allungando troppo i tempi: per un logo e "
        "una maglietta ci sono voluti 5 mesi ed è ancora indeciso; propone una riunione in serata per "
        "tagliare corto sui prossimi argomenti, più seri."),
    ("19:57", "Luca Cicchelli"): ("decisione",
        "Propone di mettere tutte le questioni ancora in discussione a votazione, invece di "
        "continuare a parlarne senza concludere."),
    ("19:58", "Elvis Ippoliti"): ("decisione",
        "Propone di preparare una lista di tutte le cose imminenti e importanti da trattare in "
        "riunione, per non perdersi in chiacchiere."),
    ("20:01", "Elvis Ippoliti"): ("info",
        "Invita tutti a fare una birra quella sera a Venere, dove suonano i Santo California."),
    ("20:12", "Antonio Sabatini"): ("info",
        "Conferma che si parte con l'evento dei materassi, per cui serve preparare un buffet: una "
        "piccola quota di partecipazione è necessaria per iniziare."),
    ("20:15", "Luca Cicchelli"): ("decisione",
        "Sottolinea che un fondo cassa ci deve essere, ad esempio per spese come la targa per "
        "Corinaldo."),
    ("20:20", "Antonio Aceto"): ("decisione",
        "Propone di portare 20€ a testa alla prossima riunione come base di partenza, almeno per il "
        "buffet dell'evento materassi e per il riallaccio della corrente alla sede."),
    ("20:30", "Luca Cicchelli"): ("info",
        "Precisa che la cifra di 20€ non può essere decisa a priori da uno solo: bisogna deciderla "
        "tutti insieme in riunione."),
    ("21:12", "Emanuele Sciarra"): ("info",
        "Le serate con sponsor tipo materassi e depuratori possono far guadagnare 500-600€; serve "
        "garantire almeno 30 coppie di partecipanti."),
    ("21:17", "Emanuele Sciarra"): ("domanda",
        "Chiede a Emidio Cerasani un aiuto per un programma di massima (orari indicativi di partenza "
        "e ritorno) per la gita a Corinaldo, da girare a un'agenzia per avere un preventivo."),
    ("21:19", "Emanuele Sciarra"): ("info",
        "Lunedì sentirà Pikkitt per vedere se possono dare la sala per la riunione/evento."),
    ("21:22", "Dante Caniglia"): ("info",
        "Presenta un'app comunitaria che sta sviluppando (adattata da un progetto simile per "
        "Avezzano): gratuita per associazioni e proloco per pubblicare eventi e notifiche alla "
        "popolazione, con un tab dedicato anche al Comune; senza login per gli utenti, con "
        "possibilità di donazioni e di sponsorizzazioni a pagamento per attività locali. Al momento è "
        "online su un server di appoggio, sarà pubblicata su Google entro 15-20 giorni. Link: "
        "https://san-benedetto-eventi.vercel.app/ (su Android: menu con i tre puntini > \"Installa\" "
        "o \"Aggiungi scorciatoia\"; su iOS: tasto Condividi > \"Aggiungi a Home\")."),
    ("21:26", "Dante Caniglia"): ("info",
        "Rassicura sulla privacy dell'app: il server è a suo nome, non pubblico, e cancellerà i dati "
        "non appena tutti l'avranno vista/provata."),
    ("21:46", "Emanuele Sciarra"): ("info",
        "Pensa che l'idea dell'app di Dante sia buona: consiglia di parlarne anche con Pikkitt, "
        "perché potrebbe essere utile anche per loro, e se lanciata/appoggiata dal Comune potrebbe "
        "avere benefici."),
    ("21:48", "Dante Caniglia"): ("info",
        "Condivide come esempio il canale WhatsApp ufficiale del Comune di San Benedetto dei Marsi, "
        "facendo notare quanti post pubblica: https://whatsapp.com/channel/0029Vb1K85jJP213lZOSpK2S"),
}

MEDIA_OVERRIDES = {
    (DATE, "17:01", "Dante Caniglia", "IMG-20260905-WA0117.jpg"):
        "Pubblicità Facebook (Shade Pro) di uno stand completo per fiere/eventi (gazebo + bandiera "
        "vela + tavolo, tutti personalizzabili con logo stampato) a 369€+IVA prezzo fisso.",
    (DATE, "17:13", "Emanuele Sciarra", "IMG-20260905-WA0118.jpg"):
        "Screenshot della chat del gruppo che mostra 311 messaggi non letti, con la didascalia "
        "scherzosa \"vi amo\" per la mole di messaggi scambiati sul logo.",
    (DATE, "18:54", "Antonio Aceto", "IMG-20260905-WA0123.jpg"):
        "Versione DEFINITIVA della maglietta del comitato con il nuovo logo, indicata dall'utente "
        "come immagine finale scelta tra le numerose bozze discusse nel pomeriggio.",
    (DATE, "18:54", "Antonio Aceto", "IMG-20260905-WA0124.jpg"):
        "Versione DEFINITIVA del logo del comitato, indicata dall'utente come immagine finale scelta "
        "tra le numerose bozze discusse nel pomeriggio.",
    (DATE, "19:50", "Dante Caniglia", "IMG-20260905-WA0150.jpg"):
        "Mappa/schema riassuntivo degli eventi proposti per il comitato nella stagione 2026-2027: "
        "gita a Corinaldo e Halloween (ottobre 2026), San Martino (novembre), Casa di Babbo Natale e "
        "Capodanno (dicembre), Capodanno/Befana/Sant'Antonio (gennaio 2027), Carnevale e San Gabriele "
        "(febbraio), Pasqua e Pasquetta (marzo), festa patronale San Vincenzo (giugno), Santa Maria "
        "Goretti e feste d'agosto con cantante (agosto); più una sezione su collaborazioni con "
        "Proloco, Misericordia, altre associazioni locali ed eventuali nuovi eventi/giochi.",
    (DATE, "19:59", "Emanuele Sciarra", "IMG-20260905-WA0153.jpg"):
        "Foto della signora referente per la sponsorizzazione dei materassi: propone di fissare una "
        "data per l'evento e decidere anche dove farlo.",
    (DATE, "20:01", "Dante Caniglia", "IMG-20260905-WA0154.jpg"):
        "Contatto di un'azienda di depuratori d'acqua (Aquapharma) a cui Dante ha scritto per una "
        "possibile sponsorizzazione, avendone acquistato uno personalmente.",
    (DATE, "21:31", "Costantino Mariani", "IMG-20260905-WA0195.jpg"):
        "Selfie serale di due uomini sorridenti, presumibilmente al concerto dei Santo California a "
        "Venere di cui si parlava in chat.",
    (DATE, "21:34", "Costantino Mariani", "IMG-20260905-WA0200.jpg"):
        "Foto ravvicinata di una bottiglia di birra Beck's su un tavolo — foto conviviale della "
        "serata.",
    (DATE, "21:56", "Elvis Ippoliti", "IMG-20260905-WA0211.jpg"):
        "Foto del concerto dei Santo California sul palco a Venere, la serata a cui il gruppo era "
        "stato invitato nel pomeriggio.",
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
skipped_logo_drafts = []

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
        if is_logo_draft(time_, fname):
            skipped_logo_drafts.append((time_, sender, fname))
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
print(f"bozze di logo/maglietta ignorate (finestra {LOGO_WINDOW_START}-{LOGO_WINDOW_END}): {len(skipped_logo_drafts)}")
print(f"gif di reazione travestite da mp4, ignorate: {skipped_reaction_gifs}")
