from django.urls import path
from allin.views import (
    LooseContainerListView,
    LooseCargoListView,
    FullCargoListView,
    FullContainerListView,
    InvoiceListView,
    ExpensesListView,
    ProductListView,

    LooseContainerCreateView,
    LooseCargoCreateView,
    FullContainerCreateView,
    FullCargoCreateView,
    InvoiceCreateView,
    ExpensesCreateView,
    ProductCreateView,

    LooseContainerDetailView,
    LooseCargoDetailView,
    FullCargoDetailView,
    FullContainerDetailView,
    InvoiceDetailView,
    ExpensesDetailView,
    ProductDetailView,
)

app_name = 'allin'

urlpatterns = [
    path('l_containers/', LooseContainerListView.as_view(), name='l_containers'),
    path('l_cargos/', LooseCargoListView.as_view(), name='l_cargos'),
    path('f_containers/', FullContainerListView.as_view(), name='f_containers'),
    path('f_cargos/', FullCargoListView.as_view(), name='f_cargos'),
    path('invoices/', InvoiceListView.as_view(), name='invoices'),
    path('expenses/', InvoiceListView.as_view(), name='expenses'),
    path('products/', ProductListView.as_view(), name='products'),
    

    path('create/l_containers/', LooseContainerCreateView.as_view(), name='create_l_containers'),
    path('create/l_cargos/', LooseCargoCreateView.as_view(), name='create_l_cargos'),
    path('create/f_containers/', FullContainerCreateView.as_view(), name='create_f_containers'),
    path('create/f_cargos/', FullCargoCreateView.as_view(), name='create_f_cargos'),
    path('create/invoices/', InvoiceCreateView.as_view(), name='create_invoices'),
    path('create/expences/', ExpensesCreateView.as_view(), name='create_expences'),
    path('create/products/', ProductCreateView.as_view(), name='create_products'),
    

    path('l_containers/<int:pk>/', LooseContainerDetailView.as_view(), name='l_container'),
    path('l_cargos/<int:pk>/', LooseCargoDetailView.as_view(), name='l_cargo'),
    path('f_containers/<int:pk>/', FullContainerDetailView.as_view(), name='f_container'),
    path('f_cargos/<int:pk>/', FullCargoDetailView.as_view(), name='f_cargo'),
    path('invoices/<int:pk>/', InvoiceDetailView.as_view(), name='invoice'),
    path('expenses/<int:pk>/', ExpensesDetailView.as_view(), name='expense'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
    
]
