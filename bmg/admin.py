from django.contrib import admin

# Register your models here.
from .models import Property, PropertyImage, CustomUser, AboutUs, Service, News, Faq

class PropertyImageInline(admin.TabularInline):  # or admin.StackedInline
    model = PropertyImage
    extra = 1  # how many image upload slots to show initially

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_available', 'category', 'status','created_at', )
    inlines = [PropertyImageInline]
    search_fields = ('title',)
    list_filter = ('created_at', 'price', 'is_available')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'phone_number', 'status', 'date_joined')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('about_us', 'last_modified_at',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_modified_at')


