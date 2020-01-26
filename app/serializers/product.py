from rest_framework.serializers import ModelSerializer
import django_filters
from rest_framework.pagination import PageNumberPagination

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
        
class ProductPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100
