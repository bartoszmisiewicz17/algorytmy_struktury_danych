LICZBA_DNI = 7
DNI_TYGODNIA = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]



temperatury: list = [None] * LICZBA_DNI



def wpisz_temperatury() -> None:
    przykladowe_temp = [12.5, 14.0, 9.8, 11.3, 16.7, 20.1, 18.4]
    for i in range(LICZBA_DNI):
        temp = przykladowe_temp[i]
        temperatury[i] = temp

def oblicz_srednia() -> float:
    suma = sum(temperatury)
    srednia = suma / LICZBA_DNI
    return srednia

def najcieplejszy_dzien() -> tuple[str, float]:
    max_temp = max(temperatury)
    index_max = temperatury.index(max_temp)
    return DNI_TYGODNIA[index_max], max_temp


if __name__ == "__main__":
    wpisz_temperatury()

    print(" === Temperatura w ciągu tygodnia === ")
    for i in range(LICZBA_DNI):
        print(f"{DNI_TYGODNIA[i]}: {temperatury[i]} °C")

    srednia = oblicz_srednia()
    print(f"\nŚrednia temperatura: {srednia:.2f} °C")

    dzien, temp = najcieplejszy_dzien()
    print(f"Najcieplejszy dzień: {dzien} z temperaturą {temp} °C")