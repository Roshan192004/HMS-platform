from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicines/add/', views.add_medicine, name='add_medicine'),
    path('medicines/update/<int:pk>/', views.update_medicine, name='update_medicine'),
    path('medicines/delete/<int:pk>/', views.delete_medicine, name='delete_medicine'),
    path('pharmacy-dashboard/', views.pharmacy_dashboard, name='dashboard'),
    path('login/', views.pharmacist_login, name='pharmacy_login'),
    path('register/', views.pharmacist_register, name='pharmacy_register'),
    path('logout/', views.pharmacist_logout, name='pharmacy_logout'),
    path('pending-orders/', views.pending_orders, name='pending_orders'),
    path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('accept-order/<int:order_id>/', views.accept_order, name='accept_order'),
    path('add-to-cart/<int:medicine_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),

]
