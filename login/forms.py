from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from clientes.models import Clientes
from empleado.models import Empleados
from login.models import User


class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['nombre', 'email', 'password1', 'password2', 'user_type']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user_type = self.cleaned_data.get('user_type')

        if commit:
            user.save()
            if user_type == User.EMPLOYEE:
                Empleados.objects.create(user=user, nombre=user.nombre)
            elif user_type == User.CLIENT:
                Clientes.objects.create(user=user)

        return user
