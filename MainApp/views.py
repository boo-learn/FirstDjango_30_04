from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello!!")


def about(request):
    return HttpResponse("Юрченко Евгений Витальевич")