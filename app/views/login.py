from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
# from django.contrib import User
from django.contrib.auth import authenticate
from app.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class LoginView(ModelViewSet):
    '''
    Vista de autenticación
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def create(self, request):
    #     username = request.data['username']
    #     password = request.data['password']
    #     print('username', username, password)
    #     user = authenticate(username=username, password=password)
    #     print('user', user)
    #     if user is not None:
    #         print('es')
    #         return Response({'detail': 'Existe'})
    #         # A backend authenticated the credentials
    #     else:
    #         print('no es')
    #         return Response({'detail': 'No existe'}, status=400)
    

    def create(self, request):
        errors = {}
        username = request.data['username']
        password = request.data['password']

        if username == '' or username is None:
            errors['username'] = ['El correo electrónico es obligatorio.']
        if password == '' or password is None:
            errors['password'] = ['La contraseña es obligatoria.']

        if len(errors) > 0:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(username=username, password=password)
        
        if user:
            return Response({'detail': 'Autenticación realizada con éxito'}, status=200)
        else:
            return Response({'detail': 'El usuario no se encuentra registrado.'}, status=status.HTTP_401_UNAUTHORIZED)