from django.contrib import admin
# from django.urls import path
# from .import views

from django.urls import path
from . import views

urlpatterns = [
    # path('pre_patient/', views.pre_patient, name='pre_patient'),      # Remove 'accounts/'
    # path('pre_doctor/', views.pre_doctor, name='pre_doctor'),      # Remove 'accounts/'
    # path('pre_receptionist/', views.pre_receptionist, name='pre_receptionist'),      # Remove 'accounts/'
    # path('login_patient/', views.patient_login, name='login_patient'),      # Remove 'accounts/'
    # path('register_patient/', views.patient_register, name='register_patient'),  # Remove 'accounts/'
    # path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),  # Remove 'accounts/'
    # path('view_patient_profile/', views.view_profile, name='view_profile_patient'),  # Remove 'accounts/'
    # path('login_doctor/', views.doctor_login, name='login_doctor'),      # Remove 'accounts/'
    # path('register_doctor/', views.doctor_register, name='register_doctor'),  # Remove 'accounts/'
    # path('login_receptionist/', views.receptionist_login, name='login_receptionist'),      # Remove 'accounts/'
    # path('register_receptionist/', views.receptionist_register, name='register_receptionist'),  # Remove 'accounts/'
    path('', views.landing, name='landing'),  # Remove 'accounts/'
    path('temp/', views.temp, name='temp'),  # Remove 'accounts/'
    path('logout/', views.logout_patient, name='logout'),  # Remove 'accounts/'
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Remove 'accounts/'
    path('patient/', views.p, name='patient'),  # Remove 'accounts/'
    path('doctor/', views.d, name='doctor'),  # Remove 'accounts/'
    # path('base_patient/', views.base_patient, name='base_patient'),  # Remove 'accounts/'
    # path('appointment/', views.appointment, name='patient_my_appointment'),  # Remove 'accounts/'
]