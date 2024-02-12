from django.shortcuts import render, redirect, get_object_or_404

from clientes.models import Clientes


def lista_clientes_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            email = request.POST.get('email')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            metodo_de_pago = request.POST.get('metodo_de_pago')
            cliente = Clientes(nombre=nombre, apellidos=apellidos, email=email, telefono=telefono, direccion=direccion, metodo_de_pago=metodo_de_pago)
            cliente.save()

        user = request.user
        clientes = Clientes.objects.all()
        return render(request, 'clientes/listaClientes.html', {'user': user, 'clientes': clientes})
    else:
        return redirect("../login/")


def modificar_cliente_view(request, id_cliente):
    if request.user.is_authenticated:
        user = request.user
        cliente = get_object_or_404(Clientes, idcliente=id_cliente)
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            apellidos = request.POST.get('apellidos')
            email = request.POST.get('email')
            telefono = request.POST.get('telefono')
            direccion = request.POST.get('direccion')
            metodo_de_pago = request.POST.get('metodo_de_pago')
            cliente.apellidos = apellidos if apellidos is not None else cliente.apellidos
            cliente.telefono = telefono if telefono is not None else cliente.telefono
            cliente.direccion = direccion if direccion is not None else cliente.direccion
            cliente.metodo_de_pago = metodo_de_pago if metodo_de_pago is not None else cliente.metodo_de_pago
            cliente.save()
            # messages.success(request, 'Empleado modificado correctamente')
            return redirect('../')
        else:
            return render(request, "clientes/modificaCliente.html", {"user": user, "cliente": cliente})
    else:
        return redirect("../login/")


def eliminar_cliente(request, id_cliente):
    if request.user.is_authenticated:
        cliente = get_object_or_404(Clientes, idcliente=id_cliente)
        cliente.delete()
        return redirect('listaClientes')
    else:
        return redirect("../login/")
