# Generated by Django 2.2.7 on 2020-03-23 16:19

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre cliente')),
                ('nit', models.CharField(max_length=25, verbose_name='Nit')),
                ('phone', models.CharField(max_length=30, verbose_name='Número telefónico')),
                ('agent', models.CharField(max_length=150, verbose_name='Asesor de venta')),
                ('city', models.CharField(max_length=150, verbose_name='Ciudad')),
                ('phone_two', models.CharField(blank=True, max_length=30, null=True, verbose_name='Número telefónico alternativo')),
                ('email', models.CharField(max_length=150, null=True, verbose_name='Correo electrónico')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Número telefónico')),
                ('dependece', models.CharField(max_length=100, verbose_name='Dependencia o área')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Fecha última actualización')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Clientes',
                'db_table': 'cp_client',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referency_id', models.CharField(max_length=64, null=True, verbose_name='Identificador producto')),
                ('cod_product', models.CharField(max_length=64, null=True, verbose_name='Codigo del producto')),
                ('provier_name', models.CharField(max_length=64, null=True, verbose_name='Nombre del proveedor')),
                ('image', models.CharField(max_length=512, null=True, verbose_name='Imagen')),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Nombre del producto')),
                ('description', models.CharField(max_length=512, null=True, verbose_name='Descripción del producto')),
                ('inventory', models.CharField(max_length=64, null=True, verbose_name='Existencia')),
                ('cost', models.FloatField(null=True, verbose_name='Costo de compra')),
                ('detail', models.CharField(max_length=500, null=True, verbose_name='Descripción del producto')),
                ('size', models.CharField(max_length=128, null=True, verbose_name='Medidas')),
                ('colors', models.CharField(max_length=128, null=True, verbose_name='colores disponibles')),
                ('prints', models.CharField(max_length=128, null=True, verbose_name='Tipo de marcación')),
                ('material', models.CharField(max_length=128, null=True, verbose_name='Material del producto')),
                ('more_info', django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='Información adiccional')),
            ],
            options={
                'verbose_name': 'Productos',
                'db_table': 'cp_product',
            },
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_time', models.CharField(max_length=5, null=True, verbose_name='Tiempo de entrega')),
                ('pay_format', models.CharField(max_length=10, null=True, verbose_name='Formato de pago')),
                ('units', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Unidades a evaluar')),
                ('status', models.CharField(max_length=20, verbose_name='Estado cotización')),
                ('products', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Productos')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Fecha última actualización')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Client', verbose_name='cliente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ejecutivo de ventas')),
            ],
            options={
                'verbose_name': 'Cotización',
                'db_table': 'cp_quotation',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, null=True, verbose_name='Código usuario')),
                ('phone_number', models.CharField(max_length=30, null=True, verbose_name='Número telefónico')),
                ('type_identification', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería'), ('P', 'Pasaporte')], max_length=50, verbose_name='Tipo de identificación')),
                ('identification_number', models.CharField(max_length=20, unique=True, verbose_name='Documento')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Fecha última actualización')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Usuarios',
                'db_table': 'cp_profile',
            },
        ),
    ]
