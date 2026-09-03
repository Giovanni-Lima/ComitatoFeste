using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class MemberProfilePhotoConfiguration : IEntityTypeConfiguration<MemberProfilePhoto>
{
    public void Configure(EntityTypeBuilder<MemberProfilePhoto> builder)
    {
        builder.ToTable("MemberProfilePhotos");

        builder.HasKey(p => p.Id);

        builder.Property(p => p.Content).IsRequired();

        builder.Property(p => p.ContentType)
            .IsRequired()
            .HasMaxLength(100);

        builder.Property(p => p.Sha256)
            .HasMaxLength(64)
            .IsFixedLength();

        // 1:1 con Member.
        builder.HasIndex(p => p.MemberId).IsUnique();

        builder.HasOne(p => p.Member)
            .WithOne(m => m.ProfilePhoto)
            .HasForeignKey<MemberProfilePhoto>(p => p.MemberId)
            .OnDelete(DeleteBehavior.Cascade);
    }
}
