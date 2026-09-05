# Pipeline WhatsApp → digest_<data>.json

Genera i file `Export/digest_<data>.json` (e le sottocartelle `Export/<data>/`
con i media rinominati) a partire dall'export della chat WhatsApp Android
("Esporta chat" → "Includi media"), per l'`ComitatoFeste.Importer`.

## Prerequisiti sulla VM del device (già presenti)

- Python 3
- `ffmpeg`/`ffprobe` (per distinguere i video veri dalle GIF di reazione)

## Come si genera un nuovo giorno

1. **Esporta di nuovo la chat** da WhatsApp Android ("Esporta chat" con
   media) e sovrascrivi
   `C:\ComitatoFeste\Chat WhatsApp con Il branco dei pazzi 87\Chat WhatsApp con Il branco dei pazzi 87.txt`
   (+ tutti i media). Più a lungo i partecipanti hanno aperto/riprodotto un
   media nell'app, più probabilità che finisca nell'export (vedi nota sotto
   su `<Media omessi>`).

2. **Parsa il `.txt`**:
   ```
   python3 parse_wa.py
   ```
   Legge `Chat WhatsApp con Il branco dei pazzi 87.txt`, scrive
   `~/whatsapp_parsed_full.json` (tutti i messaggi, tutte le date) nella
   home della sessione device-linked. Stampa anche qualche statistica di
   controllo (messaggi/mittenti/tipi per le date recenti — modifica lo
   script se serve un'altra data).

3. **Leggi i messaggi di testo del giorno** e scrivi/aggiorna un
   `build_digest_<MMGG>.py` dedicato (copia uno dei tre esistenti come
   base, cambia `DATE`). Per ogni giorno serve:
   - **`CURATED`**: dict `(time, sender) -> (type, text)` per i messaggi di
     testo davvero significativi (decisione/domanda/info). La maggior
     parte dei messaggi di testo è rumore (saluti, emoji, battute in
     dialetto, conferme brevi) e va lasciata fuori — lo script la conta e
     basta, non genera una entry.
   - **`MEDIA_OVERRIDES`**: dict `(date, time, sender, filename source) ->
     descrizione` per le foto/video/PDF il cui contenuto va descritto
     davvero (non un placeholder generico) — per scriverle bisogna
     guardare l'immagine/il documento, non indovinare dal nome del file.
   - I **vocali (audio)** NON si curano uno per uno: restano un placeholder
     "Vocale di X, non trascritto" (li riempie poi il Transcriber via
     Groq). Ogni vocale resta comunque una entry a sé, mai raggruppato o
     scartato come rumore.

4. **Esegui lo script**:
   ```
   python3 build_digest_<MMGG>.py
   ```
   Scrive `Export/digest_<data>.json` e popola `Export/<data>/` con i
   media rinominati (`HHMM_Nome-Cognome[-N].ext`). Non richiede permessi
   di cancellazione: i file della cartella non più prodotti in questo giro
   vengono spostati in `Export/_rimossi_<data>/` invece che eliminati (lo
   script controlla `existing_before - kept_filenames` a fine giro).

5. **Verifica** (sempre, prima di dire che è pronto):
   - conteggio entry per tipo, media mancanti (`file sorgente mancanti`
     deve essere `[]`), duplicati di `file` nel JSON (deve essere 0),
     numero di file su disco == numero di entry media nel JSON.

## Regole stabili (vedi anche `CLAUDE.md` alla radice del repo)

- **Ogni vocale va tenuto**, una entry per vocale anche se simile a uno
  precedente — l'audio non è mai "rumore" in questa fase.
- **Sticker e GIF si ignorano**: niente entry, niente copia in
  `Export/<data>/`. Riconoscimento per estensione (`.webp`, `.gif`).
- **Le GIF di reazione mascherate da `.mp4` si ignorano anch'esse**:
  WhatsApp le salva come `.mp4` muti e brevi, indistinguibili per
  estensione da un video vero. Prima di includere un `.mp4` si controlla
  con `ffprobe` se ha una traccia audio:
  ```
  ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 <file>
  ```
  Output vuoto = nessun audio = GIF, si scarta. Output non vuoto = video
  vero, si tiene. (`is_reaction_gif()` nei tre script fa già questo.)
- **Testo "rumore"** (saluti, emoji, conferme brevi, battute) si scarta in
  fase di curatela manuale (`CURATED`), non genera entry.
- **`<Media omessi>`** nel `.txt` = media che WhatsApp stesso ha escluso
  dall'export (di solito perché mai aperto nell'app sul telefono che ha
  fatto l'export) — non recuperabile, si segnala e basta (non si inventa
  un placeholder).
- **I link condivisi in un messaggio di testo vanno riportati per intero**
  nel testo di `CURATED`, non solo descritti (es. "condivide un link a un
  video Facebook: https://...") — altrimenti il punto è incompleto.

## Percorsi

- Repo/progetto: `C:\ComitatoFeste` (spostato da `C:\Digest` il 4/9/2026 —
  se trovi ancora `mnt/Digest` in uno script vecchio, va corretto).
- Export sorgente della pipeline: `C:\ComitatoFeste\Export\`.
- I file `whatsapp_parsed_*.json` intermedi restano nella home della
  sessione device-linked (non sono nel repo, sono usa-e-getta — si
  rigenerano sempre da `parse_wa.py`).
