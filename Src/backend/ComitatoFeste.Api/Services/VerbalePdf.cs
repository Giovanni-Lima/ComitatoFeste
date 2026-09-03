using System.Globalization;
using QuestPDF.Fluent;
using QuestPDF.Helpers;
using QuestPDF.Infrastructure;

namespace ComitatoFeste.Api.Services;

/// <summary>
/// Rende il verbale (Markdown salvato in <c>Verbali.Content</c>) in un PDF A4.
/// Gestisce il sottoinsieme di Markdown che il modello effettivamente produce:
/// intestazioni <c>#</c> / <c>##</c>, elenchi <c>-</c>/<c>*</c>, grassetto <c>**…**</c>,
/// righe vuote come separatori di paragrafo.
/// </summary>
public static class VerbalePdf
{
    private static readonly CultureInfo It = CultureInfo.GetCultureInfo("it-IT");

    public static byte[] Render(string groupName, DateOnly date, string markdown)
    {
        var lines = markdown.Replace("\r\n", "\n").Split('\n');

        return Document.Create(doc =>
        {
            doc.Page(page =>
            {
                page.Size(PageSizes.A4);
                page.Margin(2, Unit.Centimetre);
                page.DefaultTextStyle(t => t.FontSize(11).FontColor(Colors.Grey.Darken4).LineHeight(1.35f));

                page.Header().PaddingBottom(14).Column(h =>
                {
                    h.Item().Text(groupName).FontSize(10).FontColor(Colors.Grey.Darken1);
                    h.Item().Text($"Verbale del {date.ToString("dd MMMM yyyy", It)}").FontSize(18).SemiBold();
                });

                page.Content().Column(col =>
                {
                    col.Spacing(5);
                    foreach (var raw in lines)
                    {
                        var line = raw.TrimEnd();
                        if (line.Length == 0)
                        {
                            col.Item().Height(3);
                            continue;
                        }

                        if (line.StartsWith("## "))
                            col.Item().PaddingTop(10).Text(line[3..].Trim())
                                .FontSize(13).Bold().FontColor(Colors.Blue.Darken2);
                        else if (line.StartsWith("# "))
                            col.Item().PaddingTop(10).Text(line[2..].Trim()).FontSize(15).Bold();
                        else if (line.StartsWith("- ") || line.StartsWith("* "))
                            col.Item().Row(r =>
                            {
                                r.ConstantItem(14).Text("•").FontColor(Colors.Grey.Medium);
                                r.RelativeItem().Text(t => Inline(t, line[2..].Trim()));
                            });
                        else
                            col.Item().Text(t => Inline(t, line));
                    }
                });

                page.Footer().PaddingTop(12).Text(t =>
                {
                    t.Span($"Generato il {DateTimeOffset.Now.ToString("dd/MM/yyyy HH:mm", It)}  ·  pag. ")
                        .FontSize(8).FontColor(Colors.Grey.Medium);
                    t.CurrentPageNumber().FontSize(8).FontColor(Colors.Grey.Medium);
                    t.Span(" / ").FontSize(8).FontColor(Colors.Grey.Medium);
                    t.TotalPages().FontSize(8).FontColor(Colors.Grey.Medium);
                });
            });
        }).GeneratePdf();
    }

    /// <summary>Emette gli span di una riga alternando il grassetto sui delimitatori <c>**</c>.</summary>
    private static void Inline(TextDescriptor text, string s)
    {
        var parts = s.Split("**");
        for (var i = 0; i < parts.Length; i++)
        {
            if (parts[i].Length == 0)
                continue;
            var span = text.Span(parts[i]);
            if (i % 2 == 1)
                span.Bold();
        }
    }
}
