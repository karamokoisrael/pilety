from allin.forms import (ExpenseForm, FilterForm, FullCargoForm,
                         FullContainerForm, InvoiceForm, LooseCargoForm,
                         LooseContainerForm, ProductForm,
                         ProductQuoteForm,  ShippingQuoteForm, 
                         ProductShippingQuoteForm, DeliveryForm, DeliveryVehicleForm,)
from allin.models import (Expense, ExpenseCategory, FullCargo, FullContainer,
                          Invoice, LooseCargo, LooseContainer, Product, 
                          ProductQuote, ProductQuoteImages, ShippingQuote, 
                          ProductShippingQuote, Delivery, DeliveryVehicle,)
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.contrib import messages


def error_handler(request, *args, **kwargs):
    return render(request, 'pilety/404.html', {'error_message': 'An internal server error occurred.'}, status=500)

class DeliveryVehicleListView(ListView):
    model = DeliveryVehicle
    template_name = 'allin/sales/vehicles.html' 
    context_object_name = 'vehicles'
    # paginate_by = 10  


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'allin/sales/deliveries.html' 
    context_object_name = 'deliveries'
    # paginate_by = 10  



def deliver_cargo(request):
    if request.method == 'POST':
        selected_goods_to_deliver = request.POST.getlist('selected_goods')
        return redirect('allin:create_delivery', cargo_ids=','.join(selected_goods_to_deliver))
    
    cargos = LooseCargo.objects.all()
    return render(request, 'allin/loose/loosecargos.html', {'cargos': cargos})
    
def create_delivery(request, cargo_ids):
    # cargo_ids = cargo_ids.strip("[]").replace("'", "").split(", ")
    cargo_ids = [int(cargo_id) for cargo_id in cargo_ids.strip("[]").replace("'", "").split(',')]
    if request.method == 'POST':
        delivery_id = request.POST.get('delivery_id')
        cargos = LooseCargo.objects.filter(id__in=cargo_ids, container__status="AT")
        if cargos.exists():
            if delivery_id:
                delivery = Delivery.objects.get(id=delivery_id)
            else:
                delivery = Delivery.objects.create()

            delivery.cargos.add(*cargos)
            cargos.update(status="DV")
            messages.warning(request, "Only The arrived cargos have been added to the container")

            return redirect('allin:delivery', delivery.id)
        else:
            messages.warning(request, "None of the selected cargo has arrived yet")
            return redirect('allin:l_cargos')
    
    deliveries = Delivery.objects.all()
    return render(request, 'allin/sales/deliveries_form.html', {'deliveries': deliveries, 'cargo_ids': cargo_ids})

def softsignup(request):
    return render(request, 'allin/accounts/softsignup.html')

class ProductShippingQuoteListView(ListView):
    model = ProductShippingQuote
    template_name = 'allin/quotes/product_shipping_quote.html' 
    context_object_name = 'products'
    # paginate_by = 10  


class ShippingQuoteListView(ListView):
    model = ShippingQuote
    template_name = 'allin/quotes/shipping_quotes.html' 
    context_object_name = 'shipping_quote'
    # paginate_by = 10  

    
class ProductQuoteListView(ListView):
    model = ProductQuote
    template_name = 'allin/quotes/products_quote.html' 
    context_object_name = 'products'
    # paginate_by = 10  

 


class LooseContainerListView(ListView):
    model = LooseContainer
    template_name = 'allin/loose/loosecontainers.html' 
    context_object_name = 'containers'
    # paginate_by = 10  

 
class LooseCargoListView(ListView):
    model = LooseCargo
    template_name = 'allin/loose/loosecargos.html' 
    context_object_name = 'cargos'
    # paginate_by = 10

    # def get_queryset(self):
    #     queryset = super(LooseCargoListView, self).get_queryset()
    #     queryset = LooseCargo.objects.filter(status='True') # TODO
    #     return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["delivered"] = LooseCargo.objects.filter(reciever=self.request.user).exclude(status__in=['DC', 'AT', 'RW'])
            context["undelivered"] = LooseCargo.objects.filter(reciever=self.request.user).exclude(status__in=['DV', 'RC'])
            return context  
        elif self.request.user.is_staff:
            context["delivered"] = LooseCargo.objects.exclude(status__in=['DC', 'AT', 'RW'])
            context["undelivered"] = LooseCargo.objects.exclude(status__in=['DV', 'RC'])
            return context
        else:
            return redirect('allin:softsignup')  


