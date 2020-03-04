from rest_framework.serializers import ModelSerializer


class GeneralSerializer(ModelSerializer):    
    def __init__(self, Model):
        '''
        Serializador generico
        '''
        self.Model = Model
    class Meta:
        def __init__(self):
        #     self.Model = Model
        #     self.fields = ('__all__')
            self.set_params()
        
        def set_params(self):
            model = self.Model
            fields = ('__all__')
    