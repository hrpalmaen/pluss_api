from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status 
from app.models import Quotation, Client
from app.serializers import QuotationSerializer, QuotationFilter, getQuotationSerializer

from django.core.mail import send_mail
from django.core.mail import EmailMessage
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication

from django.conf import settings

import pdfkit
import re
from django.http import HttpResponse

class QuotationView(ModelViewSet):
    '''
    Vista de cotizaciones
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
        print('obl_alert: ', obl_alert)
        

        if not data['subject']:
            errors['subject'] = obl_alert
        if not data['message']:
            errors['message'] = obl_alert
        if not data['client']:
            errors['client'] = 'El campo cliente de la cotización es requerido'
        if errors:
            return Response(errors, status=400)

        attachments = []
        try:
            # pdfkit.from_url('https://www.pythoncircle.com/post/711/hello-word-in-django-2-how-to-start-with-django-2/', "prueba.pdf")
            file_attachment = self.pdf(request)
            print('file_attachment: ', file_attachment)
        except Exception as e:
            print('error pdf', e)
        if data['status'] == "Finalizado":

            try:
                current_client = Client.objects.get(id=data['client'])
                print('current_client', current_client)
                email = current_client.email
                validate_email = re.search('^[a-zA-Z0-9.!#$%&*+/=?^_{|}~-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+){1,}$', email)

                if not validate_email:
                    return Response({'error': 'El email asociado al cliente no es válido'})
                    
                try:
                    content = open(file_attachment, 'rb').read() 
                    attachment = (file_attachment, content, 'application/pdf')
                    attachments.append(attachment)
                    print('attachments: ', attachments)
                except Exception as e:
                    print('error pdf', e)

                try:
                    print('email', email)

                    # send_mail(
                    #     subject= 'prueba',
                    #     message='envio de la url de la cotización',
                    #     from_email= settings.EMAIL_HOST_USER,
                    #     recipient_list=[email]
                    # )

                    email = EmailMessage(
                        'prueba con adjunto',
                        'prueba no se que va acá',
                        settings.EMAIL_HOST_USER,
                        [email],
                        attachments=attachments
                    )                   
                    email.send()

                except Exception as e:
                    print('error en send_email', e)
            except Exception as e:
                print('error 1', e)
                return Response({'error': 'Error consultando la informaicón del usuario'})

        return Response({'whasssss': 'siii algo'})

    @action(detail=False, methods=['post'])
    def pdf(self, request, **response_kwargs):
        '''
        Vista para construir pdf
        '''
        print('url: ', request)
        url = request.data

        pdf_settings = {
            'page-size': 'Letter',
            'margin-top': '0.25in',
            'margin-right': '0.25in',
            'margin-bottom': '0.25in',
            'margin-left': '0.25in',
            'encoding': "UTF-8",
            'no-outline': None
        }

        print('entro al pdf')
        pdf = pdfkit.from_url('https://www.pythoncircle.com/post/470/generating-and-returning-pdf-as-response-in-django/', False)#, options=pdf_settings)
        print('pdf: ', pdf)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Cotizacion.pdf'#.format('export')
        return response

