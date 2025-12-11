""" 9. feladat - OOP + lista: Tanulók kezelése
Student osztály: név, életkor, átlag.
Kérj be 3 tanulót, tedd őket listába, majd írd ki annak a nevét, akinek a legjobb az átlaga. """

class Student():
    students = []


    def __init__(self,nev,eletkor,atlag):
        self.name = nev
        self.age = eletkor
        self.avg = atlag
        self.students.append(self)

        max = self.students[0].avg
        id = 0

        for i in range(len(self.students)):
            if self.students[i].avg > max:
                max = self.students[i] 
                id = i
                
        print(self.students[id].name)

    
    

for i in range(3):
    nev = input(f"Kérem a(z) {i}. nevet: ")
    kor = input(f"Kérem az {i}. életkort: ")
    atlag = float(input(f"Kérem az {i}. átlagot: "))
    Student(nev,kor,atlag)
