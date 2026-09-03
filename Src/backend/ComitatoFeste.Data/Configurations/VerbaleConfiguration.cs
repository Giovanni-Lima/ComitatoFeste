using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class VerbaleConfiguration : IEntityTypeConfiguration<Verbale>
{
    public void Configure(EntityTypeBuilder<Verbale> builder)
    {
        builder.ToTable("Verbali");

        builder.HasKey(v => v.Id);

        builder.Property(v => v.Content).IsRequired();

        builder.Property(v => v.Model).IsRequired().HasMaxLength(60);

        builder.Property(v => v.GeneratedAt).IsRequired().HasDefaultValueSql("now()");

        // Un verbale per gruppo e per giorno: la seconda richiesta lo trova qui e non rigenera.
        builder.HasIndex(v => new { v.GroupId, v.Date })
            .IsUnique()
            .HasDatabaseName("UX_Verbali_Group_Date");

        builder.HasOne(v => v.Group)
            .WithMany(g => g.Verbali)
            .HasForeignKey(v => v.GroupId)
            .OnDelete(DeleteBehavior.Cascade);
    }
}
