namespace ComitatoFeste.Domain;

/// <summary>
/// Categoria di un punto del digest, corrisponde al campo <c>type</c> del JSON di ingestion.
/// Persistito come stringa minuscola ("decisione" | "proposta" | "domanda" | "media" | "info" |
/// "rumore") con CHECK lato DB.
/// "Proposta" è un'idea/proposta operativa avanzata al gruppo ma non ancora decisa o votata
/// ("potremmo...", "io farei...", "proviamo a..."); diventa "decisione" solo quando il gruppo la
/// conferma. "Rumore" è assegnato dalla classificazione post-trascrizione dei vocali
/// (ComitatoFeste.Transcriber) ai contenuti senza valore informativo (saluti, reazioni, conferme
/// brevi): resta archiviato ma è escluso dalla timeline di default.
/// </summary>
public enum DigestPointType
{
    Decisione,
    Proposta,
    Domanda,
    Media,
    Info,
    Rumore
}

/// <summary>
/// Tipo di file dietro un <see cref="DigestPoint"/> di tipo media (derivato dall'estensione in fase di ingestion).
/// Persistito come stringa minuscola ("foto" | "audio" | "documento") con CHECK lato DB.
/// </summary>
public enum MediaType
{
    Foto,
    Audio,
    Documento
}

/// <summary>
/// Ruolo di accesso di un <see cref="Member"/> al login "casereccio" (vedi AuthService).
/// Persistito come stringa minuscola ("lettore" | "amministratore") con CHECK lato DB.
/// Oggi nessun endpoint distingue i due ruoli: la colonna prepara future funzionalità
/// riservate agli amministratori.
/// </summary>
public enum MemberRole
{
    Lettore,
    Amministratore
}
