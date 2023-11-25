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
    phonenumber= models.IntegerField()
    adress = models.CharField(max_length=100)
    register_date = models.DateField(auto_now_add= True)
    
    
    def __str__(self):
        return f'Имя: {self.name}, Email: {self.email}, Номер телефона: {self.phonenumber}, адрес: {self.adress}, дата регистрации: {self.register_date} '

class Product(models.Model):
    product_name= models.CharField(max_length=50)
    description_name= models.TextField()
    price= models.DecimalField(max_digits=8, decimal_places=2)
    quantity_products= models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Имя: {self.product_name}, Описание: {self.description_name}, цена: {self.price}, Количество товаров: {self.quantity_products}, дата добавления: {self.date} '
    
class Order(models.Model):
    client= models.ForeignKey('Client', on_delete=models.CASCADE)
    products= models.ManyToManyField('Product')
    total_price=models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Имя клиента: {self.client.name}, Товары: {self.products}, Общая цена: {self.total_price}, Дата заказа: {self.date} '