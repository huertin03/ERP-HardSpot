from django.shortcuts import render, redirect

from proveedores.models import Proveedores


def lista_proveedores_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            categoria = request.POST.get('categoria')
            proveedor = Proveedores(nombre=nombre, email=email, telefono=telefono, direccion=direccion, categoria=categoria)
            proveedor.save()

        user = request.user
        proveedores = Proveedores.objects.all()
        return render(request, 'proveedores/listaProveedores.html', {'user': user, 'proveedores': proveedores})
    else:
        return redirect("login")


def modificar_proveedor_view(request, id_proveedor):
    if request.user.is_authenticated:
        user = request.user
        proveedor = Proveedores.objects.get(idproveedor=id_proveedor)
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            categoria = request.POST.get('categoria')
            proveedor.nombre = nombre if nombre is not None else proveedor.nombre
            proveedor.email = email if email is not None else proveedor.email
            proveedor.telefono = telefono if telefono is not None else proveedor.telefono
            proveedor.direccion = direccion if direccion is not None else proveedor.direccion
            proveedor.save()
            # messages.success(request, 'Empleado modificado correctamente')
            return redirect('listaProveedores')
        else:
            return render(request, "proveedores/modificaProveedor.html", {"user": user, "proveedor": proveedor})
    else:
        return redirect("login")


def eliminar_proveedor(request, id_proveedor):
    if request.user.is_authenticated:
        proveedor = Proveedores.objects.get(idproveedor=id_proveedor)
        proveedor.delete()
        return redirect('listaProveedores')
    else:
        return redirect("login")