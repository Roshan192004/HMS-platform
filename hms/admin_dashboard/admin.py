from django.contrib import admin
from .models import (
    Department, Patient, Doctor, StaffMember,
    Appointment, BillingRecord, InventoryItem, Report,
)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'created')
    search_fields = ('first_name', 'last_name', 'phone', 'email')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty', 'dept')
    list_filter = ('dept',)

@admin.register(StaffMember)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'phone')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'when', 'status')
    list_filter = ('status', 'when')

@admin.register(BillingRecord)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'amount', 'paid', 'date')

@admin.register(InventoryItem)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'qty', 'unit_price')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
