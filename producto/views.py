from collections import defaultdict

from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect

from login.models import User
from producto.models import Productos
from proveedores.models import Proveedores
from clientes.models import Clientes


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
        productos = Productos.objects.all().prefetch_related('productostock_set')
        return render(request, 'producto/listaProducto.html', {'user': user, 'productos': productos})
    else:
        return redirect("login")


def lista_productos_cliente_view(request):
    if request.user.is_authenticated:
        user = request.user
        productos = Productos.objects.all().prefetch_related('productostock_set')
        return render(request, 'producto/listaProductoCliente.html', {'user': user, 'productos': productos})
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


def hacer_pedido(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            productos_ids = request.POST.getlist('producto')
            cantidades = request.POST.getlist('cantidad')

            # Asegúrate de que las listas de productos y cantidades tienen la misma longitud
            if len(productos_ids) != len(cantidades):
                messages.error(request, 'Los datos del formulario son inválidos.')
                return redirect('hacerPedido')

            # Crear un diccionario para almacenar las categorías y los productos correspondientes
            categorias_productos = defaultdict(list)
            categorias_cantidades = defaultdict(list)

            # Recorrer la lista de productos
            for i in range(len(productos_ids)):
                producto_id = productos_ids[i]
                cantidad = cantidades[i]

                # Obtener el producto y su categoría
                producto = Productos.objects.get(idproducto=producto_id)
                categoria = producto.categoria

                # Agregar el id del producto y la cantidad al diccionario en la entrada correspondiente a su categoría
                categorias_productos[categoria].append(producto_id)
                categorias_cantidades[categoria].append(cantidad)

            # Recorrer el diccionario y buscar un proveedor para cada categoría
            for categoria, productos in categorias_productos.items():
                # Buscar un proveedor que tenga la misma categoría
                proveedor = Proveedores.objects.filter(categoria=categoria).first()

                if proveedor:
                    # Finalizar el pedido con el proveedor
                    # Aquí puedes agregar el código para finalizar el pedido con el proveedor
                    ids_productos = ','.join(productos)
                    cantidades = ','.join(categorias_cantidades[categoria])
                    llamar_procedimiento_almacenado(proveedor.idproveedor, ids_productos, cantidades)
                    pass
                else:
                    messages.error(request, f'No se encontró un proveedor para la categoría {categoria}.')

        return redirect('listaProductos')
    else:
        return redirect('login')


def hacer_pedido_cliente(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            productos_ids = request.POST.getlist('producto')
            productos_string = ','.join(productos_ids)
            cantidades = request.POST.getlist('cantidad')
            cantidades_string = ','.join(cantidades)

            # Asegúrate de que las listas de productos y cantidades tienen la misma longitud
            if len(productos_ids) != len(cantidades):
                messages.error(request, 'Los datos del formulario son inválidos.')
                return redirect('hacerPedido')

            user = User.objects.get(id=request.user.id)
            user_cliente = Clientes.objects.get(user=user)

            llamar_procedimiento2_almacenado(user_cliente.idcliente, productos_string, cantidades_string, user_cliente.direccion)

        return redirect('listaProductosCliente')
    else:
        return redirect('login')


def hacer_pedido_proveedor(request, id_proveedor):
    if request.user.is_authenticated:
        if request.method == 'POST':
            productos_ids = request.POST.getlist('producto')
            cantidades = request.POST.getlist('cantidad')

            # Asegúrate de que las listas de productos y cantidades tienen la misma longitud
            if len(productos_ids) != len(cantidades):
                messages.error(request, 'Los datos del formulario son inválidos.')
                return redirect('hacerPedido')

            ids_productos = ','.join(productos_ids)
            cantidades = ','.join(cantidades)
            print("productos_ids: ", productos_ids)
            print("cantidades: ", cantidades)
            llamar_procedimiento_almacenado(id_proveedor, ids_productos, cantidades)
            pass

        return redirect('modificar_proveedor', id_proveedor)
    else:
        return redirect('login')


def borrar_pedido_cliente(request, id_factura):
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            cursor.callproc('EliminarFactura', [id_factura])
        return redirect('listaFacturasCliente')
    else:
        return redirect('login')


def csrf(request):
    return HttpResponse(get_token(request))


def llamar_procedimiento_almacenado(id_proveedor, ids_productos, cantidades):
    with connection.cursor() as cursor:
        cursor.callproc('GenerarPedidoConCantidad', [id_proveedor, ids_productos, cantidades])


def llamar_procedimiento2_almacenado(id_cliente, ids_productos, cantidades, direccion):
    with connection.cursor() as cursor:
        cursor.callproc('GenerarFacturaConCantidad', [id_cliente, ids_productos, cantidades, direccion])
