using Amazon.Runtime;
using Amazon.S3;
using Amazon.S3.Model;

namespace ComitatoFeste.Data;

/// <summary>
/// Object storage per i byte dei file (foto, audio, documenti, foto profilo, thumbnail), per
/// non tenerli in Postgres: lo spazio su Aiven è il vincolo. Implementazione: Cloudflare R2
/// (API S3). Le chiavi includono lo SHA-256 del contenuto (vedi <see cref="BlobKeys"/>), quindi
/// un oggetto è immutabile: se il file cambia cambia la chiave.
/// </summary>
public interface IBlobStore
{
    Task PutAsync(string key, byte[] content, string contentType, CancellationToken ct = default);

    /// <summary>I byte dell'oggetto, o <c>null</c> se la chiave non esiste.</summary>
    Task<byte[]?> GetAsync(string key, CancellationToken ct = default);

    Task<bool> ExistsAsync(string key, CancellationToken ct = default);

    Task DeleteAsync(IEnumerable<string> keys, CancellationToken ct = default);
}

/// <summary>Schema delle chiavi: <c>media/{id}/{sha}</c>, <c>memberphoto/{id}/{sha}</c>,
/// <c>thumb/{kind}/{id}/{width}/{sha}</c> (sha = SHA-256 del <b>sorgente</b> per le thumbnail).</summary>
public static class BlobKeys
{
    public static string Media(int mediaAssetId, string sha256) => $"media/{mediaAssetId}/{sha256}";
    public static string MemberPhoto(int memberId, string sha256) => $"memberphoto/{memberId}/{sha256}";
    public static string Thumbnail(string kind, int sourceId, int width, string sourceSha256) =>
        $"thumb/{kind}/{sourceId}/{width}/{sourceSha256}";
}

/// <summary>Configurazione R2 da variabili d'ambiente. Se una manca lo store non c'è e i byte
/// restano in Postgres come prima (sviluppo locale, o R2 non ancora configurato).</summary>
public static class BlobStoreFactory
{
    public const string AccountIdVar = "COMITATOFESTE_R2_ACCOUNT_ID";
    public const string AccessKeyVar = "COMITATOFESTE_R2_ACCESS_KEY_ID";
    public const string SecretKeyVar = "COMITATOFESTE_R2_SECRET_ACCESS_KEY";
    public const string BucketVar = "COMITATOFESTE_R2_BUCKET";

    /// <summary>Lo store R2, o <c>null</c> se le quattro variabili non sono tutte impostate.</summary>
    public static IBlobStore? FromEnvironment()
    {
        var account = Get(AccountIdVar);
        var accessKey = Get(AccessKeyVar);
        var secret = Get(SecretKeyVar);
        var bucket = Get(BucketVar);
        if (account is null || accessKey is null || secret is null || bucket is null)
            return null;
        return new R2BlobStore(account, accessKey, secret, bucket);
    }

    private static string? Get(string name)
    {
        var v = Environment.GetEnvironmentVariable(name);
        return string.IsNullOrWhiteSpace(v) ? null : v.Trim();
    }
}

public sealed class R2BlobStore : IBlobStore
{
    private readonly AmazonS3Client _s3;
    private readonly string _bucket;

    public R2BlobStore(string accountId, string accessKeyId, string secretAccessKey, string bucket)
    {
        _bucket = bucket;
        _s3 = new AmazonS3Client(
            new BasicAWSCredentials(accessKeyId, secretAccessKey),
            new AmazonS3Config
            {
                ServiceURL = $"https://{accountId}.r2.cloudflarestorage.com",
                AuthenticationRegion = "auto",
                ForcePathStyle = true,
                // Le versioni recenti dell'SDK aggiungono checksum di default che R2 non
                // accetta su tutte le operazioni: si calcolano solo quando richiesti.
                RequestChecksumCalculation = RequestChecksumCalculation.WHEN_REQUIRED,
                ResponseChecksumValidation = ResponseChecksumValidation.WHEN_REQUIRED,
            });
    }

    public async Task PutAsync(string key, byte[] content, string contentType, CancellationToken ct = default)
    {
        using var ms = new MemoryStream(content, writable: false);
        await _s3.PutObjectAsync(new PutObjectRequest
        {
            BucketName = _bucket,
            Key = key,
            InputStream = ms,
            ContentType = contentType,
            DisablePayloadSigning = true,   // R2 è già su TLS; evita il chunked signing
        }, ct);
    }

    public async Task<byte[]?> GetAsync(string key, CancellationToken ct = default)
    {
        try
        {
            using var res = await _s3.GetObjectAsync(_bucket, key, ct);
            using var ms = new MemoryStream();
            await res.ResponseStream.CopyToAsync(ms, ct);
            return ms.ToArray();
        }
        catch (AmazonS3Exception ex) when (ex.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            return null;
        }
    }

    public async Task<bool> ExistsAsync(string key, CancellationToken ct = default)
    {
        try
        {
            await _s3.GetObjectMetadataAsync(_bucket, key, ct);
            return true;
        }
        catch (AmazonS3Exception ex) when (ex.StatusCode == System.Net.HttpStatusCode.NotFound)
        {
            return false;
        }
    }

    public async Task DeleteAsync(IEnumerable<string> keys, CancellationToken ct = default)
    {
        foreach (var key in keys)
            await _s3.DeleteObjectAsync(_bucket, key, ct);
    }
}

public static class BlobStoreExtensions
{
    /// <summary>
    /// I byte di un blob: quelli già letti dal DB se presenti, altrimenti quelli in R2 alla
    /// <paramref name="key"/>. <c>null</c> se non ci sono da nessuna parte (o se non c'è uno store
    /// e nemmeno il DB li ha).
    /// </summary>
    public static async Task<byte[]?> ResolveAsync(
        this IBlobStore? store, byte[]? dbContent, string? key, CancellationToken ct = default)
    {
        if (dbContent is not null) return dbContent;
        if (store is null || key is null) return null;
        return await store.GetAsync(key, ct);
    }
}

/// <summary>Contenitore per registrare nel DI uno store che può non esserci (R2 non configurato).</summary>
public sealed class BlobStoreHolder
{
    public IBlobStore? Store { get; }
    public BlobStoreHolder(IBlobStore? store) => Store = store;
    public static BlobStoreHolder FromEnvironment() => new(BlobStoreFactory.FromEnvironment());
}
