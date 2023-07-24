from django.db import models

class People(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    city = models.CharField(max_length=15)
    salary = models.IntegerField()
    business = models.BooleanField()



