from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=12, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Doctor(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    specialty = models.CharField(max_length=80, blank=True)
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"


class StaffMember(models.Model):
    name = models.CharField(max_length=80)
    role = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS = [
        ('sch', 'Scheduled'),
        ('done', 'Completed'),
        ('cxl', 'Canceled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    when = models.DateTimeField()
    status = models.CharField(max_length=8, choices=STATUS, default='sch')
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.patient} — {self.when:%Y-%m-%d %H:%M}"


class BillingRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} — ${self.amount}"


class InventoryItem(models.Model):
    name = models.CharField(max_length=120)
    qty = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} ({self.qty})"


class Report(models.Model):
    title = models.CharField(max_length=140)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
