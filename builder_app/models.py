from django.db import models

# Create your models here.
class builder_details(models.Model):
    photo=models.ImageField()
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


    
class property_details(models.Model):
    userid=models.CharField(max_length=10)
    property_photo=models.ImageField()
    property_name=models.CharField(max_length=100)
    property_category=models.CharField(max_length=100)
    property_location=models.CharField(max_length=100)
    property_budget=models.CharField(max_length=100)
    property_bedroom=models.CharField(max_length=100)
    property_bathroom=models.CharField(max_length=100)
    property_area=models.CharField(max_length=100)
    property_floor=models.CharField(max_length=100)
    property_parking=models.CharField(max_length=100)