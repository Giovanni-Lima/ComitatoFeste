#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re, shutil, subprocess
from collections import defaultdict

HOME = os.path.expanduser("~")
SRC = os.path.join(HOME, "mnt", "ComitatoFeste", "Chat WhatsApp con Il branco dei pazzi 87")
EXPORT = os.path.join(HOME, "mnt", "ComitatoFeste", "Export")
DATE = "2026-09-03"

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
    ("07:38", "Dante Caniglia"): ("decisione",
        "Ha parlato con il presidente: sabato, in riunione, si farà una lista di cose da fare anche "
        "riguardo le pagine social; serve creare un account \"classe\", una nuova email (creata dal "
        "presidente), la PEC e altri dettagli. I social sono quindi rimandati a sabato."),
    ("07:39", "Elvis Ippoliti"): ("domanda",
        "Chiede quando sia stato deciso che sabato ci sia la riunione (non ne era al corrente)."),
    ("07:41", "Elvis Ippoliti"): ("info",
        "Ritiene comunque meglio parlare di queste cose a voce piuttosto che in chat."),
    ("10:25", "Antonio Aceto"): ("info",
        "Ha sentito gli \"85\" (comitato di un'altra classe): gli hanno detto di aspettare una decina "
        "di giorni finché non finiscono di pubblicare premi e ringraziamenti. Quando proporranno la "
        "gita dovranno farlo come \"classe 1987\" e non come \"comitato\", perché legalmente il "
        "comitato non è ancora costituito — loro (gli 85) avevano iniziato a pubblicare a fine "
        "novembre."),
    ("11:20", "Barbara Rizio"): ("domanda",
        "Chiede se la domanda della mattina (di Elvis) fosse proprio quella su quando sarà la "
        "prossima riunione."),
    ("11:41", "Alessandra Simonetti"): ("info",
        "La riunione l'aveva proposta Emanuele per sabato, quando è andato a parlare col sindaco (se "
        "non si sbaglia); al momento nessuno ha ancora risposto in merito."),
    ("11:44", "Antonio Aceto"): ("info",
        "Pare che Don Enzo sia andato al mare (secondo Emidio): bisogna aspettare che torni."),
    ("11:44", "Alessandro Di Benedetto"): ("domanda",
        "Fa notare che la data della riunione non è ancora stata decisa né comunicata."),
    ("11:45", "Emidio Cerasani"): ("info",
        "Don Enzo sta tornando stamattina, lo vedrà nel pomeriggio."),
    ("11:48", "Antonio Aceto"): ("decisione",
        "Chiede a Emidio di domandare a Don Enzo quando ci si può incontrare per organizzare la gita "
        "a Corinaldo."),
    ("11:50", "Alessandro Di Benedetto"): ("domanda",
        "Chiede se, non potendo avanzare proposte a nome del \"comitato 87\", anche la pagina "
        "Facebook debba essere a nome \"classe 87\", almeno fino alla costituzione legale prevista "
        "per l'anno nuovo."),
    ("14:14", "Dante Caniglia"): ("info",
        "Sostiene che, per la legge italiana, il comitato non può vendere nulla senza qualche "
        "compromesso; lotterie e raccolte fondi sono legali, la vendita no."),
    ("14:51", "Dante Caniglia"): ("decisione",
        "Propone la soluzione: non \"vendere\" ma fare una raccolta fondi con offerta minima, per "
        "restare nella legalità."),
    ("15:24", "Emanuele Sciarra"): ("domanda",
        "Chiede foto del corteo di Santa Maria Goretti (moto e macchina con la reliquia in primo "
        "piano), anche vecchie, per creare una bozza delle prossime magliette."),
    ("15:57", "Emilio Caniglia"): ("info",
        "Il presidente conferma: il comitato può vendere magliette, gadget ecc.: è legale, non "
        "tassato, e ci sarà un bilancio in forma semplificata."),
    ("16:00", "Emanuele Sciarra"): ("domanda",
        "Chiede conferma: stasera l'appuntamento è confermato alle 20:45 alla chiesa di Santa Maria "
        "Goretti?"),
    ("16:10", "Emilio Caniglia"): ("info",
        "Conferma l'appuntamento delle 20:45."),
    ("16:13", "Emilio Caniglia"): ("info",
        "Spiega perché è legale: non c'è scopo di lucro, per lo Stato il corrispettivo di una "
        "maglietta equivale a un'offerta al comitato; il problema si porrebbe solo senza tracciabilità "
        "(a nero) — con fattura e ricevute di vendita non ci sono problemi."),
    ("16:22", "Emilio Caniglia"): ("info",
        "Appena il comitato sarà ufficializzato, invierà una PEC al Comune per riservare lo spazio "
        "abitualmente destinato al Comitato; se le magliette useranno simboli religiosi, sarà "
        "informata la Curia."),
    ("16:26", "Emilio Caniglia"): ("decisione",
        "Conferma il punto di ritrovo di stasera: in piazza, dove aspetterà Osvaldo, per lo "
        "spostamento delle statue."),
    ("16:52", "Emanuele Sciarra"): ("domanda",
        "Chiede se qualcuno ha una piastra elettrica o a gas, per fare panini con la salsiccia."),
    ("16:53", "Emilio Caniglia"): ("info",
        "Segnala che le iniziative con somministrazione di cibi e bevande possono avere limitazioni; "
        "la soluzione è collaborare con la Pro Loco (l'incasso resta comunque solo al Comitato)."),
    ("16:55", "Emanuele Sciarra"): ("info",
        "Ha l'HACCP personalmente, ma serve anche il SAB (somministrazione alimenti e bevande): "
        "qualcuno ce l'ha libera."),
    ("16:56", "Emanuele Sciarra"): ("info",
        "Ha un gazebo 3x3 disponibile; verifica se un amico può prestare un furgoncino da porchetta."),
    ("17:11", "Emilio Caniglia"): ("info",
        "La somministrazione di cibo/bevande in stile sagra è problematica per un Comitato Feste "
        "Patronali: troppe norme e prescrizioni da rispettare."),
    ("17:34", "Luca Cicchelli"): ("domanda",
        "Propone di ripensare il primo premio della lotteria: invece dell'auto (circa 8000€ secondo "
        "Emanuele), usare quella cifra per creare una lotteria con più premi diversi."),
    ("18:37", "Elvis Ippoliti"): ("info",
        "Propone la crociera come secondo premio della lotteria, accanto all'auto; nota che la "
        "poltrona vinta da Tina Giarrante varrebbe intorno ai 7000€, quindi più di una crociera "
        "(poco dopo condivide uno screenshot con prezzi reali di crociere, 299-449€ a persona)."),
    ("18:47", "Ugo Trinchini"): ("info",
        "La poltrona (premio di una lotteria precedente) è costata sui 2000€, ma molti premi come "
        "quello sono stati offerti/donati."),
    ("20:58", "Emidio Cerasani"): ("info",
        "Indicazioni per raggiungere il gruppo stasera: arrivati a Santa Maria Goretti, salire alla "
        "chiesa grande passando per la sagrestia; c'è anche Don Enzo."),
    ("21:34", "Cesare Raglione"): ("domanda",
        "Si scusa di non essere riuscito ad arrivare, è appena tornato a casa; chiede di nuovo quando "
        "sarà la riunione."),
    ("21:45", "Emidio Cerasani"): ("info",
        "Risponde: non è stata ancora decisa la data della riunione."),
}

