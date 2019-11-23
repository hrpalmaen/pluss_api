from rest_framework.serializers import ModelSerializer, ReadOnlyField
from app.models import Profile
from django.contrib.auth.models import User

class ProfileSerializer(ModelSerializer):
    '''
    Serializador para el perfil de usuario
    '''
    class Meta:
        model = Profile
        fields = ('__all__')