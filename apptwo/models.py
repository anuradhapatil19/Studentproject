from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20)
    price=models.FloatField()
    quantity=models.IntegerField()