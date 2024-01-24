from django.shortcuts import render, redirect

from proveedores.models import Proveedores


def lista_proveedores_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            proveedor = Proveedores(nombre=nombre, email=email, telefono=telefono, direccion=direccion)
            proveedor.save()

        user = request.user
        proveedores = Proveedores.objects.all()
        return render(request, 'proveedores/listaProveedores.html', {'user': user, 'proveedores': proveedores})
    else:
        return redirect("../login/")
