from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    name = models.CharField(max_length=100)
    Description = models.TextField()
    price=models.IntegerField()
    exist=models.BooleanField()

    def __str__(self):
        return self.name

class buyproduct(models.Model):
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product, on_delete=models.CASCADE)
