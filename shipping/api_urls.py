# from django.urls import path
# from shipping.api_views import (
#                     ShipmentListAPIView, VehicleListAPIView, 
#                     LooseContainerListAPIView, FullContainerListAPIView, 
#                     LooseCargoListAPIView, FullCargoListAPIView,
#                     LooseCargoInvoiceListAPIView, FullCargoInvoiceListAPIView,
                    
#                     ShipmentListCreateAPIView, 
#                     VehicleListCreateAPIView, 
#                     LooseContainerListCreateAPIView, 
#                     FullContainerListCreateAPIView, 
#                     LooseCargoListCreateAPIView, 
#                     FullCargoListCreateAPIView,
#                     LooseCargoInvoiceListCreateAPIView, 
#                     FullCargoInvoiceListCreateAPIView,
                    
#                     ShipmentRetrieveUpdateDestroyAPIView, 
#                     VehicleRetrieveUpdateDestroyAPIView, 
#                     LooseContainerRetrieveUpdateDestroyAPIView, 
#                     FullContainerRetrieveUpdateDestroyAPIView, 
#                     LooseCargoRetrieveUpdateDestroyAPIView, 
#                     FullCargoRetrieveUpdateDestroyAPIView,
#                     LooseCargoInvoiceRetrieveUpdateDestroyAPIView, 
#                     FullCargoInvoiceRetrieveUpdateDestroyAPIView,
#                     )



# app_name = 'shipping'

# urlpatterns = [
#     path('shipment/',  ShipmentListAPIView.as_view()),
#     path('vehicle/',  VehicleListAPIView.as_view()),
#     path('lco/',  LooseContainerListAPIView.as_view()),
#     path('fco/',  FullContainerListAPIView.as_view()),
#     path('lca/',  LooseCargoListAPIView.as_view()),
#     path('fca/',  FullCargoListAPIView.as_view()),
#     path('lcai/',  LooseCargoInvoiceListAPIView.as_view()),
#     path('fcai/',  FullCargoInvoiceListAPIView.as_view()),

#     #ListCreateApi Views
#     path('list_create_shipment/',  ShipmentListCreateAPIView.as_view()),
#     path('list_create_vehicle/',  VehicleListCreateAPIView.as_view()),
#     path('list_create_lco/',  LooseContainerListCreateAPIView.as_view()),
#     path('list_create_fco/',  FullContainerListCreateAPIView.as_view()),
#     path('list_create_lca/',  LooseCargoListCreateAPIView.as_view()),
#     path('list_create_fca/',  FullCargoListCreateAPIView.as_view()),
#     path('list_create_lcai/',  LooseCargoInvoiceListCreateAPIView.as_view()),
#     path('list_create_fcai/',  FullCargoInvoiceListCreateAPIView.as_view()),

#         #Update details views
#     # path('_detail/<int:pk>/',  ),
#     # path('_detail/<int:pk>/',  ),

#     # Update retrieve destroy
#     # path('_detail/<int:pk>/',  ),
#     path('shipment_detail/<int:pk>/',  ShipmentRetrieveUpdateDestroyAPIView.as_view()),
#     path('vehicle_detail/<int:pk>/',  VehicleRetrieveUpdateDestroyAPIView.as_view()),
#     path('lco_detail/<int:pk>/',  LooseContainerRetrieveUpdateDestroyAPIView.as_view()),
#     path('fco_detail/<int:pk>/',  FullContainerRetrieveUpdateDestroyAPIView.as_view()),
#     path('lca_detail/<int:pk>/',  LooseCargoRetrieveUpdateDestroyAPIView.as_view()),
#     path('fca_detail/<int:pk>/',  FullCargoRetrieveUpdateDestroyAPIView.as_view()),
#     path('lcai_detail/<int:pk>/',  LooseCargoInvoiceRetrieveUpdateDestroyAPIView.as_view()),
#     path('fcai_detail/<int:pk>/',  FullCargoInvoiceRetrieveUpdateDestroyAPIView.as_view()),
    
    
# ]