from django.urls import path
from allin.views import (
    LooseContainerListView,
    LooseCargoListView,
    InvoiceListView,
    ProductListView,

    LooseContainerCreateView,
    LooseCargoCreateView,
    InvoiceCreateView,
    ProductCreateView,

    LooseContainerDetailView,
    LooseCargoDetailView,
    InvoiceDetailView,
    ProductDetailView,
)

app_name = 'allin'

urlpatterns = [
    path('containers/', LooseContainerListView.as_view(), name='containers'),
    path('cargos/', LooseCargoListView.as_view(), name='cargos'),
    path('invoices/', InvoiceListView.as_view(), name='invoices'),
    path('products/', ProductListView.as_view(), name='products'),
    

    path('create/containers/', LooseContainerCreateView.as_view(), name='create_containers'),
    path('create/cargos/', LooseCargoCreateView.as_view(), name='create_cargos'),
    path('create/invoices/', InvoiceCreateView.as_view(), name='create_invoices'),
    path('create/products/', ProductCreateView.as_view(), name='create_products'),
    

    path('containers/<int:pk>/', LooseContainerDetailView.as_view(), name='container'),
    path('cargos/<int:pk>/', LooseCargoDetailView.as_view(), name='cargo'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
    
]
