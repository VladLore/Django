from django.contrib import admin
from .models import Client
# Register your models here.

class AdminClient(admin.ModelAdmin):
    list_display = ('name_client', 'email','phonenumber')
    
admin.site.register(Client, AdminClient)