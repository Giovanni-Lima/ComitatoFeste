using ComitatoFeste.Domain;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.ChangeTracking;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using Pgvector;

namespace ComitatoFeste.Data.Configurations;

public class DigestPointEmbeddingConfiguration : IEntityTypeConfiguration<DigestPointEmbedding>
{
    /// <summary>Dimensione del vettore: deve coincidere con quella richiesta al modello di embedding.</summary>
    public const int Dimensions = 768;

    public void Configure(EntityTypeBuilder<DigestPointEmbedding> builder)
    {
        builder.ToTable("DigestPointEmbeddings");

        // PK = FK: un solo embedding per punto, cancellato a cascata insieme a lui.
        builder.HasKey(e => e.DigestPointId);

        builder.HasOne(e => e.DigestPoint)
            .WithOne()
            .HasForeignKey<DigestPointEmbedding>(e => e.DigestPointId)
            .OnDelete(DeleteBehavior.Cascade);

        // Il Domain resta senza dipendenze da pgvector: espone float[], qui lo si converte nel
        // tipo Vector del provider. Il comparer esplicito serve perché EF non sa confrontare
        // un array dietro un converter (altrimenti avvisa e rileva modifiche per riferimento).
        builder.Property(e => e.Embedding)
            .IsRequired()
            .HasColumnType($"vector({Dimensions})")
            .HasConversion(
                v => new Vector(v),
                v => v.ToArray(),
                new ValueComparer<float[]>(
                    (a, b) => a!.SequenceEqual(b!),
                    v => v.Aggregate(0, (h, x) => HashCode.Combine(h, x)),
                    v => v.ToArray()));

        builder.Property(e => e.Model).IsRequired().HasMaxLength(60);

        builder.Property(e => e.InputSha256).IsRequired().HasMaxLength(64);

        builder.Property(e => e.EmbeddedAt).IsRequired().HasDefaultValueSql("now()");

        // Niente indice vettoriale (HNSW/IVFFlat) di proposito: con qualche migliaio di righe la
        // scansione esatta con ORDER BY <=> costa pochi ms, ha recall perfetto e funziona con i
        // filtri per data/autore, dove un indice approssimato può restituire meno righe del
        // richiesto. Da aggiungere solo se le righe superano ~100k.
    }
}
