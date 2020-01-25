from rest_framework.viewsets import ModelViewSet
from app.models import Product
from app.serializers import ProductSerializer, ProductFilter
from django_filters import rest_framework as filters

class ProductView(ModelViewSet):
    '''
    Vista de productos
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's MySQL backend.)
    # '$' Regex search.
