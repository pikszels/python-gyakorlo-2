""" 7. feladat - OOP: Egyszerű Osztály - Auto
Hozz létre egy Auto osztályt, amely attribútumai: márka, típus, évjárat
Az osztály tartalmazzon metódust, ami kiírja a teljes adatot szép formában. """

class Auto:
    def __init__(self, gyarto, tipus, evjarat):
        self.gyarto = gyarto
        self.tipus = tipus
        self.evjarat = evjarat
    def mutat(self):
        print(f"{self.gyarto} {self.tipus}, {self.evjarat}")

auto1 = Auto("Honda", "Civic", 2001)
auto2 = Auto("Fiat", "Tipo", 1992)
auto3 = Auto("Lamborghini", "Countach", 1971)

auto1.mutat()
auto2.mutat()
auto3.mutat()