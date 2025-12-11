""" 8. feladat - OOP: BankAccount osztály
Készíts egy BankAccount osztályt:
attribútumok: név, egyenleg
metódusok: deposit(), withdraw(), get_balance()
Hozz létre két bankszámla objektumot, és teszteld. """

class BankAccount:
    def __init__(self,nev,egyenleg = 0):
        self.name = nev
        self.balance = egyenleg

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):    
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Nincs elég fedezet!")

    def getBalance(self):
        return self.balance

acc1 = BankAccount("Han Solo",500000)
acc2 = BankAccount("Lando Calrissian",210000)
acc3 = BankAccount("Jabba",78900000)

acc1.deposit(7000)
acc1.withdraw(357)

accs = [acc1,acc2,acc3]

""" print(f"{acc1.name}")
print(f"Egyenleg: {acc1.getBalance()}") """

""" for i in accs:
    print(f"Név: {i.name}, Egyenleg: {i.balance} Ft") """

for d in accs:
    d.deposit(78000)
    print(f"Név: {d.name}, Egyenleg: {d.balance} Ft")