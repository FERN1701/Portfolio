from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
           
            
        }
