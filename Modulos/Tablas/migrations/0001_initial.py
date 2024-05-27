# Generated by Django 5.0.2 on 2024-02-23 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('codAdmin', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=20)),
                ('contraseña', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('codInstalacion', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_instalacion', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('Identificacion', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=20)),
                ('cargo', models.CharField(max_length=20)),
                ('fecha_registro', models.DateField(null=True)),
                ('archivo', models.FileField(null=True, upload_to='archivos/')),
                ('codadmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tablas.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('codBitacora', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('estado', models.CharField(max_length=15)),
                ('cantidad', models.CharField(max_length=10)),
                ('observaciones', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=40)),
                ('nivel_riesgo', models.CharField(max_length=40)),
                ('fecha_registro', models.DateField(null=True)),
                ('codInstalacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tablas.instalacion')),
            ],
        ),
    ]
