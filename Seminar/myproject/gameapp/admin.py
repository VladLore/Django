from django.contrib import admin

# Register your models here.
from .models import Coin

class AdminCoin(admin.ModelAdmin):
    list_display = ('site',)


admin.site.register(Coin, AdminCoin)