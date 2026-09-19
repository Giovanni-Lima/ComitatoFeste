using Microsoft.EntityFrameworkCore;
using Pgvector.EntityFrameworkCore;

namespace ComitatoFeste.Data;

/// <summary>
/// Unico punto in cui si configura il provider Npgsql per <see cref="ComitatoFesteDbContext"/>.
/// Il modello contiene una colonna <c>vector</c> (embedding), quindi OGNI consumatore del
/// contesto — anche l'Importer e il Transcriber, che non li usano — deve abilitare
/// <c>UseVector()</c>, altrimenti EF fallisce nel costruire il modello. Passare da qui invece
/// di chiamare <c>UseNpgsql</c> direttamente evita di dimenticarselo.
/// </summary>
public static class ComitatoFesteDbOptionsExtensions
{
    public static DbContextOptionsBuilder UseComitatoFesteNpgsql(
        this DbContextOptionsBuilder builder, string? connectionString) =>
        builder.UseNpgsql(connectionString, o => o.UseVector());

    public static DbContextOptionsBuilder<TContext> UseComitatoFesteNpgsql<TContext>(
        this DbContextOptionsBuilder<TContext> builder, string? connectionString) where TContext : DbContext =>
        builder.UseNpgsql(connectionString, o => o.UseVector());
}
