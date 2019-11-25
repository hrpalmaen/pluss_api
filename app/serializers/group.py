from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group, Permission

class GroupSerializer(ModelSerializer):
    '''
    Serializador para grupos
    '''
    class Meta:
        model = Group
        fields = ('__all__')