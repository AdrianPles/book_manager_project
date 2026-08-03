from django.http import HttpResponse

def decreasing_sorted_nb(request):
    numbers = [73, 28, 95, 14, 61, 39, 87, 5, 46, 32, 345, 232, 12, 33, 99, 96, 35, 1, 9, 10]
    sorted_numbers = sorted(numbers, reverse=True)
    rezultat = "<h2>Numerele sortate descrescator</h2>"
    for number in sorted_numbers:
        rezultat += f"{number}<br>"  # introducem line break pentru a afisa numerele pe cate o linie noua
    return HttpResponse(rezultat)