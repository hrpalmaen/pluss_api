from rest_framework.serializers import ModelSerializer, ValidationError
from app.models import Profile
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    '''
    Serializador de usuarios django
    '''
    class Meta:
        model = User
        fields = ('password', 'first_name', 'username', 'email')

class ProfileSerializer(ModelSerializer):
    '''
    Serializador para el perfil de usuario
    '''
    # def create(self, validated_data):
    #     groups_data = validated_data.pop('groups')
    #     print('groups_data: ', groups_data)
    #     try:
    #         queryset = User.objects.filter(username=validated_data['username'])
    #         user = User.objects.create_user(**validated_data)
    #         user.groups.set(groups_data)
    #         print('user serializer: ', validated_data)

    #         try:
    #             Profile.objects.create(user=user, code=validated_data['code'], phone_number=validated_data['phone_number'], type_identification=validated_data['type_identification'],
    #             identification_number=validated_data['identification_number'])
    #             # profile.code = validated_data['code']
    #             # profile.phone_number = validated_data['phone_number']
    #             # profile.type_identification = validated_data['type_identification']
    #             # profile.identification_number = validated_data['identification_number']
    #             # profile.save()
    #             return user
    #         except Exception as ese:
    #             print('ese tan raro: ', ese)
    #             raise ValidationError(ese)
    #     except Exception as yaaaa:
    #         raise ValidationError(yaaaa)
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('user','code','phone_number','type_identification','identification_number')
    
    # def create(self, validated_data):
    #     print('validated_data: ', validated_data)
    #     if UserSerializer.isvalid() :
    #         UserSerializer.save()
    #     else:
    #         raise ValidationError('entro pero no puedo')
    #     return super().create()
    

class getProfileSerializer(ModelSerializer):
    '''
    Serializador para consultar info usuarios
    '''
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('__all__')

# class ProfileSerializer(ModelSerializer):
#     '''
#     Serializador para el perfil de usuario
#     '''
#     profile=ProfileSerializerss()

#     class Meta:
#         model = User
#         fields = ('password', 'username', 'first_name', 'groups','profile')

#     # def create(self):
#     #     if ProfileSerializerss.isvalid() :

#     #     print('validated_data', validated_data)