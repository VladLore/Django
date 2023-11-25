from django.db import models

# Create your models here.

class Author(models.Model):
    name= models.CharField(max_length=100)
    surname= models.CharField(max_length=100)
    email=models.EmailField()
    biography=models.TextField()
    birthday=models.DateField()
    
    def __str__(self):
        return f'{self.surname} {self.name}'