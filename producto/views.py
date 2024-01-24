from django.shortcuts import render, redirect

from producto.models import Productos


def lista_productos_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            precio = request.POST.get('precio')
            categoria = request.POST.get('categoria')
            descripcion = request.POST.get('descripcion')
            producto = Productos(nombre=nombre, descripcion=descripcion, precio=precio, categoria=categoria)
            producto.save()

        user = request.user
        productos = Productos.objects.all()
        return render(request, 'producto/listaProducto.html', {'user': user, 'productos': productos})
    else:
        return redirect("../login/")
