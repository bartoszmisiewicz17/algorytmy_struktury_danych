lista_zakupow: list[str] = []


def dodaj_produkt(produkt: str) -> None:
    if produkt not in lista_zakupow:
        lista_zakupow.append(produkt)
    else:
        print(f"Produkt '{produkt}' już znajduje się na liście zakupów.")


def usun_produkt(produkt: str) -> None:
    if produkt in lista_zakupow:
        lista_zakupow.remove(produkt)
    else:
        print(f"Produkt '{produkt}' nie znajduje się na liście zakupów.")


def posortuj_liste() -> None:
    lista_zakupow.sort()


def wyswietl_liste() -> None:
    if not lista_zakupow:
        print("Lista zakupów jest pusta.")
    else:
        print(f"Lista zakupów ({len(lista_zakupow)} produktów):")
        for index, produkt in enumerate(lista_zakupow, start=1):
            print(f"{index}. {produkt}")


if __name__ == "__main__":
    dodaj_produkt("Mleko")
    dodaj_produkt("Chleb")
    dodaj_produkt("Jajka")
    dodaj_produkt("Masło")
    dodaj_produkt("Ser")

    print("\nPo dodaniu produktów:")
    wyswietl_liste()

    usun_produkt("Chleb")

    print("\nPo usunięciu produktu 'Chleb':")
    wyswietl_liste()

    posortuj_liste()

    print("\nPo posortowaniu listy:")
    wyswietl_liste()
