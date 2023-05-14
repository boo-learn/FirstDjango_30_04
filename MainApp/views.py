from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Item, Color

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
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id={id} не найден")

    context = {
        'item': item
    }
    return render(request, 'item-page.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'item-list.html', context)


def item_add(request):
    if request.method == "GET":
        colors = Color.objects.all()
        context = {
            "colors": colors
        }
        return render(request, "item-add.html", context)


# Получаем данные от формы
def item_create(request):
    if request.method == "POST":
        form_data = request.POST
        # print(f"{form_data=}")
        item = Item(
            name=form_data['name'],
            brand=form_data['brand'],
            count=form_data['count'],
        )
        item.save()
        return redirect('items-list')
