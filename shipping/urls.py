from django.urls import path
from .views import (
    

    LooseContainerListView,
    LooseContainerDetailView,
    LooseContainerCreateView,

    FullContainerListView,
    FullContainerDetailView,
    FullContainerCreateView,

    LooseCargoListView,
    LooseCargoDetailView,
    LooseCargoCreateView,

    FullCargoListView,
    FullCargoDetailView,
    FullCargoCreateView,

    LooseCargoInvoiceListView,
    LooseCargoInvoiceDetailView,
    LooseCargoInvoiceCreateView,

    FullCargoInvoiceListView,
    FullCargoInvoiceDetailView,
    FullCargoInvoiceCreateView,
)
from .other_views import (Homepage,
                          AboutPage,
                          ContactPage,
                          PolicyPage,
                        #   RequestPage,
                          ServicesPage,
                          TeamPage,
                          TermsPage,
                          WhyUsPage
                          )

app_name = 'shipping'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('about/', AboutPage.as_view(), name='about'),
    path('contact', ContactPage.as_view(), name='contact'),
    path('policy', PolicyPage.as_view(), name='policy'),
    path('services', ServicesPage.as_view(), name='services'),
    path('team', TeamPage.as_view(), name='team'),
    path('terms', TermsPage.as_view(), name='terms'),
    path('why-choose-us', WhyUsPage.as_view(), name='whyus'),
    # path('', Homepage.as_view(), name='homepage'),
    # path('', Homepage.as_view(), name='homepage'),

    path('loose-containers/', LooseContainerListView.as_view(), 
                                    name='loose_container_list'),
    path('loose-containers-create/', LooseContainerCreateView.as_view(), 
                                    name='loose_container_create'),
    path('loose-containers/<int:pk>/', LooseContainerDetailView.as_view(), 
                                    name='loose_container_detail'),

    path('full-containers/', FullContainerListView.as_view(), 
                                    name='full_container_list'),
    path('full-containers-create/', FullContainerCreateView.as_view(), 
                                    name='full_container_create'),
    path('full-containers/<int:pk>/', FullContainerDetailView.as_view(), 
                                    name='full_container_detail'),

    path('loose-cargos/', LooseCargoListView.as_view(), 
                                    name='loose_cargo_list'),
    path('loose-cargos-create/', LooseCargoCreateView.as_view(), 
                                    name='loose_cargo_create'),
    path('loose-cargos/<int:pk>/', LooseCargoDetailView.as_view(), 
                                    name='loose_cargo_detail'),

    path('full-cargos/', FullCargoListView.as_view(), 
                                    name='full_cargo_list'),
    path('full-cargos-create/', FullCargoCreateView.as_view(), 
                                    name='full_cargo_create'),
    path('full-cargos/<int:pk>/', FullCargoDetailView.as_view(), 
                                    name='full_cargo_detail'),

    path('loose-cargo-invoices/', LooseCargoInvoiceListView.as_view(), 
                                    name='loose_cargo_invoice_list'),
    path('loose-cargo-invoices-create/', LooseCargoInvoiceCreateView.as_view(), 
                                    name='loose_cargo_invoice_create'),
    path('loose-cargo-invoices/<int:pk>/', LooseCargoInvoiceDetailView.as_view(), 
                                    name='loose_cargo_invoice_detail'),
    
    path('full-cargo-invoices/', FullCargoInvoiceListView.as_view(), 
                                    name='full_cargo_invoice_list'),
    path('full-cargo-invoices-create/', FullCargoInvoiceCreateView.as_view(), 
                                    name='full_cargo_invoice_create'),
    path('full-cargo-invoices/<int:pk>/', FullCargoInvoiceDetailView.as_view(), 
                                    name='full_cargo_invoice_detail'),
]
