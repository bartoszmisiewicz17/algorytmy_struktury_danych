import heapq

Zadanie = tuple[int, str, str]



def utworz_harmonogram(zadania: list[Zadanie]) -> list[Zadanie]:
    heapq.heapify(zadania)
    harmonogram = []
    while zadania:
        zadanie = heapq.heappop(zadania)
        harmonogram.append(zadanie)
    return harmonogram

def najpilniejsze(harmonogram: list[Zadanie], n: int) -> list[Zadanie]:
    return harmonogram[:n]

def usun_najpilniejsze(harmonogram: list[Zadanie], n: int) -> None:
    del harmonogram[:n]

def dodaj_zadanie(harmonogram: list[Zadanie], priorytet: int, opis: str, termin: str) -> None:
    heapq.heappush(harmonogram, (priorytet, opis, termin))

def _separator(tytul: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {tytul}")
    print('=' * 55)


def _wyswietl_wszystkie(harmonogram: list[Zadanie]) -> None:
    """Wypisuje wszystkie zadania posortowane wg deadline'u (nie niszczy kopca)."""
    if not harmonogram:
        print("  Harmonogram jest pusty.")
        return
    for dni, nazwa, priorytet in sorted(harmonogram):
        pasek = "█" * min(dni, 30) + "░" * (30 - min(dni, 30))
        print(f"  [{dni:>3}d] {pasek} {nazwa} ({priorytet})")


if __name__ == "__main__":
    print("=== Harmonogram Sprintu – heapify / nsmallest / heappop ===\n")

    # Backlog zadań: (dni_do_deadline, nazwa, priorytet_biznesowy)
    backlog: list[Zadanie] = [
        (14, "Migracja bazy danych do PostgreSQL",    "WYSOKI"),
        (3,  "Hotfix: błąd w module płatności",       "KRYTYCZNY"),
        (30, "Refaktoryzacja modułu raportów",        "NISKI"),
        (7,  "Integracja z API kuriera",              "WYSOKI"),
        (21, "Dokumentacja REST API",                 "SREDNI"),
        (2,  "Naprawa błędu logowania OAuth",         "KRYTYCZNY"),
        (45, "Migracja na Python 3.13",               "NISKI"),
        (10, "Testy wydajnościowe load balancera",    "WYSOKI"),
    ]

    # --- Krok 1: Zamień backlog w kopiec ---
    _separator("Tworzenie harmonogramu (heapify)")
    harmonogram = utworz_harmonogram(backlog)

    # --- Krok 2: Podgląd całego harmonogramu ---
    _separator("Pełny harmonogram (posortowany wg deadline'u)")
    _wyswietl_wszystkie(harmonogram)

    # --- Krok 3: Co robimy w tym tygodniu? ---
    _separator("Top 3 najpilniejsze zadania (stand-up)")
    najpilniejsze(harmonogram, 3)

    # --- Krok 4: Sprint startuje — bierzemy 3 najpilniejsze do realizacji ---
    _separator("Start sprintu – bierzemy 3 najpilniejsze zadania")
    usuniete = usun_najpilniejsze(harmonogram, 3)

    _separator("Harmonogram po zabraniu 3 zadań do sprintu")
    _wyswietl_wszystkie(harmonogram)

    # --- Krok 5: Nowe zgłoszenie z zewnątrz ---
    _separator("Nowe zadanie wpada w trakcie sprintu")
    dodaj_zadanie(harmonogram, 1, "PRODUKCJA: błąd 500 na stronie głównej", "KRYTYCZNY")
    dodaj_zadanie(harmonogram, 60, "Aktualizacja polityki cookies", "NISKI")

    # --- Krok 6: Aktualne top 3 po zmianach ---
    _separator("Top 3 najpilniejsze po aktualizacji")
    najpilniejsze(harmonogram, 3)

    _separator("Pełny harmonogram po aktualizacji")
    _wyswietl_wszystkie(harmonogram)