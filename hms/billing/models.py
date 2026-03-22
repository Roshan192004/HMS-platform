from django.db import models
from accounts.models import patient

# Create your models here.

class Bill(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('billed', 'Billed'),
        ('paid', 'Paid'),
    ]
    
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    bill_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    bill_number = models.CharField(max_length=100, unique=True)
    due_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-bill_date']
    
    def __str__(self):
        return f"Bill #{self.bill_number} - {self.patient.patient_name}"
