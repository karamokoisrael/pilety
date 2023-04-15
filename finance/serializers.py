from rest_framework import serializers
from finance.models import (Company, CompanyAddress,
                            Account, Deposit,
                            Expenses, Transfer, 
                            Product, Invoice
                            ) 

# class CustomerAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerAddress
#         field = [ 'address', 'city', 'postal', 'state', 'country']
#         read_only_fields = ['id', 'customer']

# class CustomerSerializer(serializers.HyperlinkedModelSerializer):
#     # images = AddressSerializer(many=True,)
#     # reviews = ReviewSerializer(many=True,)
#     address = CustomerAddressSerializer(many=True)
    
#     class Meta:
#         model = Customer
#         fields =['telephone', 'email', 'notes', 'mc_number']
#         read_only_fields = ['id']


#     def create(self, validated_data):
#         # images_data = self.context.get('view').request.FILES
#         address_data = validated_data.pop('address', [])
#         customer = Customer.objects.create(**validated_data)

        
#         # create new reviews
#         for address_datrum in address_data:
#             CustomerAddress.objects.create(customer=customer, **address_datrum)

#         # create new image
#         # for image_data in images_data.values():
#         #     Images.objects.create(product=product, image=image_data)

#         return customer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAddress
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

