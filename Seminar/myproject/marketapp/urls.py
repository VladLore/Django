from django.contrib import admin
from django.urls import path, include
from .views import index, get_users, fake_users, fake_products
from .views import delete_users, get_products, delete_products
from .views import fake_orders


urlpatterns = [
    path('', index, name='index'),
    path('users/', get_users, name='get_users'),
    path('fake_users/', fake_users, name='fake_users'),
    path('delete_user/<int:user_id>', delete_users, name='delete_user'),
    path('fake_products/', fake_products, name='fake_products'),
    path('get_products/', get_products, name='get_products'),
    path('delete_products/<int:prod_id>', delete_products, name='get_products'),
    path('fake_orders/', fake_orders, name='fake_orders'),
]
