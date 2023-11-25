from django.shortcuts import render
from django.http import HttpResponse
from random import *
from .models import Coin

# Create your views here.


def index(request):
    return HttpResponse("Hello world")


def coin(request):
    site=choice(['Орел','Решка'])
    arg=Coin(site=site)
    arg.save()
    return HttpResponse(str(site))


def kub(request):
    return HttpResponse(str(randint(1, 7)))


def numbers(request):
    return HttpResponse(str(randint(0, 1000)))

def coin_values(request):
    value=Coin.values()
    print(value)
    lst=[]
    for i in value:
        print(i)
        lst.append(i.site)
    return HttpResponse(lst)
