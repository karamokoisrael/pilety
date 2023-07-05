# from django.shortcuts import render
# from django.views.generic import CreateView, DetailView, ListView, TemplateView

# from shipping.models import FullCargo, FullContainer, LooseCargo, LooseContainer, FullCargoInvoice, LooseCargoInvoice
# from shipping.forms import (
#                             LooseContainerForm,
#                             FullContainerForm,
#                             LooseCargoForm,
#                             FullCargoForm,
#                             LooseCargoInvoiceForm,
#                             FullCargoInvoiceForm,)

# # class Homepage(TemplateView):
# #     template_name = 'homepage.html'

# class LooseContainerListView(ListView):
#     model = LooseContainer
#     template_name = 'shipping/loosecontainer_list.html' 
#     context_object_name = 'loose_containers'
#     paginate_by = 10  # Set the number of items per page

# class FullContainerListView(ListView):
#     model = FullContainer
#     template_name = 'shipping/fullcontainer_list.html' 
#     context_object_name = 'full_containers'
#     paginate_by = 10  # Set the number of items per page

# class LooseCargoListView(ListView):
#     model = LooseCargo
#     template_name = 'shipping/loosecargo_list.html' 
#     context_object_name = 'loose_cargos'
#     paginate_by = 10  # Set the number of items per page

# class FullCargoListView(ListView):
#     model = FullCargo
#     template_name = 'shipping/fullcargo_list.html' 
#     context_object_name = 'full_cargos'
#     paginate_by = 10  # Set the number of items per page

# class LooseCargoInvoiceListView(ListView):
#     model = LooseCargoInvoice
#     template_name = 'shipping/loosecargo_invoice_list.html' 
#     context_object_name = 'full_cargos'
#     paginate_by = 10  # Set the number of items per page

# class FullCargoInvoiceListView(ListView):
#     model = FullCargoInvoice
#     template_name = 'shipping/fullcargo_invoice_list.html' 
#     context_object_name = 'full_cargos'
#     paginate_by = 10  # Set the number of items per page

# class LooseContainerCreateView(CreateView):
#     model = LooseContainer
#     template_name = 'shipping/loosecontainer_form.html' 
#     form_class = LooseContainerForm  # Replace with your form class
#     success_url = '/loosecontainers/'  # Replace with your success URL

# class FullContainerCreateView(CreateView):
#     model = FullContainer
#     template_name = 'shipping/fullcontainer_form.html' 
#     form_class = FullContainerForm  # Replace with your form class
#     success_url = '/fullcontainers/'  # Replace with your success URL

# class LooseCargoCreateView(CreateView):
#     model = LooseCargo
#     template_name = 'shipping/loosecargo_form.html' 
#     form_class = LooseCargoForm  # Replace with your form class
#     success_url = '/loosecargos/'  # Replace with your success URL

# class FullCargoCreateView(CreateView):
#     model = FullCargo
#     template_name = 'shipping/fullcargo_form.html' 
#     form_class = FullCargoForm  # Replace with your form class
#     success_url = '/fullcargos/'  # Replace with your success URL

# class LooseCargoInvoiceCreateView(CreateView):
#     model = LooseCargoInvoice
#     template_name = 'shipping/loosecargo_invoice_form.html' 
#     # context_object_name = 'loose_cargos_inv'
#     form_class = LooseCargoInvoiceForm  # Replace with your form class
#     success_url = '/loosecargos_invoice/'  # Replace with your success URL

# class FullCargoInvoiceCreateView(CreateView):
#     model = FullCargoInvoice
#     template_name = 'shipping/fullcargo_invoice_form.html' 
#     # context_object_name = 'full_cargos_inv'
#     form_class = FullCargoInvoiceForm  # Replace with your form class
#     success_url = '/fullcargos_invoice/'  # Replace with your success URL

    
# class LooseContainerDetailView(DetailView):
#     model = LooseContainer
#     template_name = 'shipping/loosecontainer_detail.html' 
#     context_object_name = 'loose_container'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['loose_cargos'] = self.object.cargo.all()
#         return context
    

# class FullContainerDetailView(DetailView):
#     model = FullContainer
#     template_name = 'shipping/fullcontainer_detail.html' 
#     context_object_name = 'full_container'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['full_cargos'] = self.object.cargo.all()
    
#         return context
    

# class LooseCargoDetailView(DetailView):
#     model = LooseCargo
#     template_name = 'shipping/loosecargo_detail.html' 
#     context_object_name = 'loose_cargo'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = self.object.product.all()
#         return context
    

# class FullCargoDetailView(DetailView):
#     model = FullCargo
#     template_name = 'shipping/fullcargo_detail.html' 
#     context_object_name = 'full_cargo'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = self.object.product.all()
    
#         return context
    

# class LooseCargoInvoiceDetailView(DetailView):
#     model = LooseCargoInvoice
#     template_name = 'shipping/loosecargo_invoice_detail.html' 
#     context_object_name = 'full_cargo_inv_details'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
    
#         return context
    

# class FullCargoInvoiceDetailView(DetailView):
#     model = FullCargoInvoice
#     template_name = 'shipping/fullcargo_invoice_detail.html' 
#     context_object_name = 'full_cargos_inv_details'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
    
#         return context
    
