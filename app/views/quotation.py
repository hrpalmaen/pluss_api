from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status 
from app.models import Quotation, Client
from app.serializers import QuotationSerializer, QuotationFilter, getQuotationSerializer

from django.core.mail import send_mail
from django.core.mail import EmailMessage
import smtplib
import pdfkit

from django.conf import settings
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
        subject = request.data['subject']
        send_copy = request.data['send_copy']
        body = data['message']
        client = data['client']

        obl_alert =  'Este campo es requerido.'
        errors = {}

        if not subject:
            errors['subject'] = obl_alert
        if not body:
            errors['message'] = obl_alert
        if not client:
            errors['client'] = 'El campo cliente de la cotización es requerido'
        if errors:
            return Response(errors, status=400)
        
        if data['status'] == "Finalizado":
            try:
                current_client = Client.objects.get(id=data['client'])
                email = current_client.email
                validate_email = re.search('^[a-zA-Z0-9.!#$%&*+/=?^_{|}~-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+){1,}$', email)

                if not validate_email:
                    return Response({'error': 'El email asociado al cliente no es válido'}, status=400)

                try:
                    file_attachment = self.build_pdf()
                except Exception as e:
                    return Response({'error': 'Se presento problemas generando el pdf.'}, status=400)

                try:
                    email = EmailMessage(
                        subject,
                        body,
                        settings.EMAIL_HOST_USER,
                        [email],
                        cc = [send_copy]
                    )
                    email.attach('Cotizacion.pdf', file_attachment, 'application/pdf')
                    email.send()
                except Exception as e:
                    return Response({'error': 'No se pudo enviar el mail, por favor intente nuevamente.'}, status=400)

            except Exception as e:
                return Response({'error': 'Error consultando la información del usuario'}, status=400)

        return Response({'sucess': 'Se envió el correo electrónico exitosamente.'}, status=200)


    @action(detail=False, methods=['post'])
    def pdf(self, request, **response_kwargs):
        '''
        Vista para construir pdf
        '''
        url = request.data

        new_pdf = self.build_pdf()
        response = HttpResponse(new_pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Cotizacion.pdf'#.format('export')
        return response


    def build_pdf(self):
        '''
        Función para construir pdf
        '''
        pdf_settings = {
            'page-size': 'Letter',
            'margin-top': '0.25in',
            'margin-right': '0.25in',
            'margin-bottom': '0.25in',
            'margin-left': '0.25in',
            'encoding': "UTF-8",
            'no-outline': None
        }

        pdf = pdfkit.from_url('https://www.pythoncircle.com/post/470/generating-and-returning-pdf-as-response-in-django/', False)#, options=pdf_settings)

        return pdf
