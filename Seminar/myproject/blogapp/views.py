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
    html = """
            <div>
            <h1>Главная страница</h1>
            <h2>Мой первый сайт:</h2>
            <p>Создайте пару представлений в вашем первом приложении:</p>
            <ul>
                <li>главная</li>
                <li>о себе</li>
            </ul>
            <p>Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.</p>
            <p>Сохраняйте в логи данные о посещении страниц.</p>
        </div>
        <form action='http://127.0.0.1:8000/blog/about_me/' target="_blank">
            <button>О себе</button>
        </form>
        <br>
        <footer>
            <div>
                <p> Контакты: </p>
            </div>
        </footer>
        """
    logger.info(f'Страница "главная" успешно открыта')
    return HttpResponse(html)


def about_me(request):
    html = """
    <h1>Моё имя, Влдадислав.</h>
    <p>Тут должна быть информация об мне, но я не знаю что писать. :-)</p>
    """
    logger.info("Информация об авторе получена")
    return HttpResponse(html)
