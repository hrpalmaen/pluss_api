from rest_framework.serializers import ModelSerializer, ValidationError
from app.models import Profile
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    '''
    Serializador de usuarios django
    '''
    class Meta:
        model = User
        fields = ('__all__')

class ProfileSerializer(ModelSerializer):
    '''
    Serializador para el perfil de usuario
    '''
    # def create(self, validated_data):
    #     groups_data = validated_data.pop('group')
    #     queryset = User.objects.filter(username__iexact=validated_data['username'])
    #     print('queryset', queryset)
    #     if not queryset:
    #         user = User()
    #         user.first_name = validated_data['first_name']
    #         user.username = validated_data['username']
    #         user.password = validated_data['identification_number']
    #         user.email = validated_data['username']
    #         user.save()

    #         # user = User.objects.create_user(**validated_data)
    #         user.groups.set(groups_data) 
    #         print('user', user)
    #         return user
    #     raise ValidationError("Ya existe un registro igual")

    class Meta:
        model = Profile
        fields = ('__all__')