using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class MemberConfiguration : IEntityTypeConfiguration<Member>
{
    public void Configure(EntityTypeBuilder<Member> builder)
    {
        builder.ToTable("Members", t =>
            t.HasCheckConstraint(
                "CK_Members_Role",
                "\"Role\" IN ('lettore', 'amministratore')"));

        builder.HasKey(m => m.Id);

        builder.Property(m => m.DisplayName)
            .IsRequired()
            .HasMaxLength(200);

        builder.Property(m => m.Role)
            .IsRequired()
            .HasMaxLength(20)
            .HasDefaultValue(MemberRole.Lettore)
            .HasConversion(
                v => v.ToString().ToLowerInvariant(),
                v => Enum.Parse<MemberRole>(v, true));

        // Match sull'autore per DisplayName esatto: unico all'interno del gruppo.
        builder.HasIndex(m => new { m.GroupId, m.DisplayName }).IsUnique();

        builder.HasMany(m => m.DigestPoints)
            .WithOne(d => d.Member)
            .HasForeignKey(d => d.MemberId)
            .OnDelete(DeleteBehavior.Restrict);
    }
}
