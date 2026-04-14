from django.shortcuts import*
from accounts.models import*
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

def pre_doctor(request):
    doctor_id = request.session.get('doctor_id')
    d = doctor.objects.get(id= doctor_id)
    return render(request,'doctors/pre_doctor.html',{'d':d})

def doctor_login(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_password = request.POST.get('doctor_password')
        m = doctor.objects.filter(
            doctor_name = doctor_name,
            doctor_password = doctor_password

        ).first()
        if m:
            request.session['doctor_id'] = m.id
            return redirect('pre_doctor')
        
            
    return render(request, 'doctors/login_doctor.html')

def doctor_register(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_speciality = request.POST.get('doctor_speciality')
        doctor_fee = request.POST.get('doctor_fee')
        doctor_slots = request.POST.get('doctor_slots')
        doctor_number = request.POST.get('doctor_number')
        doctor_email = request.POST.get('doctor_email')
        doctor_password = request.POST.get('doctor_password')
        doctor_image = request.FILES.get('doctor_image')

        doctor.objects.create(
            doctor_name=doctor_name,
            doctor_fee=doctor_fee,
            doctor_slots=doctor_slots,
            doctor_speciality=doctor_speciality,
            doctor_number=doctor_number,
            doctor_email=doctor_email,
            doctor_password=doctor_password,
            doctor_image = doctor_image

        )

        send_mail(
            subject="Welcome to Hospital Management System",
            message=f'Hello Dr. {doctor_name}, Thanks for registering with us',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[doctor_email],
            fail_silently=False
        )
        return render(request,'doctors/login_doctor.html')

    return render(request, 'doctors/register_doctor.html')

def doctor_dashboard(request):
    d = request.session.get('doctor_id')
    db = doctor.objects.get(id=d)
    today = timezone.now().date()

    today_appointments = appointments.objects.filter(
        doctor=db.doctor_name,
        appointment_data=today,
        status='Accepted'
    )

    total_today = today_appointments.count()

    total_all = appointments.objects.filter(
        doctor=db.doctor_name,
        status='Accepted'
    ).count()

    prescribed_patients = prescription.objects.filter(
        patient_name__in=today_appointments.values_list('patient_name', flat=True)
    ).values_list('patient_name', flat=True)

    prescribed_patients_count = prescription.objects.filter(
        patient_name__in=today_appointments.values_list('patient_name', flat=True)
    ).values('patient_name').distinct().count()

    pending_count = total_today - prescribed_patients_count

    return render(request, 'doctors/doctor_dashboard.html', {
        'c': total_all,
        'c2': today_appointments,
        'c3': total_today,
        'db': db,
        'check': prescribed_patients,
        'check2': prescribed_patients_count,
        'pending_count': pending_count
    })
def my_appointment(request):
    d = request.session.get('doctor_id')
    k = doctor.objects.get(id = d)
    m = appointments.objects.filter(doctor=k.doctor_name, status='Accepted')
    return render(request,'doctors/my_appointments.html',{'q':m})

def patient_record(request):
    k = request.session.get('doctor_id')

    m = doctor.objects.get(id=k)   # single doctor

    a = appointments.objects.filter(doctor=m.doctor_name, status='Accepted')  # all accepted appointments
    # p = patient.objects.filter(patient_name = a.patient)

    return render(request, 'doctors/patient_record.html', {
        'z': a,
        'd' : m
    })

def create_prescription(request):
    d = request.session.get('doctor_id')
    d2 = doctor.objects.get(id = d)
    f = appointments.objects.filter(doctor = d2.doctor_name, status='Accepted')
    if request.method == 'POST':

        patient_name  = request.POST.get('patient_name')
        medicines = request.POST.get('medicines')
        prescription.objects.create(
            patient_name = patient_name,
            medicines = medicines
        )
        return redirect('/doctors/doctor_dashboard')
    
    return render(request,'doctors/prescription.html', {'f':f})


def my_profile(request):
    k = request.session.get('doctor_id')
    d = doctor.objects.get(id = k)
    return render(request,'doctors/my_profile.html',{'d':d})

