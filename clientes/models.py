from django.db import models


class Clientes(models.Model):
    idcliente = models.AutoField(db_column='IdCliente', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    metodo_de_pago = models.CharField(db_column='Metodo_de_pago', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'clientes'
