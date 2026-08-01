
# Primind această listă de numere:
#
# numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17]
#
# Si lista de persoane:
#
# people = ["Codrin", "Adrian", "John", "Maria", "Tudor", "Maximilian", "Spike"]
#  Creati o functie care returnează: o lista de dicționare, care arată astfel:
#
# result = { "name": "Codrin", "age": 30, "of_age": True}
#
# Pentru fiecare persoană, alegeți un număr random din lista de numere.
# Unde of_age este true doar daca numărul ales este mai mare de 18
#
# import random
# picked = random.choice(numbers)
#
# Creati o altă funcție care filtrează toate persoanele și returnează doar persoanele of_age.
# Creați oldest_person, o funcție care returnează cea mai bătrână persoană
# La fel și pentru youngest_person, cea mai tânără
#
# Printați acel rezultat.

# result = [{ "name": "Codrin", "age": 30, "of_age": True}, ...]

import random


numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17]
people = ["Codrin", "Adrian", "John", "Maria", "Tudor", "Maximilian", "Spike"]


class MainConstuctor:
    def __init__(self, lista_people, lista_numbers):
        self.people = lista_people
        self.numbers = lista_numbers
        self.dict_list = []

    def generate_list(self):
        if len(self.numbers) < len(self.people):
            return f"EROARE: Nu sunt suficiente numere unice in lista pentru toate numele!"
        # aici curatam valorile duplicate din lista de numere [13, 13]
        # cream o noua lista cu valori unice
        cleaned_duplicate_nb = list(set(self.numbers))
        # cream o variabila prin care extragem un grup de valori unice pentru lungimea listei people
        unique_numbers = random.sample(cleaned_duplicate_nb, len(self.people))
        print(f"Valorile unice: {unique_numbers}")
        self.dict_list = [
            {"name": n, "age": a, "of_age": a > 18}
            for n, a in zip(self.people, unique_numbers)
        ]
        return self.dict_list

    def filter_of_age(self, major=True):
        return [nume for nume in self.dict_list if nume["of_age"] == major]

    def oldest_person(self):
        # returnam din lista dict_list, maximul filtrat dupa 'age'
        oldest_person = max(self.dict_list, key=lambda nume: nume["age"])
        return oldest_person

    def youngest_person(self):
        # returnam din lista dict_list, maximul filtrat dupa 'age'
        oldest_person = min(self.dict_list, key=lambda nume: nume["age"])
        return oldest_person

generator = MainConstuctor(people, numbers)
result = generator.generate_list()
print(result)
print()
print("Lista completa:")
for i in result:
    print(i)

print()
filter = generator.filter_of_age(major=True)
print('Majorii:')
for a in filter:
    print(a)

oldest_p = generator.oldest_person()
print()
print("Persoana cea mai in varsta este:")
print(oldest_p)

youngest_p = generator.youngest_person()
print()
print("Persoana cea mai tanara este:")
print(youngest_p)