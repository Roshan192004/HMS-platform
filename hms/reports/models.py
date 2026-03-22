from django.db import models
from accounts.models import patient

# Create your models here.

class LabReport(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('reviewed', 'Reviewed'),
    ]
    
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=200)
    test_date = models.DateField(auto_now_add=True)
    report_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    result = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    report_file = models.FileField(upload_to='lab_reports/', null=True, blank=True)
    
    class Meta:
        ordering = ['-test_date']
    
    def __str__(self):
        return f"{self.test_name} - {self.patient.patient_name}"
