from django.db import models


class Empleados(models.Model):
    idempleado = models.AutoField(db_column='IdEmpleado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=255, blank=True, null=True)  # Field name made
    # lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=20, blank=False, null=False)  # Field name made
    # lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made
    # lowercase.

    class Meta:
        # managed = False
        db_table = 'Empleados'