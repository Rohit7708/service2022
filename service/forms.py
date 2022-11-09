from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Customer, Employee, Order
from django import forms
from django.contrib.auth.forms import UserCreationForm


class Formcreate(ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'

class Orders(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class Emp(ModelForm):
    class Meta:
        model=Employee
        fields='__all__'



        

