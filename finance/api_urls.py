from django.urls import path

from finance.api_views import (AccountListAPIView, AccountListCreateAPIView,
                               AccountRetrieveUpdateDestroyAPIView,
                               CompanyAddressListAPIView,
                               CompanyAddressListCreateAPIView,
                               CompanyAddressRetrieveUpdateDestroyAPIView,
                               CompanyListAPIView, CompanyListCreateAPIView,
                               CompanyRetrieveUpdateDestroyAPIView)


app_name = 'finance'

urlpatterns = [
    path('company/', CompanyListAPIView.as_view()),
    path('company/address/', CompanyAddressListAPIView.as_view()),
    path('bank/ac/', AccountListAPIView.as_view()),
    
    path('company/', CompanyListCreateAPIView.as_view()),
    path('company/address/', CompanyAddressListCreateAPIView.as_view()),
    path('bank/ac/', AccountListCreateAPIView.as_view()),
    
    path('company/', CompanyRetrieveUpdateDestroyAPIView.as_view()),
    path('company/address/', CompanyAddressRetrieveUpdateDestroyAPIView.as_view()),
    path('bank/ac/', AccountRetrieveUpdateDestroyAPIView.as_view()),
        
]
