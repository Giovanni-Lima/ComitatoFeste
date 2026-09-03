using ComitatoFeste.Domain;

namespace ComitatoFeste.Importer;

/// <summary>Deriva <see cref="MediaType"/> e MIME type dall'estensione del file scaricato.</summary>
public static class MediaKind
{
    private static readonly Dictionary<string, (MediaType Type, string Mime)> Map = new(StringComparer.OrdinalIgnoreCase)
    {
        [".jpg"] = (MediaType.Foto, "image/jpeg"),
        [".jpeg"] = (MediaType.Foto, "image/jpeg"),
        [".png"] = (MediaType.Foto, "image/png"),
        [".webp"] = (MediaType.Foto, "image/webp"),
        [".gif"] = (MediaType.Foto, "image/gif"),
        [".heic"] = (MediaType.Foto, "image/heic"),

        [".ogg"] = (MediaType.Audio, "audio/ogg"),
        [".opus"] = (MediaType.Audio, "audio/ogg"),
        [".m4a"] = (MediaType.Audio, "audio/mp4"),
        [".mp3"] = (MediaType.Audio, "audio/mpeg"),
        [".wav"] = (MediaType.Audio, "audio/wav"),
        [".aac"] = (MediaType.Audio, "audio/aac"),

        // Nessun MediaType "video" a schema: i video restano "documento" ma con MIME corretto,
        // così l'endpoint li serve riproducibili e il frontend può mostrarli in un <video>.
        [".mp4"] = (MediaType.Documento, "video/mp4"),
        [".mov"] = (MediaType.Documento, "video/quicktime"),
        [".webm"] = (MediaType.Documento, "video/webm"),
        [".mkv"] = (MediaType.Documento, "video/x-matroska"),
        [".3gp"] = (MediaType.Documento, "video/3gpp"),
        [".avi"] = (MediaType.Documento, "video/x-msvideo"),

        [".pdf"] = (MediaType.Documento, "application/pdf"),
        [".doc"] = (MediaType.Documento, "application/msword"),
        [".docx"] = (MediaType.Documento, "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
        [".xls"] = (MediaType.Documento, "application/vnd.ms-excel"),
        [".xlsx"] = (MediaType.Documento, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
    };

    public static (MediaType Type, string Mime) Resolve(string fileName)
    {
        var ext = Path.GetExtension(fileName);
        return Map.TryGetValue(ext, out var hit)
            ? hit
            : (MediaType.Documento, "application/octet-stream");
    }
}
