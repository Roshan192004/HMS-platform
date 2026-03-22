from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('home/', views.home, name='home'),
    # path('patient/', views.p, name='patient'),

]
