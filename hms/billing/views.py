from django.shortcuts import render, redirect
from billing.models import Bill
from accounts.models import patient

# Create your views here.
def billing(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login_patient')
    
    p = patient.objects.get(id=patient_id)
    bills = Bill.objects.filter(patient=p, status='pending')
    
    total_pending = sum(bill.amount for bill in bills)
    
    context = {
        'patient': p,
        'bills': bills,
        'total_pending': total_pending
    }
    return render(request, 'billing/billing.html', context)

def billing_history(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login_patient')
    
    p = patient.objects.get(id=patient_id)
    bills = Bill.objects.filter(patient=p).order_by('-bill_date')
    
    context = {
        'patient': p,
        'bills': bills
    }
    return render(request, 'billing/billing_history.html', context)   


