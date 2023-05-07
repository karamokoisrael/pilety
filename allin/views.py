from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from allin.forms import (LooseCargoForm, LooseContainerForm, 
                         FullCargoForm, FullContainerForm,
                         InvoiceForm, ExpenseForm, ProductForm, FilterForm)

from allin.models import (LooseCargo, LooseContainer, FullCargo, 
                        FullContainer, Invoice, Expense, Product, ExpenseCategory)


class LooseContainerListView(ListView):
    model = LooseContainer
    template_name = 'allin/loose/loosecontainers.html' 
    context_object_name = 'containers'
    paginate_by = 10  # Set the number of items per page


class LooseCargoListView(ListView):
    model = LooseCargo
    template_name = 'allin/loose/loosecargos.html' 
    context_object_name = 'cargos'
    paginate_by = 10  # Set the number of items per page


class FullContainerListView(ListView):
    model = FullContainer
    template_name = 'allin/full/fullcontainers.html' 
    context_object_name = 'containers'
    paginate_by = 10  # Set the number of items per page


class FullCargoListView(ListView):
    model = FullCargo
    template_name = 'allin/full/fullcargos.html' 
    context_object_name = 'cargos'
    paginate_by = 10  # Set the number of items per page


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'allin/sales/invoices.html' 
    context_object_name = 'invoices'
    paginate_by = 10  # Set the number of items per page


class ExpensesListView(ListView):
    model = Expense
    template_name = 'allin/sales/expenses.html' 
    context_object_name = 'expenses'
    paginate_by = 10  # Set the number of items per page

class ExpenseFilterView(ListView):
    model = Expense
    template_name = 'expenses.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = FilterForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            if name:
                queryset = queryset.filter(name=name)
            if start_date:
                queryset = queryset.filter(date__gte=start_date)
            if end_date:
                queryset = queryset.filter(date__lte=end_date)
        return queryset

class ProductListView(ListView):
    model = Product
    template_name = 'allin/sales/productss.html' 
    context_object_name = 'products'
    paginate_by = 10  # Set the number of items per page


class LooseContainerCreateView(CreateView):
    model = LooseContainer
    template_name = 'allin/loose/loosecontainer_form.html' 
    form_class = LooseContainerForm
    success_url = '/loosecontainers/'


class LooseCargoCreateView(CreateView):
    model = LooseCargo
    template_name = 'allin/loose/loosecargo_form.html' 
    form_class = LooseCargoForm
    success_url = '/l_cargos/'


class FullContainerCreateView(CreateView):
    model = FullContainer
    template_name = 'allin/full/fullcontainer_form.html' 
    form_class = FullContainerForm
    success_url = '/fullcontainers/'


class FullCargoCreateView(CreateView):
    model = FullCargo
    template_name = 'allin/full/fullcargo_form.html' 
    form_class = FullCargoForm
    success_url = '/f_cargos/'


class InvoiceCreateView(CreateView):
    model = Invoice
    template_name = 'allin/sales/invoice_form.html' 
    form_class = InvoiceForm
    success_url = '/invoices/'


class ExpensesCreateView(CreateView):
    model = Expense
    template_name = 'allin/sales/expenses_form.html' 
    form_class = ExpenseForm
    success_url = '/expenses/'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'allin/sales/products_form.html' 
    form_class = ProductForm
    success_url = '/products/'
   

class LooseContainerDetailView(DetailView):
    model = LooseContainer
    template_name = 'allin/loose/loosecontainer.html' 
    context_object_name = 'container'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargos'] = self.object.cargo.all()
        context['stocks'] = self.object.cargo.product.filter(has_stock=True)
        
        return context
    

class LooseCargoDetailView(DetailView):
    model = LooseCargo
    template_name = 'allin/loose/loosecargo.html' 
    context_object_name = 'cargo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()
        context['stocks'] = self.object.products.filter(has_stock=True)
        # context['invoices'] = self.object.invoices.all()
        return context
    

class FullContainerDetailView(DetailView):
    model = FullContainer
    template_name = 'allin/full/fullcontainer.html' 
    context_object_name = 'container'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargos'] = self.object.cargo.all()
        context['stocks'] = self.object.cargo.product.filter(has_stock=True)
        
        return context
    

class FullCargoDetailView(DetailView):
    model = FullCargo
    template_name = 'allin/full/fullcargo.html' 
    context_object_name = 'cargo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()
        context['stocks'] = self.object.products.filter(has_stock=True)
        return context
    

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'allin/sales/invoice.html' 
    context_object_name = 'invoice'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loose_cargos'] = self.object.cargo.all()
        return context
    

class ExpensesDetailView(DetailView):
    model = Expense
    template_name = 'allin/sales/expense.html' 
    context_object_name = 'expense'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loose_cargos'] = self.object.cargo.all()
        return context
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'allin/sales/product.html' 
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #  context['loose_cargos'] = self.object.cargo.all()
        return context
    