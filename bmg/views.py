from django.shortcuts import render, redirect
from .models import Display, Property, AboutUs, Service, News, Faq, CustomUser, Enquiry, Contact
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm

from django.contrib import messages

# Create your views here.

#000080 navy-blue
#4169e1 royal-blue
#{% load static tailwind_tags %}
def home1(request):
  return render(request, "base.html", {"name":"Richard Amoo"})

def home0(request):
    return redirect('bmg:home')

def home(request):
    avail_properties = Property.objects.all()
    section = 'home'
    services = Service.objects.all()
    news = News.objects.all()[0:5]
    display = Display.objects.filter(name__icontains="home page animated")[0]
    display_images = display.images.all()
    context = {
        "section":section,
        "avail_properties":avail_properties,
        "display_images":display_images,
        "news_list": news,
        "services":services,

    }

    return render(request, "bluemoonglobal2.html", context)

def login_register_user(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in!")
        return redirect('bmg:home')
    section = "login"
    if request.method != 'POST':
        form = UserRegistrationForm()
        
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, "Your Soliss Account was created successfully. You may now log in to your account using your Username and Password.", extra_tags="time-15000")
            return redirect('bmg:login')
    
        else:
            messages.error(request, "Sorry, your account was NOT created as the submitted form contains some errors. Please correct the errors and try again.", "time-15000")
            form.add_error(None, "Error with account creation !")

    login_form = UserLoginForm()
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
                
                #return redirect('bmg:user-login')
        else:
            #form.add_error(None, "There was a problem with your login credentials !")
            messages.error(request, "There was a problem with your login credentials !", extra_tags="time-10000")
            #return redirect('bmg:login-register')
    reg_form = UserRegistrationForm()
    context = {'form': reg_form, 'login_form':form, "section":'login',}
    return render(request,"login_register.html", context)
    

def user_logout(request):
    logout(request)
    messages.error(request, "You have logged out of your Account!")
    return redirect('bmg:home')


def about_us(request):
    section = "login"
    about_us = AboutUs.objects.all().first()
    services = Service.objects.all()

    return render(request, "about_us.html", {'about_us':about_us.about_us,'services':services, 'section':'about'})

def contact(request):
    section = "contact"
    contact = Contact.objects.all().first()
    return render(request, "contact_us.html", {'contact':contact, 'section':section})

def services(request):
    section = "service"
    services = Service.objects.all()

    return render(request, "services.html", {'services':services, 'section':section})


def news(request):
    section = "news"
    news = News.objects.all()

    return render(request, "news.html", {"news":news, "section":section})

def faqs(request):
    section = "faqs"
    faqs = Faq.objects.all()

    return render(request, "faqs.html", {"faqs":faqs, "section":section})


def enquiry(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["number"]
        enquiry = request.POST["enquiry"]
        user = None
        print(request.POST)
        print(name, email, phone, enquiry, sep=" ### ")
        if request.user.is_authenticated:
            user = request.user
        try:
            new_enquiry = Enquiry.objects.create(full_name=name, email=email, phone_number=phone, enquiry=enquiry, user=user)
        except:
            messages.error(request, "Sorry, there was a problem with the submitted form. Please try again!", extra_tags="time-10000")
            return redirect('bmg:home')
        
        messages.success(request, "Your enquiry has been successfully submitted. We will respond to you as promptly as possible. Thank you.", extra_tags="time-10000")
        return redirect('bmg:home')



def property_details(request, pk):
    property = Property.objects.get(pk=pk)
    print(property)

    return render(request, "prop_details.html", {'property':property})



       
        

  
