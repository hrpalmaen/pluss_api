from rest_framework.serializers import ModelSerializer
import django_filters

from app.models import Product

class ProductSerializer(ModelSerializer):
    '''
    Serializador para productos
    '''
    class Meta:
        model = Product
        fields = ('__all__')

class ProductFilter(django_filters.FilterSet):
    '''
    Filtro para productos
    '''
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = [
            'referency_id',
            'provier_name',
            'name'
            ]
