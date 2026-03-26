from django.db import models

# Create your models here.
class patient(models.Model):
    patient_name = models.CharField(max_length=20)
    patient_age = models.CharField(max_length=5)
    patient_otp = models.CharField(max_length=10)
    patient_number = models.CharField(max_length=20)
    patient_email = models.EmailField(max_length=20)
    patient_password = models.CharField(max_length=20)
    patient_blood_group = models.CharField(max_length=20)
    patient_gender = models.CharField(max_length=10)
    patient_weight = models.IntegerField()
    patient_height = models.IntegerField()
    patient_image = models.ImageField(upload_to='patients/')
    def __str__(self):
        return self.patient_name
class doctor(models.Model):
    doctor_name = models.CharField(max_length=20)
    doctor_speciality = models.CharField(max_length=20)
    doctor_fee = models.IntegerField()
    doctor_slots = models.IntegerField()
    doctor_otp = models.CharField(max_length=10)
    doctor_number = models.CharField(max_length=20)
    doctor_email = models.EmailField(max_length=20)
    doctor_password = models.CharField(max_length=20)
    doctor_image = models.ImageField(upload_to='doctors/', null=True, blank=True)
    def __str__(self):
        return self.doctor_name

class receptionist(models.Model):
    receptionist_name = models.CharField(max_length=20)
    receptionist_number = models.CharField(max_length=20)
    receptionist_email = models.EmailField(max_length=20)
    receptionist_otp = models.CharField(max_length=10)
    receptionist_password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.receptionist_name

class appointments(models.Model):
    patient_name  = models.CharField(max_length=20)
    patient_age = models.IntegerField(null=True, blank=True)
    patient_email = models.EmailField()
    patient_number = models.CharField(max_length=20)
    appointment_data = models.DateField()
    appointment_time = models.TimeField()
    doctor = models.CharField(max_length=20)
    reason = models.TextField()
    def __str__(self):
        return self.patient_name
# ================================================================
class pharmacist(models.Model):
    pharmacist_name = models.CharField(max_length=20)
    pharmacist_number = models.CharField(max_length=20)
    pharmacist_email = models.EmailField(max_length=20)
    pharmacist_otp = models.CharField(max_length=10)
    pharmacist_password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.pharmacist_name
    

class prescription(models.Model):
    patient_name = models.CharField(max_length=20)
    medicines = models.TextField()
    def __str__(self):
        return self.patient_name

# ============================
class laboratory(models.Model):
    laboratory_name = models.CharField(max_length=20)
    laboratory_number = models.CharField(max_length=20)
    laboratory_email = models.EmailField(max_length=20)
    laboratory_otp = models.CharField(max_length=10)
    laboratory_password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.laboratory_name