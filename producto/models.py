from django.db import models


class Productos(models.Model):
    idproducto = models.AutoField(db_column='IdProducto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=10, decimal_places=2, blank=True,
                                 null=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock', blank=True, null=True)  # Field name made lowercase.q

    class Meta:
        db_table = 'productos'


class ProductoStock(models.Model):
    idproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='IdProducto', blank=True, primary_key=True)  # Field name made lowercase.
    cantidadactual = models.IntegerField(db_column='CantidadActual', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'producto_stock'
