import heapq

Zgloszenie = tuple[int, int, str]


def dodaj_zgloszenie(kolejka: list, priorytet: int, id_zgloszenia: int, opis: str) -> None:
    heapq.heappush(kolejka, (priorytet, id_zgloszenia, opis))


def obsluz_zgloszenie(kolejka: list) -> Zgloszenie | None:
    if not kolejka:
        return None
    return heapq.heappop(kolejka)


def wyswietl_kolejke(kolejka: list) -> None:
    heapq.heapify(kolejka)
    for zgloszenie in kolejka:
        print(zgloszenie)


def _separator(tytul: str) -> None:
    """Drukuje czytelny separator sekcji w demo."""
    print(f"\n{'=' * 50}")
    print(f"  {tytul}")
    print('=' * 50)


if __name__ == "__main__":
    print("=== Helpdesk IT – Kolejka Priorytetowa ===\n")

    kolejka_it: list = []

    # --- Napływają zgłoszenia w losowej kolejności ---
    _separator("Dodawanie zgłoszeń")
    dodaj_zgloszenie(kolejka_it, 3, 1, "Drukarka w sali 204 nie działa")
    dodaj_zgloszenie(kolejka_it, 1, 2, "AWARIA: serwer bazy danych nie odpowiada")
    dodaj_zgloszenie(kolejka_it, 5, 3, "Prośba o zmianę tapety pulpitu")
    dodaj_zgloszenie(kolejka_it, 2, 4, "Klient VIP nie może się zalogować do CRM")
    dodaj_zgloszenie(kolejka_it, 4, 5, "Brak dostępu do drukarki sieciowej")
    dodaj_zgloszenie(kolejka_it, 1, 6, "AWARIA: strona www zwraca błąd 500")

    # --- Podgląd stanu kolejki ---
    _separator("Stan kolejki (wszystkie zgłoszenia)")
    wyswietl_kolejke(kolejka_it)

    # --- Technik zaczyna obsługę ---
    _separator("Obsługa zgłoszeń (od najważniejszych)")
    obsluz_zgloszenie(kolejka_it)
    obsluz_zgloszenie(kolejka_it)
    obsluz_zgloszenie(kolejka_it)

    # --- Podgląd po obsłudze 3 zgłoszeń ---
    _separator("Stan kolejki po obsłudze 3 zgłoszeń")
    wyswietl_kolejke(kolejka_it)

    # --- Obsłuż pozostałe ---
    _separator("Obsługa pozostałych zgłoszeń")
    obsluz_zgloszenie(kolejka_it)
    obsluz_zgloszenie(kolejka_it)
    obsluz_zgloszenie(kolejka_it)

    # --- Próba obsługi pustej kolejki ---
    _separator("Próba obsługi pustej kolejki")
    obsluz_zgloszenie(kolejka_it)