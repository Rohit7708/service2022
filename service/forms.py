from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Customer, Workers
from django import forms
from django.contrib.auth.forms import UserCreationForm


class Formcreate(ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'

class Myworker(ModelForm):
    class Meta:
        model=Workers
        fields='__all__'



        

