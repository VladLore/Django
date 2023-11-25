from django.shortcuts import render
from django.http import HttpResponse
from .models import Author

# Create your views here.


def index(request):
    return HttpResponse("Hello")


def view_author(request):
    return HttpResponse("author")


def fake_author(request):
    for i in range(101):
        author = Author(
            name=f"aaa{i}",
            surname=f"bbb{i}",
            email=f"user{i}@mail.ru",
            biography=f"jjjjjjjjjj{i}",
            birthday= "2023-06-06"
        )
        author.save()
    return HttpResponse(author)