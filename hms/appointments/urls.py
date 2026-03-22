from django.urls import path
from appointments import views

urlpatterns = [
    # path('dashboard/', user_dashboard, name='user_dashboard'),
    path('book_appointment/',views.book_appointment,name='book_appointment'),
    path('appointment/',views.appointment,name='appointment'),
    path('patient_my_appointment/',views.my_appointment,name='patient_my_appointment'),
]
