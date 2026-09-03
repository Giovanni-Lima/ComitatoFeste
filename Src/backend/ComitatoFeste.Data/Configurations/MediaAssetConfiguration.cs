using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class MediaAssetConfiguration : IEntityTypeConfiguration<MediaAsset>
{
    public void Configure(EntityTypeBuilder<MediaAsset> builder)
    {
        builder.ToTable("MediaAssets", t =>
            t.HasCheckConstraint(
                "CK_MediaAssets_MediaType",
                "\"MediaType\" IN ('foto', 'audio', 'documento')"));

        builder.HasKey(a => a.Id);

        builder.Property(a => a.MediaType)
            .IsRequired()
            .HasMaxLength(20)
            .HasConversion(
                v => v.ToString().ToLowerInvariant(),
                v => Enum.Parse<MediaType>(v, true));

        builder.Property(a => a.FileName)
            .IsRequired()
            .HasMaxLength(260);

        builder.Property(a => a.StoragePath).HasMaxLength(500);

        // Relazione 1:1 con DigestPoint (FK + lato principale configurati in DigestPointConfiguration).
        builder.HasIndex(a => a.DigestPointId).IsUnique();
    }
}
