from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ClassBooking

@admin.register(ClassBooking)
class ClassBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'class_type', 'booking_date')
    list_filter = ('class_type', 'booking_date')
