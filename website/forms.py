from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import contsave


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Use Django's default User model
        fields = ('username', 'email', 'password1', 'password2')
class ContactForm(forms.ModelForm):
    class Meta:
        model = contsave
        fields = ('name', 'email', 'phone', 'textarea')  # Specify the fields you want in the form
