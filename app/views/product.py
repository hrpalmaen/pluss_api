from rest_framework.viewsets import ModelViewSet
from app.models import Product
from app.serializers import ProductSerializer

class ProductView(ModelViewSet):
    '''
    Vista de productos
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer