from rest_framework.viewsets import ModelViewSet
from app.models import Quotation, QuotationTemp
from app.serializers import QuotationSerializer, getQuotationSerializer, QuotationTempSerializer

class QuotationView(ModelViewSet):
    '''
    Vista de corizaciones
    '''
    queryset = Quotation.objects.all()
    # serializer_class = QuotationSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return getQuotationSerializer
        return QuotationSerializer

class QuotationTempView(ModelViewSet):
    '''
    Vista de corizaciones
    '''
    queryset = QuotationTemp.objects.all().order_by('-id')
    serializer_class = QuotationTempSerializer