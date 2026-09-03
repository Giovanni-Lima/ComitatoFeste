using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class DigestPointConfiguration : IEntityTypeConfiguration<DigestPoint>
{
    public void Configure(EntityTypeBuilder<DigestPoint> builder)
    {
        builder.ToTable("DigestPoints", t =>
            t.HasCheckConstraint(
                "CK_DigestPoints_Type",
                "\"Type\" IN ('decisione', 'domanda', 'media', 'info', 'rumore')"));

        builder.HasKey(d => d.Id);

        builder.Property(d => d.OccurredAt).IsRequired();

        builder.Property(d => d.Text).IsRequired();

        builder.Property(d => d.Type)
            .IsRequired()
            .HasMaxLength(20)
            .HasConversion(
                v => v.ToString().ToLowerInvariant(),
                v => Enum.Parse<DigestPointType>(v, true));

        // Dedup livello 1 — vincolo UNIQUE hard: blocca i rerun letterali (stesso testo esatto),
        // senza falsi positivi sui due vocali diversi dello stesso autore nello stesso minuto.
        builder.HasIndex(d => new { d.GroupId, d.MemberId, d.OccurredAt, d.Text })
            .IsUnique()
            .HasDatabaseName("UX_DigestPoints_Group_Member_OccurredAt_Text");

        // Dedup livello 2 — indice GIN pg_trgm: pensato per una query applicativa
        // similarity(Text, $1) > soglia che intercetti le riformulazioni tra run diversi.
        builder.HasIndex(d => d.Text)
            .HasMethod("gin")
            .HasOperators("gin_trgm_ops")
            .HasDatabaseName("IX_DigestPoints_Text_Trgm");

        builder.HasOne(d => d.MediaAsset)
            .WithOne(a => a.DigestPoint)
            .HasForeignKey<MediaAsset>(a => a.DigestPointId)
            .OnDelete(DeleteBehavior.Cascade);
    }
}
