from rest_framework import generics, permissions

from finance.models import (Account, Company, CompanyAddress,)


from finance.serializers import (CompanySerializer, CompanyAddressSerializer,
                            AccountSerializer,) 


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.AllowAny, )


class CompanyAddressListAPIView(generics.ListAPIView):
    queryset = CompanyAddress.objects.all()
    serializer_class = CompanyAddressSerializer
    permission_classes = (permissions.AllowAny, )


class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.AllowAny, )


# #RetrieveAPIViews
# class ProductDetailsAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = 
#     permission_classes = (permissions.AllowAny, )



class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class CompanyAddressListCreateAPIView(generics.ListCreateAPIView):
    queryset = CompanyAddress.objects.all()
    serializer_class = CompanyAddressSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class AccountListCreateAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)



# RetrieveUpdateDestroy

class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.AllowAny, )


class CompanyAddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyAddress.objects.all()
    serializer_class = CompanyAddressSerializer
    permission_classes = (permissions.AllowAny, )


class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.AllowAny, )

