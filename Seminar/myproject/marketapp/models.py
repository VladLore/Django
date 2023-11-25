from django.db import models
from django.utils import timezone

# Create your models here.
"""
Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа
"""

class Client(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber= models.IntegerField(max_length=10)
    adress = models.CharField()
    register_date = models.DateTimeField(default= timezone.now)

class Product(models.Model):
    product_name= models.CharField(max_length=50)
    description_name= models.TextField()
    price= models.DecimalField(max_digits=8, decimal_places=2)
    quantity_products= models.IntegerField()
    date = models.DateTimeField(default= timezone.now)
    
class Order(models.Model):
    client= models.ForeignKey('Client', on_delete=models.CASCADE)
    products= models.ForeignKey('Product', on_delete=models.CASCADE)
    total_price=models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(default= timezone.now)
    