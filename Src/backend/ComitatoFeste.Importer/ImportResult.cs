namespace ComitatoFeste.Importer;

/// <summary>Esito dell'import di un singolo file <c>digest_&lt;data&gt;.json</c>.</summary>
public sealed class ImportResult
{
    public required string SourceFile { get; init; }
    public int RunId { get; set; }

    public int EntriesRead { get; set; }
    public int PointsInserted { get; set; }
    public int DuplicatesSkipped { get; set; }
    public int FuzzyDuplicatesSkipped { get; set; }
    public int MembersCreated { get; set; }

    public int MediaStored { get; set; }
    public int MediaFilesMissing { get; set; }

    public List<string> Warnings { get; } = new();
}
