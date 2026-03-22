from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'manufacturer', 'stock', 'price', 'expiry_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicine Name'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Manufacturer'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Current Stock'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price per unit'}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
