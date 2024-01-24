from django.db import models


class Productos(models.Model):
    idproducto = models.AutoField(db_column='IdProducto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=10, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'productos'
