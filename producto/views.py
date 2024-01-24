from django.shortcuts import render, redirect

from producto.models import Productos


def lista_productos_view(request):
    if request.user.is_authenticated:
        user = request.user
        productos = Productos.objects.all()
        return render(request, 'producto/listaProducto.html', {'user': user, 'productos': productos})
    else:
        return redirect("../login/")
