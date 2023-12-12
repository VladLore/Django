from django.shortcuts import render
import logging
from .models import User
from .forms import UserForm, ManyFieldsForm, ImageForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            age = form.cleaned_data["age"]
            logger.info(f"Получили {name=}, {email=}, {age=}")
    else:
        form = UserForm()
    return render(request, "myapp4/user_form.html", {"form": form})


def many_field_form(request):
    if request.method == "POST":
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            logger.info(f"Получили {form.cleaned_data=}")
    else:
        form = ManyFieldsForm()
    return render(request, "myapp4/many_fields_form.html", {"form": form})


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        message = "Ошибка в данных"
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            age = form.cleaned_data["age"]
            logger.info(f"Получили {name=} {email=} {age=}")
            user = User(name=name, email=email, age=age)
            user.save()
            message = "Пользователь сохранен"
    else:
        form = UserForm()
        message = "Заполните форму"
    return render(request, "myapp4/user_form.html", {"form": form, "message": message})


def upload_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]
            fs = FileSystemStorage()
            fs.save()
    else:
        form = ImageForm()
    return render(request, "myapp4/upload_image.html", {"form": form})
