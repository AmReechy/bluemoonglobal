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
    last_modified_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=PROPERTY_CATEGORY_CHOICES, default='APARTMENT')
    status = models.CharField(max_length=50, choices=PROPERTY_STATUS_CHOICES, default='FOR_SALE')
    added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
      return self.title
    
    class Meta:
        ordering = ["-last_modified_at"]
        verbose_name = "Property"
        verbose_name_plural = "Properties"


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
      return f"Image for {self.property.title}"
   
    

class AboutUs(models.Model):
   about_us = RichTextField()
   last_modified_at = models.DateTimeField(auto_now=True)

   class Meta:
       ordering = ["-last_modified_at"]
       verbose_name = "About Us"
       verbose_name_plural = "About Us"


class Service(models.Model):
   title = models.CharField(max_length=128, blank=False)
   details = RichTextField()
   created_at = models.DateTimeField(auto_now_add=True)
   last_modified_at = models.DateTimeField(auto_now=True)

   class Meta:
       ordering = ["-last_modified_at"]

class News(models.Model):
   title = models.CharField(max_length=128, blank=False)
   details = RichTextField()
   created_at = models.DateTimeField(auto_now_add=True)
   last_modified_at = models.DateTimeField(auto_now=True)
   added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
   
   class Meta:
       ordering = ["-last_modified_at"]
       verbose_name = "News"
       verbose_name_plural = "News"

class Faq(models.Model):
   question = models.TextField()
   answer = RichTextField()
   created_at = models.DateTimeField(auto_now_add=True)
   last_modified_at = models.DateTimeField(auto_now=True)
   added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

   class Meta:
       ordering = ["-last_modified_at"]
       verbose_name = "FAQ"
       verbose_name_plural = "FAQs"


class Enquiry(models.Model):
    enquiry = models.TextField(max_length=1000)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    responded_to = models.BooleanField(default=False)

    class Meta:
        ordering = ["-sent_at"]
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquiries"
                       

