from django.shortcuts import*
from accounts.models import*
from django.conf import settings
from django.core.mail import send_mail
from .models import PrescriptionOrder
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from datetime import datetime
from accounts.models import*   # change if model name different
# from django.utils import timezone

def download_prescription(request, id):
    # Fetch one row from DB
    pres = prescription.objects.get(id=id)

    # Create HTTP response as PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="prescription_{id}.pdf"'

    # Create PDF document
    doc = SimpleDocTemplate(response, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()

    # Add content from that specific row
    elements.append(Paragraph("Hospital Management System", styles["Heading1"]))
    elements.append(Spacer(1, 0.5 * inch))

    elements.append(Paragraph(f"Date: {datetime.now().strftime('%d-%m-%Y')}", styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"Patient Name: {pres.patient_name}", styles["Normal"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("Prescription:", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(pres.medicines, styles["Normal"]))

    doc.build(elements)

    return response


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
        
    return render(request, 'patients/login_patient.html')
def view_profile(request):
    patient_id = request.session.get('patient_id')    
    patients = patient.objects.get(id=patient_id)
    return render(request, 'patients/view_profile_patient.html', {'patient': patients})
def pre_patient(request):
    patient_id = request.session.get('patient_id')
    # print(patient_id)
    objs = patient.objects.get(id=patient_id)

    return render(request,'patients/pre_patient.html',
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
        return render(request,'patients/login_patient.html')
    return render(request, 'patients/register_patient.html')

def patient_dashboard(request):
    return render(request,'patients/patient_dashboard.html')
def base_patient(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('login_patient')
    m = patient.objects.get(id = patient_id)
    appointment_count = appointments.objects.filter(
        patient_name=m.patient_name
    ).count()
    pt = m.patient_name
    p = datetime.today().date()
    k = appointments.objects.filter(appointment_data = p , patient_name = pt).count()
    return render(request,'patients/base_patient.html',{
        'm':m,
        'count':appointment_count,
        'qws':k})


# =======================================================================================
def prescription_home(request):
    return render(request, 'patients/prescription_home.html')

def my_prescription(request):
    k  = request.session.get('patient_id')
    p = patient.objects.get(id = k)
    k = p.patient_name
    m = prescription.objects.filter(patient_name  = p.patient_name)
    return render(request,'patients/my_prescription.html',{'m':m , 'k':k})
<<<<<<< HEAD

=======
>>>>>>> a60adfbd7ca1c80757c21657537762cdf9c82e82
def order_medicine(request):
    patient_id_session = request.session.get('patient_id')
    if not patient_id_session:
        return redirect('login_patient')
    
    patient_obj = patient.objects.get(id=patient_id_session)

    if request.method == "POST":
        prescription = request.FILES.get("prescription_file")

        PrescriptionOrder.objects.create(
            patient_name=patient_obj.patient_name,
            patient_id=str(patient_obj.id),
            prescription_file=prescription
        )

        return redirect('base_patient')

    return render(request, 'patients/order_medicine.html', {'patient': patient_obj})



