from django.shortcuts import render, redirect

from clientes.models import Clientes
from login.models import User


def home_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        if user.user_type == User.EMPLOYEE:
            return render(request, 'core/home.html', {'user': request.user})
        elif user.user_type == User.CLIENT:
            return render(request, 'core/homeCliente.html', {'user': request.user})
    else:
        return redirect("login")
