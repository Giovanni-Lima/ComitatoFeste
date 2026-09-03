using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;

namespace ComitatoFeste.Data;

public class ComitatoFesteDbContext : DbContext
{
    public ComitatoFesteDbContext(DbContextOptions<ComitatoFesteDbContext> options)
        : base(options)
    {
    }

    public DbSet<Group> Groups => Set<Group>();
    public DbSet<Member> Members => Set<Member>();
    public DbSet<MemberProfilePhoto> MemberProfilePhotos => Set<MemberProfilePhoto>();
    public DbSet<IngestionRun> IngestionRuns => Set<IngestionRun>();
    public DbSet<DigestPoint> DigestPoints => Set<DigestPoint>();
    public DbSet<MediaAsset> MediaAssets => Set<MediaAsset>();
    public DbSet<MediaBlob> MediaBlobs => Set<MediaBlob>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Necessaria per l'indice GIN pg_trgm su DigestPoints.Text (fuzzy dedup applicativo).
        modelBuilder.HasPostgresExtension("pg_trgm");

        modelBuilder.ApplyConfigurationsFromAssembly(typeof(ComitatoFesteDbContext).Assembly);
    }
}
