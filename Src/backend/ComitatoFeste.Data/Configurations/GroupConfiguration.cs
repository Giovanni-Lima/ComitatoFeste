using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class GroupConfiguration : IEntityTypeConfiguration<Group>
{
    public void Configure(EntityTypeBuilder<Group> builder)
    {
        builder.ToTable("Groups");

        builder.HasKey(g => g.Id);

        builder.Property(g => g.Name)
            .IsRequired()
            .HasMaxLength(200);

        builder.HasIndex(g => g.Name).IsUnique();

        builder.Property(g => g.CreatedAt)
            .IsRequired()
            .HasDefaultValueSql("now()");

        builder.HasMany(g => g.Members)
            .WithOne(m => m.Group)
            .HasForeignKey(m => m.GroupId)
            .OnDelete(DeleteBehavior.Cascade);

        builder.HasMany(g => g.IngestionRuns)
            .WithOne(r => r.Group)
            .HasForeignKey(r => r.GroupId)
            .OnDelete(DeleteBehavior.Cascade);

        // I DigestPoint vengono ripuliti attraverso la catena IngestionRun -> DigestPoint,
        // quindi la FK diretta sul gruppo resta Restrict (una sola catena di cascade).
        builder.HasMany(g => g.DigestPoints)
            .WithOne(d => d.Group)
            .HasForeignKey(d => d.GroupId)
            .OnDelete(DeleteBehavior.Restrict);
    }
}
