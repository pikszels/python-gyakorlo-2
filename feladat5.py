""" 5. feladat - Lista elemeinek négyzetre emelése
Adott egy lista, készíts új listát, amely minden elem négyzetét tartalmazza. """

lista = [5,8,12,51,82,77]
nlista = []

for i in range(len(lista)):
    nlista.append(lista[i] ** 2)

print(f"A lista elemei: {lista}")
print(f"A lista elemeinek négyzete: {nlista}")