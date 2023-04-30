from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

author = {
    "name": "Евгений",
    "surname": "Юрченко",
    "phone": "89007001122",
    "email": "eyurchenko@specialist.ru",
}
items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def home(request):
    context = {
        "name": author['name'],
        "surname": author['surname']
    }
    return render(request, 'index.html', context)


def about(request):
    text = f"""
    Имя: <b>{author['name']}</b><br>
    Фамилия: <b>{author['surname']}</b><br>
    телефон: <b>{author['phone']}</b><br>
    email:   <b>{author['email']}</b>
    """
    return HttpResponse(text)


def item_page(request, id):
    for item in items:
        if item['id'] == id:
            text = f"""<h2>{item['name']}</h2>
            количество: {item['quantity']}<br>
            <a href='/items/'>Назад</a>
            """
            return HttpResponse(text)

    return HttpResponseNotFound(f"Товар с id={id} не найден")


def items_list(request):
    # text = "<h2>Список товаров</h2><ol>"
    # for item in items:
    #     text += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # text += "</ol>"
    # return HttpResponse(text)
    context = {
        'items': items
    }
    return render(request, 'item-list.html', context)