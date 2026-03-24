from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine, Bill, Cart, CartItem
from django.utils import timezone
from accounts.models import pharmacist
from patients.models import PrescriptionOrder
from .models import Cart, CartItem, Bill
from django.db import models
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import MedicineForm


# ===============================
# Landing Page
# ===============================

def landing_page(request):
    return render(request, 'pharmacy/landing_page.html')


# ===============================
# READ - View All Medicines
# ===============================

def medicine_list(request):
    query = request.GET.get('q')
    if query:
        medicines = Medicine.objects.filter(name__icontains=query)
    else:
        medicines = Medicine.objects.all()
    return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines, 'query': query})


# ===============================
# CREATE - Add Medicine
# ===============================

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicine added successfully!')
            return redirect('add_medicine')
    else:
        form = MedicineForm()

    return render(request, 'pharmacy/add_medicine.html', {'form': form})


# ===============================
# UPDATE - Edit Medicine
# ===============================

def update_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'pharmacy/update_medicine.html', {'form': form})


# ===============================
# DELETE - Delete Medicine
# ===============================

def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)

    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')

    return render(request, 'pharmacy/delete_medicine.html', {'medicine': medicine})

# ===========================================
def pharmacy_dashboard(request):
    pharmacist_id = request.session.get('pharmacist_id')
    if not pharmacist_id:
        return redirect('pharmacy_login')
    
    pharmacist_obj = get_object_or_404(pharmacist, id=pharmacist_id)
    pending_count = PrescriptionOrder.objects.filter(status='Pending').count()
    recent_prescriptions = PrescriptionOrder.objects.all().order_by('-uploaded_at')[:5]
    
    # Real-time stats
    today = timezone.now().date()
    today_revenue = Bill.objects.filter(created_at__date=today).aggregate(models.Sum('total_amount'))['total_amount__sum'] or 0
    low_stock_count = Medicine.objects.filter(stock__lt=50).count()
    
    # Inventory Alerts (Low stock or near expiry)
    low_stock_medicines = Medicine.objects.filter(stock__lt=50)
    near_expiry_medicines = Medicine.objects.filter(expiry_date__lte=today + timezone.timedelta(days=30), expiry_date__gte=today)
    
    return render(request, 'pharmacy/pharmacy_dashboard.html', {
        'pharmacist': pharmacist_obj,
        'pending_count': pending_count,
        'recent_prescriptions': recent_prescriptions,
        'today_revenue': today_revenue,
        'low_stock_count': low_stock_count,
        'low_stock_medicines': low_stock_medicines,
        'near_expiry_medicines': near_expiry_medicines
    })


# =================================================================
# ---------------- REGISTER ----------------
def pharmacist_register(request):
    if request.method == 'POST':
        pharmacist_name = request.POST.get('pharmacist_name')
        pharmacist_number = request.POST.get('pharmacist_number')
        pharmacist_email = request.POST.get('pharmacist_email')
        pharmacist_password = request.POST.get('pharmacist_password')

        pharmacist.objects.create(
            pharmacist_name=pharmacist_name,
            pharmacist_number=pharmacist_number,
            pharmacist_email=pharmacist_email,
            pharmacist_password=pharmacist_password
        )

        send_mail(
            subject="Welcome to Hospital Management System",
            message=f'Hello {pharmacist_name}, Thanks for registering with us',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[pharmacist_email],
            fail_silently=False
        )

        return redirect('pharmacy_login')

    return render(request, 'pharmacy/register.html')
# ---------------- LOGIN ----------------
def pharmacist_login(request):
    if request.method == "POST":
        username = request.POST.get("pharmacist_name")
        password = request.POST.get("pharmacist_password")

        print("Entered Username:", username)
        print("Entered Password:", password)

        try:
            user = pharmacist.objects.get(
                pharmacist_name__iexact=username,
                pharmacist_password=password
            )

            print("User Found:", user)

            request.session['pharmacist_id'] = user.id
            request.session['pharmacist_name'] = user.pharmacist_name

            return redirect('landing')

        except pharmacist.DoesNotExist:
            print("User NOT found in DB")
            messages.error(request, "Invalid Username or Password")
            return redirect('pharmacy_login')

    return render(request, 'pharmacy/login.html')




