from django.shortcuts import render
from django.http import HttpResponse
from random import *
from .models import Coin

# Create your views here.


def index(request):
    return HttpResponse("Hello world")


# def coin(request):
#     site=choice(['Орел','Решка'])
#     arg=Coin(site=site)
#     arg.save()
#     return HttpResponse(str(site))


def kub(request, count):
    lst=[]
    for i in range(count):
        num=randint(1,7)
        lst.append(num)
    context={'game_name':'Кубик', 'value':lst}
    return render(request, 'gameapp/game.html', context)


def numbers(request, count):
    lst=[]
    for i in range(count):
        num = randint(0,1000)
        lst.append(num)
    context={'game_name':'Числа', 'value':lst}
    return render(request, 'gameapp/game.html', context)

def coin_values(request):
    value=Coin.values()
    print(value)
    lst=[]
    for i in value:
        print(i)
        lst.append(i.site)
    return HttpResponse(lst)


def coin(request, count=5):
    # context={'game_name':'Орел и решка', 'value':lst()}
    lst=[]
    for i in range(count): 
        site=choice(['Орел','Решка'])
        lst.append(site)
    context={'game_name':'Орел и решка', 'value':lst}
    return render(request, 'gameapp/game.html', context)