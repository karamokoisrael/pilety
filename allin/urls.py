from django.urls import path
from allin.views import (
    LooseContainerListView,
    LooseCargoListView,
    FullCargoListView,
    FullContainerListView,
    InvoiceListView,
    ExpensesListView,
    ExpenseFilterView,
    ExpensesView,
    ProductListView,
    DeliveryListView,
    DeliveryVehicleListView,
    ProductQuoteListView,
    ShippingQuoteListView,
    ProductShippingQuoteListView,

    LooseContainerCreateView,
    LooseCargoCreateView,
    FullContainerCreateView,
    FullCargoCreateView,
    InvoiceCreateView,
    ExpensesCreateView,
    ProductCreateView,
    DeliveryCreateView,
    DeliveryVehicleCreateView,
    ProductQuoteCreateView,
    ShippingQuoteCreateView,
    ProductShippingQuoteCreateView,

    LooseContainerDetailView,
    LooseCargoDetailView,
    FullCargoDetailView,
    FullContainerDetailView,
    InvoiceDetailView,
    ExpensesDetailView,
    ProductDetailView,
    DeliveryDetailView,
    ShippingQuoteDetailView,

    create_delivery,
    deliver_cargo,
)

from allin.other_views import (Homepage,
                          AboutPage,
                          ContactPage,
                          PolicyPage,
                        #   RequestPage,
                          ServicesPage,
                          TeamPage,
                          TermsPage,
                          WhyUsPage,
                          PriceLiftPage,
                          InvoiceGeneratorView,
                          generate_invoice,
                          generate_fullco_packing_list,
                          generate_looseco_packing_list
                          )

app_name = 'allin'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('about/', AboutPage.as_view(), name='about'),
    path('contact', ContactPage.as_view(), name='contact'),
    path('policy', PolicyPage.as_view(), name='policy'),
    path('services', ServicesPage.as_view(), name='services'),
    path('team', TeamPage.as_view(), name='team'),
    path('terms', TermsPage.as_view(), name='terms'),
    path('why-choose-us', WhyUsPage.as_view(), name='whyus'),
    path('prices', PriceLiftPage.as_view(), name='price_list'),
    # path('gen-inv/<str:invoice_number>', InvoiceGeneratorView.as_view(), name='generate_invoice'),
    # path('', Homepage.as_view(), name='homepage'),
    path('gen-inv/<str:invoice_number>/', generate_invoice, name='generate_invoice'),

    

    path('l_containers/', LooseContainerListView.as_view(), name='l_containers'),
    path('l_cargos/', LooseCargoListView.as_view(), name='l_cargos'),
    path('f_containers/', FullContainerListView.as_view(), name='f_containers'),
    path('f_cargos/', FullCargoListView.as_view(), name='f_cargos'),
    path('invoices/', InvoiceListView.as_view(), name='invoices'),
    path('expenses/', ExpensesListView.as_view(), name='expenses'),
    path('filter/', ExpenseFilterView.as_view(), name='filter_expenses'),
    path('exp/', ExpensesView.as_view(), name='exp'),
    path('products/', ProductListView.as_view(), name='products'),
    path('deliveries/', DeliveryListView.as_view(), name='deliveries'),
    path('vehicles/', DeliveryVehicleListView.as_view(), name='vehicles'),
    path('product_quotes/', ProductQuoteListView.as_view(), name='product_quotes'),
    path('shipping_quotes/', ShippingQuoteListView.as_view(), name='shipping_quotes'),
    path('products_shipping_quotes/', ProductShippingQuoteListView.as_view(), name='products_shipping_quotes'),
    

    path('create/l_containers/', LooseContainerCreateView.as_view(), name='create_l_containers'),
    path('create/l_cargos/', LooseCargoCreateView.as_view(), name='create_l_cargos'),
    path('create/f_containers/', FullContainerCreateView.as_view(), name='create_f_containers'),
    path('create/f_cargos/', FullCargoCreateView.as_view(), name='create_f_cargos'),
    path('create/invoices/', InvoiceCreateView.as_view(), name='create_invoices'),
    path('create/expenses/', ExpensesCreateView.as_view(), name='create_expenses'),
    path('create/products/', ProductCreateView.as_view(), name='create_products'),
    path('deliveries_form/', DeliveryCreateView.as_view(), name='create_deliveries'),
    path('vehicles_form/', DeliveryVehicleCreateView.as_view(), name='create_vehicles'),
    path('product_quotes_form/', ProductQuoteCreateView.as_view(), name='create_product_quotes'),
    path('shipping_quotes_form/', ShippingQuoteCreateView.as_view(), name='create_shipping_quotes'),
    path('products_shipping_quotes_form/', ProductShippingQuoteCreateView.as_view(), name='create_products_shipping_quotes'),
    path('create_delivery/<str:cargo_ids>/', create_delivery, name='create_delivery'),
    


    path('l_containers/<int:pk>/', LooseContainerDetailView.as_view(), name='l_container'),
    path('l_cargos/<int:pk>/', LooseCargoDetailView.as_view(), name='l_cargo'),
    path('f_containers/<int:pk>/', FullContainerDetailView.as_view(), name='f_container'),
    path('f_cargos/<int:pk>/', FullCargoDetailView.as_view(), name='f_cargo'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice'),
    path('expenses/<int:pk>/', ExpensesDetailView.as_view(), name='expense'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('delivery/<int:pk>/', DeliveryDetailView.as_view(), name='delivery'),
    path('shippingquote/<int:pk>/', ShippingQuoteDetailView.as_view(), name='shipping_quote'),



    # utility
    path('deliver_cargo/', deliver_cargo, name='deliver_cargo'),
    path('generate_fullco_packing_list/<int:container_id>/', generate_fullco_packing_list, name='generate_fullco_packing_list'),
    path('generate_looseco_packing_list/<int:container_id>/', generate_looseco_packing_list, name='generate_looseco_packing_list'),


    
]
