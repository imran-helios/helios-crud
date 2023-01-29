from django import forms
import re
from .models import Registration
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm


## Sign_Up Form

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password',widget = forms.PasswordInput(attrs= {'class': 'password_field'}))
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput(attrs= {'class': 'con_password_field'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'uname_field', 'placeholder': 'Enter Your User Name'}),

            'first_name': forms.TextInput(attrs={'class': 'first_name_field', 'placeholder': 'Enter Your First Name'}),

            'last_name': forms.TextInput(attrs={'class': 'last_name_field', 'placeholder': 'Enter Your Last Name'}),
            
            'email': forms.EmailInput(attrs={'class': 'email_field', 'placeholder': 'Enter Your Email Address'})
        }
## Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label = 'Username',widget = forms.TextInput(attrs= {'class': 'uname_field'}))
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs= {'class': 'password_field'}))
    

## Student Registration Form
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