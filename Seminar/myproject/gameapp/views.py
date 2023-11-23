from django.shortcuts import render
from django.http import HttpResponse
from random import *

# Create your views here.


def index(request):
    return HttpResponse("Hello world")


def orel_reshka(request):
    return HttpResponse(choice(["Орел", "Решка"]))


def kub(request):
    return HttpResponse(str(randint(1, 7)))


def numbers(request):
    return HttpResponse(str(randint(0, 1000)))
