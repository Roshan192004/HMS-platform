from django.shortcuts import render, redirect
from reports.models import LabReport
from accounts.models import patient

# Create your views here.
def index(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login_patient')
    
    p = patient.objects.get(id=patient_id)
    reports = LabReport.objects.filter(patient=p)
    
    completed_reports = reports.filter(status='completed').count()
    pending_reports = reports.filter(status='pending').count()
    
    context = {
        'patient': p,
        'reports': reports,
        'completed_reports': completed_reports,
        'pending_reports': pending_reports
    }
    return render(request, 'reports/index.html', context)
