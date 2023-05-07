from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item

author = {
    "name": "Евгений",
    "surname": "Юрченко",
    "phone": "89007001122",
    "email": "eyurchenko@specialist.ru",
}


# Create your views here.
def home(request):
    context = {
        "name": author['name'],
        "surname": author['surname']
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'author': author
    }
    return render(request, 'about.html', context)


def item_page(request, id):
    for item in items:
        if item['id'] == id:
            context = {
                'item': item
            }
            return render(request, 'item-page.html', context)

    return HttpResponseNotFound(f"Товар с id={id} не найден")


def items_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'item-list.html', context)
