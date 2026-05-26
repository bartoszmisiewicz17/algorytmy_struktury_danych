from collections import deque

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

def bfs_znajomi_drugiego_stopnia(
    graf: dict[str, list[str]],
    osoba_startowa: str
) -> set[str]:

    odwiedzone: set[str] = set()
    kolejka: deque[tuple[str, int]] = deque([(osoba_startowa, 0)])
    znajomi_drugiego_stopnia: set[str] = set()

    while kolejka:
        osoba, poziom = kolejka.popleft()

        if osoba in odwiedzone:
            continue

        odwiedzone.add(osoba)

        if poziom == 2:
            znajomi_drugiego_stopnia.add(osoba)
        elif poziom < 2:
            for znajomy in graf.get(osoba, []):
                if znajomy not in odwiedzone:
                    kolejka.append((znajomy, poziom + 1))

    return znajomi_drugiego_stopnia


if __name__ == "__main__":
    print("=" * 55)
    print("Zadanie 1 – BFS: Znajomi drugiego stopnia")
    print("=" * 55)

    osoby_testowe = ["Alicja", "Damian", "Jan"]

    for osoba in osoby_testowe:
        wynik = bfs_znajomi_drugiego_stopnia(siec_spolecznosciowa, osoba)
        bezposredni = set(siec_spolecznosciowa[osoba])

        print(f"\nOsoba startowa : {osoba}")
        print(f"Znajomi 1. st. : {sorted(bezposredni)}")
        print(f"Znajomi 2. st. : {sorted(wynik)}")
