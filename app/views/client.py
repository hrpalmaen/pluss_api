from rest_framework.viewsets import ModelViewSet
from app.models import Client
from app.serializers import ClientSerializer

class ClientView(ModelViewSet):
    '''
    Vista de clientes
    '''
    queryset = Client.objects.all()
    serializer_class = ClientSerializer