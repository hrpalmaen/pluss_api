from rest_framework.serializers import ModelSerializer


class GeneralSerializer(ModelSerializer):    
    def __init__(self, Model):
        '''
        Serializador generico
        '''
        print('ENtramos--------------------------------')
        self.Model = Model
    class Meta:
        print('ENtramos--------------2------------------')
        def __init__(self):
        #     self.Model = Model
        #     self.fields = ('__all__')
            self.set_params()
        
        def set_params(self):
            model = self.Model
            fields = ('__all__')
    