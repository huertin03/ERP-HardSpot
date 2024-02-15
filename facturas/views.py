from django.shortcuts import render, redirect, get_object_or_404

from facturas.models import FacturasCabecera, FacturasCompuesto

from clientes.models import Clientes


def listaFacturaXCliente_view(request, idCliente):
    if request.user.is_authenticated:
        id_cliente = request.GET.get('idCliente', idCliente)
        facturas = FacturasCabecera.objects.filter(idcliente=id_cliente)
        context = {
            'facturas': facturas,
            'idCliente': id_cliente,
        }
        return render(request, 'facturas/listaFacturaXCliente.html', context)
    else:
        return redirect("login")


def listarFacturas(request):
    if request.user.is_authenticated:
        user = request.user
        facturas = FacturasCabecera.objects.all()
        return render(request, "facturas/listaFacturaXCliente.html", {"facturas": facturas})
    else:
        return redirect("login")


def listaFacturasCliente(request):
    if request.user.is_authenticated:
        user = request.user
        cliente = Clientes.objects.get(user=user)
        facturas = FacturasCabecera.objects.filter(idcliente=cliente)
        return render(request, "facturas/listaFacturaXCliente.html", {"facturas": facturas})
    else:
        return redirect("login")


def detalleFactura(request, idFactura):
    if request.user.is_authenticated:
        factura = get_object_or_404(FacturasCabecera, idfactura=idFactura)
        facturadetalles = FacturasCompuesto.objects.filter(idfactura=idFactura)
        return render(request, 'facturas/detalleFactura.html', {'factura': factura, 'facturadetalles': facturadetalles})
    else:
        return redirect("login")

