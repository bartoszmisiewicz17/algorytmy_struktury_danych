from collections import deque


historia: deque[str] = deque()

bufor_dalej: deque[str] = deque()

def odwiedz_strone(url: str) -> None:
    historia.append(url)
    bufor_dalej.clear()
    print(f"Odwiedzono stronę: {url}")

def cofnij_strone() -> None:
    if len(historia) > 1:
        ostatnia_strona = historia.pop()
        bufor_dalej.appendleft(ostatnia_strona)
        print(f"Cofnięto stronę: {ostatnia_strona}")
    if historia[0] == historia[-1]:
        print("Jesteś na pierwszej stronie, nie można cofnąć.")
    else:
        print("Nie można cofnąć, brak historii.")

def strona_dalej() -> None:
    if bufor_dalej:
        nastepna_strona = bufor_dalej.popleft()
        historia.append(nastepna_strona)
        print(f"Przesunięto się dalej do strony: {nastepna_strona}")
    else:
        print("Nie można przesunąć dalej, brak stron w buforze.")

def pokaz_historie() -> None:
    if not historia:
        print("Brak historii odwiedzonych stron.")
        return
    print("Historia odwiedzonych stron:")
    for strona in historia:
        if strona == historia[-1]:
            print(f" <- {strona} (aktualna strona)")
        elif strona == historia[0]:
                print(f" ->  {strona} (pierwsza strona)")
        elif strona != historia[-1] and strona != historia[0]:
            print(f" <-  -> {strona}")

if __name__ == "__main__":
    odwiedz_strone("https://www.instagram.com")
    odwiedz_strone("https://www.facebook.com")
    odwiedz_strone("https://www.youtube.com")

    pokaz_historie()

    cofnij_strone()
    pokaz_historie()

    strona_dalej()
    pokaz_historie()
