import random

random.seed(7)
PULA_ADRESOW_IP = [
    f"192.168.{random.randint(0, 9)}.{random.randint(1, 254)}"
    for _ in range(200)
]


def generuj_logi(liczba_wpisow: int = 50_000) -> list[str]:

    return [random.choice(PULA_ADRESOW_IP) for _ in range(liczba_wpisow)]

def unikalne_ip(lista_logow: list[str]) -> set[str] | None:
    if not lista_logow:
        return None
    return set(lista_logow)

def licznik_wystapien(lista_logow: list[str]) -> dict[str, int]:
    licznik: dict[str, int] = {}
    for ip in lista_logow:
        licznik[ip] = licznik.get(ip, 0) + 1
    return licznik

def top_adresow(licznik: dict[str, int], ile: int = 10) -> list[tuple[str, int]]:
    posortowane = sorted(licznik.items(), key=lambda para: para[1], reverse=True)
    return posortowane[:ile]

def wypisz_raport(logi: list[str], unikalne: set[str] | None,
                  licznik: dict[str, int] | None) -> None:

    print("\n" + "=" * 60)
    print("  RAPORT ANALIZY LOGÓW SIECIOWYCH")
    print("=" * 60)
    print(f"  Łączna liczba wpisów w logach : {len(logi):>8,}")

    if unikalne is None:
        print("  Unikalne adresy IP            :  [!] uzupełnij unikalne_ip()")
    else:
        print(f"  Unikalne adresy IP            : {len(unikalne):>8,}")

    if licznik is None or len(licznik) == 0:
        print("  Licznik wystąpień             :  [!] uzupełnij licznik_wystapien()")
        print("=" * 60)
        return

    print("-" * 60)
    print("  TOP 10 najczęstszych adresów IP:")
    print(f"  {'Adres IP':<22} {'Liczba połączeń':>15}")
    print(f"  {'-' * 22} {'-' * 15}")
    for adres, liczba in top_adresow(licznik, ile=10):
        print(f"  {adres:<22} {liczba:>15,}")
    print("=" * 60)
    print()
    print("  Wniosek:")
    print("  Słownik pozwolił policzyć 50 000 wpisów w jednym")
    print("  przebiegu pętli (O(n)) zamiast zagnieżdżonych pętli O(n²).")
    print("  To różnica między milisekundami a sekundami!")
    print("=" * 60)


if __name__ == "__main__":
    print("=" * 60)
    print("  ZADANIE 3 – Analityka logów sieciowych")
    print("=" * 60)

    print("\n  [>>] Generuję 50 000 wpisów logów...")
    logi_serwera = generuj_logi(50_000)
    print(f"  Przykładowe wpisy: {logi_serwera[:5]}")

    print("\n  [>>] Szukam unikalnych adresów IP...")
    wynik_unikalnych = unikalne_ip(logi_serwera)

    print("  [>>] Zliczam wystąpienia każdego adresu IP...")
    wynik_licznika = licznik_wystapien(logi_serwera)

    wypisz_raport(logi_serwera, wynik_unikalnych, wynik_licznika)