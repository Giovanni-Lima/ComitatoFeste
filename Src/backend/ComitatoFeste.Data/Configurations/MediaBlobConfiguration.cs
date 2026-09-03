using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class MediaBlobConfiguration : IEntityTypeConfiguration<MediaBlob>
{
    public void Configure(EntityTypeBuilder<MediaBlob> builder)
    {
        builder.ToTable("MediaBlobs");

        builder.HasKey(b => b.Id);

        builder.Property(b => b.Content).IsRequired();

        builder.Property(b => b.ContentType)
            .IsRequired()
            .HasMaxLength(100);

        builder.Property(b => b.Sha256)
            .HasMaxLength(64)
            .IsFixedLength();

        // Relazione 1:1 con MediaAsset: i byte vivono qui, fuori dalle query sui metadati.
        builder.HasIndex(b => b.MediaAssetId).IsUnique();

        // Lookup per dedup di file identici tra rerun.
        builder.HasIndex(b => b.Sha256);

        builder.HasOne(b => b.MediaAsset)
            .WithOne(a => a.Blob)
            .HasForeignKey<MediaBlob>(b => b.MediaAssetId)
            .OnDelete(DeleteBehavior.Cascade);
    }
}
