from django.contrib import admin

# Register your models here.
from .models import Property, PropertyImage, CustomUser, AboutUs, Service, News, Faq, Enquiry, Contact, Display, DisplayImage, NewsImage



class PropertyImageInline(admin.TabularInline):  # or admin.StackedInline
    model = PropertyImage
    extra = 4  # how many image upload slots to show initially

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available', 'property_type', 'property_size','created_at', )
    inlines = [PropertyImageInline]
    search_fields = ('title',)
    list_filter = ('created_at','is_available')


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


class NewsImageInline(admin.TabularInline):  # or admin.StackedInline
    model = NewsImage
    extra = 2  # how many image upload slots to show initially


@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ("title", "added_by", "created_at")
    list_filter = ("created_at", "added_by")
    inlines = [NewsImageInline]

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ("email", "phone_number", "office_address")

class DisplayImageInline(admin.TabularInline):  # or admin.StackedInline
    model = DisplayImage
    extra = 3  # how many image upload slots to show initially


@admin.register(Display)
class DisplayAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [DisplayImageInline]


admin.site.site_header = "Bluemoon Global Services Administration"
admin.site.site_title = "Bluemoonglobal Admin"
admin.site.index_title = "Welcome to Bluemoon Global Services Admin Panel"

