from rest_framework.serializers import ModelSerializer
from app.models import Quotation

class QuotationSerializer(ModelSerializer):
    '''
    Serializador para cotizaciones
    '''
    class Meta:
        model = Quotation
        fields = ('__all__')