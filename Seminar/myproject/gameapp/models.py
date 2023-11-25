from django.db import models
from django.utils import timezone

"""
Создайте модель Автор. Модель должна содержать следующие поля: 
●	имя до 100 символов
●	фамилия до 100 символов
●	почта
●	биография
●	день рождения
Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.
"""

# Create your models here.

class Coin(models.Model):
    time = models.DateTimeField(default=timezone.now)
    site=models.CharField(max_length= 10)
    
    @staticmethod
    def values():
        value=Coin.objects.order_by('-time')[:5]
        # print(value)
        return value
        
    def __str__(self):
        return f'time: {self.time}, site: {self.site}'
