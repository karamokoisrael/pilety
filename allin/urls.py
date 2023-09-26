from django.urls import path
from . import views, other_views
from .api_urls import api_routes


app_name = 'allin'

urlpatterns = api_routes + [
    path('', other_views.Homepage.as_view(), name='homepage'),
    path('about/', other_views.AboutPage.as_view(), name='about'),
    path('contact', other_views.ContactPage.as_view(), name='contact'),
    path('policy', other_views.PolicyPage.as_view(), name='policy'),
    path('services', other_views.ServicesPage.as_view(), name='services'),
    path('team', other_views.TeamPage.as_view(), name='team'),
    path('terms', other_views.TermsPage.as_view(), name='terms'),
    path('why-choose-us', other_views.WhyUsPage.as_view(), name='whyus'),
    path('prices', other_views.PriceLiftPage.as_view(), name='price_list'),
    # path('gen-inv/<str:invoice_number>', views.InvoiceGeneratorView.as_view(), name='generate_invoice'),
    # path('', views.Homepage.as_view(), name='homepage'),

    

    path('l_containers/', views.LooseContainerListView.as_view(), name='l_containers'),
    path('l_cargos/', views.LooseCargoListView.as_view(), name='l_cargos'),
    path('f_containers/', views.FullContainerListView.as_view(), name='f_containers'),
    path('f_cargos/', views.FullCargoListView.as_view(), name='f_cargos'),
    path('invoices/', views.InvoiceListView.as_view(), name='invoices'),
    path('expenses/', views.ExpensesListView.as_view(), name='expenses'),
    path('filter/', views.ExpenseFilterView.as_view(), name='filter_expenses'),
    path('exp/', views.ExpensesView.as_view(), name='exp'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('deliveries/', views.DeliveryListView.as_view(), name='deliveries'),
    path('vehicles/', views.DeliveryVehicleListView.as_view(), name='vehicles'),
    path('product_quotes/', views.ProductQuoteListView.as_view(), name='product_quotes'),
    path('shipping_quotes/', views.ShippingQuoteListView.as_view(), name='shipping_quotes'),
    path('products_shipping_quotes/', views.ProductShippingQuoteListView.as_view(), name='products_shipping_quotes'),
    

    path('create/l_containers/', views.LooseContainerCreateView.as_view(), name='create_l_containers'),
    path('create/l_cargos/', views.LooseCargoCreateView.as_view(), name='create_l_cargos'),
    path('create/f_containers/', views.FullContainerCreateView.as_view(), name='create_f_containers'),
    path('create/f_cargos/', views.FullCargoCreateView.as_view(), name='create_f_cargos'),
    path('create/invoices/', views.InvoiceCreateView.as_view(), name='create_invoices'),
    path('create/expenses/', views.ExpensesCreateView.as_view(), name='create_expenses'),
    path('create/products/', views.ProductCreateView.as_view(), name='create_products'),
    path('deliveries_form/', views.DeliveryCreateView.as_view(), name='create_deliveries'),
    path('vehicles_form/', views.DeliveryVehicleCreateView.as_view(), name='create_vehicles'),
    path('product_quotes_form/', views.ProductQuoteCreateView.as_view(), name='create_product_quotes'),
    path('shipping_quotes_form/', views.ShippingQuoteCreateView.as_view(), name='create_shipping_quotes'),
    path('products_shipping_quotes_form/', views.ProductShippingQuoteCreateView.as_view(), name='create_products_shipping_quotes'),
    path('create_delivery/<str:cargo_ids>/', views.create_delivery, name='create_delivery'),
    


    path('l_container/<int:pk>/', views.LooseContainerDetailView.as_view(), name='l_container'),
    path('l_cargos/<int:pk>/', views.LooseCargoDetailView.as_view(), name='l_cargo'),
    path('f_containers/<int:pk>/', views.FullContainerDetailView.as_view(), name='f_container'),
    path('f_cargos/<int:pk>/', views.FullCargoDetailView.as_view(), name='f_cargo'),
    path('invoices/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice'),
    path('expenses/<int:pk>/', views.ExpensesDetailView.as_view(), name='expense'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('delivery/<int:pk>/', views.DeliveryDetailView.as_view(), name='delivery'),
    path('shippingquote/<int:pk>/', views.ShippingQuoteDetailView.as_view(), name='shipping_quote'),

    path('update_invoices/<int:pk>/', other_views.update_invoice_number, name='update_invoice_number'),

    path('gen-inv/<str:invoice_number>/', other_views.generate_invoice, name='generate_invoice'),
    path('share-inv/<str:invoice_number>/', other_views.share_invoice, name='share_invoice'),
    path('softsignup/', views.softsignup, name='softsignup'),
    path('404/', views.error_handler, name='error_handler'),



    # utility
    path('deliver_cargo/', views.deliver_cargo, name='deliver_cargo'),
    path('generate_fullco_packing_list/<int:container_id>/', other_views.generate_fullco_packing_list, name='generate_fullco_packing_list'),
    path('generate_looseco_packing_list/<int:container_id>/', other_views.generate_looseco_packing_list, name='generate_looseco_packing_list'),


    
] 
