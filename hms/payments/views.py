from django.shortcuts import render, redirect
from payments.models import Payment
from accounts.models import patient

# Create your views here.
def index(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login_patient')
    
    p = patient.objects.get(id=patient_id)
    payments = Payment.objects.filter(patient=p)
    
    total_amount = sum(pay.amount for pay in payments if pay.status == 'completed')
    pending_amount = sum(pay.amount for pay in payments if pay.status == 'pending')
    
    context = {
        'patient': p,
        'payments': payments,
        'total_amount': total_amount,
        'pending_amount': pending_amount
    }
    return render(request, 'payments/index.html', context)
