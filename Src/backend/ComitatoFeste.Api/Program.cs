using ComitatoFeste.Api.Services;
using ComitatoFeste.Data;
using Microsoft.EntityFrameworkCore;
using QuestPDF.Infrastructure;

// QuestPDF Community License: gratuita per privati e aziende sotto 1M$ di fatturato.
QuestPDF.Settings.License = LicenseType.Community;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<ComitatoFesteDbContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("ComitatoFeste")));

// Client Groq per il verbale giornaliero (chiave da env GROQ_API_KEY o config Groq:ApiKey).
builder.Services.AddHttpClient<GroqRecapClient>(c => c.Timeout = TimeSpan.FromMinutes(2));

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

const string DevCors = "dev";
builder.Services.AddCors(options => options.AddPolicy(DevCors, policy => policy
    .WithOrigins("http://localhost:5173", "http://localhost:3000")
    .AllowAnyHeader()
    .AllowAnyMethod()));

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
    app.UseCors(DevCors);
}

app.MapControllers();

app.Run();
