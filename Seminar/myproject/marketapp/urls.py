from django.contrib import admin
from django.urls import path, include
from .views import index, fake_author, about_me, main


urlpatterns = [
    path('', index, name='index'),
    # path('fake_authors/', fake_author, name='fake_authors'),
]
