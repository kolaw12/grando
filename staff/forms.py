from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from django import forms
from carapp.models import *
class RegistrationForm(UserCreationForm):

    username = forms.CharField(
        label='Username',
        widget= forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    email = forms.EmailField(
        label = 'Email',
        widget= forms.EmailInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password1 = forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs= {
                'class':'form-control'
            }
        )
    )
    first_name = forms.CharField(
        required= False,
        label='First Name',
        widget=forms.TextInput(
            attrs= {
                'class':'form-control'
            }
        )
    )
    last_name = forms.CharField(
        required= False,
        label='Last Name',
        widget=forms.TextInput(
            attrs= {
                'class':'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']

    def save(self, commit= True):
        user = super().save(commit=True)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            return user



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__' 
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'arrival_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'departure_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'adult': forms.NumberInput(attrs={'class':'form-control'}),
            'child': forms.NumberInput(attrs={'class':'form-control'}),
            'room': forms.Select(attrs={'class':'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class':'form-control'}),
            'additional_requirement': forms.Textarea(attrs={'class':'form-control'}),
            'total_guests': forms.NumberInput(attrs={'class':'form-control'}),
            'total_rooms': forms.NumberInput(attrs={'class':'form-control'}),
        }
