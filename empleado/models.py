from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from login.models import User


class Empleados(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleados')
    idempleado = models.AutoField(db_column='IdEmpleado', primary_key=True)  # Field name made lowercase.
    # lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=255, blank=True, null=True)  # Field name made
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made
    sexo = models.CharField(max_length=6, choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Hombre')
    direccion = models.CharField(db_column='Direccion', max_length=255, blank=True, null=True)  # Field name made
    # lowercase

    class Meta:
        # managed = False
        db_table = 'Empleados'
