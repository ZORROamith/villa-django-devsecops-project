from django.shortcuts import render,redirect
from builder_app.models import *
from .models import *
from user_app.models import *
from admin_app.models import *
# Create your views here.
def reqbuilder(request):
    data=builder_details.objects.all()
    return render(request,'reqbuilders.html',{'builders':data})
def delete_builder(request,id):
    data=builder_details.objects.get(pk=id)
    data.delete()
    return redirect(reqbuilder)
def approved_builder(request,id):
    builder_data=builder_details.objects.get(pk=id)
    data=approve_builder(photo=builder_data.photo,name=builder_data.name,email=builder_data.email,phone=builder_data.phone,password=builder_data.password)
    data.save()
    builder_data.delete()
    return redirect(reqbuilder)
def view_approved_builders(request):
    data=approve_builder.objects.all()
    return render(request,'view_approved_builders.html',{'result':data})
def admin_prop_view(request):
    data=property_details.objects.all()
    return render(request,'admin_prop_view.html',{'result':data})
def propdelete(reqeust,id):
    data=property_details.objects.get(pk=id)
    data.delete()
    return redirect(admin_prop_view)
def propupdate(request,id):
    data=property_details.objects.get(pk=id)
    return render(request,'propupdate.html',{'result':data})
def propupdates(request,id):
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
       data=property_details(id=id,userid=userid,property_photo=photo,property_name=name,property_category=category,property_location=location,property_budget=budget,property_bedroom=bedroom,property_bathroom=bathroom,property_area=area,property_floor=floor,property_parking=parking)
       data.save()
       return redirect(admin_prop_view)
def admin_book_view(request):
    data=booking.objects.all()
    return render(request,'admin_book_view.html',{'result':data})
def userview(request):
    data=usersinfo.objects.all()
    return render(request,'userview.html',{'result':data})
def userdelete(request,id):
    data=usersinfo.objects.get(pk=id)
    data.delete()
    return redirect(userview)

    
def admin_dashboard(request):

    total_builders=approve_builder.objects.count()
    total_properties=property_details.objects.count()
    total_bookings=booking.objects.count()

    context={
        "total_builders": total_builders,
        "total_properties":total_properties,
        "total_bookings": total_bookings

    }

    return render(request,'dashboard.html',context)