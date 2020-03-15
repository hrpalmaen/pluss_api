'''
Archivo de vistas de usuarios
'''
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
        '''
        Vista para crear usuarios
        '''
        #Validate data with serializer
        serializer = ProfileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        try:
            #Search user current
            user_current = Profile.objects.get(user__username=request.data['username'])
            return Response({'error': 'El usuario ya se encuentra creado en el aplicativo.'}, status=400)
        except:            
            try:
                #Validate correct group
                group = Group.objects.get(id=request.data['groups'])
                try:
                    #Save user in modalnative django
                    user = User.objects.create_user(
                        username = request.data['username'],
                        password = request.data['password'],
                        first_name = request.data['first_name'],
                        email = request.data['username'],
                        is_active = True
                        )
                    group.user_set.add(user.id)
                    try:
                        #Save info complementary in model profile
                        profile = Profile.objects.create(
                            user = user,
                            code = request.data['code'],
                            phone_number = request.data['phone_number'],
                            type_identification = request.data['type_identification'],
                            identification_number = request.data['identification_number']
                        )
                        return Response({
                            'id':profile.id,
                            'user':{
                                'id': user.id,
                                'first_name':user.first_name, 
                                'username':user.username,
                                'groups': group.id
                                }, 
                            'code':profile.code, 
                            'identification_number':profile.identification_number, 
                            'phone_number':profile.phone_number
                            }, status=200)
                    except:
                        return Response({'error': 'No se pudo crear el usuario, vuelva a intentarlo.'}, status=400)
                except:
                    return Response({'error': 'No se puso guardar el usuario.'}, status=400)
            except :
                return Response({'error': 'No se encontró el tipo de usuario seleccionado. Contacte al administrador.'}, status=400)

    def update(sefl, request, pk=None):
        '''
        Vista para actualizar usuario
        '''
        # serializer = ProfileSerializer(data=request.data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=400)

        try:
            profile = Profile.objects.get(id=pk)

            profile.code = request.data['code']
            profile.identification_number = request.data['identification_number']
            profile.phone_number = request.data['phone_number']
            profile.type_identification = request.data['type_identification']
            # for value in request.data:
            #     setattr(profile, value, request.data[str(value)])
            profile.save()
            try:
                group = Group.objects.get(id=request.data['groups'])

                try:
                    user = User.objects.get(id=profile.user_id)
                    # for value in request.data:
                    #     setattr(user, value, request.data[str(value)])
                    user.first_name = request.data['first_name']
                    user.username = request.data['username']
                    # user.password = request.data['password']
                    user.save()

                    #validate groups user for save new
                    group_current = user.groups.all()[0]
                    if group_current.name != group:
                        user.groups.clear()
                        group.user_set.add(user.id)
                    return Response({
                        'id': profile.id,
                        'code': profile.code,
                        'user':{
                            'id': user.id,
                            'first_name': user.first_name,
                            'username': user.username,
                            'groups': group.id
                        },
                        'identification_number': profile.identification_number,
                        'phone_number': profile.phone_number},
                        status=200)
                except:
                    return Response({'Se presento problemas actualizando el usuario.'}, status=400)

            except:
                return Response({'error': 'No se encontró el tipo de usuario seleccionado. Contacte al administrador.'})

        except:
            return Response({'error': 'No se pudo consultar la información del usuario'})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    