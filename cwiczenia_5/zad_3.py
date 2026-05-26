import networkx as nx

polaczenia_kurierskie: list[tuple[str, str, int]] = [
    ("Magazyn",    "Adamowo",    15),
    ("Magazyn",    "Brzeziny",   25),
    ("Adamowo",    "Centrum",    20),
    ("Adamowo",    "Dęblin",     40),
    ("Brzeziny",   "Centrum",    10),
    ("Brzeziny",   "Elbląg",     30),
    ("Centrum",    "Falenty",    15),
    ("Centrum",    "Dęblin",     20),
    ("Dęblin",     "Punkt_Cel",  10),
    ("Falenty",    "Punkt_Cel",  25),
    ("Elbląg",     "Punkt_Cel",  35),
]

def zbuduj_graf_kurierski(
    polaczenia: list[tuple[str, str, int]]
) -> nx.Graph:

    G = nx.Graph()

    for miasto_a, miasto_b, czas in polaczenia:
        G.add_edge(miasto_a, miasto_b, czas=czas)

    return G

def znajdz_optymalna_trase(
    G: nx.Graph,
    magazyn: str,
    punkt_odbioru: str
) -> tuple[list[str], float]:

    trasa = nx.shortest_path(G, source=magazyn, target=punkt_odbioru, weight="czas")
    laczny_czas = nx.shortest_path_length(G, source=magazyn, target=punkt_odbioru, weight="czas")

    return trasa, laczny_czas

if __name__ == "__main__":
    print("=" * 55)
    print("Zadanie 3 – NetworkX: Optymalna trasa kurierska")
    print("=" * 55)

    # Budowanie grafu (kod gotowy)
    G_kurier = zbuduj_graf_kurierski(polaczenia_kurierskie)

    print(f"\nGraf wczytany poprawnie.")
    print(f"  Liczba miast (węzłów):        {G_kurier.number_of_nodes()}")
    print(f"  Liczba połączeń (krawędzi):   {G_kurier.number_of_edges()}")

    # Podgląd wag krawędzi
    print("\nPołączenia z czasami przejazdu:")
    for u, v, dane in G_kurier.edges(data=True):
        print(f"  {u:12} -- {v:12}  czas: {dane['czas']} min")

    # Wyznaczanie optymalnej trasy (do zaimplementowania)
    print("\n" + "-" * 55)
    print("Szukam optymalnej trasy: Magazyn → Punkt_Cel")
    print("-" * 55)

    trasa, czas = znajdz_optymalna_trase(G_kurier, "Magazyn", "Punkt_Cel")

    if trasa is not None:
        print(f"\nOptymalna trasa ({len(trasa) - 1} odcinków):")
        print(f"  {' → '.join(trasa)}")
        print(f"\nŁączny czas przejazdu: {czas} minut")
    else:
        print("\n  [!] Funkcja nie została jeszcze zaimplementowana.")