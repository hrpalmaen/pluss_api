from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group

from django.contrib.auth import get_user_model
from app.models import Profile
from app.serializers import ProfileSerializer, UserSerializer, getProfileSerializer
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
    # serializer_class = ProfileSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return getProfileSerializer
        return ProfileSerializer

    def create(self, request):
        print('request: ', request.data)
        '''
        Vista para crear usuarios
        '''

        serializer = ProfileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        try:
            group = Group.objects.get(id=request.data['groups'])

            # user, create = User.objects.get_or_create(username=request.data['username'])
            if create:
                print('lo creo')
            else:
                print('entro por el else')
            return Response({'error':"No se guardo al información complementaria del usuario."}, status=401)
        except Exception as err:
            print('err: ', err)
            return Response({'error': 'No se encontró el grupo ingresado.'})
        # try:
        #     if not queryset:
        #         try:
        #             # groups = Group
        #             try:
        #                 # user = User.objects.create_user(
        #                 #     username=request.data['username'],
        #                 #     email=request.data['username'],
        #                 #     password=request.data['password'],
        #                 #     first_name=request.data['first_name']
        #                 #     )
        #                 # user.save()
        #                 # group.user_set.add(user.id)
        #             # user = User()
        #             # user.first_name = request.data['first_name']
        #             # user.username = request.data['username']
        #             # user.password = request.data['password']
        #             # user.email = request.data['username']
        #             # user.save()
        #             except:
        #                 return Response({'error':''}, status=400)
        #         except Exception as e:
        #             print('error en userrrr: ', e)
        #             return Response({'error':"No se pudo crear el usuario, por favor vuelva a intentarlo."}, status=400)
        #         # user = User.objects.create(request.data)

        #         try:
        #             profile = Profile(user=user)
        #             profile.code = request.data['code']
        #             profile.phone_number = request.data['phone_number']
        #             profile.type_identification = request.data['type_identification']
        #             profile.identification_number = request.data['identification_number']
        #             profile.save()
        #         except:
        #             return Response({'error':"No se guardo al información complementaria del usuario."}, status=400)

        #         return Response({'detail': 'El usuario se creo correctamente'}, status=201)
        #     return Response({'error':"Ya existe un registro con este usuario"}, status=400)
        # except Exception as e:
        #     return Response({'error': e}, status=400)
