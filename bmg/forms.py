from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser


class UserRegistrationForm(UserCreationForm):
  username = forms.CharField(
     max_length=20,
     widget=forms.TextInput(attrs={'class': 'form-input', "max_length":"20", "placeholder":"provide a username ..."}),
  )
  email = forms.CharField(
     widget=forms.EmailInput(attrs={'class': 'form-input', "placeholder":"provide a valid email ..."})
  )
  phone_number = forms.CharField(
     required=False,
     widget=forms.EmailInput(attrs={'class': 'form-input', "placeholder":"your phone number ..."})
  )
  password1 = forms.CharField(
     widget=forms.PasswordInput(attrs={'class': 'form-input', "placeholder":"provide a strong password ..."})
  )
  password2 = forms.CharField(
     widget=forms.PasswordInput(attrs={'class': 'form-input', "placeholder":"Confirm your password ..."})
  )
  class Meta:
    model = CustomUser
    fields = ['username', 'email','phone_number', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder':"Username"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':"Password"}))
    
