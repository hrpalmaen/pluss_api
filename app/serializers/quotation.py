# from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers
from app.serializers import ClientSerializer, UserSerializer
from app.models import Quotation
import django_filters

class QuotationSerializer(serializers.ModelSerializer):
    '''
    Serializador para cotizaciones
    '''
    client_name = serializers.CharField(source='client.name', read_only = True)
    user_name = serializers.CharField(source='user.first_name', read_only = True)
    class Meta:
        model = Quotation
        fields = (
            'id',
            'client',
            'client_name',
            'user',
            'user_name',
            'delivery_time',
            'pay_format',
            'units',
            'status',
            'products',
            'date_created'
        )

class getQuotationSerializer(QuotationSerializer):
    '''
    Serializador para cotizaciones
    '''
    client = ClientSerializer()
    user = UserSerializer()


class QuotationFilter(django_filters.FilterSet):
    '''
    Filtros para cotizaciones
    '''

    class Meta:
        model = Quotation
        fields = {
            'id': ['exact']
        }