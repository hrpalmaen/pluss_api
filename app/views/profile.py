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
        queryset = User.objects.filter(username=request.data['username'])
        try:
            if not queryset:
                user = User()
                user.first_name = request.data['first_name']
                user.username = request.data['username']
                user.password = request.data['password']
                user.email = request.data['email']
                user.save()
                print('user',user)

                profile = Profile(user=user)
                print('profile', profile)
                profile.code = request.data['code']
                profile.phone_number = request.data['phone_number']
                profile.type_identification = request.data['type_identification']
                profile.identification_number = request.data['identification_number']
                profile.save()

                return Response({'detail': 'El usuario se creo correctamente'}, status=201)
            return Response({'error':"Ya existe un registro con este usuario"}, status=400)
        except Exception as e:
            print('error', e)
            return Response({'error': e}, status=400)
