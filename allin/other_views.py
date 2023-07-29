import os
import threading
from io import BytesIO

import openpyxl
import pdfkit
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import TemplateView
from openpyxl.styles import Alignment
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Image, KeepTogether, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

from .models import FullContainer, LooseCargo, LooseContainer
from .utility import generate_fullco_excel_file, generate_looseco_excel_file


class Homepage(TemplateView):
    template_name = 'homepage.html'


class AboutPage(TemplateView):
    template_name = 'pilety/about.html'


class ContactPage(TemplateView):
    template_name = 'pilety/contact.html'



class PolicyPage(TemplateView):
    template_name = 'pilety/privacy-policy.html'


class ServicesPage(TemplateView):
    template_name = 'pilety/request-quote.html'


class TeamPage(TemplateView):
    template_name = 'pilety/team.html'


class TermsPage(TemplateView):
    template_name = 'pilety/terms-conditions.html'


class WhyUsPage(TemplateView):
    template_name = 'pilety/why-us-choose.html'


class PriceLiftPage(TemplateView):
    template_name = 'pilety/price_list.html'





def generate_invoice(request, invoice_number):
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
            str(product.qty * product.cbm_cost),
        ]
        table_data.append(row)

    row = ["TOTAL", str(cargo.cbms), str(cargo.weight), str(cargo.ctns),str(cargo.cost),]
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

    # # Create the first grid for Address 1
    # address1_content = [
    #     Paragraph("USHIRIKA BUILDING 8TH FLOOR,P.O.BOX 77592, Dar es salaam, Tanzania", normal_style),
    # ]
    # address1_table = Table([address1_content])

    # # Create the second grid for the image
    # image_table = Table([[Image("firstvision.png", width=2*inch, height=0.5*inch)]])

    # # Create the third grid for Address 2
    # address2_content = [
    #     Paragraph("Nyerere Road, Seif Plaza,Ghorofa ya nne (4), Mwanza", normal_style),
    # ]
    # address2_table = Table([address2_content])

    # # Combine the three tables side by side in the footer
    # footer_table = Table([
    #     [address1_table, Spacer(0, 0, True), image_table, Spacer(0, 0, True), address2_table],
    # ], colWidths=[2*inch, 0.5*inch, 2*inch, 0.5*inch, 2*inch])

    # # Set up the table style (hide grid lines)
    # footer_table.setStyle(TableStyle([
    #     ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    #     ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    #     ('LINEBELOW', (0, 0), (-1, -1), 1, colors.white),  # Hide grid lines
    # ]))



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

    # Return the PDF file as a download response
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={invoice_number}.pdf'

    # Return the response with success message
    success_message = "Successfully generated the invoice."
    response['X-Invoice-Status'] = success_message

    return response


class InvoiceGeneratorView(View):
    def get(self, request, invoice_number):
        # Retrieve the LooseCargo instance based on the invoice number
        cargo = LooseCargo.objects.get(invoice_number=invoice_number)
        products = cargo.products.all()

        # Render the HTML template to a string
        html = render_to_string('allin/loose/invoice.html', {'cargo': cargo, 'products':products})

        # Define the PDF file path with the invoice number in the filename
        pdf_file_path = os.path.join(settings.MEDIA_ROOT, f'{invoice_number}.pdf')

        # Generate the PDF
        pdfkit.from_string(html, pdf_file_path)

        # Define the function to delete the PDF after 10 minutes
        def delete_pdf():
            os.remove(pdf_file_path)

        # Schedule the PDF deletion after 10 minutes
        timer = threading.Timer(600, delete_pdf)
        timer.start()

        # Return the download link for the generated PDF
        download_link = f'<a href="{pdf_file_path}">Download Invoice</a>'
        return HttpResponse(download_link)






def generate_fullco_packing_list(request, container_id):
    container = get_object_or_404(FullContainer, id=container_id)
    products = container.cargos.values_list(
        "products__recieved", "products__name",
        "products__chinese", "products__qty", "products__f_cargo__mark", 
        "products__packaging", "products__units", "products__price",
        "products__ttprice", "products__cbm", "products__cbms", "products__wght",
        "products__weight", 
        "products__item_number"
    )

    # Generate the Excel file
    wb = generate_fullco_excel_file(products, container)

    # Create a response with the Excel file
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=PackingList_{container_id}.xlsx"
    wb.save(response)

    return response



def generate_looseco_packing_list(request, container_id):
    container = get_object_or_404(LooseContainer, id=container_id)
    products = container.cargos.values_list(
        "products__recieved", "products__name",
        "products__chinese", "products__qty", "products__l_cargo__mark", 
        "products__packaging", "products__units", "products__price",
        "products__ttprice", "products__cbm", "products__cbms", "products__wght",
        "products__weight", 
        "products__item_number", "products__l_cargo__reciever__telephone"
    )

    # Generate the Excel file
    wb = generate_looseco_excel_file(products, container)

    # Create a response with the Excel file
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=PackingList_{container_id}.xlsx"
    wb.save(response)

    return response
