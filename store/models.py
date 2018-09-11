from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()

    def __unicode__(self):
        return self.name

# class History(models.Model):
