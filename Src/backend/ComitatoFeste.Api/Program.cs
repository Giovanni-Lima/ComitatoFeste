using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
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

// Login "casereccio": passphrase condivisa da env COMITATOFESTE_AUTH_PASSWORD o config Auth:Password.
builder.Services.AddSingleton<AuthService>();

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
