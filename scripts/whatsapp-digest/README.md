# Pipeline WhatsApp → digest_<data>.json

Genera i file `Export/digest_<data>.json` (e le sottocartelle `Export/<data>/`
con i media rinominati) a partire dall'export della chat WhatsApp Android
("Esporta chat" → "Includi media"), per l'`ComitatoFeste.Importer`.

**Dal 6/9/2026 l'export grezzo arriva sempre via Dropbox**, non più come
sottocartella scompattata a mano dentro il progetto: vedi il passo 1 e
"Percorsi" sotto.

**Dal 6/9/2026 la logica comune è in `digest_lib.py`** (parsing, copia
media, `is_reaction_gif`, `media_text`, il loop di costruzione, il
checkpoint): ogni `build_digest_MMGG.py` è ora solo un file dati (`DATE`,
`CURATED`, `MEDIA_OVERRIDES`, eventuali eccezioni del giorno) che chiama
`digest_lib.build_digest(...)`. Prima ogni script duplicava tutta la
logica — un bug fix (vedi "Regole stabili" sotto) era rimasto per giorni
non propagato ai vecchi script per questo motivo. Un bug fix/miglioramento
alla logica comune va fatto **solo** in `digest_lib.py`.

## Prerequisiti sulla VM del device (già presenti)

- Python 3 (pacchetto `requests`, usato da `transcribe_new.py`)
- `ffmpeg`/`ffprobe` (per distinguere i video veri dalle GIF di reazione)

## Come si genera un nuovo giorno

1. **Esporta di nuovo la chat** da WhatsApp Android ("Esporta chat" con
   media): il file arriva/si aggiorna nella root di Dropbox come
   `Chat WhatsApp con Il branco dei pazzi 87.zip` (~150 MB, contiene sia il
   `.txt` che tutti i media). La cartella Dropbox è quella dell'utente loggato
   (vista finora: `C:\Users\giova\Dropbox`, in altre sessioni
   `C:\Users\glima\Dropbox`).

   > **Usa SEMPRE e SOLO lo zip senza suffisso numerico.** Se nella cartella
   > trovi anche `Chat WhatsApp con Il branco dei pazzi 87_1.zip`, `_2.zip`,
   > ecc., **vanno ignorati**: sono copie vecchie che il download tiene quando
   > arriva un nuovo export con lo stesso nome. Lo zip senza suffisso è quello
   > corrente, anche se risulta più piccolo di un `_N.zip` (WhatsApp include
   > nel `.txt` solo le righe dei media effettivamente esportati in quella
   > finestra, quindi un export più recente può avere meno righe-media di uno
   > vecchio — è normale, non è un troncamento).

   Estrai lo zip per procedere (in una cartella di lavoro qualsiasi, non
   necessariamente dentro il repo — es. nella sessione cloud se manca una
   shell diretta sul PC, vedi nota sotto). Più a lungo i partecipanti hanno
   aperto/riprodotto un media nell'app, più probabilità che finisca
   nell'export (vedi nota sotto su `<Media omessi>`).

2. **Parsa il `.txt`** estratto dallo zip:
   ```
   python3 parse_wa.py
   ```
   (adatta `BASE`/`F` in cima allo script al percorso in cui hai estratto
   lo zip, se diverso dal default). Legge
   `Chat WhatsApp con Il branco dei pazzi 87.txt`, scrive
   `whatsapp_parsed_full.json` (tutti i messaggi, tutte le date). Stampa
   anche qualche statistica di controllo (messaggi/mittenti/tipi per le
   date recenti — modifica lo script se serve un'altra data). La funzione
   di parsing (`parse_messages`) è riusabile da altri script — vedi punto
   2-bis.

2-bis. **Trascrivi in anticipo i vocali nuovi** (regola aggiunta il
   15/9/2026 — vedi CLAUDE.md, "Trascrizione anticipata dei vocali"):
   ```
   python3 transcribe_new.py
   ```
   Recupera da solo i messaggi dopo `checkpoint.json` e chiama Groq Whisper
   (solo trascrizione, niente classificazione) su ogni vocale nuovo, con
   cache di resume in `.transcript_cache.json` (gitignored — se lo script
   si interrompe/va in rate-limit, rilancialo: riparte solo dai file non
   ancora in cache, senza ripagare quelli già trascritti). Scrive
   `nuovi_messaggi_<data>.json`: **leggi questo file per la curatela**
   (testo dei messaggi + trascrizioni dei vocali già inline), non più il
   `.txt` grezzo con `grep`/`sed` per i vocali — risparmia tool-call/token
   in sessione. Serve `requests` (`pip install requests` se manca) e la
   stessa chiave Groq del Transcriber (env `GROQ_API_KEY` o `key.txt` alla
   radice del repo).

3. **Leggi i messaggi (testo + trascrizioni)** e scrivi/aggiorna un
   `build_digest_<MMGG>.py` dedicato (copia uno degli esistenti come base,
   cambia `DATE` — la logica di costruzione vera e propria vive in
   `digest_lib.py`, il file del giorno resta solo dati). Per ogni giorno
   serve:
   - **`CURATED`**: dict `(time, sender) -> (type, text)` per i messaggi di
     testo davvero significativi (decisione/proposta/domanda/info —
     `proposta` per un'idea avanzata al gruppo ma non ancora decisa). La maggior
     parte dei messaggi di testo è rumore (saluti, emoji, battute in
     dialetto, conferme brevi) e va lasciata fuori — lo script la conta e
     basta, non genera una entry.
   - **`MEDIA_OVERRIDES`**: dict `(date, time, sender, filename source) ->
     descrizione` per le foto/video/PDF il cui contenuto va descritto
     davvero (non un placeholder generico) — per scriverle bisogna
     guardare l'immagine/il documento, non indovinare dal nome del file.
     Se nella foto/video sono ritratte persone, **non descriverne i tratti
     fisici** (corporatura, capelli, barba, viso, abbigliamento): solo
     azione/contesto — es. "un uomo sorride mostrando una bottiglia di
     birra", non "un uomo con testa rasata e barba folta sorride..."
     (regola aggiunta il 6/9/2026).
   - I **vocali (audio)**, con la trascrizione già disponibile dal punto
     2-bis, vanno classificati in curatela come il testo:
     - **`AUDIO_CURATED`**: dict `(date, time, sender, filename) ->
       (type, text)` per un vocale che è di per sé un argomento atomico —
       resta una entry propria col file tenuto, ma già classificato invece
       che lasciato al Transcriber.
     - **`AUDIO_MERGES`**: lista di gruppi
       `{"anchor_time", "anchor_sender", "type", "text", "members": [file,
       ...]}` per vocali "cloni" (anche di autori diversi) che ripetono lo
       stesso concetto — diventano **una sola** entry di sintesi, i file
       elencati in `members` si scartano.
     - **Vocale di rumore** (regola 19/9/2026): si mette in `AUDIO_CURATED`
       con type `"rumore"` (testo ignorato, es. `("rumore", "")`) e viene
       **buttato del tutto** — nessuna entry, file non copiato: né
       Importer né Transcriber lo vedranno mai. Va fatto per ogni vocale
       senza contenuto (saluti, battute, chiacchiere non legate al comitato).
     - Un vocale non coperto da nessuna delle tre strutture resta come prima
       (placeholder "non trascritto", lo classifica poi il Transcriber) —
       rete di sicurezza se la curatela non arriva a coprire tutto; in
       condizioni normali non dovrebbero restarne.
   - **Checkpoint**: mentre leggi i messaggi del giorno, aggiorna via via
     `scripts/whatsapp-digest/checkpoint.json` con l'ultimo messaggio
     effettivamente esaminato (data del digest, data/ora/mittente del
     messaggio) — non solo a fine giornata. Se il lavoro si interrompe a
     metà, si riparte da lì invece che rileggere il giorno da capo (regola
     aggiunta il 6/9/2026).

4. **Esegui lo script** (che chiama `digest_lib.build_digest(...)`):
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

- **Vocali "cloni" si accorpano** (`AUDIO_MERGES`), un vocale atomico va
  comunque classificato in curatela (`AUDIO_CURATED`) invece di lasciato al
  Transcriber — regola aggiunta il 15/9/2026, vedi punto 2-bis/3 sopra e
  CLAUDE.md. Solo un vocale non coperto da nessuno dei due resta come
  prima (placeholder). **Un vocale classificato "rumore" in curatela si scarta
  del tutto** (regola 19/9/2026, `AUDIO_CURATED` con type `"rumore"`).
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
  vero, si tiene. (`is_reaction_gif()` in `digest_lib.py` fa già questo.)
- **Testo "rumore"** (saluti, emoji, conferme brevi, battute) si scarta in
  fase di curatela manuale (`CURATED`), non genera entry.
- **`<Media omessi>`** nel `.txt` = media che WhatsApp stesso ha escluso
  dall'export (di solito perché mai aperto nell'app sul telefono che ha
  fatto l'export) — non recuperabile, si segnala e basta (non si inventa
  un placeholder).
- **I link condivisi in un messaggio di testo vanno riportati per intero**
  nel testo di `CURATED`, non solo descritti (es. "condivide un link a un
  video Facebook: https://...") — altrimenti il punto è incompleto.
- **Niente tratti fisici delle persone ritratte** nelle didascalie di
  `MEDIA_OVERRIDES`: solo azione/contesto (regola aggiunta il 6/9/2026,
  vedi punto 3 sopra).
- **Checkpoint dell'ultimo messaggio letto** in
  `scripts/whatsapp-digest/checkpoint.json`, aggiornato progressivamente
  durante la curatela (regola aggiunta il 6/9/2026, vedi punto 3 sopra).
- **Bug di deduplicazione (fix 6/9/2026, in `digest_lib.build_digest`)**:
  due messaggi consecutivi con stesso `(time, sender)` che matchano la
  stessa chiave in `CURATED` generavano un'entry duplicata per ciascuno.
  Ora ne genera una sola. Il refactor ha verificato che questo bug era
  presente, non corretto, in tutti gli script dei giorni 1-5/9/2026 (vedi
  `CLAUDE.md` per i dettagli su cosa questo implica per i dati già
  importati a DB).
- **Sondaggi WhatsApp (regola aggiunta l'8/9/2026)**: nel `.txt` un
  sondaggio è già un messaggio di testo normale (multi-riga), che inizia
  con `SONDAGGIO:` seguito dal titolo e da una riga `OPZIONE: <testo> (N
  voti)` per opzione — nessuna modifica al parser serve. Va sempre curato
  come **`proposta`** (mai `decisione`, anche se ha già dei voti al momento
  dell'export: il sondaggio resta aperto), riportando per intero domanda e
  tutte le opzioni con il conteggio voti. Se un messaggio successivo
  dichiara l'esito, va curato come `decisione` in una entry separata.
- **Menzioni di Giovanni Lima (regola aggiunta l'11/9/2026)**: quando un
  altro membro nomina Giovanni Lima in un messaggio, non è necessario
  creare un'entry in `CURATED` solo per questo (resta soggetto alle
  normali regole di curatela come qualsiasi altro messaggio: se è
  "rumore" si scarta comunque). In compenso, alla fine della sessione di
  export, nel recap finale a Giovanni va segnalato che è stato nominato
  (con orario, autore e un breve contesto), così può valutare se rispondere
  o intervenire, anche quando il messaggio non è finito nel digest.
- **Condivisione di posizione (regola aggiunta l'11/9/2026)**: nel `.txt`
  è una riga di testo con un link Google Maps (`posizione:
  https://maps.google.com/?q=lat,long`), non un media — nessuna voce in
  `MEDIA_OVERRIDES`. Statica (es. punto di ritrovo) → curata come un link
  qualsiasi, testo integrale in `CURATED`, tipo `info` (o `decisione` se è
  la posizione definitiva di un appuntamento già deciso). In tempo reale
  (`live location`) → sempre rumore, scartata in curatela.
- **Compleanni (regola aggiunta il 13/9/2026)**: un gruppo di
  "buongiorno"/"auguri" rivolti a un membro taggato → un solo punto
  `info` in `CURATED` all'orario del primo messaggio di auguri ("Oggi è
  il compleanno di `<Nome>`, il gruppo si scambia auguri in chat"), va
  automaticamente in cima al giorno essendo il primo in ordine
  cronologico. Dedotto dalla chat, non da un calendario a DB — funziona
  solo se il gruppo lo festeggia quel giorno. I singoli messaggi restano
  rumore, non generano entry a parte.
- **Chiusura giorni passati (regola aggiunta il 12/9/2026, automatica dal
  13/9/2026)**: `close_past_days.py` gira da solo a fine di
  `import-transcribe-aiven.ps1` (dopo Importer+Transcriber) — non serve più
  lanciarlo a mano a ogni export. Cancella da `Export/` i giorni con data <
  `digest_data` del checkpoint (json + cartella media + `_rimossi_<data>/`)
  — evita che l'Importer "resusciti" un punto cancellato dall'app (dedup
  media confrontato col DB attuale, non con uno storico). Vedi CLAUDE.md
  per il dettaglio del bug e perché è sicuro farlo senza verifica su Aiven.
  Per un check manuale/dry-run: `python close_past_days.py --dry-run`.

## Percorsi

- Repo/progetto: `C:\temp\ComitatoFeste` (spostato da `C:\Digest` il 4/9/2026,
  poi da `C:\ComitatoFeste` il 6/9/2026 — se trovi ancora `mnt/Digest` o un
  riferimento a `C:\ComitatoFeste` senza `temp` in uno script vecchio, va
  corretto).
- Export sorgente della pipeline (i `digest_<data>.json` già generati e i
  media rinominati): `C:\temp\ComitatoFeste\Export\`.
- **Export grezzo della chat (input)**: dal 6/9/2026 non è più dentro il
  repo, arriva come
  `C:\Users\giova\Dropbox\Chat WhatsApp con Il branco dei pazzi 87.zip`.
  Se in uno script vecchio trovi ancora `SRC` puntato dentro
  `...\ComitatoFeste\Chat WhatsApp con Il branco dei pazzi 87`, quel
  percorso presuppone lo zip già estratto lì manualmente — con il flusso
  Dropbox lo zip va estrattato altrove (es. nella cartella di lavoro della
  sessione cloud, se manca una shell diretta sul PC) e i percorsi degli
  script (`SRC` in `parse_wa.py`/`build_digest_MMGG.py`) vanno adattati di
  conseguenza per quel run.
- I file `whatsapp_parsed_*.json` intermedi sono usa-e-getta (non vanno nel
  repo) — si rigenerano sempre da `parse_wa.py`.
- **Se manca una shell diretta sul PC dell'utente** nella sessione
  device-linked (solo lettura/scrittura file + eventuale controllo remoto
  a click): estrai lo zip Dropbox e lancia `parse_wa.py`/
  `build_digest_MMGG.py` nell'ambiente cloud della sessione (Python e
  ffmpeg/ffprobe sono già disponibili lì), poi ricopia sul PC solo
  `Export\digest_<data>.json`, `Export\<data>\` e lo script
  `build_digest_MMGG.py` finito.
