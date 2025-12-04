""" 1. feladat - Faktoriális számítása ciklussal
Kérj be egy számot, és számold ki a faktoriálisát iterációval. """

n = int(input("Kérem az egész számot: "))
f = 1

for i in range(1, n + 1):
    f = f * i

print(f"{n} faktoriálisa {f}")