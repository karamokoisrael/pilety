# from rest_framework import generics, permissions

# from shipping.models import (Shipment, Vehicle, 
#                              LooseContainer, FullContainer, 
#                              LooseCargo, FullCargo,
#                              LooseCargoInvoice, FullCargoInvoice,
#                              )
# from shipping.serializers import (ShipmentSerializer, VehicleSerializer, 
#                              LooseContainerSerializer, FullContainerSerializer, 
#                              LooseCargoSerializer, FullCargoSerializer,
#                              LooseCargoInvoiceSerializer, FullCargoInvoiceSerializer,
#                              )

# # ListAPIViews
# class ShipmentListAPIView(generics.ListAPIView):
#     queryset = Shipment.objects.all()
#     serializer_class = ShipmentSerializer
#     permission_classes = (permissions.AllowAny, )


# class VehicleListAPIView(generics.ListAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer
#     permission_classes = (permissions.AllowAny, )

# class LooseContainerListAPIView(generics.ListAPIView):
#     queryset = LooseContainer.objects.all()
#     serializer_class =LooseCargoSerializer
#     permission_classes = (permissions.AllowAny, )


# class FullContainerListAPIView(generics.ListAPIView):
#     queryset = FullContainer.objects.all()
#     serializer_class = FullContainerSerializer
#     permission_classes = (permissions.AllowAny, )

# class LooseCargoListAPIView(generics.ListAPIView):
#     queryset = LooseCargo.objects.all()
#     serializer_class =LooseCargoSerializer
#     permission_classes = (permissions.AllowAny, )


# class FullCargoListAPIView(generics.ListAPIView):
#     queryset = FullCargo.objects.all()
#     serializer_class = FullCargoSerializer
#     permission_classes = (permissions.AllowAny, )

# class LooseCargoInvoiceListAPIView(generics.ListAPIView):
#     queryset = LooseCargoInvoice.objects.all()
#     serializer_class = LooseCargoInvoiceSerializer
#     permission_classes = (permissions.AllowAny, )


# class FullCargoInvoiceListAPIView(generics.ListAPIView):
#     queryset = FullCargoInvoice.objects.all()
#     serializer_class = FullCargoInvoiceSerializer
#     permission_classes = (permissions.AllowAny, )



# # #RetrieveAPIViews
# # class ProductDetailsAPIView(generics.RetrieveAPIView):
# #     queryset = Product.objects.all()
# #     serializer_class = 
# #     permission_classes = (permissions.AllowAny, )


# class ShipmentListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Shipment.objects.all()
#     serializer_class = ShipmentSerializer
#     permission_classes = (permissions.AllowAny, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class VehicleListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer
#     permission_classes = (permissions.AllowAny, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)

# class LooseContainerListCreateAPIView(generics.ListCreateAPIView):
#     queryset = LooseContainer.objects.all()
#     serializer_class =LooseCargoSerializer
#     permission_classes = (permissions.AllowAny, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class FullContainerListCreateAPIView(generics.ListCreateAPIView):
#     queryset = FullContainer.objects.all()
#     serializer_class = FullContainerSerializer
#     permission_classes = (permissions.AllowAny, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)

# class LooseCargoListCreateAPIView(generics.ListCreateAPIView):
#     queryset = LooseCargo.objects.all()
#     serializer_class =LooseCargoSerializer
#     permission_classes = (permissions.AllowAny, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class FullCargoListCreateAPIView(generics.ListCreateAPIView):
#     queryset = FullCargo.objects.all()
#     serializer_class = FullCargoSerializer
#     permission_classes = (permissions.AllowAny, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)

# class LooseCargoInvoiceListCreateAPIView(generics.ListCreateAPIView):
#     queryset = LooseCargoInvoice.objects.all()
#     serializer_class = LooseCargoInvoiceSerializer
#     permission_classes = (permissions.AllowAny, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class FullCargoInvoiceListCreateAPIView(generics.ListCreateAPIView):
#     queryset = FullCargoInvoice.objects.all()
#     serializer_class = FullCargoInvoiceSerializer
#     permission_classes = (permissions.AllowAny, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)




# class ShipmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Shipment.objects.all()
#     serializer_class = ShipmentSerializer
#     permission_classes = (permissions.AllowAny, )


# class VehicleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer
#     permission_classes = (permissions.AllowAny, )

# class LooseContainerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = LooseContainer.objects.all()
#     serializer_class =LooseCargoSerializer
#     permission_classes = (permissions.AllowAny, )


# class FullContainerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FullContainer.objects.all()
#     serializer_class = FullContainerSerializer
#     permission_classes = (permissions.AllowAny, )

# class LooseCargoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = LooseCargo.objects.all()
#     serializer_class =LooseCargoSerializer
#     permission_classes = (permissions.AllowAny, )


# class FullCargoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FullCargo.objects.all()
#     serializer_class = FullCargoSerializer
#     permission_classes = (permissions.AllowAny, )

# class LooseCargoInvoiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = LooseCargoInvoice.objects.all()
#     serializer_class = LooseCargoInvoiceSerializer
#     permission_classes = (permissions.AllowAny, )


# class FullCargoInvoiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FullCargoInvoice.objects.all()
#     serializer_class = FullCargoInvoiceSerializer
#     permission_classes = (permissions.AllowAny, )




