namespace ComitatoFeste.Data;

/// <summary>
/// Risolve la chiave API di Groq condivisa da <c>ComitatoFeste.Transcriber</c> e
/// <c>ComitatoFeste.Api</c>: prima la variabile d'ambiente <c>GROQ_API_KEY</c>, poi un file
/// <c>key.txt</c> (in <c>.gitignore</c>) cercato risalendo dalla cartella di lavoro e da
/// quella dell'eseguibile fino alla radice del repo. Restituisce <c>null</c> se assente.
/// </summary>
public static class GroqKey
{
    public static string? Resolve()
    {
        var env = Environment.GetEnvironmentVariable("GROQ_API_KEY");
        if (!string.IsNullOrWhiteSpace(env))
            return env.Trim();

        foreach (var start in new[] { Directory.GetCurrentDirectory(), AppContext.BaseDirectory })
        {
            var dir = new DirectoryInfo(start);
            for (var i = 0; i < 8 && dir is not null; i++, dir = dir.Parent)
            {
                var path = Path.Combine(dir.FullName, "key.txt");
                if (!File.Exists(path))
                    continue;

                var text = File.ReadAllText(path).Trim();
                if (text.Length > 0)
                    return text;
            }
        }

        return null;
    }
}
