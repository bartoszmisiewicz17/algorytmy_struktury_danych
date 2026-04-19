class KategoriaNode:
    nazwa: str
    dzieci: list["KategoriaNode"]

    def __init__(self, nazwa: str):
        self.nazwa = nazwa
        self.dzieci = []

    def dodaj_podkategorie(self, podkategorie: "KategoriaNode") -> None:
        self.dzieci.append(podkategorie)

    def repr(self) -> str:
        return f"KategoriaNode(nazwa={self.nazwa}, dzieci={self.dzieci})"


def wyswietl_drzewo(kategoria: KategoriaNode, poziom: int = 0) -> None:
    print(" " * poziom * 4 + kategoria.nazwa)
    for dziecko in kategoria.dzieci:
        wyswietl_drzewo(dziecko, poziom + 1)

def policz_wszystkie(kategoria: KategoriaNode) -> int:
    liczba_kategorii = 1
    for dziecko in kategoria.dzieci:
        liczba_kategorii += policz_wszystkie(dziecko)
    return liczba_kategorii

if __name__ == "__main__":

    # --- Budowa drzewa kategorii sklepu -------------------------------------
    # Gotowy kod – NIE modyfikuj tej sekcji.
    # Twoje funkcje muszą poprawnie obsłużyć poniższe drzewo.

    sklep = KategoriaNode("Sklep (korzeń)")

    # Gałąź 1: Elektronika
    elektronika = KategoriaNode("Elektronika")
    laptopy     = KategoriaNode("Laptopy")
    telefony    = KategoriaNode("Telefony")
    android     = KategoriaNode("Android")
    iphone      = KategoriaNode("iPhone")

    telefony.dodaj_podkategorie(android)
    telefony.dodaj_podkategorie(iphone)
    elektronika.dodaj_podkategorie(laptopy)
    elektronika.dodaj_podkategorie(telefony)

    # Gałąź 2: Dom i Ogród
    dom_i_ogrod = KategoriaNode("Dom i Ogród")
    meble       = KategoriaNode("Meble")
    narzedzia   = KategoriaNode("Narzędzia")
    fotele      = KategoriaNode("Fotele")
    sofy        = KategoriaNode("Sofy")

    meble.dodaj_podkategorie(fotele)
    meble.dodaj_podkategorie(sofy)
    dom_i_ogrod.dodaj_podkategorie(meble)
    dom_i_ogrod.dodaj_podkategorie(narzedzia)

    # Gałąź 3: Odzież
    odziez      = KategoriaNode("Odzież")
    meska       = KategoriaNode("Męska")
    damska      = KategoriaNode("Damska")
    odziez.dodaj_podkategorie(meska)
    odziez.dodaj_podkategorie(damska)

    # Podpięcie gałęzi do korzenia
    sklep.dodaj_podkategorie(elektronika)
    sklep.dodaj_podkategorie(dom_i_ogrod)
    sklep.dodaj_podkategorie(odziez)

    # --- Test 1: Wyświetlenie całego drzewa ----------------------------------
    print("=" * 50)
    print("Test 1 – Struktura drzewa kategorii:")
    print("=" * 50)
    wyswietl_drzewo(sklep)

    # --- Test 2: Zliczanie węzłów --------------------------------------------
    print("\n" + "=" * 50)
    print("Test 2 – Liczba kategorii w drzewie:")
    print("=" * 50)
    liczba = policz_wszystkie(sklep)
    print(f"Łączna liczba kategorii (węzłów): {liczba}")
    print("(Oczekiwana wartość: 14)")