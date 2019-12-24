from rest_framework.viewsets import ModelViewSet
from app.models import Quotation, QuotationTemp
from app.serializers import QuotationSerializer, QuotationTempSerializer

class QuotationView(ModelViewSet):
    '''
    Vista de corizaciones
    '''
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer

class QuotationTempView(ModelViewSet):
    '''
    Vista de corizaciones
    '''
    queryset = QuotationTemp.objects.all().order_by('-id')
    serializer_class = QuotationTempSerializer