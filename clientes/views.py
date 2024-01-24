from django.shortcuts import render, redirect

from clientes.models import Clientes


def lista_clientes_view(request):
    if request.user.is_authenticated:
        user = request.user
        clientes = Clientes.objects.all()
        return render(request, 'clientes/listaClientes.html', {'user': user, 'clientes': clientes})
    else:
        return redirect("../login/")
