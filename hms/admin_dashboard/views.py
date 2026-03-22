from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from accounts.models import*


<<<<<<< HEAD
def home(request):
    
=======

def home(request):


>>>>>>> a60adfbd7ca1c80757c21657537762cdf9c82e82
    return render(request, 'admin_dashboard/home.html')


# def p(request):
#     pc = patient.objects.all()
#     return render(request,'admin_dashboard/patients.html',{'pc':pc})