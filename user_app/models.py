from django.db import models

# Create your models here.
class usersinfo(models.Model):
    photo=models.ImageField()
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=50)
class booking(models.Model):
    user_id=models.CharField(max_length=12)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    property_photo=models.ImageField()
    property_name=models.CharField(max_length=50)
    property_location=models.CharField(max_length=50)
    property_budget=models.CharField(max_length=50)
    date=models.DateField()