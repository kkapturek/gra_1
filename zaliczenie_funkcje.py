# Funkcje do projektu zaliczeniowego

# Importowanie modułów do użycia w funkcjach
import zaliczenie_klasy as zk
import time as t

def zapis_pliku():
    """Funkcja tworząca i zapisująca plik tekstowy."""
    #Definiujemy nazwę pliku
    nazwa=input('\nPodaj nazwę nowego pliku: ')
    #Definiujemy treść pliku
    tresc=input('Podaj treść pliku tekstowego: ')
    #Tworzymy plik
    plik_kolejnosci = open(f'{nazwa}.txt', 'wt')
    plik_kolejnosci.write(f"{tresc}")
    plik_kolejnosci.close()
    #Kontrolnie pokazujemy jego treść
    odczyt = open(f'{nazwa}.txt', 'rt')
    print(f'Treść nowopowstałego pliku to: {odczyt.read()}')
    odczyt.close()
    #Koniec funkcji

def odczyt_pliku():
    """Odczytuje zawartość istniejącego pliku obsługując wyjątki"""
    #Tworzymy pętlę, aby móc wspisywać nazwę aż wpiszemy poprawną
    while True:
        nazwa = input('Podaj nazwę zapisanego pliku: ')
        #Uwzględniamy obsługę wyjątku
        try:
            odczyt = open(f'{nazwa}.txt', 'rt')
        except FileNotFoundError:
            print(f"Nie ma pliku: {nazwa}")
        else:
            tresc = odczyt.read()
            odczyt.close()
            break
    #Drukujemy zawartość pliku
    print(f"Kolejność zdjęć to: " + tresc)



