from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'BookingDate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }