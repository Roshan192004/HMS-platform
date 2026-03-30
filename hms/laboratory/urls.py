from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page,name='landing'),
    path('login/', views.laboratory_login, name='laboratory_login'),
    path('register/', views.laboratory_register, name='laboratory_register'),
    path('dashboard/', views.laboratory_dashboard, name='laboratory_dashboard'),
]