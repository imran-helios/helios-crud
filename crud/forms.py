from django import forms
import re
from .models import Registration

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name_field', 'placeholder': 'Enter Your Name'}),
            'phone': forms.TextInput(attrs={'class': 'phone_field', 'placeholder': 'Enter Your Phone NUmber'})
        }
        labels = {
            'name': 'Full Name :',
            "phone": 'Phone Number :',
            }
        error_messages = {
            'name': {'required': 'name fIeld should not be empty'},
            'phone': {'required':'phone fIeld should not be empty'},
        }

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data.get('phone',''))
        phone = cleaned_data.get('phone','')
        validate_paterns = re.findall("^(\+88|88)?01[3-9]\d{8}$",phone)
        if not validate_paterns:
            msg = 'Invalid Phone Number'
            self.add_error('phone',msg)