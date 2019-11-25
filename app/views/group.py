from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Group, Permission
from app.serializers import GroupSerializer

class GroupView(ModelViewSet):
    '''
    Vista de grupos
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer