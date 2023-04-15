from django.urls import path

from finance.api_views import (AccountListAPIView, AccountListCreateAPIView,
                               AccountRetrieveUpdateDestroyAPIView,
                               CompanyAddressListAPIView,
                               CompanyAddressListCreateAPIView,
                               CompanyAddressRetrieveUpdateDestroyAPIView,
                               CompanyListAPIView, CompanyListCreateAPIView,
                               CompanyRetrieveUpdateDestroyAPIView,
                               DepositListAPIView, DepositListCreateAPIView,
                               DepositRetrieveUpdateDestroyAPIView,
                               ExpensesListAPIView, ExpensesListCreateAPIView,
                               ExpensesRetrieveUpdateDestroyAPIView,
                               InvoiceListAPIView, InvoiceListCreateAPIView,
                               InvoiceRetrieveUpdateDestroyAPIView,
                               ProductListAPIView, ProductListCreateAPIView,
                               ProductRetrieveUpdateDestroyAPIView,
                               TransferListAPIView, TransferListCreateAPIView,
                               TransferRetrieveUpdateDestroyAPIView)


app_name = 'finance'

urlpatterns = [
    path('company/', CompanyListAPIView.as_view()),
    path('company/address/', CompanyAddressListAPIView.as_view()),
    path('bank/ac/', AccountListAPIView.as_view()),
    path('deposit/', DepositListAPIView.as_view()),
    path('expenses/', ExpensesListAPIView.as_view()),
    path('transfer/', TransferListAPIView.as_view()),
    path('product/', ProductListAPIView.as_view()),
    path('invoice/', InvoiceListAPIView.as_view()),

    path('company/', CompanyListCreateAPIView.as_view()),
    path('company/address/', CompanyAddressListCreateAPIView.as_view()),
    path('bank/ac/', AccountListCreateAPIView.as_view()),
    path('deposit/', DepositListCreateAPIView.as_view()),
    path('expenses/', ExpensesListCreateAPIView.as_view()),
    path('transfer/', TransferListCreateAPIView.as_view()),
    path('product/', ProductListCreateAPIView.as_view()),
    path('invoice/', InvoiceListCreateAPIView.as_view()),

    path('company/', CompanyRetrieveUpdateDestroyAPIView.as_view()),
    path('company/address/', CompanyAddressRetrieveUpdateDestroyAPIView.as_view()),
    path('bank/ac/', AccountRetrieveUpdateDestroyAPIView.as_view()),
    path('deposit/', DepositRetrieveUpdateDestroyAPIView.as_view()),
    path('expenses/', ExpensesRetrieveUpdateDestroyAPIView.as_view()),
    path('transfer/', TransferRetrieveUpdateDestroyAPIView.as_view()),
    path('product/', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('invoice/', InvoiceRetrieveUpdateDestroyAPIView.as_view()),

    
]