class FullContainerListView(ListView):
    model = FullContainer
    template_name = 'allin/full/fullcontainers.html' 
    context_object_name = 'containers'
    # paginate_by = 10  


class FullCargoListView(ListView):
    model = FullCargo
    template_name = 'allin/full/fullcargos.html' 
    context_object_name = 'cargos'
    # paginate_by = 10  


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'allin/sales/invoices.html' 
    context_object_name = 'invoices'
    # paginate_by = 10  


class ExpensesListView(ListView):
    model = Expense
    template_name = 'allin/sales/expenses.html' 
    context_object_name = 'expenses'
    # paginate_by = 10  

class ExpenseFilterView(ListView):
    model = Expense
    template_name = 'allin/sales/expenses.html'

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

class ExpensesView(TemplateView):
    template_name = 'allin/sales/exp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_month = timezone.now().month
        expenses_by_category = Expense.objects.filter(
            date__month=current_month
        ).values('name__name').annotate(total=Sum('amount'))
        expenses_by_month = Expense.objects.filter(
            date__month=current_month
        ).annotate(month=TruncMonth('date')).values('month').annotate(total=Sum('amount')).order_by('month')
        total_expenses = Expense.objects.filter(date__month=current_month).aggregate(Sum('amount'))
        context['expenses_by_category'] = expenses_by_category
        context['expenses_by_month'] = expenses_by_month
        context['total_expenses'] = total_expenses['amount__sum']
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'allin/sales/products.html' 
    context_object_name = 'products'
    # paginate_by = 10  

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        queryset = Product.objects.filter(has_stock=True) # TODO
        return queryset
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[""] = 
    #     return context
    


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
   

class DeliveryVehicleCreateView(CreateView):
    model = DeliveryVehicle
    template_name = 'allin/sales/vehicles_form.html'
    form_class = DeliveryVehicleForm
    success_url = '/vehicle/'  


class DeliveryCreateView(CreateView):
    model = Delivery
    template_name = 'allin/sales/deliveries_form.html'
    form_class = DeliveryForm
    success_url = '/deliveries/'  


class ProductShippingQuoteCreateView(CreateView):
    model = ProductShippingQuote
    template_name = 'allin/quotes/product_shipping_quote_form.html'
    form_class = ProductShippingQuoteForm
    success_url = '/product_shipping_quotes/'  


class ShippingQuoteCreateView(CreateView):
    model = ShippingQuote
    template_name = 'allin/quotes/shipping_quote_form.html'
    form_class = ShippingQuoteForm
    success_url = '/shipping_Quote/'  


class ProductQuoteCreateView(CreateView):
    model = ProductQuote
    template_name = 'allin/quotes/products_quote_form.html'
    form_class = ProductQuoteForm
    success_url = '/products_quotes/'  

 

class LooseContainerDetailView(DetailView):
    model = LooseContainer
    template_name = 'allin/loose/loosecontainer.html' 
    context_object_name = 'container'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargos'] = self.object.cargos.all()
        # context['stocks'] = self.object.cargos.products.filter(has_stock=True)
        
        return context
    
    

class LooseCargoDetailView(DetailView):
    model = LooseCargo
    template_name = 'allin/loose/loosecargo.html' 
    context_object_name = 'cargo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['products'] = self.object.products.all()
            context['stocks'] = self.object.products.filter(has_stock=True)
            # context['invoices'] = self.object.invoices.all()
            return context
        elif self.request.user.is_authenticated:
            context['products'] = self.object.products.filter()
            context['stocks'] = self.object.products.filter()
            return context
    

class FullContainerDetailView(DetailView):
    model = FullContainer
    template_name = 'allin/full/fullcontainer.html' 
    context_object_name = 'container'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargos'] = self.object.cargos.all()
        # context['stocks'] = self.object.cargos.products.filter(has_stock=True)
        
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
    

class ShippingQuoteDetailView(DetailView):

    model = ShippingQuote
    template_name = 'allin/quotes/shipping_quote.html' 
    context_object_name = 'cargo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()

        return context
    

class DeliveryDetailView(DetailView):
    model = Delivery
    template_name = 'allin/sales/delivery.html' 
    context_object_name = 'delivery'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargos'] = self.object.cargos.all()
        return context
