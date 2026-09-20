namespace ComitatoFeste.Api.Services;

/// <summary>
/// Limita l'uso dell'assistente: la quota gratuita di Groq/Gemini è condivisa da tutti i membri e
/// (Groq) anche dal Transcriber e dai verbali, quindi senza freni uno solo potrebbe esaurirla per
/// tutti. Tre livelli: domande per utente all'ora, domande totali al giorno, chiamate contemporanee.
/// I contatori stanno in memoria: si azzerano al riavvio del processo (su Render free anche a ogni
/// cold start) — è una protezione dagli abusi, non una contabilità precisa. Configurabili con
/// <c>Assistant:PerUserPerHour</c> (default 10), <c>Assistant:GlobalPerDay</c> (default 80) e
/// <c>Assistant:MaxConcurrent</c> (default 2).
/// </summary>
public sealed class AssistantLimiter
{
    private readonly int _perUserPerHour;
    private readonly int _globalPerDay;
    private readonly SemaphoreSlim _slots;
    private readonly object _lock = new();
    private readonly Dictionary<string, List<DateTimeOffset>> _perUser = new();
    private readonly List<DateTimeOffset> _global = new();

    public AssistantLimiter(IConfiguration config)
    {
        _perUserPerHour = Math.Max(1, config.GetValue("Assistant:PerUserPerHour", 10));
        _globalPerDay = Math.Max(1, config.GetValue("Assistant:GlobalPerDay", 80));
        _slots = new SemaphoreSlim(Math.Max(1, config.GetValue("Assistant:MaxConcurrent", 2)));
    }

    /// <summary>
    /// Registra una domanda di <paramref name="user"/> se rientra nei limiti. Se no restituisce
    /// <c>null</c> e valorizza <paramref name="denial"/> con messaggio e attesa consigliata.
    /// Il biglietto va restituito a <see cref="Refund"/> se la domanda fallisce per colpa dei
    /// servizi esterni, così l'utente non paga un errore non suo.
    /// </summary>
    public DateTimeOffset? TryAcquire(string user, out (string Message, TimeSpan RetryAfter) denial)
    {
        var now = DateTimeOffset.UtcNow;
        lock (_lock)
        {
            _global.RemoveAll(t => t <= now.AddDays(-1));
            if (!_perUser.TryGetValue(user, out var mine))
                _perUser[user] = mine = new List<DateTimeOffset>();
            mine.RemoveAll(t => t <= now.AddHours(-1));

            if (_global.Count >= _globalPerDay)
            {
                var wait = _global.Min().AddDays(1) - now;
                denial = ("L'assistente ha raggiunto il limite giornaliero di domande (la quota gratuita è condivisa da tutti). Riprova più tardi.", wait);
                return null;
            }

            if (mine.Count >= _perUserPerHour)
            {
                var wait = mine.Min().AddHours(1) - now;
                var minutes = Math.Max(1, (int)Math.Ceiling(wait.TotalMinutes));
                denial = ($"Hai raggiunto il limite di {_perUserPerHour} domande all'ora. Riprova tra circa {minutes} minuti.", wait);
                return null;
            }

            mine.Add(now);
            _global.Add(now);
            denial = default;
            return now;
        }
    }

    public void Refund(string user, DateTimeOffset ticket)
    {
        lock (_lock)
        {
            _global.Remove(ticket);
            if (_perUser.TryGetValue(user, out var mine))
                mine.Remove(ticket);
        }
    }

    /// <summary>
    /// Attende un posto per parlare con i modelli (max qualche chiamata insieme: il limite vero
    /// è il tetto di token al minuto di Groq). <c>null</c> se non si libera entro il timeout.
    /// </summary>
    public async Task<IDisposable?> WaitSlotAsync(TimeSpan timeout, CancellationToken ct)
    {
        if (!await _slots.WaitAsync(timeout, ct))
            return null;
        return new Slot(_slots);
    }

    private sealed class Slot : IDisposable
    {
        private SemaphoreSlim? _slots;

        public Slot(SemaphoreSlim slots) => _slots = slots;

        public void Dispose() => Interlocked.Exchange(ref _slots, null)?.Release();
    }
}
