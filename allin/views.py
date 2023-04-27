from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from allin.forms import (LooseCargoForm, LooseContainerForm, 
                         FullCargoForm, FullContainerForm,
                         InvoiceForm, ExpensesForm, ProductForm,)

from allin.models import (LooseCargo, LooseContainer, FullCargo, 
                        FullContainer, Invoice, Expenses, Product,)


class LooseContainerListView(ListView):
    model = LooseContainer
    template_name = 'shipping/allin/loose/loosecontainers.html' 
    context_object_name = 'containers'
    paginate_by = 10  # Set the number of items per page


class LooseCargoListView(ListView):
    model = LooseCargo
    template_name = 'shipping/allin/loose/loosecargos.html' 
    context_object_name = 'cargos'
    paginate_by = 10  # Set the number of items per page


class FullContainerListView(ListView):
    model = FullContainer
    template_name = 'shipping/allin/full/fullcontainers.html' 
    context_object_name = 'containers'
    paginate_by = 10  # Set the number of items per page


class FullCargoListView(ListView):
    model = FullCargo
    template_name = 'shipping/allin/full/fullcargos.html' 
    context_object_name = 'cargos'
    paginate_by = 10  # Set the number of items per page


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'shipping/allin/sales/invoices.html' 
    context_object_name = 'invoices'
    paginate_by = 10  # Set the number of items per page


class ExpensesListView(ListView):
    model = Expenses
    template_name = 'shipping/allin/sales/expenses.html' 
    context_object_name = 'expenses'
    paginate_by = 10  # Set the number of items per page


class ProductListView(ListView):
    model = Product
    template_name = 'shipping/allin/sales/productss.html' 
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
    success_url = '/l_cargos/'

class FullContainerCreateView(CreateView):
    model = FullContainer
    template_name = 'shipping/allin/full/fullcontainer_form.html' 
    form_class = FullContainerForm
    success_url = '/fullcontainers/'

class FullCargoCreateView(CreateView):
    model = FullCargo
    template_name = 'shipping/allin/full/fullcargo_form.html' 
    form_class = FullCargoForm
    success_url = '/f_cargos/'

class InvoiceCreateView(CreateView):
    model = Invoice
    template_name = 'shipping/allin/sales/invoice_form.html' 
    form_class = InvoiceForm
    success_url = '/invoices/'

class ExpensesCreateView(CreateView):
    model = Expenses
    template_name = 'shipping/allin/sales/expenses_form.html' 
    form_class = ExpensesForm
    success_url = '/expenses/'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'shipping/allin/sales/products_form.html' 
    form_class = ProductForm
    success_url = '/products/'
   


class LooseContainerDetailView(DetailView):
    model = LooseContainer
    template_name = 'shipping/allin/loose/loosecontainer.html' 
    context_object_name = 'container'
    
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
    

class FullContainerDetailView(DetailView):
    model = FullContainer
    template_name = 'shipping/allin/full/fullcontainer.html' 
    context_object_name = 'container'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargos'] = self.object.cargo.all()
        context['stocks'] = self.object.cargo.product.filter(has_stock=True)
        
        return context
    


class FullCargoDetailView(DetailView):
    model = FullCargo
    template_name = 'shipping/allin/full/fullcargo.html' 
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
    

class ExpensesDetailView(DetailView):
    model = Expenses
    template_name = 'shipping/allin/sales/expense.html' 
    context_object_name = 'expense'
    
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
    

