from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    rating = models.IntegerField()
    name = models.CharField(max_length=100)
    site = models.URLField()
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=15)
    street = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    lat = models.FloatField()
    lng = models.FloatField()
