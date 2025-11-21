from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__' 
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'arrival_date': forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}),
            'departure_date': forms.DateTimeInput(attrs={'class':'form-control','type':'date'}),
            'adult': forms.NumberInput(attrs={'class':'form-control'}),
            'child': forms.NumberInput(attrs={'class':'form-control'}),
            'room': forms.Select(attrs={'class':'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class':'form-control'}),
            'additional_requirement': forms.Textarea(attrs={'class':'form-control'}),
            'total_guests': forms.NumberInput(attrs={'class':'form-control'}),
            'total_rooms': forms.NumberInput(attrs={'class':'form-control'}),
        }
