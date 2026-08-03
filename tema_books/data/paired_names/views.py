from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random
def lista_names(request):
    names = [
        "Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana",
        "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai",
        "Diana", "Radu", "Laura", "Cristian", "Raluca",
        "Bianca",
    ]
    numbers = [73, 28, 95, 14, 61, 39, 87, 5, 46, 32, 345, 232, 12, 33, 99, 96, 35, 1, 9, 10]
    lista_dict = [
        {"name": name, "count": random.choice(numbers)} # pentru valori "count" atribuite random la fiecare request
        for name in names
        # for name, number in zip(names, numbers) # pentru valori "count":number -> fixe
    ]
    # aici sortam lista de dictionare dupa nume, in ordine alfabetica
    sorted_list = sorted(lista_dict, key=lambda x: x["name"])

    return render(request, template_name="tema_books/sorted_names.html", context={"scrambled": sorted_list})
