from django.db import models
from patients.models import PrescriptionOrder
from accounts.models import pharmacist

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    stock = models.IntegerField()
    price = models.FloatField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    pharmacist = models.ForeignKey(pharmacist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.medicine.price * self.quantity

class Bill(models.Model):
    prescription_order = models.ForeignKey(PrescriptionOrder, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(pharmacist, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    items_summary = models.TextField() # Store a string summary of items

    def __str__(self):
        return f"Bill for {self.prescription_order.patient_name} - {self.total_amount}"
