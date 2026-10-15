from django.shortcuts import render
from .models import *

# Create your views here.
def builder_reg(request):
    if request.method=="POST":
        photo=request.FILES['builderphoto']
        name=request.POST.get('buildername')
        email=request.POST.get('builderemail')
        phone=request.POST.get('builderphone')
        password=request.POST.get('builderpassword')
        data=builder_details(photo=photo,name=name,email=email,phone=phone,password=password)
        data.save()
    return render(request,'builder_registration.html')

def add_prop(request):
    userid=request.session['bid'] 
    if request.method == "POST":
       photo=request.FILES['photo']
       name=request.POST.get('name')
       category=request.POST.get('category')
       location=request.POST.get('location')
       budget=request.POST.get('budget')
       bedroom=request.POST.get('bedroom')
       bathroom=request.POST.get('bathroom')
       floor=request.POST.get('floor')
       area=request.POST.get('area')
       parking=request.POST.get('parking')
       data=property_details(userid=userid,property_photo=photo,property_name=name,property_category=category,property_location=location,property_budget=budget,property_bedroom=bedroom,property_bathroom=bathroom,property_area=area,property_floor=floor,property_parking=parking)
       data.save()
    return render(request,'add_property.html')