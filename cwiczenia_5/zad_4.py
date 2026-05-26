import networkx as nx

polaczenia_lotnicze: list[tuple[str, str]] = [
    ("WAW", "LHR"),
    ("WAW", "CDG"),
    ("WAW", "FRA"),
    ("JFK", "LHR"),
    ("JFK", "LAX"),
    ("JFK", "CDG"),
    ("LHR", "CDG"),
    ("LHR", "DXB"),
    ("LHR", "JFK"),   # duplikat kierunkowy – NetworkX zignoruje
    ("CDG", "DXB"),
    ("LAX", "DXB"),
    ("FRA", "DXB"),
]

def zbuduj_graf_lotniczy(polaczenia: list[tuple[str, str]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(polaczenia)
    return G

def znajdz_glowny_hub(G: nx.Graph) -> tuple[str, int]:
    stopnie = G.degree()
    hub: str = ""
    max_stopien: int = 0
    hub, max_stopien = max(stopnie, key=lambda x: x[1])
    for miasto, stopien in stopnie:
        if stopien > max_stopien:
            hub = miasto
            max_stopien = stopien
    return hub, max_stopien


if __name__ == "__main__":
    print("=" * 55)
    print("Zadanie 4 – NetworkX: Analiza sieci lotniczej")
    print("=" * 55)

    # Budowanie grafu (kod gotowy)
    G_loty = zbuduj_graf_lotniczy(polaczenia_lotnicze)

    print(f"\nGraf wczytany poprawnie.")
    print(f"  Liczba lotnisk (węzłów):       {G_loty.number_of_nodes()}")
    print(f"  Liczba połączeń (krawędzi):    {G_loty.number_of_edges()}")

    print("\nWszystkie lotniska w sieci:")
    for lotnisko in sorted(G_loty.nodes()):
        print(f"  {lotnisko}")

    # Analiza stopni (do zaimplementowania)
    print("\n" + "-" * 55)
    print("Szukam głównego hubu przesiadkowego...")
    print("-" * 55)

    hub, liczba = znajdz_glowny_hub(G_loty)

    if hub:
        print(f"\nGłówny hub: {hub}  ({liczba} bezpośrednich połączeń)")

        # Bonus: wypisz pełny ranking lotnisk posortowany malejąco
        print("\nRanking lotnisk wg liczby połączeń:")
        wszystkie_stopnie = dict(G_loty.degree())
        ranking = sorted(wszystkie_stopnie.items(), key=lambda x: x[1], reverse=True)
        for miejsce, (lotnisko, stopien) in enumerate(ranking, start=1):
            znacznik = " ← HUB" if lotnisko == hub else ""
            print(f"  {miejsce}. {lotnisko}: {stopien} połączeń{znacznik}")
    else:
        print("\n  [!] Funkcja nie została jeszcze zaimplementowana.")