from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

"""
## Models
- Users: email, username, password
- Properties: title, description, images (as many as possible), price
- About Us: content (richtextfield)
- Services: title, content(richtextfield)
- News: title, content(richtextfield)
- FAQ: question (TextField), answer(TextField)
- Contact: md_name, legal_title, name, email, phone, address
"""

class CustomUser(AbstractUser):
  USER_STATUS_CHOICES = {
    1:"REGULAR",
    2:"STANDARD",
    3:"PREMIUM",
  }

  phone_number = models.CharField(max_length=20, blank=True)
  status = models.IntegerField(default=1, choices=USER_STATUS_CHOICES)

  USERNAME_FIELD = "username"
  EMAIL_FIELD = "email"
  REQUIRED_FIELDS = ["email"]



class Property(models.Model):
    PROPERTY_CATEGORY_CHOICES = {
       'APARTMENT':'Apartment',
       'LAND':'Land',
    }

    PROPERTY_STATUS_CHOICES = {
       'FOR_SALE': 'For Sale',
       'FOR_RENT': 'For Rent',
    }

    title = models.CharField(max_length=255)
    details = RichTextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=PROPERTY_CATEGORY_CHOICES, default='APARTMENT')
    status = models.CharField(max_length=50, choices=PROPERTY_STATUS_CHOICES, default='FOR_SALE')

    def __str__(self):
      return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
      return f"Image for {self.property.title}"
    

class AboutUs(models.Model):
   about_us = RichTextField()
   last_modified_at = models.DateTimeField(auto_now=True)


class Service(models.Model):
   title = models.CharField(max_length=128, blank=False)
   details = RichTextField()
   created_at = models.DateTimeField(auto_now_add=True)
   last_modified_at = models.DateTimeField(auto_now=True)


class News(models.Model):
   title = models.CharField(max_length=128, blank=False)
   details = RichTextField()
   created_at = models.DateTimeField(auto_now_add=True)
   last_modified_at = models.DateTimeField(auto_now=True)


class Faq(models.Model):
   question = models.TextField()
   answer = RichTextField()
   created_at = models.DateTimeField(auto_now_add=True)
   last_modified_at = models.DateTimeField(auto_now=True)


                       

