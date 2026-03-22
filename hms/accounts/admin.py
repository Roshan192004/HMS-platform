from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(receptionist)
admin.site.register(appointments)
admin.site.register(prescription)
