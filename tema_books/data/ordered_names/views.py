from django.http import HttpResponse

def alphabetically_sorted_names(request):
    names = [
        "Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana",
        "Vasile", "Ioana", "George", "Gabriela", "Florin", "Mihai",
        "Diana", "Radu", "Laura", "Cristian", "Raluca",
        "Bianca",
    ]
    sorted_names = sorted(names)
    rezultat = "<h2>Nume sortate alfabetic</h2>"
    rezultat += "<br>".join(sorted_names)
    return HttpResponse(rezultat)