namespace ComitatoFeste.Api.Contracts;

/// <summary>
/// Anteprima "unfurl" di un link condiviso in un punto del digest, ricavata dai meta tag
/// OpenGraph della pagina di destinazione. Tutti i campi tranne <see cref="Url"/> sono
/// facoltativi (una pagina può non esporre nulla di utile).
/// </summary>
public sealed record LinkPreviewDto
{
    /// <summary>L'URL richiesto (identico a quello passato dal frontend).</summary>
    public required string Url { get; init; }

    public string? Title { get; init; }

    public string? Description { get; init; }

    /// <summary>URL assoluto di <c>og:image</c>: il frontend lo carica in hotlink dal sito originale.</summary>
    public string? Image { get; init; }

    /// <summary><c>og:site_name</c>, altrimenti l'host della pagina finale (dopo i redirect).</summary>
    public string? SiteName { get; init; }
}
