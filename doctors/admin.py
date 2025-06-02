from django.contrib import admin
from .models import Doctor

# Register your models here.

@admin.register(Doctor) # Using the decorator to register the Doctor model
class DoctorAdmin(admin.ModelAdmin): # Customizing the admin interface for the Doctor model
    list_display = ('get_full_name', 'specialization', 'get_email', 'phone')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'specialization')

    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Full Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
