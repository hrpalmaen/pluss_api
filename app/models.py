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
    group = models.ForeignKey(Group, verbose_name='Tipo de usuario', on_delete=models.CASCADE)

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
    phone = models.CharField('Número telefónico', max_length=30)
    agent = JSONField('Asesor de venta')
    city = models.CharField('Ciudad', max_length=150)

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
    illustration = models.CharField('Imagen', max_length=500)
    name = models.CharField('Nombre del producto', max_length=100)
    detail = models.CharField('Descripción del producto', max_length=500)
    measurements = models.CharField('Medidas', max_length=20)
    color = models.CharField('colores disponibles', max_length=50)
    mark_type = models.CharField('Tipo de marcación', max_length=50)
    material = models.CharField('Material del producto', max_length=50)
    
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
    delivery_time = models.CharField('Tiempo de entrega', max_length=5)
    pay_format = models.CharField('Formato de pago', max_length=10)
    units = JSONField('Unidades a evaluar')
    cost = models.CharField('Costo', max_length=20)
    discount_rate = models.CharField('Porcentaje de descuento', max_length=5)
    mark = JSONField('Marcación')
    profitability_rate = JSONField('Porcentaje de rentabilidad')
    sale_value =  models.CharField('Valor venta', max_length=50)
    transport =  models.CharField('Precio transporte', max_length=20)

    date_created = models.DateTimeField('Fecha creación',auto_now_add=True)
    date_update = models.DateTimeField('Fecha última actualización',auto_now=True)
    is_active = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Cotización'
        db_table = 'cp_quotation'