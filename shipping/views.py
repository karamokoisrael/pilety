from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from shipping.models import FullCargo, FullContainer, LooseCargo, LooseContainer, FullCargoInvoice, LooseCargoInvoice
from shipping.forms import (
                            LooseContainerForm,
                            FullContainerForm,
                            LooseCargoForm,
                            FullCargoForm,
                            LooseCargoInvoiceForm,
                            FullCargoInvoiceForm,)



class LooseContainerListView(ListView):
    model = LooseContainer
    template_name = 'loosecontainer_list.html'  # Replace with your template name
    context_object_name = 'loose_containers'
    paginate_by = 10  # Set the number of items per page

class FullContainerListView(ListView):
    model = FullContainer
    template_name = 'fullcontainer_list.html'  # Replace with your template name
    context_object_name = 'full_containers'
    paginate_by = 10  # Set the number of items per page

class LooseCargoListView(ListView):
    model = LooseCargo
    template_name = 'loosecargo_list.html'  # Replace with your template name
    context_object_name = 'loose_cargos'
    paginate_by = 10  # Set the number of items per page

class FullCargoListView(ListView):
    model = FullCargo
    template_name = 'fullcargo_list.html'  # Replace with your template name
    context_object_name = 'full_cargos'
    paginate_by = 10  # Set the number of items per page

class LooseCargoInvoiceListView(ListView):
    model = LooseCargoInvoice
    template_name = 'loosecargo_invoice_list.html'  # Replace with your template name
    context_object_name = 'full_cargos'
    paginate_by = 10  # Set the number of items per page

class FullCargoInvoiceListView(ListView):
    model = FullCargoInvoice
    template_name = 'fullcargo_invoice_list.html'  # Replace with your template name
    context_object_name = 'full_cargos'
    paginate_by = 10  # Set the number of items per page

class LooseContainerCreateView(CreateView):
    model = LooseContainer
    template_name = 'loosecontainer_form.html'  # Replace with your template name
    form_class = LooseContainerForm  # Replace with your form class
    success_url = '/loosecontainers/'  # Replace with your success URL

class FullContainerCreateView(CreateView):
    model = FullContainer
    template_name = 'fullcontainer_form.html'  # Replace with your template name
    form_class = FullContainerForm  # Replace with your form class
    success_url = '/fullcontainers/'  # Replace with your success URL

class LooseCargoCreateView(CreateView):
    model = LooseCargo
    template_name = 'loosecargo_form.html'  # Replace with your template name
    form_class = LooseCargoForm  # Replace with your form class
    success_url = '/loosecargos/'  # Replace with your success URL

class FullCargoCreateView(CreateView):
    model = FullCargo
    template_name = 'fullcargo_form.html'  # Replace with your template name
    form_class = FullCargoForm  # Replace with your form class
    success_url = '/fullcargos/'  # Replace with your success URL

class LooseCargoInvoiceCreateView(CreateView):
    model = LooseCargoInvoice
    template_name = 'loosecargo_invoice_form.html'  # Replace with your template name
    # context_object_name = 'loose_cargos_inv'
    form_class = FullCargoForm  # Replace with your form class
    success_url = '/loosecargos_invoice/'  # Replace with your success URL

class FullCargoInvoiceCreateView(CreateView):
    model = FullCargoInvoice
    template_name = 'fullcargo_invoice_form.html'  # Replace with your template name
    # context_object_name = 'full_cargos_inv'
    form_class = FullCargoInvoiceForm  # Replace with your form class
    success_url = '/fullcargos_invoice/'  # Replace with your success URL

class LooseContainerDetailView(DetailView):
    model = LooseContainer
    template_name = 'loosecontainer_detail.html'  # Replace with your template name
    context_object_name = 'loose_container'

class FullContainerDetailView(DetailView):
    model = FullContainer
    template_name = 'fullcontainer_detail.html'  # Replace with your template name
    context_object_name = 'full_container'

class LooseCargoDetailView(DetailView):
    model = LooseCargo
    template_name = 'loosecargo_detail.html'  # Replace with your template name
    context_object_name = 'loose_cargo'

class FullCargoDetailView(DetailView):
    model = FullCargo
    template_name = 'fullcargo_detail.html'  # Replace with your template name
    context_object_name = 'full_cargo'

class LooseCargoInvoiceDetailView(DetailView):
    model = LooseCargoInvoice
    template_name = 'loosecargo_invoice_detail.html'  # Replace with your template name
    context_object_name = 'full_cargo_inv_details'

class FullCargoInvoiceDetailView(DetailView):
    model = FullCargoInvoice
    template_name = 'fullcargo_invoice_detail.html'  # Replace with your template name
    context_object_name = 'full_cargos_inv_details'
