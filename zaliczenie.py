# Projekt zaliczeniowy - gra przygodowa

# Import modułów
import random
import time as t
import zaliczenie_funkcje as zf
import zaliczenie_klasy as zk
import matplotlib.pyplot as plt

# Informacje wraz z poborem informacji od użytkownika
print('\nMałe miasteczko gdzieś przy granicy. Ludzie spoglądają na Ciebie z zaciekawieniem.\n '
      'Leniwym krokiem zmierzasz do obskórnego budynku, tuż przy fontannie.')
# Używamy funkcji sleep w celach ładniejszego wyświetlania programu
t.sleep(1)
print('\n~KOMISARIAT~\n')
t.sleep(1)
print('-Witamy. Jesteś pewnie tym detektywem ze stolicy? W końcu. Wyleciało mi z głowy imię...')
t.sleep(2)
imie = input('-Mów mi ')
t.sleep(1)
print(f'-Oh, no tak! Więc dzień dobry, {imie}. Ja jestem komisarz John.')
print('Chcesz odrazu przejrzeć akta sprawy, czy oprowadzić Cię po okolicy?')
# Tworzymy pierwszą pętlę - rozwidlenie w fabule.
# Uwzględniamy możliwość powrotu do zapytania w przypadku wpisania opcji, której nie ma

