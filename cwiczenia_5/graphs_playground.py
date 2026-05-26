import networkx as nx
import matplotlib.pyplot as plt

GRAF_SLOWNIK: dict[str, list[str]] = {
    "Alicja":  ["Bartosz", "Celina"],
    "Bartosz": ["Alicja", "Celina", "Damian"],
    "Celina":  ["Alicja", "Bartosz", "Ewa"],
    "Damian":  ["Bartosz", "Ewa"],
    "Ewa":     ["Celina", "Damian"],
}

def pokaz_graf_jako_slownik(graf: dict[str, list[str]]) -> None:

    print("=" * 50)
    print("CZĘŚĆ 1 – Graf jako słownik Pythona")
    print("=" * 50)

    print("\nWierzchołki (osoby) w grafie:")
    for osoba in graf:
        print(f"  {osoba}")

    print("\nKrawędzie (znajomości) w grafie:")
    wypisane: set[frozenset] = set()
    for osoba, znajomi in graf.items():
        for znajomy in znajomi:
            krawedz = frozenset({osoba, znajomy})
            if krawedz not in wypisane:
                print(f"  {osoba} -- {znajomy}")
                wypisane.add(krawedz)

    print(f"\nLiczba wierzchołków: {len(graf)}")
    print(f"Liczba krawędzi:     {len(wypisane)}")


def pokaz_graf_networkx(graf: dict[str, list[str]]) -> nx.Graph:

    print("\n" + "=" * 50)
    print("CZĘŚĆ 2 – Graf w bibliotece NetworkX")
    print("=" * 50)


    G = nx.Graph()

    for osoba, znajomi in graf.items():
        for znajomy in znajomi:
            G.add_edge(osoba, znajomy)

    print(f"\nWierzchołki NetworkX: {list(G.nodes())}")
    print(f"Krawędzie NetworkX:   {list(G.edges())}")
    print(f"Liczba wierzchołków:  {G.number_of_nodes()}")
    print(f"Liczba krawędzi:      {G.number_of_edges()}")

    print("\nStopień każdego wierzchołka (liczba znajomych):")
    for osoba, stopien in G.degree():
        print(f"  {osoba}: {stopien} znajomych")

    return G

def wizualizuj_graf(G: nx.Graph, nazwa_pliku: str = "playground_siec_spolecznosciowa.png") -> None:

    print("\n" + "=" * 50)
    print("CZĘŚĆ 3 – Wizualizacja (NetworkX + Matplotlib)")
    print("=" * 50)


    uklad = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(7, 5))
    plt.title("Sieć społecznościowa – 5 osób", fontsize=14)

    nx.draw(
        G,
        pos=uklad,
        with_labels=True,       # wyświetl nazwy wierzchołków
        node_color="skyblue",   # kolor węzłów
        node_size=1800,         # rozmiar węzłów
        font_size=11,
        font_weight="bold",
        edge_color="gray",
        width=2,
    )

    plt.show()

    plt.savefig(nazwa_pliku, dpi=120, bbox_inches="tight")
    print(f"\nWykres zapisano do pliku: {nazwa_pliku}")
    print("Aby wyświetlić wykres w oknie, odkomentuj linię 'plt.show()' w kodzie.")

if __name__ == "__main__":
    pokaz_graf_jako_slownik(GRAF_SLOWNIK)
    G = pokaz_graf_networkx(GRAF_SLOWNIK)
    wizualizuj_graf(G)
