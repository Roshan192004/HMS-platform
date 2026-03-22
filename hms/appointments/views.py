from django.shortcuts import*
from appointments.models import Appointment
from django.utils.timezone import now
from accounts.models import*
from django.core.mail import send_mail
from hms import settings
from patients import views
# Create your views here.
def user_dashboard(request):
    p = patient.objects.count()
    d = doctor.objects.count()
    a = appointments.objects.count()
    return render(request,'Reception/reception_dashboard.html',
                  {'pcount':p ,
                   'dcount':d,
                   'acount':a},
                   )

# ==
def book_appointment(request):
    patient_id = request.session.get('patient_id')
    k = patient.objects.filter(id = patient_id)
    d = doctor.objects.all()
    # p = patient.objects.count()
    return render(request,'appointments/book_appointment.html' , 
                  {'k':k ,
                    'doctor':d })
def appointment(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_age = request.POST.get('patient_age')
        if not patient_age:
            patient_age = None
        patient_email = request.POST.get('patient_email')
        patient_number = request.POST.get('patient_number')
        appointment_data = request.POST.get('appointment_data')
        appointment_time = request.POST.get('appointment_time')
        doctor = request.POST.get('doctor')
        reason = request.POST.get('reason')
        appointments.objects.create(
            patient_name=patient_name,
            patient_age = patient_age,
            patient_email = patient_email,
            patient_number = patient_number,
            appointment_data = appointment_data,
            appointment_time = appointment_time,
            doctor = doctor,
            reason = reason
        )
        m=patient.objects.filter(
            patient_name = patient_name
        ).first()
        if m:
            request.session['patient_id'] = m.id 
             
        send_mail(
            subject= "Appointment Scheduled",
            message=f"Hello {patient_name}, Your appointment is scheduled on {appointment_data} with Dr.{doctor}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[patient_email],
            fail_silently=False
        )
        return redirect('base_patient')
            
    return render(request,'appointments/book_appointment.html')
def my_appointment(request):

        patient_id = request.session.get('patient_id')
        if not patient_id:
            return redirect('login_patient')
        patient_obj = patient.objects.get(id=patient_id)
        m = appointments.objects.filter(
            patient_name=patient_obj.patient_name
        )
        return render(request,'appointments/patient_my_appointment.html',{'m9':m})
        