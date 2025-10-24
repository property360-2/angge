
from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError
from datetime import date

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'date', 'time', 'guests', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_date(self):
        reservation_date = self.cleaned_data.get('date')
        if reservation_date and reservation_date < date.today():
            raise ValidationError("Cannot make reservations for past dates.")
        return reservation_date