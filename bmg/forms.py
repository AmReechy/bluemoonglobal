from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser



class UserRegistrationForm(UserCreationForm):
  username = forms.CharField(
     label='Username',
     max_length=20,
     widget=forms.TextInput(attrs={'class': 'form-input', "max_length":"20", "placeholder":"Provide a username ..."}),
  )
  email = forms.CharField(
     label='Email',
     widget=forms.EmailInput(attrs={'class': 'form-input', "placeholder":"Provide a valid email ..."})
  )
  phone_number = forms.CharField(
     label='Phone Number',
     required=True,
     widget=forms.TextInput(attrs={'class': 'form-input', "placeholder":"Type your phone number ..."})
  )
  password1 = forms.CharField(
     label='Password',
     widget=forms.PasswordInput(attrs={'class': 'form-input', "placeholder":"Provide a strong password ..."})
  )
  password2 = forms.CharField(
     label='Password Again',
     widget=forms.PasswordInput(attrs={'class': 'form-input', "placeholder":"Retype your password ..."})
  )
  class Meta:
    model = CustomUser
    fields = ['username', 'email','phone_number', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder':"Username"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':"Password"}))
    
