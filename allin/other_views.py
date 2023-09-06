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
from django.shortcuts import render, redirect

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
    template_name = 'allin/pilety/about.html'


class ContactPage(TemplateView):
    template_name = 'allin/pilety/contact.html'



class PolicyPage(TemplateView):
    template_name = 'allin/pilety/privacy-policy.html'


class ServicesPage(TemplateView):
    template_name = 'allin/pilety/services.html'


class TeamPage(TemplateView):
    template_name = 'allin/pilety/team.html'


class TermsPage(TemplateView):
    template_name = 'allin/pilety/terms-conditions.html'


class WhyUsPage(TemplateView):
    template_name = 'allin/pilety/why-us-choose.html'


class PriceLiftPage(TemplateView):
    template_name = 'allin/pilety/price_list.html'





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
            str(product.cbm_cost),
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
    action = request.GET.get('action')

    if action == 'share':
        # Return the PDF file as a response without attachment disposition
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
    else:
        # Return the PDF file as a download response
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={invoice_number}.pdf'

    # Return the response with success message
    success_message = "Successfully generated the invoice."
    response['X-Invoice-Status'] = success_message


    # # Return the PDF file as a download response
    # response = HttpResponse(buffer, content_type='application/pdf')
    # response['Content-Disposition'] = f'attachment; filename={invoice_number}.pdf'

    # # Return the response with success message
    # success_message = "Successfully generated the invoice."
    # response['X-Invoice-Status'] = success_message

    return response

def share_invoice(request, invoice_number):
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


    # Create a response with PDF content
    share_response = HttpResponse(buffer, content_type='application/pdf')
    share_response['Content-Disposition'] = f'inline; filename="{invoice_number}.pdf"'

    return share_response


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


def update_invoice_number(request, pk):
    '''This function takes a container and changes the cargo invoice number 
    and increments it by increasing order'''
    if request.user.is_staff:
        if request.method == 'POST':
            invoice_number = int(request.POST['initial_invoice_number'])
            
            container = LooseContainer.objects.get(id = pk)
            container_cargos = container.cargos.all()
            for cargo in container_cargos:
                cargo.invoice_number = invoice_number + 0
                cargo.save()
                invoice_number += 1
            container.is_modified = True
            container.save()
            return redirect('allin:l_container', container.id)
        
    else:
        return redirect('allin:error_handler')
        
        # else:    #it should returfn a message that its not a post message

        #     return redirect('allin:l_container', container.id)


# def update_cost_per_cbm():
#     '''setting the price per cbm for a specific goods in a specific cargo'''
#     cargo = LooseCargo.objects.get()

def track_cargo(request, tracking_number):
    # Retrieve the LooseCargo instance based on the invoice number
    
    if request.user.is_authenticated:
        cargo = LooseCargo.objects.get(invoice_number=tracking_number)
        # Retrieve the associated products
        products = cargo.products.all()
    
        return render(request, 'allin/sales/tracking.html', {'cargo':cargo, 'products':products})
    else:
        cargo = LooseCargo.objects.get(invoice_number=tracking_number)

        return render(request, 'allin/sales/tracking.html', {'cargo':cargo})
        