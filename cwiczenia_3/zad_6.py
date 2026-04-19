import heapq
import random
from dataclasses import dataclass, field


POZIOMY = ["INFO", "WARNING", "ERROR", "CRITICAL"]

_WAGI_POZIOMOW = [70, 20, 8, 2]



@dataclass(order=True)
class LogEntry:
    timestamp: int  # Unix timestamp w sekundach (klucz sortowania)
    serwer: str = field(compare=False)  # Nazwa serwera (nie porównujemy)
    poziom: str = field(compare=False)  # INFO / WARNING / ERROR / CRITICAL
    komunikat: str = field(compare=False)  # Treść logu

    def __str__(self) -> str:
        return f"[{self.timestamp}] {self.serwer:<12} {self.poziom:<9} {self.komunikat}"

def generuj_logi_serwera(nazwa: str, start_ts: int, ile: int, seed: int) -> list[LogEntry]:
    rng = random.Random(seed)
    komunikaty = {
        "INFO": ["Żądanie obsłużone", "Połączenie nawiązane", "Cache odświeżony",
                 "Użytkownik zalogowany", "Sesja wygasła"],
        "WARNING": ["Wysokie użycie CPU (85%)", "Wolne zapytanie SQL (>2s)",
                    "Retry połączenia z DB", "Bufor kolejki zapełniony w 80%"],
        "ERROR": ["Timeout połączenia z Redis", "Błąd parsowania JSON",
                  "Nieudana autentykacja", "Wyjątek NullPointerError"],
        "CRITICAL": ["Brak miejsca na dysku!", "Serwer bazy danych niedostępny",
                     "OOM Killer uruchomiony"],
    }
    logi = []
    ts = start_ts
    for _ in range(ile):
        ts += rng.randint(1, 15)  # losowy przyrost czasu (1–15 s)
        poziom = rng.choices(POZIOMY, weights=_WAGI_POZIOMOW)[0]
        komunikat = rng.choice(komunikaty[poziom])
        logi.append(LogEntry(ts, nazwa, poziom, komunikat))
    return logi  # już posortowane, bo timestamp rośnie


def _separator(tytul: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {tytul}")
    print('=' * 60)


def scalaj_logi(*strumienie: list[LogEntry]) -> list[LogEntry]:
    scalone = []
    heap = []
    for i, strumien in enumerate(strumienie):
        if strumien:
            heapq.heappush(heap, (strumien[0].timestamp, i, 0, strumien[0]))
    while heap:
        _, i_strumienia, idx_logu, log = heapq.heappop(heap)
        scalone.append(log)
        if idx_logu + 1 < len(strumienie[i_strumienia]):
            next_log = strumienie[i_strumienia][idx_logu + 1]
            heapq.heappush(heap, (next_log.timestamp, i_strumienia, idx_logu + 1, next_log))
    return scalone