from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from accounts.models import laboratory
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def landing_page(request):
    return render(request,'laboratory/landing_page.html')

# register
def laboratory_register(request):
    if request.method == 'POST':
        laboratory_name = request.POST.get('laboratory_name')
        laboratory_number = request.POST.get('laboratory_number')
        laboratory_email = request.POST.get('laboratory_email')
        laboratory_password = request.POST.get('laboratory_password')
        
        laboratory.objects.create(
            laboratory_name=laboratory_name,
            laboratory_number=laboratory_number,
            laboratory_email=laboratory_email,
            laboratory_password=laboratory_password
        )

        send_mail(
            subject="Welcome to Hospital Management System",
            message=f'Hello {laboratory_name}, Thanks for registering with us',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[laboratory_email],
            fail_silently=False
        )

        return redirect('laboratory_login')

    return render(request, 'laboratory/register.html')

# ==========login
def laboratory_login(request):
    if request.method == "POST":
        username = request.POST.get("laboratory_name")
        password = request.POST.get("laboratory_password")

        print("Entered Username:", username)
        print("Entered Password:", password)

        try:
            user = laboratory.objects.get(
                laboratory_name__iexact=username,
                laboratory_password=password
            )

            print("User Found:", user)

            request.session['laboratory_id'] = user.id
            request.session['laboratory_name'] = user.laboratory_name

            return redirect('landing')

        except laboratory.DoesNotExist:
            print("User NOT found in DB")
            messages.error(request, "Invalid Username or Password")
            return redirect('laboratory_login')

    return render(request, 'laboratory/login.html')