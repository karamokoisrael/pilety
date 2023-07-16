import os
import threading
import openpyxl
from io import BytesIO

import pdfkit
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (Image, Paragraph, SimpleDocTemplate, Spacer,
                                Table, TableStyle)

from .models import LooseCargo
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from .models import LooseContainer

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

    # Create a buffer to store the PDF
    buffer = BytesIO()

    # Set up the PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Add the logo and company details
    logo = Image("allin/logo-two.png")
    logo.drawWidth = 100
    logo.drawHeight = 100
    elements.append(logo)

    company_details = [
        "                         Pilety Import Export Shipping Company",
        "      OFFICE ADDRESS: Room 301, Building 20 Futian District 4, Yiwu,Jinhua City Zhejiang Province, China",
    ]
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(name='TitleStyle', parent=styles['Heading1'], alignment=1)
    normal_style = styles["Normal"]
    elements.append(Paragraph(company_details[0], title_style))
    elements.extend(Paragraph(detail, normal_style) for detail in company_details[1:])
    elements.append(Spacer(1, 20))  # Add some space

    # Create the table for product details
    table_data = [
        ["Name", "CBM", "Weight", "Quantity", "Price", "Cost"],
    ]
    for product in products:
        row = [
            product.name,
            str(product.cbm),
            str(product.weight),
            str(product.qty),
            str(product.price),
            str(product.qty * product.price),
        ]
        table_data.append(row)

    row = [cargo.mark, str(cargo.cbms), str(cargo.weight), str(cargo.ctns),'', '',]
    table_data.append(row)
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))  # Add some space

    # Add the total
    # total = cargo.total  # Assuming you have a "total" field in the LooseCargo model
    total = 100000.223  # Assuming you have a "total" field in the LooseCargo model
    total_text = f"Total: {total}"
    elements.append(Paragraph(total_text, normal_style))

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






def generate_excel_file(products):
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Add four blank rows at the beginning
    for _ in range(4):
        sheet.append([])

    # Write the headers for the Product model fields
    headers = ["recieved", "name", "chinese", "qty", 
               "packaging", "units", "prod_type", "price", 
               "ttprice", "cbm", "cbms", "wght", 
               "weight", 
               "item_number", "cbm_cost", "cargo_types", 
               "stock", "has_stock",
               "supplier", "l_cargo", "invoice"]
    
    sheet.append(headers)

    # Write product data
    for product in products:
        sheet.append(product)

    return wb



def generate_packing_list(request, container_id):
    container = get_object_or_404(LooseContainer, id=container_id)
    products = container.cargos.values_list(
        "products__recieved", "products__name", "products__chinese", "products__qty",
        "products__packaging", "products__units", "products__prod_type", "products__price",
        "products__ttprice", "products__cbm", "products__cbms", "products__wght",
        "products__weight", 
        "products__item_number", "products__cbm_cost", "products__cargo_types",
        "products__stock", "products__has_stock", "products__supplier__username",
        "products__l_cargo__invoice_number"
    )

    # Generate the Excel file
    wb = generate_excel_file(products)

    # Create a response with the Excel file
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = f"attachment; filename=PackingList_{container_id}.xlsx"
    wb.save(response)

    return response
