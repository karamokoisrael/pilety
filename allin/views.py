from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from allin.models import LooseCargo, LooseContainer, Invoice, Product
from allin.forms import LooseCargoForm, LooseContainerForm, InvoiceForm, ProductForm

class LooseContainerListView(ListView):
    model = LooseContainer
    template_name = 'shipping/allin/loose/loosecontainer_list.html' 
    context_object_name = 'loose_containers'
    paginate_by = 10  # Set the number of items per page


class LooseCargoListView(ListView):
    model = LooseCargo
    template_name = 'shipping/allin/loose/loosecargo_list.html' 
    context_object_name = 'loose_cargos'
    paginate_by = 10  # Set the number of items per page


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'shipping/allin/sales/invoice_list.html' 
    context_object_name = 'invoices'
    paginate_by = 10  # Set the number of items per page


class ProductListView(ListView):
    model = Product
    template_name = 'shipping/allin/sales/products_list.html' 
    context_object_name = 'products'
    paginate_by = 10  # Set the number of items per page


class LooseContainerCreateView(CreateView):
    model = LooseContainer
    template_name = 'shipping/allin/loose/loosecontainer_form.html' 
    form_class = LooseContainerForm
    success_url = '/loosecontainers/'

class LooseCargoCreateView(CreateView):
    model = LooseCargo
    template_name = 'shipping/allin/loose/loosecargo_form.html' 
    form_class = LooseCargoForm
    success_url = '/cargos/'

class InvoiceCreateView(CreateView):
    model = Invoice
    template_name = 'shipping/allin/sales/invoice_form.html' 
    form_class = InvoiceForm
    success_url = '/invoices/'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'shipping/allin/sales/products_form.html' 
    form_class = ProductForm
    success_url = '/products/'
   


class LooseContainerDetailView(DetailView):
    model = LooseContainer
    template_name = 'shipping/allin/loose/loosecontainer.html' 
    context_object_name = 'containers'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargos'] = self.object.cargo.all()
        context['stocks'] = self.object.cargo.product.filter(has_stock=True)
        
        return context
    


class LooseCargoDetailView(DetailView):
    model = LooseCargo
    template_name = 'shipping/allin/loose/loosecargo.html' 
    context_object_name = 'cargo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.product.all()
        context['stocks'] = self.object.cargo.all()
        return context
    


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'shipping/allin/sales/invoice.html' 
    context_object_name = 'invoice'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loose_cargos'] = self.object.cargo.all()
        return context
    


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shipping/allin/sales/product.html' 
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loose_cargos'] = self.object.cargo.all()
        return context
    

