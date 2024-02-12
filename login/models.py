from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    EMPLOYEE = 'employee'
    CLIENT = 'client'
    USER_TYPE_CHOICES = (
        (EMPLOYEE, 'Empleado'),
        (CLIENT, 'Cliente'),
    )

    username = None
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']


