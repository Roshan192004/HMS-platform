from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from accounts.models import*


def home(request):
    return render(request, 'admin_dashboard/home.html')


# def p(request):
#     pc = patient.objects.all()
#     return render(request,'admin_dashboard/patients.html',{'pc':pc})