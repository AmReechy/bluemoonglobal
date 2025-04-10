from django.contrib import admin

# Register your models here.
from .models import Property, PropertyImage, CustomUser, AboutUs, Service, News, Faq, Enquiry

class PropertyImageInline(admin.TabularInline):  # or admin.StackedInline
    model = PropertyImage
    extra = 4  # how many image upload slots to show initially

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available', 'category', 'status','created_at', )
    inlines = [PropertyImageInline]
    search_fields = ('title',)
    list_filter = ('created_at', 'price', 'is_available')


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('sent_at', "email", "phone_number", "user", "enquiry", "responded_to")
    list_filter = ('sent_at', "responded_to")

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'phone_number', 'status', 'date_joined')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('about_us', 'last_modified_at',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_modified_at')


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question',)


@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ("title", "added_by", "created_at")
    list_filter = ("created_at", "added_by")


