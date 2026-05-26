siec_spolecznosciowa: dict[str, list[str]] = {
    "Alicja":   ["Bartosz", "Celina", "Filip"],
    "Bartosz":  ["Alicja", "Damian", "Ewa"],
    "Celina":   ["Alicja", "Grażyna"],
    "Damian":   ["Bartosz", "Henryk", "Irena"],
    "Ewa":      ["Bartosz", "Filip", "Jan"],
    "Filip":    ["Alicja", "Ewa"],
    "Grażyna":  ["Celina", "Henryk"],
    "Henryk":   ["Damian", "Grażyna"],
    "Irena":    ["Damian", "Jan"],
    "Jan":      ["Ewa", "Irena"],
}

siec_z_izolacja: dict[str, list[str]] = {
    **siec_spolecznosciowa,
    "Zofia":  ["Konrad"],
    "Konrad": ["Zofia"],
}

def czy_istnieje_sciezka_dfs(
    graf: dict[str, list[str]],
    start: str,
    cel: str
) -> bool:
    if start == cel:
        return True
    odwiedzone: set[str] = set()
    odwiedzone.add(start)
    stos: list[str] = [start]

    while stos:
        aktualny = stos.pop()
        for sasiad in graf[aktualny]:
            if sasiad == cel:
                return True
            if sasiad not in odwiedzone:
                odwiedzone.add(sasiad)
                stos.append(sasiad)
    return False


if __name__ == "__main__":
    print("=" * 55)
    print("Zadanie 2 – DFS: Czy istnieje ścieżka?")
    print("=" * 55)

    testy = [
        ("Alicja",  "Jan",    True,  siec_spolecznosciowa),
        ("Alicja",  "Irena",  True,  siec_spolecznosciowa),
        ("Grażyna", "Jan",    True,  siec_spolecznosciowa),
        ("Alicja",  "Zofia",  False, siec_z_izolacja),
        ("Konrad",  "Henryk", False, siec_z_izolacja),
    ]

    for start, cel, oczekiwany, graf in testy:
        wynik = czy_istnieje_sciezka_dfs(graf, start, cel)
        status = "OK" if wynik == oczekiwany else "BŁĄD"
        odpowiedz = "TAK, istnieje" if wynik else "NIE, brak ścieżki"
        print(f"\n  [{status}] {start} → {cel}")
        print(f"        Wynik: {odpowiedz}  (oczekiwano: {oczekiwany})")