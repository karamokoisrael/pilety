from rest_framework import generics, permissions

from users.models import (User, UserAddress,)
from users.serializers import (UserSerializer, UserAddressSerializer,)


# ListAPIViews
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )


class UserAddressListAPIView(generics.ListAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = (permissions.AllowAny, )


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class UserAddressListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class UserAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )


# class SupplierListAPIView(generics.ListAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#     permission_classes = (permissions.AllowAny, )


# class SupplierAddressListAPIView(generics.ListAPIView):
#     queryset = SupplierAddress.objects.all()
#     serializer_class = SupplierAddressSerializer
#     permission_classes = (permissions.AllowAny, )


# class ShipperListAPIView(generics.ListAPIView):
#     queryset = Shipper.objects.all()
#     serializer_class = ShipperSerializer
#     permission_classes = (permissions.AllowAny, )


# class ShipperAddressListAPIView(generics.ListAPIView):
#     queryset = ShipperAddress.objects.all()
#     serializer_class = ShipperAddressSerializer
#     permission_classes = (permissions.AllowAny, )


# class ConsigneeListAPIView(generics.ListAPIView):
#     queryset = Consignee.objects.all()
#     serializer_class = ConsigneeSerializer
#     permission_classes = (permissions.AllowAny, )


# class ConsigneeAddressListAPIView(generics.ListAPIView):
#     queryset = ConsigneeAddress.objects.all()
#     serializer_class = ConsigneeAddressSerializer
#     permission_classes = (permissions.AllowAny, )


# class DriverListAPIView(generics.ListAPIView):
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer
#     permission_classes = (permissions.AllowAny, )


# class DriverAddressListAPIView(generics.ListAPIView):
#     queryset = DriverAddress.objects.all()
#     serializer_class = DriverAddressSerializer
#     permission_classes = (permissions.AllowAny, )


# class DispatcherListAPIView(generics.ListAPIView):
#     queryset = Dispatcher.objects.all()
#     serializer_class = DispatcherSerializer
#     permission_classes = (permissions.AllowAny, )


# class DispatcherAddressListAPIView(generics.ListAPIView):
#     queryset = DispatcherAddress.objects.all()
#     serializer_class = DispatcherAddressSerializer
#     permission_classes = (permissions.AllowAny, )


# #RetrieveAPIViews
# class ProductDetailsAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = 
#     permission_classes = (permissions.AllowAny, )


#RetrieveUpdateDestroyAPIViews


# class SupplierListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class SupplierAddressListCreateAPIView(generics.ListCreateAPIView):
#     queryset = SupplierAddress.objects.all()
#     serializer_class = SupplierAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class ShipperListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Shipper.objects.all()
#     serializer_class = ShipperSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class ShipperAddressListCreateAPIView(generics.ListCreateAPIView):
#     queryset = ShipperAddress.objects.all()
#     serializer_class = ShipperAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class ConsigneeListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Consignee.objects.all()
#     serializer_class = ConsigneeSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class ConsigneeAddressListCreateAPIView(generics.ListCreateAPIView):
#     queryset = ConsigneeAddress.objects.all()
#     serializer_class = ConsigneeAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class DriverListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class DriverAddressListCreateAPIView(generics.ListCreateAPIView):
#     queryset = DriverAddress.objects.all()
#     serializer_class = DriverAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class DispatcherListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Dispatcher.objects.all()
#     serializer_class = DispatcherSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


# class DispatcherAddressListCreateAPIView(generics.ListCreateAPIView):
#     queryset = DispatcherAddress.objects.all()
#     serializer_class = DispatcherAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def get_queryset(self):
#         pass

#     def perform_create(self, serializer):
#         return super().perform_create(serializer)


#RetrieveUpdateDestroyAPIView
'''class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ This view enables creations and listings in the api for Product class  """

    serializer_class = 
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user =  self.request.user
        return Product.objects.filter(supplier=user).order_by('name')
'''



# class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Supplier.objects.all()
#     serializer_class = SupplierSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class SupplierAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SupplierAddress.objects.all()
#     serializer_class = SupplierAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class ShipperRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Shipper.objects.all()
#     serializer_class = ShipperSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class ShipperAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ShipperAddress.objects.all()
#     serializer_class = ShipperAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class ConsigneeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Consignee.objects.all()
#     serializer_class = ConsigneeSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class ConsigneeAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ConsigneeAddress.objects.all()
#     serializer_class = ConsigneeAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class DriverRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class DriverAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DriverAddress.objects.all()
#     serializer_class = DriverAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class DispatcherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Dispatcher.objects.all()
#     serializer_class = DispatcherSerializer
#     permission_classes = (permissions.IsAuthenticated, )


# class DispatcherAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DispatcherAddress.objects.all()
#     serializer_class = DispatcherAddressSerializer
#     permission_classes = (permissions.IsAuthenticated, )

   