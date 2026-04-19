from collections import deque

kolejka_drukowania: deque[str] = deque()


def dodaj_dokument(nazwa: str) -> None:
    kolejka_drukowania.append(nazwa)
    print(f"Dodano dokument {nazwa} do kolejki drukowania.")
    print(f" Pozycja: {len(kolejka_drukowania)}")


def drukuj_nastepny() -> None:
    if len(kolejka_drukowania) > 1:
        nastepny_dokument = kolejka_drukowania.popleft()
        print(f"Drukowanie dokumentu: {nastepny_dokument}")
    else:
        print("Brak dokumentów do drukowania.")

def liczba_dokumentow() -> int:
    return len(kolejka_drukowania)

def pokaz_kolejke() -> None:
    if not kolejka_drukowania:
        print("Kolejka drukowania jest pusta.")
        return
    print("Kolejka drukowania:")
    for dokument in kolejka_drukowania:
        if dokument == kolejka_drukowania[0]:
            print(f" -> {dokument} (następny do druku)")
        else:
            print(f"    {dokument}")


if __name__ == "__main__":

    print("### Kolejka drukowania ###")


    print(" -Dodawanie dokumentów- ")
    dodaj_dokument("raport.pdf")
    dodaj_dokument("prezentacja.pptx")
    dodaj_dokument("zdjecie.png")
    pokaz_kolejke()

    print(f"Dokumentów w kolejce {liczba_dokumentow()} ")

    print(" -Drukowanie dokumentów- ")
    drukuj_nastepny()
    drukuj_nastepny()
    pokaz_kolejke()

    print(" -Drukowanie pozostałych dokumentów- ")
    drukuj_nastepny()

    print(" -Próba drukowania z pustej kolejki- ")
    drukuj_nastepny()




