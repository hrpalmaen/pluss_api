'''
Archivo para vistas de autentición
'''
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from app.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password


class LoginView(ModelViewSet):
    '''
    Vista de autenticación
    '''
    queryset = User.objects.all()    
    def create(self, request):
        ''' Módulo de logueo
        ''' 

        username = request.data['username']
        password = request.data['password']

        # serializer = UserSerializer(data=request.data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        errors = {}
        if username == '' or username is None:
            errors['username'] = ['El correo electrónico es obligatorio.']
        if password == '' or password is None:
            errors['password'] = ['La contraseña es obligatoria.']
        if len(errors) > 0:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
            
        '''
        Search data user with permissions
        '''
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                permissions = user.groups.all()
                # user_permissions = [0].name if permissions else [] #user.get_all_permissions()#
                return Response({'name': user.first_name, 'permission': permissions[0].name}, status=200)
            else:
                return Response({'detail': 'El usuario o la clave no son correctas.', status:status.HTTP_401_UNAUTHORIZED})
        except:
            return Response({'detail': 'El usuario no se encuentra registrado.'}, status=status.HTTP_401_UNAUTHORIZED)
