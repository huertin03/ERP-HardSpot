"""
URL configuration for ERP_HardSpot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from login.views import *
from empleado.views import *
from producto.views import *
from clientes.views import *
from proveedores.views import *
from core.views import *


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('listaEmpleados/', lista_empleados_view, name="listaEmpleados"),
    path('listaEmpleados/<int:idempleado>/', modificar_empleado_view, name="modificar_empleado"),
    path('empleado/', empleado_view, name="empleado"),
    path('empleadoContraseña/', empleado_contrasegna_view, name="empleadoContraseña"),
    path('eliminar_empleado/<int:id_empleado>/', eliminar_empleado, name='eliminar_empleado'),

    path('listaProductos/', lista_productos_view, name="listaProductos"),
    path('productos/', lista_productos_cliente_view, name="listaProductosCliente"),
    path('listaProductos/<int:idproducto>/', modificar_producto_view, name="modificar_producto"),
    path('eliminar_producto/<int:id_producto>/', eliminar_producto, name='eliminar_producto'),

    path('hacerPedido/', hacer_pedido, name="hacerPedido"),
    path('hacerPedidoCliente/', hacer_pedido_cliente, name="hacerPedidoCliente"),

    path('listaClientes/', lista_clientes_view, name="listaClientes"),
    path('listaClientes/<int:id_cliente>/', modificar_cliente_view, name="modificar_cliente"),
    path('usuarioCliente/', modificar_cliente_usuario_view, name='modificar_cliente_usuario'),
    path('eliminar_cliente/<int:id_cliente>/', eliminar_cliente, name='eliminar_cliente'),

    path('listaProveedores/', lista_proveedores_view, name="listaProveedores"),
    path('listaProveedores/<int:id_proveedor>/', modificar_proveedor_view, name="modificar_proveedor"),
    path('eliminar_proveedor/<int:id_proveedor>/', eliminar_proveedor, name='eliminar_proveedor'),

    path('', home_view, name="home"),
    path('admin/', admin.site.urls),
    path('ruta/a/la/vista/csrf/', csrf, name='csrf'),
]
