namespace ComitatoFeste.Domain;

/// <summary>
/// Fuso orario del gruppo (Europe/Rome) e conversioni verso istanti UTC.
/// Unico punto in cui si decide come una "giornata" locale mappa su un intervallo di
/// <c>timestamptz</c>: lo usano sia l'import (data+ora del JSON -> UTC) sia le query per giorno.
/// </summary>
public static class RomeTime
{
    public static readonly TimeZoneInfo Zone = Resolve();

    /// <summary>Combina data e ora locali di Roma in un istante assoluto (UTC, offset 0 per Npgsql).</summary>
    public static DateTimeOffset ToInstant(DateOnly date, TimeOnly time)
    {
        var local = new DateTime(date.Year, date.Month, date.Day, time.Hour, time.Minute, time.Second, DateTimeKind.Unspecified);
        return new DateTimeOffset(local, Zone.GetUtcOffset(local)).ToUniversalTime();
    }

    /// <summary>
    /// Intervallo UTC semiaperto [inizio, fine) corrispondente alla giornata locale di Roma
    /// (la mezzanotte in Italia non cade mai su un cambio di ora legale, quindi è sempre univoca).
    /// </summary>
    public static (DateTimeOffset StartUtc, DateTimeOffset EndUtc) DayRangeUtc(DateOnly date) =>
        (ToInstant(date, TimeOnly.MinValue), ToInstant(date.AddDays(1), TimeOnly.MinValue));

    private static TimeZoneInfo Resolve()
    {
        foreach (var id in new[] { "Europe/Rome", "W. Europe Standard Time" })
        {
            try { return TimeZoneInfo.FindSystemTimeZoneById(id); }
            catch (TimeZoneNotFoundException) { }
            catch (InvalidTimeZoneException) { }
        }
        return TimeZoneInfo.Local;
    }
}
