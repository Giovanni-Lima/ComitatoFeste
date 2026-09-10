using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class ImageThumbnailConfiguration : IEntityTypeConfiguration<ImageThumbnail>
{
    public void Configure(EntityTypeBuilder<ImageThumbnail> builder)
    {
        builder.ToTable("ImageThumbnails", t => t.HasCheckConstraint(
            "CK_ImageThumbnails_Kind", "\"Kind\" IN ('media', 'memberphoto')"));

        builder.HasKey(t => t.Id);

        builder.Property(t => t.Kind).IsRequired().HasMaxLength(16);
        builder.Property(t => t.SourceSha256).IsRequired().HasMaxLength(64).IsFixedLength();
        builder.Property(t => t.Content).IsRequired();
        builder.Property(t => t.ContentType).IsRequired().HasMaxLength(64);
        builder.Property(t => t.CreatedAt).IsRequired();

        // Una sola riga per sorgente+larghezza; è anche la chiave di lookup dell'endpoint.
        builder.HasIndex(t => new { t.Kind, t.SourceId, t.Width })
            .IsUnique()
            .HasDatabaseName("UX_ImageThumbnails_Kind_SourceId_Width");
    }
}
