from django.contrib import messages
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
        if request.method == 'POST':
            print("Formulario recibido")
            idempleado = request.POST.get('idempleado')
            print("idempleado: ", idempleado)
            nombre = request.POST.get('nombre')
            print("nombre: ", nombre)
            apellidos = request.POST.get('apellidos')
            print("apellidos: ", apellidos)
            edad = request.POST.get('edad')
            print("edad: ", edad)
            telefono = request.POST.get('telefono')
            print("telefono: ", telefono)
            direccion = request.POST.get('direccion')
            print("direccion: ", direccion)
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
            return render(request, "empleado/modificaEmpleado.html", {"user": user})
    else:
        return redirect("../login/")

