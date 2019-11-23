from rest_framework.serializers import ModelSerializer, ReadOnlyField
from app.models import Client

class ClientSerializer(ModelSerializer):
    '''
    Serializador para el perfil de usuario
    '''
    class Meta:
        model = Client
        fields = ('__all__')