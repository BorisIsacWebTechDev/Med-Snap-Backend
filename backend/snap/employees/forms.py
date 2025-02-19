from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *

class LoginForm(AuthenticationForm):
    """Form to log in a user"""
    class Meta:
        model = BasicCustomEmployee
        fields = ['email', 'password']

class RegisterSingleForm(UserCreationForm):
    """Form to register User"""

    class Meta:
        model = DrClinicalEmployee
        fields = [
            "email", 
            "first_name", 
            "last_name", 
            "contact_number", 
            "gender",
            "medical_order_id",
            "specialty_type",
            "password1", 
            "password2", 
            ]
        
class RegisterSingleNewEmployee(UserCreationForm):
    #create form for new user. Shoud be done just by ADMIN or Superuser(Doctor)
    class Meta:
        model = BasicCustomEmployee
        fields = [
            "email", 
            "first_name", 
            "last_name", 
            "contact_number", 
            "gender",
            "role",
            "password1", 
            "password2", 
        ]

class RegisterHospitalForm(forms.ModelForm):
    """Form to register User"""
    class Meta:
        model = HospitalUser
        exclude = ["password1", "password2"]
        fields = [ 
            "clinical_name",
            "clinical_email",
            "clinical_phone",
            "tax_id",
            "clinical_type",
            "country",
            "city",
            "address",
            "zip_code",
            "num_staff",
            ]
        '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("password1", None)  
        self.fields.pop("password2", None)'''