from django.contrib import admin
from .models import Author

# Register your models here.

@admin.action(description='Тестовый')
def admintest(modeladmin, request,queryset):
    queryset.update(name='test')


class AdminAuthor(admin.ModelAdmin):
    list_display = ("name", "surname", "birthday")
    list_filter = ("surname",)
    search_fields = ("name", "surname")
    # fields = ['name', 'surname']
    # readonly_fields = ['name', 'surname', 'birthday']
    fieldsets = [
        ["Тест", {"fields": ["surname", "name"]}],
        ["Тест2", {"fields": ["email", "biography"]}],
    ]
    actions = [admintest]


admin.site.register(Author, AdminAuthor)
