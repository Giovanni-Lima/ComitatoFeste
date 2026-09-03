namespace ComitatoFeste.Domain;

/// <summary>
/// Categoria di un punto del digest, corrisponde al campo <c>type</c> del JSON di ingestion.
/// Persistito come stringa minuscola ("decisione" | "domanda" | "media" | "info") con CHECK lato DB.
/// </summary>
public enum DigestPointType
{
    Decisione,
    Domanda,
    Media,
    Info
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
