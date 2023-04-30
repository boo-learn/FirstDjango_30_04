from django.shortcuts import render, HttpResponse

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
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)


def about(request):
    text = f"""
    Имя: <b>{author['name']}</b><br>
    Фамилия: <b>{author['surname']}</b><br>
    телефон: <b>{author['phone']}</b><br>
    email:   <b>{author['email']}</b>
    """
    return HttpResponse(text)
