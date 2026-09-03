using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class IngestionRunConfiguration : IEntityTypeConfiguration<IngestionRun>
{
    public void Configure(EntityTypeBuilder<IngestionRun> builder)
    {
        builder.ToTable("IngestionRuns");

        builder.HasKey(r => r.Id);

        builder.Property(r => r.WindowStart).IsRequired();
        builder.Property(r => r.WindowEnd).IsRequired();

        builder.Property(r => r.StartedAt)
            .IsRequired()
            .HasDefaultValueSql("now()");

        builder.Property(r => r.SourceFile).HasMaxLength(260);

        builder.HasIndex(r => new { r.GroupId, r.WindowStart, r.WindowEnd });

        builder.HasMany(r => r.DigestPoints)
            .WithOne(d => d.IngestionRun)
            .HasForeignKey(d => d.IngestionRunId)
            .OnDelete(DeleteBehavior.Cascade);
    }
}
