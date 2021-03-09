# Klasy do projektu zaliczeniowego
class Dowody():
    """Przechowuje zagadki dowodowe i wykonuje manipulacje"""

    def __init__(self,seria,miejsce):
        """Definiowanie obiektów"""
        self.__seria = seria
        self.__miejsce = miejsce

    def podaj_dowody(self):
        """Podaje co wiemy o dowodach"""
        print(f'Seria liczb:         {self.__seria}')
        print(f'Gdzie były:  {self.__miejsce}')

    @property
    def odwrocona(self):
        """Zwraca odwróconą serię liczb"""
        return self.__seria[::-1]


class Znaki():
    """Przechowuje informacje o ciągach znaków i wykonuje na nich proste manipulacje."""

    def __init__(self, ciag):
        self.__ciag = ciag
        self.__dlugosc = len(self.ciag)

    def drukuj(self):
        """Drukuje informacje"""
        print(f"Ciąg: {self.__ciag}")
        print(f"Długość:   {self.__dlugosc}")

    @property
    def ciag(self):
        """Zwraca ciag."""
        return self.__ciag

    @property
    def odwrocony(self):
        """Zwraca odwróconą sekwencję."""
        return self.__ciag[::-1]

    def porownanie_1(self, ciag_2):
        """Przyrównuje dwa ciągi liter"""
        for x1, x2 in zip(self.ciag, ciag_2.ciag):
            print(f"{x1}-{x2}")

    def porownanie_2(self, ciag_2):
        """Porównuje ciąg jeden i drugi odwrócony"""
        for x1, x2 in zip(self.odwrocony,ciag_2.ciag):
            print(f"{x1}-{x2}")