MEDIA_OVERRIDES = {
    (DATE, "13:38", "Elvis Ippoliti", "Altre_Idee_Gadget_Comitato_Feste_1987_con_FOTO_complete.pdf"):
        "PDF con altre idee di gadget per le feste del comitato, con foto — primo di un gruppo di 4 "
        "PDF condivisi insieme da Elvis con proposte per gadget/eventi.",
    (DATE, "13:38", "Elvis Ippoliti", "Catalogo_Nuove_Idee_Gadget_Comitato_Feste_1987_con_FOTO_complete.pdf"):
        "Catalogo PDF di nuove idee di gadget da proporre per le feste del comitato, con foto.",
    (DATE, "13:38", "Elvis Ippoliti", "Festa_prima_delle_Feste_Comitato_1987.pdf"):
        "PDF con la proposta \"Festa prima delle Feste\" per il comitato.",
    (DATE, "13:38", "Elvis Ippoliti", "Gadget_Comitato_Feste_Nati_nel_1987.pdf"):
        "PDF con proposte di gadget dedicati a chi è nato nel 1987.",
    (DATE, "14:21", "Elvis Ippoliti", "Eventi_Raccolta_Fondi_Comitato_Feste_1987_Schede_Approfondite.pdf"):
        "PDF con schede di approfondimento su possibili eventi di raccolta fondi per il comitato.",
    (DATE, "16:34", "Elvis Ippoliti", "Eventi_Bambini_Comitato_Feste_1987_con_FOTO.pdf"):
        "PDF con proposte di eventi per bambini per le feste del comitato (con foto), condiviso da "
        "Elvis nell'ambito della discussione sulle idee per la festa.",
    (DATE, "16:49", "Emanuele Sciarra", "IMG-20260903-WA0046.jpg"):
        "Screenshot di una ricerca/idea AI per arricchire le feste patronali di San Vincenzo e San "
        "Benedetto: rievocazione storica marruviana (corteo in abiti storici, mercato artigianale), "
        "percorso enogastronomico nel centro storico, concorso di infiorate artistiche — condiviso "
        "chiedendo un parere al gruppo (\"Che ne pensate?\").",
    (DATE, "18:43", "Elvis Ippoliti", "IMG-20260903-WA0062.jpg"):
        "Screenshot da crociere.com: prezzi di crociere nel Mediterraneo (Costa/MSC) da 299 a 449€ a "
        "persona — a supporto della proposta della crociera come premio della lotteria.",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0015.jpg"):
        "Foto dentro la chiesa: alcuni uomini del gruppo risistemano/fissano la statua della Madonna "
        "sul piedistallo dell'altare.",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0029.jpg"):
        "Altra foto dello stesso momento: la statua della Madonna viene sollevata e riposizionata "
        "sul piedistallo dell'altare.",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0020.jpg"):
        "Altra foto dello stesso momento (sistemazione della statua della Madonna sull'altare).",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0025.jpg"):
        "Altra foto dello stesso momento (sistemazione della statua della Madonna sull'altare).",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0028.jpg"):
        "Altra foto dello stesso momento (sistemazione della statua della Madonna sull'altare).",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0030.jpg"):
        "Altra foto dello stesso momento (sistemazione della statua della Madonna sull'altare).",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0019.jpg"):
        "Altra foto dello stesso momento (sistemazione della statua della Madonna sull'altare).",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0021.jpg"):
        "Altra foto dello stesso momento (sistemazione della statua della Madonna sull'altare).",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0022.jpg"):
        "Altra foto dello stesso momento (sistemazione della statua della Madonna sull'altare).",
    (DATE, "21:16", "Emidio Cerasani", "IMG-20260904-WA0024.jpg"):
        "Altra foto dello stesso momento (sistemazione della statua della Madonna sull'altare).",
    (DATE, "21:17", "Daniele Boscolo", "IMG-20260904-WA0009.jpg"):
        "Foto dentro un furgone: due uomini in posa scherzosa con due statue religiose (una con fiori "
        "in mano) durante il trasporto.",
    (DATE, "21:19", "Emidio Cerasani", "IMG-20260904-WA0012.jpg"):
        "Foto di gruppo (circa 14 persone) sull'altare della chiesa, accanto alla statua della Madonna "
        "appena risistemata e alle sedie del presbiterio: foto celebrativa a lavoro concluso.",
    (DATE, "21:19", "Emidio Cerasani", "IMG-20260904-WA0013.jpg"):
        "Altra versione della foto di gruppo sull'altare, a lavoro concluso.",
    (DATE, "21:19", "Emidio Cerasani", "IMG-20260904-WA0011.jpg"):
        "Altra versione della foto di gruppo sull'altare, a lavoro concluso.",
    (DATE, "21:19", "Emidio Cerasani", "IMG-20260904-WA0010.jpg"):
        "Altra versione della foto di gruppo sull'altare, a lavoro concluso.",
    (DATE, "21:19", "Emidio Cerasani", "IMG-20260903-WA0091.jpg"):
        "Altra versione della foto di gruppo sull'altare, a lavoro concluso.",
    (DATE, "21:45", "Emidio Cerasani", "IMG-20260903-WA0088.jpg"):
        "Foto notturna in piazza: il gruppo fissa con pannelli di legno la base della statua appena "
        "spostata, a conferma della buona riuscita dell'appuntamento organizzato per stasera.",
    (DATE, "21:45", "Emidio Cerasani", "IMG-20260903-WA0089.jpg"):
        "Altra foto dello stesso momento (fissaggio della statua in piazza).",
    (DATE, "21:45", "Emidio Cerasani", "IMG-20260903-WA0090.jpg"):
        "Altra foto dello stesso momento (fissaggio della statua in piazza).",
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

with open(os.path.join(HOME, f"whatsapp_parsed_{DATE}.json"), encoding="utf-8") as f:
    msgs = json.load(f)

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
            # regola 4/9/2026: sticker e GIF si ignorano, niente entry
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
