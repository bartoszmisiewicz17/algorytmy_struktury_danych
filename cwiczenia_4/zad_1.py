class ProstaMapa:

    def __init__(self, rozmiar: int = 10):
        self.rozmiar = rozmiar
        self.kubełki = [[] for _ in range(self.rozmiar)]


    def _funkcja_hashujaca(self, klucz: str) -> int:
        return hash(klucz) % self.rozmiar

    def wstaw(self, klucz: str, wartosc) -> None:
        indeks = self._funkcja_hashujaca(klucz)
        self.kubełki[indeks].append((klucz, wartosc))


    def pobierz(self, klucz: str):
        indeks = self._funkcja_hashujaca(klucz)
        for k, v in self.kubełki[indeks]:
            if k == klucz:
                return v
        return None

    def wypisz(self) -> None:
            print("\n--- Zawartość mapy hashowej ---")
            for indeks, kubełek in enumerate(self.kubełki):
                if kubełek:
                    print(f"  Kubełek [{indeks:2d}]: {kubełek}")
                else:
                    print(f"  Kubełek [{indeks:2d}]: (pusty)")
            print("-------------------------------\n")

if __name__ == "__main__":
    print("=" * 60)
    print("  ZADANIE 1 – Własna implementacja mapy hashowej")
    print("=" * 60)

    mapa = ProstaMapa(rozmiar=10)

    # --- Wstawianie par klucz-wartość ---
    print("\n[1] Wstawianie danych do mapy...")
    mapa.wstaw("imie",    "Aleksander")
    mapa.wstaw("nazwisko", "Kowalski")
    mapa.wstaw("wiek",    "23")
    mapa.wstaw("miasto",  "Kraków")
    mapa.wstaw("język",   "Python")
    # Klucze "ab" i "ba" mają ten sam hash – celowa kolizja do testów
    mapa.wstaw("ab",      "wartość_ab")
    mapa.wstaw("ba",      "wartość_ba")
    print("  Wstawiono 7 par (w tym jedna celowa kolizja: 'ab' i 'ba').")

    # --- Podgląd wewnętrznej struktury ---
    mapa.wypisz()

    # --- Pobieranie wartości ---
    print("[2] Pobieranie wartości:")
    print(f"  mapa.pobierz('imie')     -> {mapa.pobierz('imie')}")
    print(f"  mapa.pobierz('miasto')   -> {mapa.pobierz('miasto')}")
    print(f"  mapa.pobierz('ab')       -> {mapa.pobierz('ab')}")
    print(f"  mapa.pobierz('ba')       -> {mapa.pobierz('ba')}")
    print(f"  mapa.pobierz('brakujący')-> {mapa.pobierz('brakujący')}")

    # --- Aktualizacja istniejącego klucza ---
    print("\n[3] Aktualizacja klucza 'wiek' (23 -> 24):")
    mapa.wstaw("wiek", "24")
    print(f"  mapa.pobierz('wiek')     -> {mapa.pobierz('wiek')}")

    print("\n[Gotowe] Uzupełnij metody TODO i sprawdź, czy wyniki są poprawne.")
