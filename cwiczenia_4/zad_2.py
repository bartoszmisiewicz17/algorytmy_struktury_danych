import time
import random

ROZMIAR_DANYCH = 100_000
LICZBA_POWTORZEN = 1_000

random.seed(42)
lista_danych: list[int] = [random.randint(0, 200_000) for _ in range(ROZMIAR_DANYCH)]
zbior_danych: set[int] = set(lista_danych)

SZUKANY_ELEMENT = 999_999

def zmierz_czas_listy(lista: list[int], element: int) -> float | None:
    start = time.perf_counter()
    for _ in range(LICZBA_POWTORZEN):
        if element in lista:
            end = time.perf_counter()
            return end - start
    return None

def zmierz_czas_zbioru(zbior: set[int], element: int) -> float | None:
    start = time.perf_counter()
    for _ in range(LICZBA_POWTORZEN):
        if element in zbior:
            end = time.perf_counter()
            return end - start
    return None

def wypisz_wyniki(czas_listy: float | None, czas_zbioru: float | None) -> None:
    print("\n" + "=" * 60)
    print("  WYNIKI BENCHMARKU – wyszukiwanie elementu")
    print("=" * 60)
    print(f"  Rozmiar danych      : {ROZMIAR_DANYCH:>10,} elementów")
    print(f"  Liczba powtórzeń    : {LICZBA_POWTORZEN:>10,} wyszukiwań")
    print(f"  Szukany element     : {SZUKANY_ELEMENT:>10,}  (nieobecny – najgorszy przypadek)")
    print("-" * 60)

    if czas_listy is None or czas_zbioru is None:
        print("  [!] Brak wyników – uzupełnij metody zmierz_czas_listy()")
        print("      i zmierz_czas_zbioru(), a następnie uruchom ponownie.")
        print("=" * 60)
        return

    print(f"  Czas dla listy  (O(n)): {czas_listy:>10.4f} s")
    print(f"  Czas dla zbioru (O(1)): {czas_zbioru:>10.6f} s")
    print("-" * 60)

    if czas_zbioru > 0:
        krotnosc = czas_listy / czas_zbioru
        print(f"  Zbiór był SZYBSZY o : {krotnosc:>9.1f}x")
    print("=" * 60)
    print()
    print("  Wniosek:")
    print("  Przy 100 000 elementach różnica jest wyraźna.")
    print("  Wyobraź sobie bazę danych z milionami rekordów – ")
    print("  O(1) vs O(n) to różnica między milisekundami a minutami!")
    print("=" * 60)

if __name__ == "__main__":
    print("=" * 60)
    print("  ZADANIE 2 – Benchmark: lista O(n) vs zbiór O(1)")
    print("=" * 60)
    print(f"\n  Przygotowano {ROZMIAR_DANYCH:,} elementów danych.")
    print(f"  Każde wyszukiwanie zostanie powtórzone {LICZBA_POWTORZEN:,} razy.\n")

    print("  [>>] Uruchamiam pomiar dla listy ...")
    wynik_listy = zmierz_czas_listy(lista_danych, SZUKANY_ELEMENT)

    print("  [>>] Uruchamiam pomiar dla zbioru ...")
    wynik_zbioru = zmierz_czas_zbioru(zbior_danych, SZUKANY_ELEMENT)

    wypisz_wyniki(wynik_listy, wynik_zbioru)