import base64
import os
from io import BytesIO
from rest_framework import generics, permissions

from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Image, SimpleDocTemplate, Spacer, Table,
                                TableStyle)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from twilio.rest import Client
from django.conf import settings

from .models import (FullCargo, FullContainer, LooseCargo, LooseContainer,
                     Product)
from .serializers import (FullCargoSerializer, FullContainerSerializer,
                          LooseCargoSerializer, LooseContainerSerializer,
                          ProductSerializer)


class RecentCargosView(APIView):
    def get(self, request):
        try:
            action = request.query_params.get('action', None)

            if action == 'recently_received':
                cargos = LooseCargo.objects.filter(status='RC').order_by('-id')[:10] 
            elif action == 'recently_sent':
                cargos = LooseCargo.objects.filter(status='DC').order_by('-id')[:10] 
            else:
                return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = LooseCargoSerializer(cargos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UnloadedCargoView(APIView):
    def get(self, request):
        try:
            cargotype = request.query_params.get('action', None)
            if cargotype == 'Full':
                cargos = FullCargo.objects.filter(container=None).order_by('-id')
                serializer = FullCargoSerializer(cargos, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif cargotype == 'Loose':
                cargos = LooseCargo.objects.filter(container=None).order_by('-id')
                serializer = LooseCargoSerializer(cargos, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CargosListView(APIView):
    def get(self, request):
        try:    
            cargotype = request.query_params.get('action', None)
            if cargotype == 'Full':
                cargos = FullCargo.objects.all().order_by('-id')
                serializer = FullCargoSerializer(cargos, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif cargotype == 'Loose':
                cargos = LooseCargo.objects.all().order_by('-id')
                serializer = LooseCargoSerializer(cargos, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContainersListView(APIView):
    def get(self, request):
        try:    
            containertype = request.query_params.get('action', None)
            if containertype == 'Full':
                containers = FullContainer.objects.all().order_by('-id')
                serializer = FullContainerSerializer(containers, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif containertype == 'Loose':
                containers = LooseContainer.objects.all().order_by('-id')
                serializer = LooseContainerSerializer(containers, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid action'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LooseContainerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = LooseContainer.objects.all()
    serializer_class = LooseContainerSerializer
    permission_classes = (permissions.AllowAny, )


class FullContainerRetrieveAPIView(generics.RetrieveAPIView):
    queryset = FullContainer.objects.all()
    serializer_class = FullContainerSerializer
    permission_classes = (permissions.AllowAny, )

class ProductStockListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(has_stock=True)
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )



class GenerateInvoiceView(APIView):
    def get(self, request, invoice_number):
        try:
            # Retrieve the LooseCargo instance based on the invoice number
            cargo = LooseCargo.objects.get(invoice_number=invoice_number)
            
            # Retrieve the associated products
            products = cargo.products.all()

            # Register the Chinese font
            chinese_font_path = os.path.join(settings.STATICFILES_DIRS[0], 'fonts/boxicons.ttf')
            pdfmetrics.registerFont(TTFont('boxicons', chinese_font_path))

            # Create a buffer to store the PDF
            buffer = BytesIO()

            # Set up the PDF document
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            # Add the logo and company details
            logo = Image("invoice.png")
            logo.drawWidth = 500
            logo.drawHeight = 225
            elements.append(logo)

            # Retrieve the default styles after registering the Chinese font
            styles = getSampleStyleSheet()
            normal_style = styles["Normal"]
            
            # Create the table for product details
            table_data = [
                ["Name", "CBM", "Weight", "Quantity", "CBM Cost"],
            ]
            for product in products:
                row = [
                    product.name,
                    str(product.cbm),
                    str(product.weight),
                    str(product.qty),
                    # str(product.price),
                    str(product.cbm_cost),
                ]
                table_data.append(row)

            row = ["TOTAL", str(cargo.cbms), str(cargo.weight), str(cargo.ctns), str(cargo.cost)]
            table_data.append(row)
            table = Table(table_data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.green),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
                ('TEXTCOLOR', (0, -1), (-1, -1), colors.black),
                ('FONTSIZE', (0, -1), (-1, -1), 12),
                ('LINEBELOW', (0, -2), (-1, -1), 1, colors.green),  # Hide grid lines
            ]))

            elements.append(table)
            elements.append(Spacer(1, 20))  # Add some space

            # add the bottom footer
            footer = Image("invoice_footer.png")
            footer.drawWidth = 400
            footer.drawHeight = 100

            # Add the footer table to the elements
            elements.append(Spacer(1, 20))  # Add some space
            elements.append(footer)

            # Build the PDF document
            doc.build(elements)

            # Seek to the beginning of the buffer
            buffer.seek(0)

            # Check if the user wants to download or share the PDF
            action = request.query_params.get('action')

            if action == 'share':
                # Return the PDF file as a response without attachment disposition
                response = HttpResponse(buffer, content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
            
            elif action == 'send_to_whatsapp':
                # Initialize the Twilio client
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

                # Specify the recipient's phone number (cargo.phonenumber)
                recipient_phone_number = cargo.receiver.telephone

                # Create a buffer to store the PDF
                buffer = BytesIO()

                # Save the generated PDF to the buffer
                doc.build(elements)
                buffer.seek(0)

                # Send the PDF via WhatsApp using Twilio
                try:
                    message = client.messages.create(
                        body="Here is your invoice",
                        from_=settings.TWILIO_WHATSAPP_NUMBER,
                        to=f'whatsapp:{recipient_phone_number}'
                    )

                    # Send the PDF as a media attachment
                    message.media_url = "data:application/pdf;base64," + base64.b64encode(buffer.read()).decode()
                    message.save()

                    # Return a success message
                    success_message = "Invoice sent via WhatsApp successfully."
                    return HttpResponse(success_message)
                except Exception as e:
                    error_message = f"Error sending invoice via WhatsApp: {str(e)}"
                    return HttpResponse(error_message, status=500)
            else:
                # Return the PDF file as a download response
                response = HttpResponse(buffer, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename={invoice_number}.pdf'

            # Return the response with a success message
            success_message = "Successfully generated the invoice."
            response['X-Invoice-Status'] = success_message

            return response

        except LooseCargo.DoesNotExist:
            return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


