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

def filtruj_bledy(logi: list[LogEntry], poziom: str) -> list[LogEntry]:
    return [log for log in logi if log.poziom == poziom]

def najnowsze_logi(logi: list[LogEntry], ile: int) -> list[LogEntry]:
    heapq.nlargest(ile, logi)



if __name__ == "__main__":
    print("=== Monitoring klastra – scalanie logów (heapq.merge) ===\n")

    # --- Generujemy posortowane logi z każdego serwera ---
    # Serwery startują o różnych porach, żeby logi się przeplatały
    _separator("Generowanie logów z 3 serwerów")
    logi_web_01  = generuj_logi_serwera("web-01",  start_ts=1_700_000_000, ile=15, seed=1)
    logi_web_02  = generuj_logi_serwera("web-02",  start_ts=1_700_000_005, ile=15, seed=2)
    logi_db_01   = generuj_logi_serwera("db-01",   start_ts=1_700_000_003, ile=10, seed=3)

    print(f"  web-01 : {len(logi_web_01)} wpisów  "
          f"(od {logi_web_01[0].timestamp} do {logi_web_01[-1].timestamp})")
    print(f"  web-02 : {len(logi_web_02)} wpisów  "
          f"(od {logi_web_02[0].timestamp} do {logi_web_02[-1].timestamp})")
    print(f"  db-01  : {len(logi_db_01)} wpisów  "
          f"(od {logi_db_01[0].timestamp} do {logi_db_01[-1].timestamp})")

    # --- Krok 1: Scal logi ---
    _separator("Scalanie logów (heapq.merge)")
    wszystkie = scalaj_logi(logi_web_01, logi_web_02, logi_db_01)

    # --- Krok 2: Podgląd pierwszych 10 wpisów scalonych logów ---
    _separator("Pierwsze 10 wpisów scalonych logów (chronologicznie)")
    for log in wszystkie[:10]:
        print(f"  {log}")

    # --- Krok 3: Znajdź błędy ---
    _separator("Filtrowanie: tylko ERROR")
    bledy = filtruj_bledy(wszystkie, "ERROR")
    for log in bledy:
        print(f"  {log}")

    _separator("Filtrowanie: tylko CRITICAL")
    krytyczne = filtruj_bledy(wszystkie, "CRITICAL")
    for log in krytyczne:
        print(f"  {log}")
    if not krytyczne:
        print("  Brak wpisów CRITICAL – klaster działa stabilnie.")

    # --- Krok 4: Najnowsze logi ---
    _separator("5 najnowszych wpisów z klastra")
    najnowsze_logi(wszystkie, 5)

    # --- Krok 5: Najnowsze błędy ---
    _separator("3 najnowsze wpisy ERROR lub CRITICAL")
    powazne = [log for log in wszystkie if log.poziom in ("ERROR", "CRITICAL")]
    najnowsze_logi(powazne, 3)