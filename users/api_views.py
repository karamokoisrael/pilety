from rest_framework import generics, permissions

from users.models import (Customer, CustomerAddress,
                          Supplier, SupplierAddress,
                          Shipper, ShipperAddress,
                          Consignee, ConsigneeAddress,
                          Driver, DriverAddress,
                          Dispatcher, DispatcherAddress,
                          )
from users.serializers import (CustomerSerializer, CustomerAddressSerializer,
                               SupplierSerializer, SupplierAddressSerializer,
                               ShipperSerializer, ShipperAddressSerializer,
                               ConsigneeSerializer, ConsigneeAddressSerializer,
                               DriverSerializer, DriverAddressSerializer,
                               DispatcherSerializer, DispatcherAddressSerializer
                               )


# ListAPIViews
class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.AllowAny, )


class CustomerAddressListAPIView(generics.ListAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
    permission_classes = (permissions.AllowAny, )


class SupplierListAPIView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (permissions.AllowAny, )


class SupplierAddressListAPIView(generics.ListAPIView):
    queryset = SupplierAddress.objects.all()
    serializer_class = SupplierAddressSerializer
    permission_classes = (permissions.AllowAny, )


class ShipperListAPIView(generics.ListAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer
    permission_classes = (permissions.AllowAny, )


class ShipperAddressListAPIView(generics.ListAPIView):
    queryset = ShipperAddress.objects.all()
    serializer_class = ShipperAddressSerializer
    permission_classes = (permissions.AllowAny, )


class ConsigneeListAPIView(generics.ListAPIView):
    queryset = Consignee.objects.all()
    serializer_class = ConsigneeSerializer
    permission_classes = (permissions.AllowAny, )


class ConsigneeAddressListAPIView(generics.ListAPIView):
    queryset = ConsigneeAddress.objects.all()
    serializer_class = ConsigneeAddressSerializer
    permission_classes = (permissions.AllowAny, )


class DriverListAPIView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (permissions.AllowAny, )


class DriverAddressListAPIView(generics.ListAPIView):
    queryset = DriverAddress.objects.all()
    serializer_class = DriverAddressSerializer
    permission_classes = (permissions.AllowAny, )


class DispatcherListAPIView(generics.ListAPIView):
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializer
    permission_classes = (permissions.AllowAny, )


class DispatcherAddressListAPIView(generics.ListAPIView):
    queryset = DispatcherAddress.objects.all()
    serializer_class = DispatcherAddressSerializer
    permission_classes = (permissions.AllowAny, )


# #RetrieveAPIViews
# class ProductDetailsAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = 
#     permission_classes = (permissions.AllowAny, )


#RetrieveUpdateDestroyAPIViews

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class CustomerAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class SupplierAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierAddress.objects.all()
    serializer_class = SupplierAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ShipperRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ShipperAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShipperAddress.objects.all()
    serializer_class = ShipperAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ConsigneeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consignee.objects.all()
    serializer_class = ConsigneeSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ConsigneeAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsigneeAddress.objects.all()
    serializer_class = ConsigneeAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class DriverRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class DriverAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DriverAddress.objects.all()
    serializer_class = DriverAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class DispatcherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class DispatcherAddressListAPIView(generics.ListAPIView):
    queryset = DispatcherAddress.objects.all()
    serializer_class = DispatcherAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


#RetrieveUpdateDestroyAPIView
'''class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ This view enables creations and listings in the api for Product class  """

    serializer_class = 
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user =  self.request.user
        return Product.objects.filter(supplier=user).order_by('name')
'''

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CustomerAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (permissions.IsAuthenticated, )


class SupplierAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierAddress.objects.all()
    serializer_class = SupplierAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ShipperRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ShipperAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShipperAddress.objects.all()
    serializer_class = ShipperAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ConsigneeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consignee.objects.all()
    serializer_class = ConsigneeSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ConsigneeAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConsigneeAddress.objects.all()
    serializer_class = ConsigneeAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DriverRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DriverAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DriverAddress.objects.all()
    serializer_class = DriverAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DispatcherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispatcher.objects.all()
    serializer_class = DispatcherSerializer
    permission_classes = (permissions.IsAuthenticated, )


class DispatcherAddressListAPIView(generics.ListAPIView):
    queryset = DispatcherAddress.objects.all()
    serializer_class = DispatcherAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )

   