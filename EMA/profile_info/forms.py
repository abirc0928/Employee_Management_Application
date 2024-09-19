from django import forms
from .models import user_profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ['address', 'phone_number', 'date_of_brith', 'description']
        widgets = {
            'date_of_brith': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date input with a calendar picker
        }