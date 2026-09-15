# Prompt: esegui solo l'export/curatela del digest WhatsApp

Copia-incolla questo prompt (o linkalo) a una sessione Claude Code aperta
su questo repo (`C:\temp\ComitatoFeste`), con accesso diretto al PC
dell'utente (non sandbox cloud — serve leggere Dropbox e scrivere `Export/`).

**Scope: SOLO l'export/curatela.** Non lanciare `Importer`, `Transcriber`
né notifiche push — questo prompt si ferma subito dopo aver verificato il
digest generato. Import/trascrizione/push restano un passo separato,
deciso a parte dall'utente.

---

## Cosa fare

1. **Leggi prima `CLAUDE.md`** (sezione "Generazione di `digest_<data>.json`
   dall'export WhatsApp") **e `scripts/whatsapp-digest/README.md`** — sono
   la fonte di verità per tutte le regole di curatela (vocali cloni
   accorpati/atomici classificati in curatela, sticker/GIF ignorati, GIF
   di reazione mascherate da `.mp4`, link riportati per intero, iterazioni
   di design, sondaggi, menzioni di Giovanni Lima, condivisione di
   posizione, compleanni). Non duplicarle qui a memoria: se in dubbio,
   rileggile da lì — potrebbero essere cambiate da quando è stato scritto
   questo prompt.

2. **Leggi il checkpoint**: `scripts/whatsapp-digest/checkpoint.json` dice
   `digest_data` (ultimo giorno con un digest scritto) e
   `ultimo_messaggio_letto` (data/ora/mittente esatti da cui ripartire).

3. **Trova l'export più recente** in Dropbox
   (`C:\Users\<utente>\Dropbox\Chat WhatsApp con Il branco dei pazzi
   87.zip` — **mai** un `..._1.zip`/`_2.zip`, sono copie vecchie anche se
   più grandi). Se ha la stessa dimensione/timestamp dell'ultimo già
   processato, non c'è nulla di nuovo: fermati e dillo all'utente, chiedi
   di rifare l'esportazione da WhatsApp.

4. **Estrai lo zip** in una cartella di lavoro qualsiasi (es. Desktop, non
   necessariamente nel repo).

5. **Verifica/prepara i percorsi attesi dagli script.** `parse_wa.py` e
   `digest_lib.py` si aspettano l'estrazione in
   `~/mnt/ComitatoFeste/Chat WhatsApp con Il branco dei pazzi 87/` e
   scrivono in `~/mnt/ComitatoFeste/Export/`. Su una macchina dove
   `ln -s` non crea veri symlink (capita su Windows senza privilegio
   symlink: verificalo con PowerShell — `Get-Item <path> | Format-List
   Attributes` deve mostrare `ReparsePoint`, altrimenti è una copia reale),
   dopo aver generato il digest **ricopia a mano** `digest_<data>.json` e
   la cartella media da `~/mnt/ComitatoFeste/Export/` alla vera
   `Export/` del repo, poi elimina `~/mnt` (era solo staging temporaneo,
   non lasciarlo in giro). Se invece i symlink funzionano davvero, scrivono
   già nella `Export/` vera e questo passo non serve.

6. **Parsa il `.txt`**: `python parse_wa.py` (su questa macchina il comando
   è `python`, non `python3`) — scrive `whatsapp_parsed_full.json`, da cui
   dipende `build_digest_MMGG.py` al punto 10 più avanti (non serve invece
   per il punto 7 sotto, che fa la propria scansione del `.txt`).

7. **Trascrivi in anticipo i vocali nuovi**: `python transcribe_new.py`
   (vedi CLAUDE.md, "Trascrizione anticipata dei vocali") — recupera da
   solo i messaggi dopo il checkpoint e trascrive con Groq Whisper ogni
   vocale nuovo (cache di resume in `.transcript_cache.json`: se lo script
   si interrompe/va in rate-limit, rilancialo, riparte dai soli file
   mancanti). Scrive `nuovi_messaggi_<data>.json`.

8. **Leggi i messaggi nuovi** da `nuovi_messaggi_<data>.json` (testo +
   trascrizioni dei vocali già inline, non serve più `grep`/`sed` sul
   `.txt` grezzo per gli audio) prima di scrivere codice — servono per
   decidere rumore/domanda/proposta/info, guardare le foto (mai descrivere
   tratti fisici delle persone), verificare menzioni di Giovanni Lima, e
   **riconoscere vocali "cloni"** che ripetono lo stesso concetto (anche
   di autori diversi) da accorpare in curatela.

9. **Scrivi/estendi `build_digest_MMGG.py`** per il giorno interessato
   (nuovo file se è un giorno nuovo, altrimenti estendi `CURATED`/
   `MEDIA_OVERRIDES` di quello esistente — copia uno recente come base per
   lo stile). Per gli audio, oltre a `CURATED`/`MEDIA_OVERRIDES`:
   - `AUDIO_CURATED`: vocali atomici, classificati ma tenuti come entry
     propria (file incluso).
   - `AUDIO_MERGES`: gruppi di vocali cloni accorpati in una sola entry di
     sintesi, file scartati.
   Un vocale non coperto da nessuno dei due resta come prima (placeholder,
   lo classifica poi il Transcriber) — rete di sicurezza.
   Aggiorna anche il docstring in cima con un riassunto di cosa c'è nella
   finestra curata.

10. **Esegui lo script** (`python build_digest_MMGG.py`). Copia l'output
    nella `Export/` vera se necessario (punto 5).

11. **Verifica** (sempre, prima di dire che è pronto): conteggio entry per
    tipo, `file sorgente mancanti` deve essere `[]`, numero di file su disco
    in `Export/<data>/` == numero di entry con `file` nel JSON.

12. **Non lanciare `close_past_days.py`** in questo prompt: gira già in
    automatico a fine di `import-transcribe-aiven.ps1` (un passo
    successivo, fuori scope qui).

13. **Riporta all'utente**: cosa è stato curato (riassunto puntato per
    tipo/argomento), gli eventuali accorpamenti di vocali cloni fatti, i
    conteggi di verifica, ed eventuali menzioni di Giovanni Lima (orario,
    autore, contesto) anche se non finite nel digest. Chiudi dicendo
    esplicitamente che import/trascrizione/notifica push **non** sono
    stati eseguiti e restano un passo a parte.

## Cosa NON fare

- Non lanciare `ComitatoFeste.Importer` / `ComitatoFeste.Transcriber`.
- Non impostare `COMITATOFESTE_HOOK_URL`/`_SECRET` né chiamare
  `/api/push/broadcast`.
- Non toccare Aiven o il Postgres locale.
- Non committare automaticamente: prepara i file, chiedi conferma
  all'utente prima di `git commit` (a meno che non l'abbia già chiesto lui
  di procedere).
