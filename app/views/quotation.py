from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status 
from app.models import Quotation, Client
from app.serializers import QuotationSerializer, QuotationFilter, getQuotationSerializer

from django.core.mail import send_mail
import re

class QuotationView(ModelViewSet):
    '''
    Vista de corizaciones
    '''
    queryset = Quotation.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return getQuotationSerializer
        return QuotationSerializer

    @action(detail=False, methods=['post'])
    def send_email(self, request):
        '''
        Vista para envio de email a cliente
        '''
        data = request.data
        errors = {}
        obl_alert =  'Este campo es requerido'

        if not data['subject']:
            print('entro al subject')
            errors['subject'] = obl_alert
        if not data['message']:
            errors['message'] = obl_alert
        if not data['client']:
            errors['client'] = 'El campo cliente de la cotización es requerido'
        if errors:
            return Response(errors, status=400)


        if data['status'] == "Finalizado":
            try:
                current_client = Client.objects.get(id=data['client'])
                print('current_client', current_client)
                email = current_client.email
                validate_email = re.search('^[a-zA-Z0-9.!#$%&*+/=?^_{|}~-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+){1,}$', email)

                if not validate_email:
                    return Response({'error': 'El email asociado al cliente no es válido'})

                try:
                    print('email', email)
                    send_mail(
                        subject= 'prueba',
                        message='envio de la url de la cotización',
                        from_email= 'ccdelgadop@gmail.com',
                        recipient_list=[email]
                    )
                except Exception as e:
                    print('error en send_email', e)
            except Exception as e:
                return Response({'error': 'Error consultando la informaicón del usuario'})



        return Response({'whasssss': 'siii algo'})

    @action(detail=False, methods=['post'])
    def pdf(self, request,**response_kwargs):
        content_type='application/xml'
        '''
        Vista para construir pdf
        '''
        print('selffffffffffffffffffffffff', self)
        dat= request
        print(str(request.data))

        return Response({'queeeeeee': 'llego'})
