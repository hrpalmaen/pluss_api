from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from app.models import Profile
from app.serializers import ProfileSerializer, UserSerializer
from rest_framework.response import Response

from django.core.serializers import serialize
import json
from django.core.serializers.json import DjangoJSONEncoder


User = get_user_model()

class UserView(ModelViewSet):
    '''
    Vista de usuarios
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(ModelViewSet):
    '''
    Vista de perfil de usuarios
    '''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request):
        print('entro acá', request.data)
        queryset = User.objects.filter(username=request.data['username'])
        try:
            if not queryset:
                print('queryset', queryset)
                user = User()
                user.first_name = request.data['first_name']
                user.username = request.data['username']
                user.password = request.data['identification_number']
                user.email = request.data['username']
                user.save()

                profile = Profile(user=user)
                print('profile', profile)
                profile.code = request.data['code']
                profile.phone_number = request.data['phone_number']
                profile.type_identification = request.data['type_identification']
                profile.identification_number = request.data['identification_number']
                print('profileprofile', profile)
                profile.save()
                print('profile', profile)

                return Response({'detail': 'El usuario se creo correctamente'})
            return Response({'error':"Ya existe un registro con este usuario"})
        except Exception as e:
            return Response({'error': 'Hubo un problema guardando el usuario'})
