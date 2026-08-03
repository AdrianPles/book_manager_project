from django.urls import path
from tema_books.data.ordered_names import views as ordered_names
from tema_books.data.ordered_numbers import views as ordered_numbers
from tema_books.data.paired_names import views

urlpatterns = [
    path("data/ordered_names/", ordered_names.alphabetically_sorted_names, name="alphabetically_sorted_names"),
    path("data/ordered_numbers/",ordered_numbers.decreasing_sorted_nb, name="decreasing_sorted_nb"),
    path("data/paired_names/", views.lista_names, name="lista_names"),
]