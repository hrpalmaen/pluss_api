from rest_framework.viewsets import ModelViewSet
from app.models import Profile
from app.serializers import ProfileSerializer

class ProfileView(ModelViewSet):
    '''
    Vista de perfil de usuarios
    '''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer