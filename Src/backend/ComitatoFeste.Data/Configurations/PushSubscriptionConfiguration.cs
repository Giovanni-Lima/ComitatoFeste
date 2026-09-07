using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ComitatoFeste.Data.Configurations;

public class PushSubscriptionConfiguration : IEntityTypeConfiguration<PushSubscription>
{
    public void Configure(EntityTypeBuilder<PushSubscription> builder)
    {
        builder.ToTable("PushSubscriptions");

        builder.HasKey(s => s.Id);

        builder.Property(s => s.Endpoint).IsRequired();
        builder.Property(s => s.P256dh).IsRequired();
        builder.Property(s => s.Auth).IsRequired();
        builder.Property(s => s.UserAgent).HasMaxLength(400);

        builder.Property(s => s.CreatedAt).IsRequired().HasDefaultValueSql("now()");

        // L'endpoint identifica la subscription: una re-subscribe dallo stesso browser
        // fa upsert su questa riga invece di duplicarla.
        builder.HasIndex(s => s.Endpoint)
            .IsUnique()
            .HasDatabaseName("UX_PushSubscriptions_Endpoint");

        // La subscription resta anche se il membro sparisce (potrà essere ricollegata
        // o cancellata al primo invio fallito), quindi SET NULL e non Cascade.
        builder.HasOne(s => s.Member)
            .WithMany()
            .HasForeignKey(s => s.MemberId)
            .OnDelete(DeleteBehavior.SetNull);
    }
}
