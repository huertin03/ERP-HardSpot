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
        return redirect("login")


def modificar_producto_view(request, idproducto):
    if request.user.is_authenticated:
        user = request.user
        producto = Productos.objects.get(idproducto=idproducto)
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            precio = request.POST.get('precio')
            categoria = request.POST.get('categoria')
            descripcion = request.POST.get('descripcion')
            producto.nombre = nombre if nombre is not None else producto.nombre
            producto.precio = precio if precio is not None else producto.precio
            producto.categoria = categoria if categoria is not None else producto.categoria
            producto.descripcion = descripcion if descripcion is not None else producto.descripcion
            producto.save()
            # messages.success(request, 'Empleado modificado correctamente')
            return redirect('listaProductos')
        else:
            producto.precio = str(producto.precio).replace(',', '.')
            return render(request, "producto/modificaProducto.html", {"user": user, "producto": producto})
    else:
        return redirect("login")


def eliminar_producto(request, id_producto):
    if request.user.is_authenticated:
        producto = Productos.objects.get(idproducto=id_producto)
        producto.delete()
        return redirect('listaProductos')
    else:
        return redirect("login")
