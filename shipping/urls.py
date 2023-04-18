from django.urls import path
from .views import (
    Homepage,
    
    LooseContainerListView,
    LooseContainerDetailView,
    FullContainerListView,
    FullContainerDetailView,
    LooseCargoListView,
    LooseCargoDetailView,
    FullCargoListView,
    FullCargoDetailView,
    LooseCargoInvoiceListView,
    LooseCargoInvoiceDetailView,
    FullCargoInvoiceListView,
    FullCargoInvoiceDetailView,
)

app_name = 'shipping'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),

    path('loose-containers/', LooseContainerListView.as_view(), name='loose_container_list'),
    path('loose-containers/<int:pk>/', LooseContainerDetailView.as_view(), name='loose_container_detail'),
    path('full-containers/', FullContainerListView.as_view(), name='full_container_list'),
    path('full-containers/<int:pk>/', FullContainerDetailView.as_view(), name='full_container_detail'),
    path('loose-cargos/', LooseCargoListView.as_view(), name='loose_cargo_list'),
    path('loose-cargos/<int:pk>/', LooseCargoDetailView.as_view(), name='loose_cargo_detail'),
    path('full-cargos/', FullCargoListView.as_view(), name='full_cargo_list'),
    path('full-cargos/<int:pk>/', FullCargoDetailView.as_view(), name='full_cargo_detail'),
    path('loose-cargo-invoices/', LooseCargoInvoiceListView.as_view(), name='loose_cargo_invoice_list'),
    path('loose-cargo-invoices/<int:pk>/', LooseCargoInvoiceDetailView.as_view(), name='loose_cargo_invoice_detail'),
    path('full-cargo-invoices/', FullCargoInvoiceListView.as_view(), name='full_cargo_invoice_list'),
    path('full-cargo-invoices/<int:pk>/', FullCargoInvoiceDetailView.as_view(), name='full_cargo_invoice_detail'),
]
