from django.shortcuts import render,redirect
from .models import *
from admin_app.models import *
from builder_app.models import*
from datetime import datetime
from django.conf import settings
# import razorpay

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(reqeust):
    return render(reqeust,'index.html')
def user_register(request):
    if request.method == "POST":
        photo=request.FILES.get('photo')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        data=usersinfo(photo=photo,name=name,email=email,phone=phone,password=password)
        data.save()
    return render(request,'user_registration.html')

def login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == "admin@gmail.com" and password == "admin":
            request.session['email'] = email
            request.session['admin'] = 'admin'
            return redirect('admin_dashboard')

        elif usersinfo.objects.filter(email=email, password=password).exists():

            userdetails = usersinfo.objects.get(
                email=email,
                password=password
            )

            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.name
            request.session['uemail'] = userdetails.email
            request.session['user'] = 'user'

            

            return redirect('index')

        elif approve_builder.objects.filter(email=email, password=password).exists():

            builderdetails = approve_builder.objects.get(
                email=email,
                password=password 
            )

            request.session['bid'] = builderdetails.id
            request.session['bname'] = builderdetails.name
            request.session['bemail'] = builderdetails.email
            request.session['builder'] = 'builder'

            return redirect('index')

    return render(request, 'login.html')


def user_prop_view(request):
    data=property_details.objects.all()
    return render(request,"user_prop_view.html",{'result':data})
    
def visit_date(request,id):
    data=property_details.objects.get(pk=id)
    return render(request,'visit_date.html',{'result':data})

def bookvisit(request,id):
  
    if request.method=="POST":
        user_id=request.session['uid']
        visit_date=request.POST.get("visit_date")
        visit_date=datetime.strptime(visit_date,"%Y-%m-%d").date()

        udata=usersinfo.objects.get(pk=user_id)
        pdata=property_details.objects.get(pk=id)
        bdata=booking(user_id=user_id,name=udata.name,email=udata.email,phone=udata.phone,property_photo=pdata.property_photo,
        property_name=pdata.property_name,property_location=pdata.property_location,property_budget=pdata.property_budget,date=visit_date)
        bdata.save()
        return redirect(razorpay_payment)
def user_book_view(request):
    data=booking.objects.all()
    return render(request,'user_book_view.html',{'result':data})


# client=razorpay.Client(
#     auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET)
# )

# def razorpay_payment(request):
#     amount=500

#     order=client.order.create({
#         "amount":amount*100,
#         "currency":"INR",
#         "payment_capture":"1"
#     })

#     return render(request,'payment.html',{"order_id":order["id"],"amount":amount,"key":settings.RAZORPAY_KEY_ID})

def userprofile(request):
    userid=request.session['uid']
    data=usersinfo.objects.get(pk=userid)
    return render(request,'userprofile.html',{'result':data})


def logout(request):
    session_key=list(request.session.keys())
    for key in session_key:
        del request.session[key]
    return redirect(index)