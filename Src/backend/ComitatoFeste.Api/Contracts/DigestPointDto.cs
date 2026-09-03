namespace ComitatoFeste.Api.Contracts;

/// <summary>Un punto del digest come esposto dalla API (nessuna navigazione EF ciclica).</summary>
public sealed record DigestPointDto
{
    public int Id { get; init; }

    /// <summary>Istante del messaggio (UTC).</summary>
    public DateTimeOffset OccurredAt { get; init; }

    public int AuthorId { get; init; }

    public required string Author { get; init; }

    /// <summary>Endpoint della foto profilo dell'autore, se disponibile.</summary>
    public string? AuthorPhotoUrl { get; init; }

    /// <summary>decisione | domanda | media | info</summary>
    public required string Type { get; init; }

    public required string Text { get; init; }

    /// <summary>Presente solo per i punti con un media collegato.</summary>
    public MediaDto? Media { get; init; }
}

/// <summary>Metadati del media collegato a un punto. I byte NON viaggiano qui: si scaricano da <see cref="ContentUrl"/>.</summary>
public sealed record MediaDto
{
    public int Id { get; init; }

    /// <summary>foto | audio | documento</summary>
    public required string MediaType { get; init; }

    public required string FileName { get; init; }

    public long? SizeBytes { get; init; }

    /// <summary>MIME del contenuto, se il blob è presente.</summary>
    public string? ContentType { get; init; }

    /// <summary>true se il blob binario è disponibile (scaricabile da <see cref="ContentUrl"/>).</summary>
    public bool HasContent { get; init; }

    public bool IsTranscribed { get; init; }

    public string? TranscriptionText { get; init; }

    /// <summary>Endpoint da cui scaricare/mostrare il file originale, se disponibile.</summary>
    public string? ContentUrl { get; init; }
}
