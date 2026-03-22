from django.db import models
from accounts.models import patient

# Create your models here.

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-payment_date']
    
    def __str__(self):
        return f"Payment from {self.patient.patient_name} - {self.amount}"
