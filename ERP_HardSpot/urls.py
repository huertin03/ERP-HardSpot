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

from ERP_HardSpot import settings
from login.views import login_view, register_view, empleado_contrasegna_view
from empleado.views import lista_empleados_view, empleado_view, modificar_empleado_view
from login.views import home_view


urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('empleado/', empleado_view, name="empleado"),
    path('empleadoContraseña/', empleado_contrasegna_view, name="empleadoContraseña"),
    path('listaEmpleados/', lista_empleados_view, name="listaEmpleados"),
    path('listaEmpleados/<int:idempleado>/', modificar_empleado_view, name="modificar_empleado"),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', home_view, name="home"),
    path('admin/', admin.site.urls),
]
