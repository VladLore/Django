from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('', index, name='index'),
    # path('fake_authors/', fake_author, name='fake_authors'),
]
