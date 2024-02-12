from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models

from login.models import User


class Clientes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clientes', null=True)
    idcliente = models.AutoField(db_column='IdCliente', primary_key=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    metodo_de_pago = models.CharField(db_column='Metodo_de_pago', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'clientes'
