namespace ComitatoFeste.Domain;

/// <summary>
/// Categoria di un punto del digest, corrisponde al campo <c>type</c> del JSON di ingestion.
/// Persistito come stringa minuscola ("decisione" | "domanda" | "media" | "info" | "rumore") con
/// CHECK lato DB. "Rumore" è assegnato dalla classificazione post-trascrizione dei vocali
/// (ComitatoFeste.Transcriber) ai contenuti senza valore informativo (saluti, reazioni, conferme
/// brevi): resta archiviato ma è escluso dalla timeline di default.
/// </summary>
public enum DigestPointType
{
    Decisione,
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
