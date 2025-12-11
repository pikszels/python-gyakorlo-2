""" 10. feladat - OOP: Öröklődés
Készíts egy Allat alaposztályt (név, életkor).
Készíts két leszármazottat:
Kutya (plusz: fajta)
Macska (plusz: szín)
Mindkettőnek legyen hang() metódusa, ami kiírja a saját hangját.
Példányosítsd őket és hívd meg a metódust. """

class Allat():
    def __init__(self,nev,kor):
        self.nev = nev
        self.kor = kor

class Kutya(Allat):
    def __init__(self, nev, kor, fajta):
        super().__init__(nev, kor)
        self.type = fajta
    
    def hang(self):
        print(f"{self.nev}: Vau-Vau")

class Macska(Allat):
    def __init__(self, nev, kor, szin):
        super().__init__(nev, kor)
        self.color = szin
    
    def hang(self):
        print(f"{self.nev}: Miaúúúúúúúúú")


kutya = Kutya("Rozi",5,"keverék")
kutya.hang()
macska = Macska("Batman",8,"cirmos")  
macska.hang()      
print(f"{kutya.nev}, {kutya.kor} éves, {kutya.type} kutya.")
print(f"{macska.nev}, {macska.kor} éves, {macska.color} macska.")