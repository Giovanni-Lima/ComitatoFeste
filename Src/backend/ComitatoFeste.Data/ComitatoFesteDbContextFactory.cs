using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;

namespace ComitatoFeste.Data;

/// <summary>
/// Factory usata solo dal tooling <c>dotnet ef</c> (design time) per creare/applicare le migration
/// senza avviare l'host dell'API. La stringa di connessione può essere sovrascritta con la
/// variabile d'ambiente <c>COMITATOFESTE_CONNECTION</c>; il default punta al Postgres del docker-compose.
/// </summary>
public class ComitatoFesteDbContextFactory : IDesignTimeDbContextFactory<ComitatoFesteDbContext>
{
    public ComitatoFesteDbContext CreateDbContext(string[] args)
    {
        var connectionString =
            Environment.GetEnvironmentVariable("COMITATOFESTE_CONNECTION")
            ?? "Host=localhost;Port=5432;Database=postgres;Username=postgres;Password=postgres";

        var options = new DbContextOptionsBuilder<ComitatoFesteDbContext>()
            .UseNpgsql(connectionString)
            .Options;

        return new ComitatoFesteDbContext(options);
    }
}
