from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class EmpleadosManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.contrasena = password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Empleados(AbstractBaseUser, PermissionsMixin):
    idempleado = models.AutoField(db_column='IdEmpleado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=255, blank=True, null=True)  # Field name made
    # lowercase.
    password = models.CharField(db_column='password', max_length=255, blank=False, null=False)  # Field name made
    # lowercase.
    edad = models.IntegerField(db_column='Edad', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True, unique=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20, blank=True, null=True)  # Field name made
    # lowercase.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'password']
    objects = EmpleadosManager()

    class Meta:
        # managed = False
        db_table = 'Empleados'
