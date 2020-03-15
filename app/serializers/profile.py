from rest_framework.serializers import ModelSerializer, ValidationError
from app.models import Profile
from django.contrib.auth.models import User
from .group import GroupSerializer

class UserSerializer(ModelSerializer):
    '''
    Serializador de usuarios django
    '''
    class Meta:
        model = User
        fields = ('id','password', 'first_name', 'username', 'email', 'groups')

class ProfileSerializer(ModelSerializer):
    '''
    Serializador para el perfil de usuario
    '''
    # user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('code','phone_number','type_identification','identification_number')

class getProfileSerializer(ModelSerializer):
    '''
    Serializador para consultar info usuarios
    '''
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = ('__all__')
