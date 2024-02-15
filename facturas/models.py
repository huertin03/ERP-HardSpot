from django.db import models
from clientes.models import Clientes
from producto.models import Productos


class FacturasCabecera(models.Model):
    idfactura = models.AutoField(db_column='IdFactura', primary_key=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='IdCliente', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    pago = models.DecimalField(db_column='Pago', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    preciototal = models.DecimalField(db_column='PrecioTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'facturas_cabecera'


class FacturasCompuesto(models.Model):
    id = models.BigAutoField(primary_key=True)
    idfactura = models.ForeignKey(FacturasCabecera, models.DO_NOTHING, db_column='IdFactura', blank=True, null=True)
    idproducto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='IdProducto', blank=True, null=True)
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)
    precio = models.DecimalField(db_column='Precio', max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'facturas_compuesto'
        constraints = [
            models.UniqueConstraint(fields=['idfactura', 'idproducto'], name='facturas_compuesto_idfactura_idproducto_key'),
        ]
