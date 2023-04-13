from django.contrib import admin
from django.urls import path, include
# from users.api_views import *
from users.api_views import (CustomerListAPIView, CustomerAddressListAPIView,
                             SupplierListAPIView, SupplierAddressListAPIView,
                             ShipperListAPIView, ShipperAddressListAPIView,
                             ConsigneeListAPIView, ConsigneeAddressListAPIView,
                             DriverListAPIView, DriverAddressListAPIView,
                             DispatcherListAPIView,DispatcherAddressListAPIView,
                             
                             CustomerRetrieveUpdateDestroyAPIView,
                             CustomerAddressRetrieveUpdateDestroyAPIView,
                             SupplierRetrieveUpdateDestroyAPIView,
                             SupplierAddressRetrieveUpdateDestroyAPIView,
                             ShipperRetrieveUpdateDestroyAPIView,
                             ShipperAddressRetrieveUpdateDestroyAPIView,
                             ConsigneeRetrieveUpdateDestroyAPIView,
                             ConsigneeAddressRetrieveUpdateDestroyAPIView,
                             DriverRetrieveUpdateDestroyAPIView,
                             DriverAddressRetrieveUpdateDestroyAPIView,
                             DispatcherRetrieveUpdateDestroyAPIView,
                             DispatcherAddressRetrieveUpdateDestroyAPIView,

                             )
app_name = 'users'
urlpatterns = [
    # ListApi
    path('customer/', CustomerListAPIView .as_view()),
    path('customer/ad/', CustomerAddressListAPIView.as_view()),
    path('supplier/', SupplierListAPIView.as_view()),
    path('supplier/ad/', SupplierAddressListAPIView.as_view()),
    path('shipper/', ShipperListAPIView.as_view()),
    path('shipper/ad/', ShipperAddressListAPIView.as_view()),
    path('consignee/', ConsigneeListAPIView.as_view()),
    path('consignee/ad/', ConsigneeAddressListAPIView.as_view()),
    path('driver/', DriverListAPIView.as_view()),
    path('driver/ad/', DriverAddressListAPIView.as_view()),
    path('dispatcher/', DispatcherListAPIView.as_view()),
    path('dispatcher/ad/', DispatcherAddressListAPIView.as_view()),
    
    #ListCreateApi Views 
    # path('list_create_customer/', CustomerCreateListAPIView .as_view()),
    # path('list_create_customer/ad/', CustomerAddressCreateListAPIView.as_view()),
    # path('list_create_supplier/', SupplierCreateListAPIView.as_view()),
    # path('list_create_supplier/ad/', SupplierAddressCreateListAPIView.as_view()),
    # path('list_create_shipper/', ShipperCreateListAPIView.as_view()),
    # path('list_create_shipper/ad/', ShipperAddressCreateListAPIView.as_view()),
    # path('list_create_consignee/', ConsigneeCreateListAPIView.as_view()),
    # path('list_create_consignee/ad/', ConsigneeAddressCreateListAPIView.as_view()),
    # path('list_create_driver/', DriverCreateListAPIView.as_view()),
    # path('list_create_driver/ad/', DriverAddressCreateListAPIView.as_view()),
    # path('list_create_dispatcher/', DispatcherCreateListAPIView.as_view()),
    # path('list_create_dispatcher/ad/', DispatcherAddressCreateListAPIView.as_view()),
    
    #Update details views
    # path('_detail/<int:pk>/', .as_view() ),
    # path('_detail/<int:pk>/', .as_view() ),

    # Update retrieve destroy
    # path('_detail/<int:pk>/', .as_view() ),

    path('customer_detail/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView .as_view()),
    path('customer_detail/ad/<int:pk>/', CustomerAddressRetrieveUpdateDestroyAPIView.as_view()),
    path('supplier_detail/<int:pk>/', SupplierRetrieveUpdateDestroyAPIView.as_view()),
    path('supplier_detail/ad/<int:pk>/', SupplierAddressRetrieveUpdateDestroyAPIView.as_view()),
    path('shipper_detail/<int:pk>/', ShipperRetrieveUpdateDestroyAPIView.as_view()),
    path('shipper_detail/ad/<int:pk>/', ShipperAddressRetrieveUpdateDestroyAPIView.as_view()),
    path('consignee_detail/<int:pk>/', ConsigneeRetrieveUpdateDestroyAPIView.as_view()),
    path('consignee_detail/ad/<int:pk>/', ConsigneeAddressRetrieveUpdateDestroyAPIView.as_view()),
    path('driver_detail/<int:pk>/', DriverRetrieveUpdateDestroyAPIView.as_view()),
    path('driver_detail/ad/<int:pk>/', DriverAddressRetrieveUpdateDestroyAPIView.as_view()),
    path('dispatcher_detail/<int:pk>/', DispatcherRetrieveUpdateDestroyAPIView.as_view()),
    path('dispatcher_detail/ad/<int:pk>/', DispatcherAddressRetrieveUpdateDestroyAPIView.as_view()),
    

]
