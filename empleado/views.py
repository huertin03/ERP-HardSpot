from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

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
        if request.method == 'POST':
            idempleado = user.idempleado
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            edad = request.POST.get('edad')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            empleado = Empleados.objects.get(idempleado=idempleado)
            empleado.nombre = nombre if nombre is not None else empleado.nombre
            empleado.apellidos = apellidos if apellidos is not None else empleado.apellidos
            empleado.edad = edad if edad is not None else empleado.edad
            empleado.telefono = telefono if telefono is not None else empleado.telefono
            empleado.direccion = direccion if direccion is not None else empleado.direccion
            empleado.save()
            # messages.success(request, 'Empleado modificado correctamente')
            return redirect('../')
        else:
            return render(request, "empleado/modificaEmpleado.html", {"user": user, "empleado": user})
    else:
        return redirect("../login/")


def modificar_empleado_view(request, idempleado):
    if request.user.is_authenticated:
        user = request.user
        empleado = get_object_or_404(Empleados, idempleado=idempleado)
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            edad = request.POST.get('edad')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            empleado.nombre = nombre if nombre is not None else empleado.nombre
            empleado.apellidos = apellidos if apellidos is not None else empleado.apellidos
            empleado.edad = edad if edad is not None else empleado.edad
            empleado.telefono = telefono if telefono is not None else empleado.telefono
            empleado.direccion = direccion if direccion is not None else empleado.direccion
            empleado.save()
            # messages.success(request, 'Empleado modificado correctamente')
            return redirect('../')
        else:
            return render(request, "empleado/modificaEmpleado.html", {"user": user, "empleado": empleado})
    else:
        return redirect("../login/")


