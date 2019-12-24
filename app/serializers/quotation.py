from rest_framework.serializers import ModelSerializer
from app.models import Quotation, QuotationTemp

class QuotationSerializer(ModelSerializer):
    '''
    Serializador para cotizaciones
    '''
    class Meta:
        model = Quotation
        fields = ('__all__')

class QuotationTempSerializer(ModelSerializer):
    '''
    Serializador para cotizaciones temporales
    '''
    class Meta:
        model = QuotationTemp
        fields = ('__all__')