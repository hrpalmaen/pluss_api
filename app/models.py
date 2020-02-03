from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.postgres.fields import JSONField


class Profile(models.Model):
    '''
    Modelo con información completa de usuarios
    '''
    TYPE_DOCUMENT = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('P', 'Pasaporte')
    ]

    user = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.CASCADE)
    code = models.CharField('Código usuario', max_length=30)
    phone_number = models.CharField('Número telefónico', max_length=30)
    type_identification = models.CharField('Tipo de identificación', choices=TYPE_DOCUMENT, max_length=50)
    identification_number = models.CharField('Documento', max_length=20, unique=True)

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)

    def __str__(self):
        return f'{self.code}'

    class Meta:
        verbose_name = 'Usuarios'
        db_table = 'cp_profile'

class Client(models.Model):
    '''
    Modelo de clientes
    '''
    name = models.CharField('Nombre cliente', max_length=100)
    nit = models.CharField('Nit', max_length=25)
    phone = models.CharField('Número telefónico', max_length=30)
    agent = models.CharField('Asesor de venta', max_length=150)
    city = models.CharField('Ciudad', max_length=150)
    phone_two = models.CharField('Número telefónico alternativo', max_length=30, null=True)
    email = models.CharField('Correo electrónico', max_length=150, null=True)
    address = models.CharField('Número telefónico', max_length=150, null=True)
    dependece = models.CharField('Dependencia o área', max_length=100)

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Clientes'
        db_table = 'cp_client'

class Product(models.Model):
    '''
    Modelo de productos
    '''
    referency_id = models.CharField('Identificador producto', max_length=64, null=True)
    provier_name = models.CharField('Nombre del proveedor', max_length=64, null=True)
    illustration = models.CharField('Imagen', max_length=512, null=True)
    name = models.CharField('Nombre del producto', max_length=128, null=True)
    detail = models.CharField('Descripción del producto', max_length=500, null=True)
    measurements = models.CharField('Medidas', max_length=128, null=True)
    color = models.CharField('colores disponibles', max_length=128, null=True)
    mark_type = models.CharField('Tipo de marcación', max_length=128, null=True)
    material = models.CharField('Material del producto', max_length=128, null=True)
    more_info = JSONField('Información adiccional', default=dict)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Productos'
        db_table = 'cp_product'

class Quotation(models.Model):
    '''
    Modelo de cotizaciones
    '''
    client = models.ForeignKey(Client, verbose_name='cliente', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Ejecutivo de ventas', on_delete=models.CASCADE)
    delivery_time = models.CharField('Tiempo de entrega', max_length=5, null=True)
    pay_format = models.CharField('Formato de pago', max_length=10, null=True)
    units = JSONField('Unidades a evaluar')
    status = models.CharField('Estado cotización', max_length=20)
    products = JSONField('Productos')

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Cotización'
        db_table = 'cp_quotation'

class QuotationTemp(models.Model):
    '''
    Modelo cotizaciones temporales
    '''
    data = JSONField('Info temporal')

    class Meta:
        verbose_name = 'Cotización temporal'
        db_table = 'cp_quotationTemp'