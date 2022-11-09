from contextlib import nullcontext
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template.response   import TemplateResponse
from geopy.geocoders import Nominatim

from service.helper import MessageHandler
from .forms import Emp, Formcreate, Orders
from .models import *
from .helper import MessageHandler
import random

# Create your views here.
def home(request):
    return render(request,'acc/hom.html')

def registerpage(request):
    form=Formcreate()
    # username=request.POST.get('username')
    # phone=request.POST.get('phone')
    # user=Customer.objects.create(username=username)
    # profile=Customer.objects.create(username=user,phone=phone)
    if request.method =="POST":
        form=Formcreate(request.POST)
        if form.is_valid():
            form.save()
    
    
    context={'form':form}

    return render(request,'acc/register.html',context)




def loginpage(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        

        try:
            profile=Customer.objects.get(phone=phone)
        except:
            return redirect('/register/')
            

        profile.otp=random.randint(10000,99999)
        profile.save()
        message_handler=MessageHandler(phone,profile.otp).send_otp_via_message()
        return redirect('/otp/{}'.format(profile.cust_uid))
    context={}
    return render(request,'acc/login.html',context)

def logout(request):
    return render('acc/logout.html')

def otp(request,cust_uid):
    if request.method=='POST':
        otp=request.POST.get('otp')
        otp=Customer.objects.get(otp=otp)
        print(otp)
        if otp==otp:
            return redirect(f'/dashboard/{cust_uid}')
        else:
            return redirect(f'/otp/{cust_uid}')
        
    return render(request,'acc/otp.html')

def search(request,cust_uid):
    cust_uid = cust_uid
    context={'cust_uid':cust_uid}

    return render(request,'acc/search.html',context)


def domestic(request):
    
    return render(request,'acc/domestic.html',)




def dashboard(request,cust_uid):
    cust_uid=cust_uid
    orders=Order.objects.filter(cust_uid__cust_uid=cust_uid)
    # cust_info=Customer.objects.filter(cust_uid__cust_uid=custid)
    total_count=len(list(Order.objects.filter(cust_uid__cust_uid=cust_uid)))
    # pending_work=len(list(Order.objects.filter(cust__uid__cust_uid=cust_uid,status="Pending")))
    context={'orders':orders,'total_count':total_count,'cust_uid':cust_uid}
    return render(request,'acc/dashboard.html',context)

def location(request,cust_uid):
    # if request.method=='POST':
    #     form=Orders(request.POST)
    #     if form.is_valid():
    #         form.save()
    emp=Emp()
    cust_uid=cust_uid
    # proff=request.POST.get('Domestic')
    
    zipcode=request.POST.get('pincode')
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(zipcode)
    result=Employee.objects.filter(pincode=zipcode)
    workers_count = result.count()
 
# Displaying address details
    # print("Zipcode:",zipcode)
    # print("Details of the Zipcode:")
    # print(location)
    
    context={'workers_count':workers_count,'result':result,'res':location,'cust_uid':cust_uid,'emp':emp}


    return render(request,'acc/location.html',context)

def workerlogin(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        
        try:
            profile=Employee.objects.get(phone=phone)
        except:
            return redirect('/wreg/')

        profile.otp=random.randint(1000,9999)
        profile.save()
        message_handler=MessageHandler(phone,profile.otp).send_otp_via_message()

        return redirect('/wotp/{}'.format(profile.uid))


    return render(request,'acc/wlog.html')

def wotp(request,uid):
    if request.method=='POST':
        otp=request.POST.get('otp')
        otp=Employee.objects.get(otp=otp)
        if otp==otp:
            return redirect(f'/schedule/{uid}')
        else:
            return redirect(f'/wotp/{uid}')
        
    return render(request,'acc/wotp.html')

def wreg(request):
    form=Emp()
    if request.method =="POST":
        forms=Emp(request.POST)
        if forms.is_valid():
            forms.save()

    context={'form':form}
    return render(request,'acc/wreg.html',context)

def application(request,cust_uid,uid):
    cust_details=Customer.objects.filter(cust_uid=cust_uid)
    det=cust_details. values_list('username', flat=True) 
    username=det[0]

    ser_detail=Employee.objects.filter(uid=uid)
    ser_det=ser_detail.values_list('username',flat=True)
    ser_username=ser_det[0]
    print(ser_username)
    cust_uid=cust_uid
    

    forms=Orders()
    if request.method=='POST':
        form=Orders(request.POST)
        # if form.is_valid():
        #     form.save()
        return redirect('/')


    context={'form':forms,'ser_username':ser_username,'username':username}

    return render(request,'acc/application_form.html',context)


def schedule(request,uid):
    # worker = request.user
    print(uid)
    form=Orders()
    orders=Order.objects.filter(uid__uid=uid)
    # orders=Order.objects.all()
    count = len(list(Order.objects.filter(uid__uid=uid, status="Pending")))
    total_count=len(list(Order.objects.filter(uid__uid=uid)))
    # form=Orders(instance=orders)
    status=request.POST.get('status')
    orders.update(status=status)
    
    context={'orders':orders, "count": count,'form':form,'total_count':total_count}

    return render(request,'acc/schedule.html',context)

def worker(request):

    

    return render(request,'acc/worker.html')


    

