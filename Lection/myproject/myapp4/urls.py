"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp4.views import user_form, many_field_form, add_user, upload_image

urlpatterns = [
    path('user/add/',user_form, name='user_name'),
    path('forms/', many_field_form, name='many_field_form'),
    path('add_user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
]
