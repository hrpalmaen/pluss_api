from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    '''
    Serializador de usuarios django
    '''
    class Meta:
        model = User
        fields = ('__all__')