# ==============================logout================================================
def pharmacist_logout(request):
    request.session.flush()
    return redirect('home')
# ==================================================================================
def pending_orders(request):
    if 'pharmacist_id' not in request.session:
        return redirect('pharmacy_login')
    
    # Fetch orders with 'Pending' status
    orders = PrescriptionOrder.objects.filter(status='Pending').order_by('-uploaded_at')
    
    
    return render(request, 'pharmacy/pending_orders.html', {'orders': orders})

def order_detail(request, order_id):
    if 'pharmacist_id' not in request.session:
        return redirect('pharmacy_login')
    
    order = get_object_or_404(PrescriptionOrder, id=order_id)
    return render(request, 'pharmacy/order_detail.html', {'order': order})


def accept_order(request, order_id):
    if 'pharmacist_id' not in request.session:
        return redirect('pharmacy_login')
        
    order = get_object_or_404(PrescriptionOrder, id=order_id)
    order.status = 'Accepted'
    order.save()
    
    request.session['current_order_id'] = order.id
    
    return redirect('medicine_list')



def add_to_cart(request, medicine_id):
    if 'pharmacist_id' not in request.session:
        return redirect('pharmacy_login')
    
    pharmacist_id = request.session['pharmacist_id']
    pharmacist_obj = get_object_or_404(pharmacist, id=pharmacist_id)
    medicine = get_object_or_404(Medicine, id=medicine_id)
    
    # Check if stock is available
    if medicine.stock <= 0:
        messages.error(request, f"Sorry, {medicine.name} is out of stock!")
        return redirect('medicine_list')
    
    cart, created = Cart.objects.get_or_create(pharmacist=pharmacist_obj)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, medicine=medicine)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    # Decrement stock
    medicine.stock -= 1
    medicine.save()
    
    messages.success(request, f"{medicine.name} added to cart! Stock updated.")
    return redirect('medicine_list')

def cart_view(request):
    if 'pharmacist_id' not in request.session:
        return redirect('pharmacy_login')
        
    pharmacist_id = request.session['pharmacist_id']
    pharmacist_obj = get_object_or_404(pharmacist, id=pharmacist_id)
    
    try:
        cart = Cart.objects.get(pharmacist=pharmacist_obj)
        cart_items = cart.items.all()
        total_price = cart.total_price()
    except Cart.DoesNotExist:
        cart_items = []
        total_price = 0
        
    current_order_id = request.session.get('current_order_id')
    current_order = None
    if current_order_id:
        current_order = PrescriptionOrder.objects.filter(id=current_order_id).first()
        
    return render(request, 'pharmacy/cart.html', {
        'cart_items': cart_items, 
        'total_price': total_price,
        'current_order': current_order
    })

def checkout(request):
    if 'pharmacist_id' not in request.session:
        return redirect('pharmacy_login')
        
    pharmacist_id = request.session['pharmacist_id']
    pharmacist_obj = get_object_or_404(pharmacist, id=pharmacist_id)
    
    try:
        cart = Cart.objects.get(pharmacist=pharmacist_obj)
    except Cart.DoesNotExist:
        return redirect('medicine_list')
        
    current_order_id = request.session.get('current_order_id')
    if not current_order_id:
        return redirect('pending_orders')
        
    order = get_object_or_404(PrescriptionOrder, id=current_order_id)
    
    # Create Bill
    total_amount = cart.total_price()
    items_summary = ", ".join([f"{item.medicine.name} x{item.quantity}" for item in cart.items.all()])
    
    Bill.objects.create(
        prescription_order=order,
        pharmacist=pharmacist_obj,
        total_amount=total_amount,
        items_summary=items_summary
    )
    
    # Update Order Status
    order.status = 'Completed'
    order.save()
    
    # Clear Cart
    cart.items.all().delete()
    del request.session['current_order_id']
    
    messages.success(request, f"Order for {order.patient_name} has been completed and billed successfully!")
    return render(request, 'pharmacy/order_completed.html', {'order': order})
