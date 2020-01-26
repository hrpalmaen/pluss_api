from rest_framework.viewsets import ModelViewSet
from app.models import Product
from app.serializers import ProductSerializer, ProductFilter, ProductPagination
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination

class ProductView(ModelViewSet):
    '''
    Vista de productos
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    pagination_class = ProductPagination

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's MySQL backend.)
    # '$' Regex search.
