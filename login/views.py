from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect

from login.forms import LoginForm, RegisterForm
from login.models import Empleados


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = Empleados.objects.filter(email=email).first()
            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect("../")
            else:
                form.add_error(None, "Usuario o contraseña incorrectos")

    else:
        form = LoginForm()

    return render(request, "login/login.html", {'form': form})


def register_view(request):
    if request.method == "POST":
        print('request is post')
        form = RegisterForm(data=request.POST)
        print('form creado')
        if form.is_valid():
            print('form is valid')
            user = form.save()
            login(request, user)
            return redirect("../")
        else:
            print('form is not valid')
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, "login/register.html", {'form': form})


def empleado_view(request):
    return render(request, "empleado/modificaEmpleado.html")


def empleado_contrasegna_view(request):
    return render(request, "empleado/modificaEmpleadoContraseña.html")
