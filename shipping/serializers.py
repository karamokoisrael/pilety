# from rest_framework import serializers

# from shipping.models import (Shipment, Vehicle, 
#                              LooseContainer, FullContainer, 
#                              LooseCargo, FullCargo,
#                              LooseCargoInvoice, FullCargoInvoice,
#                              )
# # class CustomerAddressSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = CustomerAddress
# #         field = [ 'address', 'city', 'postal', 'state', 'country']
# #         read_only_fields = ['id', 'customer']

# # class CustomerSerializer(serializers.HyperlinkedModelSerializer):
# #     # images = AddressSerializer(many=True,)
# #     # reviews = ReviewSerializer(many=True,)
# #     address = CustomerAddressSerializer(many=True)
    
# #     class Meta:
# #         model = Customer
# #         fields =['telephone', 'email', 'notes', 'mc_number']
# #         read_only_fields = ['id']


# #     def create(self, validated_data):
# #         # images_data = self.context.get('view').request.FILES
# #         address_data = validated_data.pop('address', [])
# #         customer = Customer.objects.create(**validated_data)

        
# #         # create new reviews
# #         for address_datrum in address_data:
# #             CustomerAddress.objects.create(customer=customer, **address_datrum)

# #         # create new image
# #         # for image_data in images_data.values():
# #         #     Images.objects.create(product=product, image=image_data)

# #         return customer
 
# class ShipmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shipment
#         fields = '__all__'


# class VehicleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vehicle
#         fields = '__all__'


# class LooseContainerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LooseContainer
#         fields = '__all__'


# class FullContainerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FullContainer
#         fields = '__all__'


# class LooseCargoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LooseCargo
#         fields = '__all__'


# class FullCargoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FullCargo
#         fields = '__all__'


# class LooseCargoInvoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LooseCargoInvoice
#         fields = '__all__'


# class FullCargoInvoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FullCargoInvoice
#         fields = '__all__'
