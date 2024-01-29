from django.shortcuts import render, redirect

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
