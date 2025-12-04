""" 6. feladat - Szótár gyakorlás
Kérj be 5 nevet és életkort, majd tárold őket egy dict-ben.
Ezután írd ki a legidősebb személy nevét. """

emberek = {}

for i in range(2):
    lista =[]
    nev = input("Adj meg egy nevet: ")
    eletkor = input("Add meg az ember életkorát: ")
    lista.append(eletkor)
    hajszin = input("Add meg az ember hajszínét: ")
    lista.append(hajszin)
    emberek[nev] = lista

print(emberek)
#print(emberek["Zoli"])
print(f"A legidősebb ember: {max(emberek, key = emberek.get)}")

for x in emberek:
    print(f"{x} életkora: {emberek[x][0]}")
    print(f"{x} hajszíne: {emberek[x][1]}")

""" max = 0
i = 0
for x in emberek:
    if int(emberek[x][0]) > int(max):
        max = int(emberek[x][0])
        i = x
print(f"A legidősebb ember neve {i}, adatai: {x}") """