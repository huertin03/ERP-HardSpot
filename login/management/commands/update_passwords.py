from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from login.models import Empleados


class Command(BaseCommand):
    help = 'Update existing passwords to use hash instead of plain text'

    def handle(self, *args, **options):
        empleados = Empleados.objects.all()

        for empleado in empleados:
            empleado.contrasena = make_password(empleado.contrasena)
            empleado.save()

        self.stdout.write(self.style.SUCCESS('Passwords successfully updated'))
