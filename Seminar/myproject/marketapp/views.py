from django.shortcuts import render
import logging
from django.http import HttpResponse
from .models import Client
from datetime import time

logger=logging.getLogger(__name__)
# Create your views here.

def index(request):
    logger.info(f'Страница магазина доступна')
    return HttpResponse('ОК')

def get_users(request):
    users= Client.objects.all()
    logger.info('Все ользователи получены')
    return HttpResponse(users)


def fake_users(request):
    for i in range(101):
        users= Client(
            name=f'aaaa{i}',
            email=f'aaaa{i}',
            phonenumber=156116574891,
            adress = f'adress{i}' 
        )
        users.save()
    logger.info('Добавлены новые пользваотели')
    return HttpResponse(users)