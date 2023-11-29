from django.shortcuts import render
import logging
from django.http import HttpResponse
from .models import Client, Product, Order
from datetime import time


logger = logging.getLogger(__name__)
# Create your views here.


def index(request):
    logger.info(f"Страница магазина доступна")
    return HttpResponse("ОК")


def get_users(request):
    users = Client.objects.all()
    logger.info("Все ользователи получены")
    return HttpResponse(users)


def fake_users(request):
    for i in range(101):
        users = Client(
            name=f"aaaa{i}",
            email=f"aaaa{i}",
            phonenumber=156116574891,
            adress=f"adress{i}",
        )
        users.save()
    logger.info("Добавлены новые пользваотели")
    return HttpResponse(users)


def delete_users(request, user_id):
    pk = user_id
    users = Client.objects.filter(pk=pk).first()
    if users is not None:
        users.delete()
    logger.info("Пользователь удален")
    return HttpResponse(users)


def fake_products(request):
    for i in range(100):
        products = Product(
            product_name=f"name{i}",
            description_name=f"description{i}",
            price=10.5,
            quantity_products=50,
        )
        products.save()
    logger.info("Продукты добавлены")
    return HttpResponse(products)


def get_products(request):
    products=Product.objects.all()
    logger.info('Продукты получены')
    return HttpResponse(products)

def delete_products(request, prod_id):
    pk=prod_id
    product=Product.objects.filter(pk=pk).first()
    if product is not None:
        product.delete()
    logger.info('Товар удален')
    return HttpResponse(product)


def fake_orders(request):
    for i in range(101):
        orders= Order(
            client = f'aaaa{i}',
            products = f'bbbb{i}',
            total_price = 120.99,
        )
        order.save()
    logger.info('Заказы созданы')
    return HttpResponse(order)    