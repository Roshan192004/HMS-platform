from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now

# Doctor model
class Doctor(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f"Dr.{self.User.username}"
    
# Time Slot Model

class TimeSlot(models.Model):
    doctor = models.ForeignKey("Doctor",
    on_delete=models.CASCADE,related_name="time_slots")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('doctor','date','start_time')
    
    def clean(self):
        # prevent past date slots
        if self.date < now().date():
            raise ValidationError("Cannot create slot in the past")
        
        # prevent invalid time 
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be after start time")
    def __str__(self):
        return f"{self.doctor}|{self.date}|{self.start_time}-{self.end_time}"
    
# appointment model
class Appointment(models.Model):
    
    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="appointments"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        
    )

    slot = models.OneToOneField(
        TimeSlot,
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Booked'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Prevent booking past date
        if self.slot.date < now().date():
            raise ValidationError("Cannot book appointment in the past")

        # Prevent double booking
        if self.slot.is_booked:
            raise ValidationError("This slot is already booked")

    def save(self, *args, **kwargs):
        self.full_clean()  # run validation

        # Mark slot as booked
        self.slot.is_booked = True
        self.slot.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient.username} → {self.doctor}"