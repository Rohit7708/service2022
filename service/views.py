from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from service.helper import MessageHandler
from .forms import Formcreate, Myworker
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

        profile.otp=random.randint(1000,9999)
        profile.save()
        message_handler=MessageHandler(phone,profile.otp).send_otp_via_message()
        return redirect('/otp/{profile.uid}')
    context={}
    return render(request,'acc/login.html',context)

def otp(request,uid):
    if request.method=='POST':
        otp=request.POST.get('otp')
        
        if otp==Customer.otp:
            return redirect('/')
        return redirect(f'/otp/{uid}')
    return render(request,'acc/otp.html')

def search(request):
    return render(request,'acc/search.html')


def domestic(request):
    work=Myworker()
    context={'work':work}
    return render(request,'acc/domestic.html',context)

def location(request):
    return render(request,'acc/location.html')


    

