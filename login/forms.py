from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from login.models import Empleados


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    class Meta:
        model = Empleados
        fields = ['nombre', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Empleados.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe")
        return email
