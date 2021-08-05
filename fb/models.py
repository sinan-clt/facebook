from os import name
from django.db import models

# Create your models here.
class signupp(models.Model):
    firstname=models.CharField(max_length=60)
    lastname=models.CharField(max_length=60)
    mobilenumber=models.CharField(max_length=60)
    birthday=models.DateField()
    gender=models.CharField(max_length=10)

class login(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    user_id=models.ForeignKey(signupp,on_delete=models.CASCADE)
