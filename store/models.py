from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    label = models.CharField(max_length=50)
    price = models.FloatField()

class History(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)