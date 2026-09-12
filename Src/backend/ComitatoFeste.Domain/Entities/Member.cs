namespace ComitatoFeste.Domain;

/// <summary>
/// Un partecipante al gruppo, identificato dal <see cref="DisplayName"/> esatto mostrato da WhatsApp.
/// Nessuna tabella alias: il match sull'autore delle entry avviene per DisplayName esatto (unico per gruppo).
/// </summary>
public class Member
{
    public int Id { get; set; }

    public int GroupId { get; set; }
    public Group Group { get; set; } = null!;

    /// <summary>Nome visualizzato in WhatsApp. Unico all'interno del gruppo.</summary>
    public string DisplayName { get; set; } = null!;

    /// <summary>Ruolo di accesso al login. Default <see cref="MemberRole.Lettore"/>.</summary>
    public MemberRole Role { get; set; } = MemberRole.Lettore;

    /// <summary>
    /// Ultima richiesta autenticata servita per questo membro (non solo il login: aggiornato da
    /// <see cref="ComitatoFeste.Api.Filters.TokenAuthAttribute"/> a ogni chiamata con token valido,
    /// throttlato per non scrivere a ogni richiesta). Solo consultabile via query diretta al DB,
    /// nessun endpoint/UI la espone di proposito.
    /// </summary>
    public DateTimeOffset? LastSeenAt { get; set; }

    /// <summary>Foto profilo (relazione 1:1). Null finché non ne viene importata una.</summary>
    public MemberProfilePhoto? ProfilePhoto { get; set; }

    public ICollection<DigestPoint> DigestPoints { get; set; } = new List<DigestPoint>();
}
