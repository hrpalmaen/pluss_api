from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from app.models import Profile
# from django.contrib import User
from django.contrib.auth import authenticate
from app.serializers import UserSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from django.http import JsonResponse
from django.core.serializers import serialize

class LoginView(ModelViewSet):
    '''
    Vista de autenticación
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
        
        user = User.objects.filter(username=username, password=password).values()
        # dddddd = ProfileSerializer(instance=list(Profile.objects.filter(user__username=username, user__password=password)), many=True).data
        # user.username = user
        print('user',user[0])
        if user:
            # return Response({'detail': user}, status=200)
            return JsonResponse(list(user), safe=False)
        else:
            return Response({'detail': 'El usuario no se encuentra registrado.'}, status=status.HTTP_401_UNAUTHORIZED)