from rest_framework.serializers import ModelSerializer
from app.serializers import ClientSerializer, UserSerializer
from app.models import Quotation, QuotationTemp

class QuotationSerializer(ModelSerializer):
    '''
    Serializador para cotizaciones
    '''
    class Meta:
        model = Quotation
        fields = ('__all__')

class getQuotationSerializer(QuotationSerializer):
    '''
    Serializador para cotizaciones
    '''
    client = ClientSerializer()
    user = UserSerializer()

class QuotationTempSerializer(ModelSerializer):
    '''
    Serializador para cotizaciones temporales
    '''
    class Meta:
        model = QuotationTemp
        fields = ('__all__')