from django.contrib import admin
from .models import Doctor, TimeSlot, Appointment

# Register your models here.


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('User', 'specialization', 'experience_years', 'consultation_fee')
    search_fields = ('user__username', 'specialization')


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'start_time', 'end_time', 'is_booked')
    list_filter = ('date', 'doctor', 'is_booked')
    search_fields = ('doctor__user__username',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'slot', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('patient__username', 'doctor__user__username')
