from rest_framework.views import APIView
from rest_framework.response import Response
# from app.serializers import GeneralSerializer
import importlib


class GeneralView(APIView):
    '''
    Vista generica
    '''
    Model = None
    Serializer = None
    @classmethod
    def as_view(cls, Model, Serializer, **kwargs):        
        view = super(GeneralView, cls).as_view(Model=Model, Serializer=Serializer,**kwargs)
        view.Model = Model
        view.Serializer = Serializer
        return view

    def get (self, request, format=None):
        queryset = self.Model.objects.all()
        serializer_class = self.Serializer(queryset)
        return Response(serializer_class.data)
    