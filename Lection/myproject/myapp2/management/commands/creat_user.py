from typing import Any
from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = 'Creat user'
    
    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        user = User(name='Jack', email='Jack@example.com', password='third', age=45)
        # user = User(name='Neo', email='NeO@example.com', password='doublesecret', age=50)
        
        user.save()
        self.stdout.write(f'{user}')