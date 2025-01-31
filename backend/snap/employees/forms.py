from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm

from .models import AbstractClinicalEmployee


class LoginForm(AuthenticationForm):
    """Form to log in a user"""
    class Meta:
        model=AbstractClinicalEmployee
        fields = ['email', 'password']

class RegisterForm(UserCreationForm):
    """Form to register User"""

    class Meta:
        model = AbstractClinicalEmployee
        fields = ["email", "password1", "password2", "first_name", "last_name", "contact_number", "employee_type", "gender_employee"]

class RessetPasswordForm(PasswordResetForm):
    """Form to resset password"""
    
    email = forms.EmailField(
        label="Email",
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control", 
                "placeholder": "Enter your email"
                }
            )
    )
