from django.urls import path
from . import views

urlpatterns = [
    path("reception_dashboard/", views.reception_dashboard, name="reception_dashboard"),
    path('pre_receptionist/', views.pre_receptionist, name='pre_receptionist'),      # Remove 'accounts/'
    path('login_receptionist/', views.receptionist_login, name='login_receptionist'),      # Remove 'accounts/'
    path('register_receptionist/', views.receptionist_register, name='register_receptionist'),  # Remove 'accounts/'
    path('all_patient/', views.all_patient, name='all_patient'),  # Remove 'accounts/'
    path('all_doctor/', views.all_doctor, name='all_doctor'),  # Remove 'accounts/'

]
