from django.shortcuts import render, redirect

from login.models import Empleados


def lista_empleados_view(request):
    if request.user.is_authenticated:
        user = request.user
        empleados = Empleados.objects.all()
        return render(request, 'empleado/listaEmpleados.html', {'user': user, 'empleados': empleados})
    else:
        return redirect("../login/")


def empleado_view(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, "empleado/modificaEmpleado.html", {"user": request.user})
    else:
        return redirect("../login/")

