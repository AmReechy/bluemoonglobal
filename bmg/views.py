from django.shortcuts import render, redirect
from .models import Property
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm

from django.contrib import messages

# Create your views here.


def home1(request):
  return render(request, "base.html", {"name":"Richard Amoo"})

def home(request):
    avail_properties = Property.objects.all()
    section = 'home'
    context = {
        "section":section,
        "avail_properties":avail_properties,
        "properties": {
            "p1":{
                "images": ["img" + str(n) for n in range(1,5)]
            },
            "p2":{
                "images": ["set2_img" + str(n) for n in range(1,6)]
            },
            "p3":{
                "images": ["set3_img" + str(n) for n in range(1,8)]
            },
        },
        "all_properties":["img" + str(n) for n in range(1,5)] + ["set2_img" + str(n) for n in range(1,6)] + ["set3_img" + str(n) for n in range(1,8)],
        "news_list": [
            "The Ongoing BLUEMOON GARDENS Project in Asokoro 2 Now Close to Completion",
            "Bluemoon Global Services Limited Received a Prestigious Real Estate Award for Our Outstanding Services",
            "Exciting Updates About Our Logistics and Supplies Services"
        ]

    }

    return render(request, "bluemoonglobal2.html", context)


def login_register_user(request):
    section = "login"
    if request.method != 'POST':
        form = UserRegistrationForm()
        login_form = UserLoginForm()

    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your Soliss Account was created successfully. You may now log in to your account using your Username and Password.", extra_tags="time-15000")
            return redirect('bmg:user-login')
    
        else:
            messages.error(request, "Sorry, your account was NOT created as the submitted form contains some errors. Please correct the errors and try again.", "time-15000")
    
    context = {'form': form, 'login_form':login_form, "section":section,}

    return render(request,"login_register.html", context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in to your Account.")
                return redirect('bmg:home')
            else:
                form.add_error(None, "You entered an invalid username or password!")
        else:
            messages.error(request, "There was a problem with your login credentials !", extra_tags="time-10000")
    

def user_logout(request):
    logout(request)
    messages.error(request, "You have logged out of your Account!")
    return redirect('bmg:home')



       
        

  
