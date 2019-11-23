from rest_framework.serializers import ModelSerializer
from app.models import Product

class ProductSerializer(ModelSerializer):
    '''
    Serializador para productos
    '''
    class Meta:
        model = Product
        fields = ('__all__')