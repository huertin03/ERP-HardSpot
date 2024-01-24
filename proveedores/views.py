from django.shortcuts import render, redirect

from proveedores.models import Proveedores


def lista_proveedores_view(request):
    if request.user.is_authenticated:
        user = request.user
        proveedores = Proveedores.objects.all()
        return render(request, 'proveedores/listaProveedores.html', {'user': user, 'proveedores': proveedores})
    else:
        return redirect("../login/")
