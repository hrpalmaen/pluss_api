from rest_framework.viewsets import ModelViewSet
from app.models import Quotation
from app.serializers import QuotationSerializer

class QuotationView(ModelViewSet):
    '''
    Vista de corizaciones
    '''
    queryset = Quotation.objects.all()
    serializer_class = QuotationSerializer