using System.IO.Compression;
using System.Net;
using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
using Microsoft.AspNetCore.ResponseCompression;
using Microsoft.AspNetCore.StaticFiles;
using Microsoft.EntityFrameworkCore;
using QuestPDF.Infrastructure;

// QuestPDF Community License: gratuita per privati e aziende sotto 1M$ di fatturato.
QuestPDF.Settings.License = LicenseType.Community;

var builder = WebApplication.CreateBuilder(args);

// In produzione (Render) la porta di ascolto arriva dall'env PORT; in locale resta il
// default di Kestrel (vedi launchSettings.json).
var port = Environment.GetEnvironmentVariable("PORT");
if (!string.IsNullOrWhiteSpace(port))
    builder.WebHost.UseUrls($"http://0.0.0.0:{port}");

// Connessione: env COMITATOFESTE_CONNECTION (stessa convenzione di Importer/Transcriber),
// altrimenti ConnectionStrings:ComitatoFeste da appsettings.json.
var connectionString = Environment.GetEnvironmentVariable("COMITATOFESTE_CONNECTION")
                       ?? builder.Configuration.GetConnectionString("ComitatoFeste");

builder.Services.AddDbContext<ComitatoFesteDbContext>(options =>
    options.UseNpgsql(connectionString));

// Client Groq per il verbale giornaliero (chiave da env GROQ_API_KEY o config Groq:ApiKey).
builder.Services.AddHttpClient<GroqRecapClient>(c => c.Timeout = TimeSpan.FromMinutes(2));

// Anteprime dei link condivisi nei punti: cache in memoria + fetch OpenGraph. Il
// SocketsHttpHandler valida ogni connessione (redirect inclusi) via ConnectCallback,
// così si esce solo verso IP pubblici (guardia SSRF, vedi LinkPreviewService).
builder.Services.AddMemoryCache();
builder.Services.AddHttpClient<LinkPreviewService>(c =>
    {
        c.Timeout = TimeSpan.FromSeconds(6);
        c.MaxResponseContentBufferSize = 1024 * 1024;
    })
    .ConfigurePrimaryHttpMessageHandler(() => new SocketsHttpHandler
    {
        AllowAutoRedirect = true,
        MaxAutomaticRedirections = 3,
        AutomaticDecompression = DecompressionMethods.All,
        ConnectCallback = LinkPreviewService.SafeConnectAsync,
    });

// Login "casereccio": passphrase condivisa da env COMITATOFESTE_AUTH_PASSWORD o config Auth:Password.
builder.Services.AddSingleton<AuthService>();

// Thumbnail WebP per gli endpoint immagine (?w=), generati una volta e persistiti in
// ImageThumbnails. Scoped: usa il DbContext della richiesta.
builder.Services.AddScoped<ImageThumbnailer>();

// Chiavi VAPID per il Web Push (env COMITATOFESTE_VAPID_* o config Vapid:*).
builder.Services.AddSingleton<PushKeys>();

// Invio Web Push: typed client (un solo HttpClient riusato dal WebPushClient).
builder.Services.AddHttpClient<PushSender>();

// Compressione delle risposte testuali (JSON/HTML/JS/CSS/SVG): senza, l'API manda
// ~355 KB non compressi a ogni GET /api/digestpoints. La whitelist MIME di default
// esclude già image/audio/video/pdf (inutile ri-comprimere binari già compressi);
// aggiungiamo solo il manifest PWA. Level=Optimal: qui la risorsa scarsa è la banda,
// non la CPU (traffico basso, piano free), e con Optimal la stessa risposta scende a
// ~55-65 KB invece dei ~106 KB di Fastest. EnableForHttps: Render fa da proxy TLS, il
// client vede HTTPS quindi va abilitato — rischio BREACH trascurabile (token nell'header, non nel body).
builder.Services.AddResponseCompression(o =>
{
    o.EnableForHttps = true;
    o.Providers.Add<BrotliCompressionProvider>();
    o.Providers.Add<GzipCompressionProvider>();
    o.MimeTypes = ResponseCompressionDefaults.MimeTypes.Concat(new[] { "application/manifest+json" });
});
builder.Services.Configure<BrotliCompressionProviderOptions>(o => o.Level = CompressionLevel.Optimal);
builder.Services.Configure<GzipCompressionProviderOptions>(o => o.Level = CompressionLevel.Optimal);

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

const string DevCors = "dev";
builder.Services.AddCors(options => options.AddPolicy(DevCors, policy => policy
    .WithOrigins("http://localhost:5173", "http://localhost:3000")
    .AllowAnyHeader()
    .AllowAnyMethod()));

var app = builder.Build();

// Applica le migration in sospeso all'avvio: il primo boot contro un DB vuoto (es. il
// servizio Aiven appena creato) crea lo schema da solo. Se il DB non è raggiungibile
// l'avvio fallisce con un errore esplicito nei log — comportamento voluto in deploy.
using (var scope = app.Services.CreateScope())
{
    scope.ServiceProvider.GetRequiredService<ComitatoFesteDbContext>().Database.Migrate();
}

// Primo nella pipeline: comprime tutto ciò che passa (risposte testuali; i binari
// sono esclusi dalla whitelist MIME). Le risposte 304/206 non vengono compresse.
app.UseResponseCompression();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
    app.UseCors(DevCors);
}

// Frontend statico (wwwroot/index.html, vedi ComitatoFeste.Api.csproj): servito dalla
// stessa origine dell'API, così in produzione non serve CORS.
// Il provider MIME di default non conosce .webmanifest (manifest PWA): aggiungiamolo,
// altrimenti UseStaticFiles non serve il file e l'app non risulta installabile.
var contentTypes = new FileExtensionContentTypeProvider();
contentTypes.Mappings[".webmanifest"] = "application/manifest+json";
app.UseDefaultFiles();
app.UseStaticFiles(new StaticFileOptions { ContentTypeProvider = contentTypes });

app.MapControllers();

app.Run();
