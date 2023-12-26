from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    prefix=models.CharField(max_length=25,null=True)
    fname=models.CharField(max_length=255)
    mname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    gender=models.CharField(max_length=8,null=True)
    father_name=models.CharField(max_length=255)
    mother_name=models.CharField(max_length=255)
    phone=models.IntegerField()
    day=models.CharField(max_length=255)
    month=models.CharField(max_length=255)
    Year=models.CharField(max_length=255)
    age=models.IntegerField(default=0)
    email=models.CharField(max_length=155)
    add1=models.TextField()
    add2=models.TextField()
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pin=models.IntegerField(default=0)
    aadhar=models.IntegerField(default=000000000000)
    pan=models.CharField(max_length=8,null=True)
    
    
class User(models.Model):
    firstname = models.CharField(max_length=100,default="null")
    lastname = models.CharField(max_length=100,default="null")
    phone=models.CharField(max_length=10,default="0000000000")
    username = models.CharField(max_length=100,default="null")
    password = models.CharField(max_length=8,default="null")
     