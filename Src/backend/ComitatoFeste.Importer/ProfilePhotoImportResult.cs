namespace ComitatoFeste.Importer;

/// <summary>Esito della sincronizzazione delle foto profilo da <c>Export/profili/</c>.</summary>
public sealed class ProfilePhotoImportResult
{
    public int Added { get; set; }
    public int Updated { get; set; }
    public int Unchanged { get; set; }

    /// <summary>Membri del gruppo per cui non è stato trovato un file in <c>profili/</c>.</summary>
    public List<string> MembersWithoutPhoto { get; } = new();

    /// <summary>File in <c>profili/</c> che non corrispondono a nessun membro.</summary>
    public List<string> UnmatchedFiles { get; } = new();

    public List<string> Warnings { get; } = new();
}
