
from django.db import models

class PrescriptionOrder(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=50)
    prescription_file = models.FileField(upload_to='prescriptions/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.patient_name
