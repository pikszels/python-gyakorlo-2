""" 4. feladat - Számjegyek összege
Kérj be egy számot, majd számold ki a számjegyeinek összegét. """

n = input("Adj meg egy számot: ")
mind = 0

for i in range(len(n)):
    mind = mind + int(n[i])

print(f"A számjegyek összege:{mind}")