baza_synonimow: dict[str, list[str]] = {}

def dodaj_synonim(slowo: str, synonim: str) -> None:
    if slowo not in baza_synonimow:
        baza_synonimow[slowo] = []
    if synonim not in baza_synonimow[slowo]:
        baza_synonimow[slowo].append(synonim)

def znajdz_synonimy(slowo: str) -> list[str] | str | None:
    if slowo in baza_synonimow:
        return baza_synonimow[slowo]
    for klucz, synonimy in baza_synonimow.items():
        if slowo in synonimy:
            return [klucz] + synonimy
    return None

def usun_slowo(slowo: str) -> None:
    if slowo in baza_synonimow:
        del baza_synonimow[slowo]
    for klucz, synonimy in list(baza_synonimow.items()):
        if slowo in synonimy:
            synonimy.remove(slowo)
            if not synonimy:
                del baza_synonimow[klucz]

def wyswietl_statystyki() -> None:
    print("\n" + "=" * 60)
    print("  STATYSTYKI BAZY SYNONIMÓW")
    print("=" * 60)
    print(f"  Łączna liczba słów        : {len(baza_synonimow):>8,}")
    print(f"  Średnia liczba synonimów : {sum(len(s) for s in baza_synonimow.values()) / len(baza_synonimow):>8.2f}")
    print("=" * 60)


if __name__ == "__main__":
    print("=" * 60)
    print("  ZADANIE 4 – Baza Synonimów (słownik / hashmap)")
    print("=" * 60)

    # --- Dodawanie synonimów ---
    print("\n[1] Dodawanie synonimów do bazy...")
    dodaj_synonim("szybki",   "prędki")
    dodaj_synonim("szybki",   "błyskawiczny")
    dodaj_synonim("szybki",   "żwawy")
    dodaj_synonim("duży",     "wielki")
    dodaj_synonim("duży",     "ogromny")
    dodaj_synonim("duży",     "potężny")
    dodaj_synonim("mądry",    "inteligentny")
    dodaj_synonim("mądry",    "rozumny")
    dodaj_synonim("piękny",   "śliczny")
    dodaj_synonim("piękny",   "czarowny")
    dodaj_synonim("smutny",   "przygnębiony")
    # Próba dodania duplikatu – nie powinno nic zmienić
    dodaj_synonim("szybki",   "prędki")
    print("  Dodano synonimy dla słów: szybki, duży, mądry, piękny, smutny.")
    print("  (Próba dodania duplikatu 'prędki' dla 'szybki' – powinna być zignorowana.)")

    # --- Wyszukiwanie synonimów ---
    print("\n[2] Wyszukiwanie synonimów:")
    print(f"  znajdz_synonimy('szybki') -> {znajdz_synonimy('szybki')}")
    print(f"  znajdz_synonimy('duży')   -> {znajdz_synonimy('duży')}")
    print(f"  znajdz_synonimy('wolny')  -> {znajdz_synonimy('wolny')}")

    # --- Statystyki przed usunięciem ---
    print("\n[3] Statystyki bazy przed usunięciem słowa:")
    wyswietl_statystyki()

    # --- Usuwanie słowa ---
    print("\n[4] Usuwanie słowa 'smutny' z bazy...")
    usun_slowo("smutny")
    print("  Próba usunięcia nieistniejącego słowa 'wesoły':")
    usun_slowo("wesoły")

    # --- Statystyki po usunięciu ---
    print("\n[5] Statystyki bazy po usunięciu słowa:")
    wyswietl_statystyki()

    print("\n[Gotowe] Uzupełnij metody TODO i sprawdź, czy wyniki są zgodne z oczekiwaniami.")