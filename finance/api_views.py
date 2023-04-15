from rest_framework import generics, permissions

from finance.models import (Account, Company, CompanyAddress, Deposit,
                            Expenses, Invoice, Product, Transfer)


from finance.serializers import (CompanySerializer, CompanyAddressSerializer,
                            AccountSerializer, DepositSerializer,
                            ExpensesSerializer, TransferSerializer, 
                            ProductSerializer, InvoiceSerializer
                            ) 


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


class DepositListAPIView(generics.ListAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = (permissions.AllowAny, )


class ExpensesListAPIView(generics.ListAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = (permissions.AllowAny, )


class TransferListAPIView(generics.ListAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = (permissions.AllowAny, )


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )


class InvoiceListAPIView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
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


class DepositListCreateAPIView(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ExpensesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class TransferListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        pass

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
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


class DepositRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = (permissions.AllowAny, )


class ExpensesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
    permission_classes = (permissions.AllowAny, )


class TransferRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = (permissions.AllowAny, )


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny, )


class InvoiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (permissions.AllowAny, )

