from django.db import models

# Create your models here.

class reg(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Username = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30,)
    Password = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.First_name}'