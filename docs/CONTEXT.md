# Contesto completo del progetto

Questo documento raccoglie la storia e le decisioni prese finora, per chi
(umano o Claude) riprende il lavoro senza aver visto le conversazioni
precedenti. `CLAUDE.md` importa questo file: tienilo aggiornato quando
cambiano decisioni importanti, ma non gonfiarlo di dettagli minuti — quelli
vanno nei commit/PR.

## Obiettivo del progetto

Riassumere automaticamente ogni giorno la chat WhatsApp del gruppo
"Comitato feste 87" (comitato organizzatore di eventi/feste paesane),
producendo un digest strutturato di ciò che conta — decisioni prese,
domande aperte, informazioni condivise (bandi, date, budget) — scartando
saluti/reazioni/rumore, e conservando i media rilevanti (foto, PDF, vocali)
con i relativi file scaricati e rinominati.

## Pipeline end-to-end (visione completa, solo in parte costruita)

1. **Ingestion** — un agente Claude legge la chat su web.whatsapp.com
   tramite l'estensione Claude-in-Chrome (browser reale dell'utente, click/
   scroll/lettura DOM) su una finestra temporale data (obiettivo finale:
   24h, per gestire il volume reale di messaggi vocali). Per ogni messaggio
   significativo produce una entry `{date, time, author, type, text, file}`
   con `type` ∈ `decisione | domanda | media | info`. Per i media (foto,
   documenti, vocali) scarica il file, lo rinomina
   `HHMM_Autore_breve-descrizione.estensione` e lo archivia in una
   sottocartella per data. **Tutti** i vocali vanno scaricati (non solo
   quelli "significativi"), perché lo scopo finale è un pass giornaliero
   senza intervento manuale messaggio-per-messaggio; se WhatsApp mostra una
   trascrizione la si cattura, altrimenti si marca "non trascritto" ma il
   file audio va comunque salvato.
2. **Persistenza** (questo repo) — i dati finiscono in Postgres via questo
   servizio .NET EF Core Code-First, invece che restare solo in file JSON
   sparsi sul filesystem dell'utente.
3. **Trascrizione audio** (da fare) — Groq Whisper API (large-v3 o
   large-v3-turbo, tier gratuito 2000 req/giorno) per trascrivere i vocali
   non trascritti da WhatsApp; Claude non può ascoltare audio nativamente,
   serve questo passaggio esterno prima che un LLM possa ragionarci sopra.
4. **API CRUD** (questo repo, base già scritta) — Web API .NET per leggere/
   scrivere i dati.
5. **Deploy** (da fare) — `docker-compose` con Postgres + servizio API.
6. **Frontend timeline** (da fare) — pagina HTML che mostra il digest in
   ordine cronologico, filtrabile per autore e tipo; consuma
   `GET /api/digestpoints`.

## Limiti noti della fase di ingestion (non risolti, l'utente li ha accettati per ora)

- **Niente API ufficiale WhatsApp** per un gruppo personale non-business:
  scartate le librerie non ufficiali (es. Baileys, whatsapp-web.js) per
  rischio ban dell'account.
- **"Esporta chat" di WhatsApp Web** non ha l'opzione "includi media" (a
  differenza dell'app mobile) — non utilizzabile come scorciatoia bulk.
- Il flusso attuale è **a due fasi manuali**: una sessione Claude-in-Chrome
  separata per leggere/scaricare dalla chat reale, e una sessione con il
  computer collegato per organizzare i file/JSON sul filesystem
  dell'utente — non ottimizzato, l'utente ha scelto di rimandare
  l'ottimizzazione ("poi capiamo quando e se ottimizzare").
- Il download dei media tramite l'estensione Claude-in-Chrome non è
  visibile a un ambiente cloud sandboxato: va gestito con il computer
  dell'utente collegato (bridge dispositivo), non da un container remoto.

## Dove vivono oggi i dati sorgente (sul PC Windows dell'utente)

- `C:\Digest\Export\digest_<data>.json` — un file per giorno, entry come
  in `docs/sample-digest_2026-09-01.json` (esempio reale allegato a questo
  repo).
- `C:\Digest\Export\<data>\` — media scaricati e rinominati per quel
  giorno (`HHMM_Autore_breve-descrizione.ext`).

Import di questi JSON in Postgres: non ancora scritto. Un semplice script/
endpoint che legge `digest_<data>.json`, risolve/crea `Group` e `Member`
per `GroupId+DisplayName`, crea un `IngestionRun` per il batch, e inserisce
un `DigestPoint` per entry (con `MediaAsset` collegato se `file != null`)
è il prossimo passo naturale per collegare pipeline e database.

## Perché lo schema è fatto così

Cinque tabelle, PascalCase, **senza tabella alias** (rimossa su richiesta
esplicita — vedi "domanda aperta" in `CLAUDE.md`):

- **Groups** — un gruppo WhatsApp monitorato.
- **Members** — un partecipante, identificato dal `DisplayName` esatto
  mostrato da WhatsApp in quel gruppo (unico per gruppo).
- **IngestionRuns** — una esecuzione della pipeline su una finestra
  temporale; i `DigestPoints` referenziano il run che li ha prodotti, così
  un rerun su una finestra sovrapposta è riconciliabile/annullabile come
  unità (cancellare un run cancella a cascata i suoi punti).
- **DigestPoints** — un punto significativo estratto dalla chat (la riga
  che corrisponde a una entry del JSON).
- **MediaAssets** — il file scaricato dietro un DigestPoint di tipo media
  (relazione 1:1), con metadati di trascrizione per l'audio.

### Dedup a due livelli (il motivo è emerso da dati reali)

Un solo vincolo "ovvio" (es. gruppo+autore+minuto) non basta, per due
problemi osservati concretamente nella chat reale del 2026-09-01:

1. **Falsi positivi**: lo stesso autore può mandare due messaggi vocali
   diversi nello stesso minuto (es. Emanuele Sciarra, due vocali diversi
   entrambi taggati 22:26) — un vincolo che ignora il testo li tratterebbe
   erroneamente come duplicati.
2. **Rerun con testo leggermente diverso**: due passate della pipeline
   sulla stessa finestra possono descrivere lo stesso messaggio WhatsApp
   con parole diverse (parafrasi), quindi un match esatto non li
   riconoscerebbe come duplicati quando in realtà lo sono.

Soluzione:
- **Vincolo UNIQUE hard** su `(GroupId, MemberId, OccurredAt, Text)` —
  economico, blocca i rerun letterali (stesso testo esatto), non genera
  falsi positivi sul caso (1) perché include il testo.
- **Indice GIN pg_trgm** su `DigestPoints.Text` — pensato per una query
  applicativa con `similarity(text, $1) > soglia` che intercetti il caso
  (2), le parafrasi tra run diversi, cosa che un vincolo DB da solo non
  può fare.

## Cronologia decisioni rilevanti

- Schema iniziale con tabella `MemberAliases` per gestire nickname multipli
  → rimossa su richiesta ("per adesso togliamo gli alias"), sostituita da
  match esatto + normalizzazione facoltativa lato service (non ancora
  implementata, vedi domanda aperta).
- Identificatori tradotti da snake_case a PascalCase tra virgolette su
  richiesta esplicita, per coerenza con l'output di default di EF
  Core/Npgsql.
- Architettura complessiva (Postgres + .NET Web API + docker-compose +
  Groq Whisper + pagina timeline) discussa e concordata prima di iniziare
  questo servizio; questo repo copre solo il livello dati/API.
