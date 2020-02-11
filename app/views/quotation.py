from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from app.models import Quotation, QuotationTemp
from app.serializers import QuotationSerializer, QuotationFilter, getQuotationSerializer

class QuotationView(ModelViewSet):
    '''
    Vista de corizaciones
    '''
    queryset = Quotation.objects.all()
    # serializer_class = QuotationSerializer
    # filter_class = QuotationFilter

    # def list(self, request):
    #     self.serializer_class = getQuotationSerializer
    #     return super().list(request)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return getQuotationSerializer
        return QuotationSerializer

    # @action(detail=False, methods=['post'])
    # def duplicate(self, request):
    #     print('request: ', request.data)
    #     # self.serializer_class = 
    #     aaa = getQuotationSerializer(request.data)

    #     return super().create(aaa)
        # return Response({'whasssss': 'siii algo'})


    #     print('request: ', request.data)
    #     try: 
    #         serializer = getQuotationSerializer(data=request.data)
    #         print('serializer: ', serializer)
    #     except Exception as eeeeee:
    #         print('eeeeeee', eeeeee)
       
    #     try: 
    #         if serializer.is_valid():
    #             qq = Quotation(serializer)
    #             qq.save()
    #             print('serializer: ', qq)
    #     except Exception as e:
    #         print('errorssss', e)
    #     return Response({'whasssss': 'siii algo'})
