class ProduktNode:
    def __init__(self, id_produktu: int, nazwa: str):
        self.id = id_produktu
        self.nazwa = nazwa
        self.lewo = None
        self.prawo = None

def wstaw(korzen: ProduktNode, nowy_wezel: ProduktNode) -> ProduktNode:
    if korzen is None:
        return nowy_wezel

    if nowy_wezel.id < korzen.id:
        korzen.lewo = wstaw(korzen.lewo, nowy_wezel)
    elif nowy_wezel.id > korzen.id:
        korzen.prawo = wstaw(korzen.prawo, nowy_wezel)
    else:
        print(f"Produkt z ID {nowy_wezel.id} już istnieje. Pomijam duplikat.")

    return korzen

def szukaj(korzen: ProduktNode, szukane_id: int) -> str:
    if korzen is None:
        return None
    elif korzen.id == szukane_id:
        return korzen
    elif szukane_id < korzen.id:
        return szukaj(korzen.lewo, szukane_id)
    else:
        return szukaj(korzen.prawo, szukane_id)

def wyswietl_katalog(korzen: ProduktNode):
    if korzen is not None:
        wyswietl_katalog(korzen.lewo)
        print(f"ID: {korzen.id}, Nazwa: {korzen.nazwa}")
        wyswietl_katalog(korzen.prawo)



if __name__ == "__main__":
    print("=== Katalog Produktów (BST) ===\n")

    # Tworzymy korzeń (środek zakresu, żeby drzewo było w miarę zbalansowane)
    katalog = ProduktNode(50, "Laptop Gamingowy")

    # Dodajemy produkty
    produkty_do_dodania = [
        (20, "Myszka bezprzewodowa"),
        (70, "Monitor 4K"),
        (10, "Klawiatura mechaniczna"),
        (30, "Słuchawki ANC"),
        (60, "Kabel HDMI"),
        (80, "Podkładka pod mysz")
    ]

    for id_p, nazwa in produkty_do_dodania:
        wstaw(katalog, ProduktNode(id_p, nazwa))

    print("-- Pełny katalog (posortowany po ID) --")
    wyswietl_katalog(katalog)

    print("\n-- Wyszukiwanie produktów --")
    print(f"Szukam ID 30: {szukaj(katalog, 30)}")
    print(f"Szukam ID 99: {szukaj(katalog, 99)}")

    print("\n-- Test duplikatu --")
    wstaw(katalog, ProduktNode(30, "DUPLIKAT Słuchawek"))
    print(f"Szukam ID 30 po próbie wstawienia duplikatu: {szukaj(katalog, 30)}")
    # Powinno nadal zwrócić "Słuchawki ANC", nie "DUPLIKAT Słuchawek"