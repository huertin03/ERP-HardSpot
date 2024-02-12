# Generated by Django 5.0.1 on 2024-02-09 17:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('idempleado', models.AutoField(db_column='IdEmpleado', primary_key=True, serialize=False)),
                ('edad', models.IntegerField(blank=True, db_column='Edad', null=True)),
                ('telefono', models.CharField(blank=True, db_column='Telefono', max_length=20, null=True)),
                ('sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Hombre', max_length=6)),
                ('direccion', models.CharField(blank=True, db_column='Direccion', max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Empleados',
            },
        ),
    ]