while True:
    wybor = input('\n [ A - akta / O - okolica ] ')

    # Zaczynamy instrukcje wyboru
    if wybor.upper() == 'A':
        print(f'\n-Dobrze, {imie}. Przejdźmy do gabinetu...')
        t.sleep(2)
        print('Proszę. Oto akta. Czuj się jak u siebie.')
        t.sleep(1)
        print('\n~Siadasz wygodnie w fotelu i oglądasz pociemniałe kartki.~')
        t.sleep(1)
        print('Czytasz historię tajemniczych zaginięć mających miejsce w ciągu ostatnich miesięcy. Przeglądasz zeznania,\n'
            'opisy ofiar, zdjęcia. Trzy z nich przykuwają Twoją uwagę. Wyglądają jakby miały do siebie pasować...\n'
            'Próbujesz ułożyć je w odpowiedniej kolejności.\n')
        t.sleep(1)

        # Tworzymy pętlę umożliwiającą nam zapis kolejności zdjęć lub rezygnację z tej opcji
        zdjecia_petla = True
        while zdjecia_petla:
            zdjecia = input('[Wpisz kolejność dla zdjęć 1, 2 i 3 (bez spacji)]\n')
            if zdjecia != '231':
                print('Chyba nie tak... Próbujesz ponownie.')
                continue
            else:
                zapis_kolejnosci = input('Udało się! Zdjęcia wyraźnie przedstawiają jedno, pełne pomieszczenie.\n'
                                        'Może warto zapisać tą kolejność?\n'
                                        '[ T - tak / N - nie] ')
                if zapis_kolejnosci.upper() == 'T':
                    # Korzystamy z funkcji zapisującej plik
                    zf.zapis_pliku()
                else:
                    print('Może faktycznie nie ma to większego znaczenia.')
            zdjecia_petla = False
        t.sleep(2)
        print('\nOkej, koniec tego dobrego, czas rozejrzeć się po okolicy.')
        print('Idziesz na piewsze miejsce zbrodni. Jest to stary, opuszczony dom.')
        # Tworzymy pętlę umożliwiającą nam wejście do budynku lub rezygnację z tej opcji
        while True:
            wchodzisz = input('Wchodzisz? [T - tak / N - nie] ')
            if wchodzisz.upper() == 'T':
                t.sleep(1)
                print('\nRozglądasz się po ciemnych pomieszczeniach. Szukasz czegoś, co może się okazać przydatne.\n'
                    'Wchodzisz do czegoś, co kiedyś pewnie było salonem. Wygląda znajomo...')
                # Pętla w pętli! Decydujemy czy chcemy sobie przypomnieć treść pliku który stworzyliśmy
                while True:
                    t.sleep(1)
                    pomieszczenie = input('\nZdjęcia! Tylko jaka była ich kolejność... Chcesz odczytać ją z pliku?\n'
                                    '[T - tak / N - nie] ')
                    if pomieszczenie.upper() == 'T':
                        zf.odczyt_pliku()
                        break

                    elif pomieszczenie.upper() == 'N':
                        t.sleep(1)
                        print('Czyli postanawiasz zaufać pamięci... Też dobrze.')
                        break

                    else:
                        print('Nie ma takiej opcji. Spróbuj ponownie.')
                        continue
                t.sleep(2)
                print('\nTak! To tutaj. Ale na ścianach są znaki, których nie było podczas robienia zdjęć.\n'
                    'Czyżby zbrodniarz tu wrócił?\n')
                t.sleep(2)
                print('Zapisujesz dwa ciągi znaków po 4 litery i łączysz je w różne kombinacje, szukając powiazań.\n')
                # Pobieramy od użytkownika znaki i analizujemy je korzystając z funkcji korzystającej z klasy
                ciag_1 = input('Podaj pierwszy ciąg znaków: \n')
                ciag_2 = input('Podaj drugi ciag znaków: \n')
                t.sleep(1)
                ciag_obiekt_1 = zk.Znaki(f'{ciag_1}')
                t.sleep(1)
                ciag_obiekt_2 = zk.Znaki(f'{ciag_2}')
                t.sleep(1)
                # Używamy klasy Znaki()
                ciag_obiekt_1.drukuj()
                t.sleep(1)
                ciag_obiekt_2.drukuj()
                t.sleep(1)
                ciag_obiekt_1.porownanie_1(ciag_obiekt_2)
                t.sleep(1)
                print('~~~~~~~~')
                t.sleep(1)
                ciag_obiekt_1.porownanie_2(ciag_obiekt_2)
                t.sleep(1)
                print('O nie... coś się dzieje!')
                t.sleep(1)
                print(':0')
                t.sleep(1)
                print("'Cahf ah nafl mglw'nafh hh' ahor syha'h ah'legeth, ng llll or'azath syha'hnahh n'ghftephai n'gha ahornah ah'mglw'nafh'!!!")
                t.sleep(2)
                print('\nObudziłeś wielkiego Cthulhu swoją impertynencją. Zjada Cię.')
                break
                # ^ Pierwsze zakończenie gry ^
            elif wchodzisz.upper() == 'N':
                print('Jesteś pewny? To w sumie jedyne co masz do roboty...')
                continue
            else:
                print('Nie ma takiej opcji. Spróbuj ponownie.')
                continue
        break
    # Drugi wybór z rozwidlenia fabularnego
    elif wybor.upper() == 'O':
        print('-Dobrze, zapraszam zatem...')
        t.sleep(2)
        print('\n~Jakiś czas później...~\n')
        t.sleep(2)
        print('-No, i tutaj miała miejsce ostatnia sprawa. Powodzenia!')
        t.sleep(1)
        print('\nOglądasz ciemny zaułek, na ścianach są wypisane cyfry. Czy możliwe, żeby miały jakiś związek?\n')
        t.sleep(1)
        # Wyświetlamy liczby pseudolosowe korzystając z modułu random
        liczby = []
        for i in range(10):
            liczby.append(random.randrange(20))
        t.sleep(1)
        print(f'Liczby na ścianie to: {liczby}')
        # Zaczynamy korzystać z klasy Dowody()
        miejsce_1 = input('Gdzie je znalazłeś? \n')
        dowod_1 = zk.Dowody(liczby, f'{miejsce_1}')
        dowod_1.podaj_dowody()
        print(f'Seria liczb od tyłu: {dowod_1.odwrocona}')
        t.sleep(1)
        print('\nHmm... A może by je tak posortować?\n')
        # Funkcje sortujące listy
        posortowane = sorted(liczby)
        t.sleep(2)
        print(posortowane)
        t.sleep(2)
        print('\nHmm... To też nic Ci nie mówi...\n'
              'Tak! Zróbmy z tego wykres! Napewno coś się z tego wyciągnie.\n')
        legenda_1 = input('Podaj nazwę dla jednej linii: ')
        legenda_2 = input('Podaj nazwę dla drugiej linii: ')
        # TWORZYMY WYKRES :)
        # Atrybuty pierwszej linii
        plt.plot(liczby, 'r-', label=f'{legenda_1}')
        # Atrybuty drugiej linii
        plt.plot(dowod_1.odwrocona, 'g-', label=f'{legenda_2}')
        plt.xlabel('liczba', fontsize=10)
        plt.ylabel('ile', fontsize=10)
        # Lokalizowanie legendy
        plt.legend(loc=0)
        plt.savefig('wykres_1.svg')
        # Wyświetlenie wykresu
        plt.show()

        print('\nZaraza! To wszystko nie ma żadnego sensu!!!\n')
        t.sleep(1)
        print('Chwila... A CO TO???')
        t.sleep(1)
        print('*')
        t.sleep(1)
        print('*')
        t.sleep(1)
        print('*')
        t.sleep(1)
        print('Budzisz się w szpitalu, z głową całą w bandażach.\n'
            'Co się stało? Nie wiesz...\n'
            'Chyba pójdziesz spać dalej...')
        break
        # ^ Drugie zakończenie gry ^
    else:
        print('Nie ma takiej opcji. Wybierz ponownie.')
        continue



