""" 3. feladat - Prímszám ellenőrzése
Döntsd el egy számról, hogy prímszám-e (szelekció + iteráció). """

n = int(input("Kérek egy egész számot: "))
prim = True

if n < 2:
    prim = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prim = False
            break
if prim == True:
    print("A megadott szám prímszám.")
else:
    print("A megadott szám nem prímszám.")