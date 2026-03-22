from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pre_patient/', views.pre_patient, name='pre_patient'),      # Remove 'accounts/'

    path('login_patient/', views.patient_login, name='login_patient'),      # Remove 'accounts/'
    path('register_patient/', views.patient_register, name='register_patient'),  # Remove 'accounts/'
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),  # Remove 'accounts/'
    path('view_patient_profile/', views.view_profile, name='view_profile_patient'),  # Remove 'accounts/'
    path('base_patient/', views.base_patient, name='base_patient'),  # Remove 'accounts/'
    path('prescriptions/', views.prescription_home, name='prescription_home'),
    path('my_prescription/', views.my_prescription, name='my_prescription'),
    path('download_prescription/<int:id>/', views.download_prescription, name='download_prescription'),

    path('order-medicine/', views.order_medicine, name='order_medicine'),
    

    ]