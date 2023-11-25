from django.contrib import admin
from django.urls import path, include
from .views import index, get_users, fake_users


urlpatterns = [
    path('', index, name='index'),
    path('users/', get_users, name='get_users'),
    path('fake_users/', fake_users, name='fake_users'),
]
