from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
import logging

logger = logging.getLogger(__name__)

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
            birthday="2023-06-06",
        )
        author.save()
    return HttpResponse(author)


def main(request):
    context = {'name': 'John', 'surname':'davids', 'age': 45}
    logger.info(f'Страница "главная" успешно открыта')
    return render (request, 'blogapp/index.html', context)
    # return HttpResponse ('Hello')


def about_me(request):
    html = """
    <h1>Моё имя, Влдадислав.</h>
    <p>Тут должна быть информация об мне, но я не знаю что писать. :-)</p>
    """
    logger.info("Информация об авторе получена")
    return HttpResponse(html)
