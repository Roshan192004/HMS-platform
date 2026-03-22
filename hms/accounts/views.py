from django.shortcuts import*
from .models import*
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from pharmacy.models import Bill
from django.db.models import Sum
def landing(request):
    return render(request,'index.html')
def patient_login(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_password = request.POST.get('patient_password')
        m = patient.objects.filter(
            patient_name = patient_name,
            patient_password = patient_password

        ).first()
        if m:
            request.session['patient_id'] = m.id
            return redirect('pre_patient')
    return render(request, 'accounts/login_patient.html')
def view_profile(request):
    patient_id = request.session.get('patient_id')    
    patients = patient.objects.get(id=patient_id)
    return render(request, 'accounts/view_profile_patient.html', {'patient': patients})
def pre_patient(request):
    patient_id = request.session.get('patient_id')
    # print(patient_id)
    objs = patient.objects.get(id=patient_id)

    return render(request,'accounts/pre_patient.html',
                  {
                      'patient':objs
                  })
def patient_register(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        patient_age = request.POST.get('patient_age')
        patient_number = request.POST.get('patient_number')
        patient_email = request.POST.get('patient_email')
        patient_password = request.POST.get('patient_password')
        patient_blood_group = request.POST.get('patient_blood_group')
        patient_gender = request.POST.get('patient_gender')
        patient_height = request.POST.get('patient_height')
        patient_weight = request.POST.get('patient_weight')
        patient_image = request.FILES.get('patient_image')

        patient.objects.create(
            patient_name=patient_name,
            patient_age=patient_age,
            patient_number=patient_number,
            patient_email=patient_email,
            patient_password=patient_password,
            patient_blood_group = patient_blood_group,
            patient_gender = patient_gender,
            patient_weight = patient_weight,
            patient_height = patient_height,
            patient_image = patient_image
        )

        send_mail(
            subject="Welcome to Hospital Management System",
            message=f'Hello {patient_name}, Thanks for registering with us',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[patient_email],
            fail_silently=False
        )
        return render(request,'accounts/login_patient.html')
<<<<<<< HEAD
    
=======





>>>>>>> a60adfbd7ca1c80757c21657537762cdf9c82e82
    return render(request, 'accounts/register_patient.html')

def patient_dashboard(request):
    return render(request,'accounts/patient_dashboard.html')


def pre_doctor(request):
    doctor_id = request.session.get('doctor_id')
    d = doctor.objects.get(id= doctor_id)
    return render(request,'accounts/pre_doctor.html',{'d':d})

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
        
            
    return render(request, 'accounts/login_doctor.html')

def doctor_register(request):
    if request.method == 'POST':
        doctor_name = request.POST.get('doctor_name')
        doctor_speciality = request.POST.get('doctor_speciality')
        doctor_fee = request.POST.get('doctor_fee')
        doctor_slots = request.POST.get('doctor_slots')
        doctor_number = request.POST.get('doctor_number')
        doctor_email = request.POST.get('doctor_email')
        doctor_password = request.POST.get('doctor_password')

        doctor.objects.create(
            doctor_name=doctor_name,
            doctor_fee=doctor_fee,
            doctor_slots=doctor_slots,
            doctor_speciality=doctor_speciality,
            doctor_number=doctor_number,
            doctor_email=doctor_email,
            doctor_password=doctor_password
        )

        send_mail(
            subject="Welcome to Hospital Management System",
            message=f'Hello Dr. {doctor_name}, Thanks for registering with us',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[doctor_email],
            fail_silently=False
        )
        return render(request,'accounts/login_doctor.html')

    return render(request, 'accounts/register_doctor.html')

def pre_receptionist(request):
    receptionist_id = request.session.get('receptionist_id')
    r = receptionist.objects.get(id = receptionist_id)
    return render(request,'accounts/pre_receptionist.html',{'r':r})

def receptionist_login(request):
    if request.method == 'POST':
        receptionist_name = request.POST.get('receptionist_name')
        receptionist_password = request.POST.get('receptionist_password')
        m = receptionist.objects.filter(
            receptionist_name = receptionist_name,
            receptionist_password = receptionist_password

        ).first()
        if m:
            request.session['receptionist_id'] = m.id
            return redirect('pre_receptionist')
        
            
    return render(request, 'accounts/login_receptionist.html')

def receptionist_register(request):
    if request.method == 'POST':
        receptionist_name = request.POST.get('receptionist_name')
        receptionist_number = request.POST.get('receptionist_number')
        receptionist_email = request.POST.get('receptionist_email')
        receptionist_password = request.POST.get('receptionist_password')

        receptionist.objects.create(
            receptionist_name=receptionist_name,
            # receptionist_otp=receptionist_otp,
            receptionist_number=receptionist_number,
            receptionist_email=receptionist_email,
            receptionist_password=receptionist_password
        )

        send_mail(
            subject="Welcome to Hospital Management System",
            message=f'Hello {receptionist_name}, Thanks for registering with us',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[receptionist_email],
            fail_silently=False
        )
        return redirect('pre_receptionist')

    return render(request, 'accounts/register_receptionist.html')

def temp(request):
    return render(request,'accounts/temp.html')
def base_patient(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login_patient')
    m = patient.objects.get(id = patient_id)
    appointment_count = appointments.objects.filter(
        patient_name=m.patient_name
    ).count()
    return render(request,'accounts/base_patient.html',{
        'm2':m,
        'count':appointment_count})

def logout_patient(request):
    if 'patient_id' in request.session:
        del request.session['patient_id']
    return redirect('login_patient')


def admin_dashboard(request):
    p2 = patient.objects.all()
    p3 = patient.objects.all().count()
    d2 = doctor.objects.all()
    d3 = doctor.objects.all().count()
    p = timezone.now().date()
    a = appointments.objects.filter(appointment_data = p)
    total_earning = Bill.objects.aggregate(
        total=Sum('total_amount')
    )['total'] or 0
<<<<<<< HEAD

    

    

=======
>>>>>>> a60adfbd7ca1c80757c21657537762cdf9c82e82
    return render(request,'accounts/admin_dashboard.html',{'p3':p3,'d3':d3,'a':a , 'total_earning':total_earning})
def p(request):
    p2 = patient.objects.all()
    p3 = patient.objects.all().count()
    return render(request,'accounts/patients.html',{'p2':p2,'p3':p3})    
def d(request):
    d2 = doctor.objects.all()
    d3 = doctor.objects.all().count()
    return render(request,'accounts/doctors.html',{'d2':d2, 'd3':d3})    
