from collections import deque

historia_operacji: deque[str] = deque()

def wykonaj_operacje(opis: str) -> None:
    historia_operacji.append(opis)
    print(f"Wykonano '{opis}', (operacji na stosie: {len(historia_operacji)}")

def cofnij() -> None:
    if len(historia_operacji) > 1:
        ostatnia_operacja = historia_operacji.pop()
        print(f"Cofnięto {ostatnia_operacja}")
        print(f"Na stosie pozostało {len(historia_operacji)}")
    else:
        print("Brak operacji do cofnięcia")

def zobacz_ostatnia() -> None:
    if len(historia_operacji) != 0:
        print(f"Ostatnia operacja: {historia_operacji[-1]}")
    else:
        print("Stos jest pusty - brak operacji.")

def wyswietl_stos() -> None:
    if len(historia_operacji) != 0:
        historia_reversed = enumerate(reversed(historia_operacji), start=1)
        print("Stos operacji:")
        for index, operacja in historia_reversed:
            print(f"{index}. {operacja}")
    else:
        print("Stos jest pusty - brak operacji.")


if __name__ == "__main__":

    print(" ### Mechanizm Cofnij / Undo ###")

    print("-- Wykonywanie operacji --")
    wykonaj_operacje("Otwarto nowy dokument")
    wykonaj_operacje("Wpisano tekst 'Hello World'")
    wykonaj_operacje("Zmieniono czcionkę na Bold")
    wykonaj_operacje("Usunięto słowo 'przykład'")
    wyswietl_stos()

    print("\n-- Podgląd wierzchołka (peek) --")
    zobacz_ostatnia()

    print("\n-- Cofnij (Undo) --")
    cofnij()
    wyswietl_stos()

    print("\n-- Cofnij jeszcze dwa razy --")
    cofnij()
    cofnij()
    wyswietl_stos()

    print("\n-- Cofnij ostatnią operację --")
    cofnij()

    print("\n-- Próba cofnięcia na pustym stosie --")
    cofnij()