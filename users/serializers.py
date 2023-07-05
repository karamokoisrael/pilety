from rest_framework import serializers
from users.models import (User, UserAddress
                          )

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        field = [ 'address', 'city', 'postal', 'state', 'country']
        read_only_fields = ['id', 'user']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # images = UserAddressSerializer(many=True,)
    # reviews = ReviewSerializer(many=True,)
    address = UserAddressSerializer(many=True)
    
    class Meta:
        model = User
        fields =['telephone', 'email', 'notes', 'mc_number']
        read_only_fields = ['id']


    def create(self, validated_data):
        # images_data = self.context.get('view').request.FILES
        address_data = validated_data.pop('address', [])
        user = User.objects.create(**validated_data)

        
        # create new reviews
        for address_datrum in address_data:
            Address.objects.create(user=user, **address_datrum)

        # create new image
        # for image_data in images_data.values():
        #     Images.objects.create(product=product, image=image_data)

        return user
 

# class SupplierAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SupplierAddress
#         field = ['supplier', 'address', 'city', 'postal', 'state', 'country']
#         read_only_fields = ['id']

# class SupplierSerializer(serializers.HyperlinkedModelSerializer):
#     # images = AddressSerializer(many=True,)
#     # reviews = ReviewSerializer(many=True,)
#     address = SupplierAddressSerializer(many=True)
    
#     class Meta:
#         model = Supplier
#         fields =['telephone', 'email', 'notes', 'company', 'wechat', 'bzness_card']
#         read_only_fields = ['id']


#     def create(self, validated_data):
#         # images_data = self.context.get('view').request.FILES
#         address_data = validated_data.pop('address', [])
#         supplier = Supplier.objects.create(**validated_data)

        
#         # create new reviews
#         for address_datrum in address_data:
#             SupplierAddress.objects.create(supplier=supplier, **address_datrum)

#         # create new image
#         # for image_data in images_data.values():
#         #     Images.objects.create(product=product, image=image_data)

#         return supplier
 

# class ShipperAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShipperAddress
#         field = ['shipper', 'address', 'city', 'postal', 'state', 'country']
#         read_only_fields = ['id']

# class ShipperSerializer(serializers.HyperlinkedModelSerializer):
#     # images = AddressSerializer(many=True,)
#     # reviews = ReviewSerializer(many=True,)
#     address = ShipperAddressSerializer(many=True)
    
#     class Meta:
#         model = Shipper
#         fields =['telephone', 'email', 'notes', 'company', 'contact', 'ext']
#         read_only_fields = ['id']


#     def create(self, validated_data):
#         # images_data = self.context.get('view').request.FILES
#         address_data = validated_data.pop('address', [])
#         shipper = Shipper.objects.create(**validated_data)

        
#         # create new reviews
#         for address_datrum in address_data:
#             ShipperAddress.objects.create(shipper=shipper, **address_datrum)

#         # create new image
#         # for image_data in images_data.values():
#         #     Images.objects.create(product=product, image=image_data)

#         return shipper
 

# class ConsigneeAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ConsigneeAddress
#         field = ['consignee', 'address', 'city', 'postal', 'state', 'country']
#         read_only_fields = ['id']

# class ConsigneeSerializer(serializers.HyperlinkedModelSerializer):
#     # images = AddressSerializer(many=True,)
#     # reviews = ReviewSerializer(many=True,)
#     address = ConsigneeAddressSerializer(many=True)
    
#     class Meta:
#         model = Consignee
#         fields =['telephone', 'email', 'notes', 'contact_person', 'type', 'mc_number']
#         read_only_fields = ['id']


#     def create(self, validated_data):
#         # images_data = self.context.get('view').request.FILES
#         address_data = validated_data.pop('address', [])
#         consignee = ConsigneeAddress.objects.create(**validated_data)

        
#         # create new reviews
#         for address_datrum in address_data:
#             ConsigneeAddress.objects.create(consignee=consignee, **address_datrum)

#         # create new image
#         # for image_data in images_data.values():
#         #     Images.objects.create(product=product, image=image_data)

#         return consignee
 

# class DriverAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DriverAddress
#         field = ['dispatcher', 'address', 'city', 'postal', 'state', 'country']
#         read_only_fields = ['id']

# class DriverSerializer(serializers.HyperlinkedModelSerializer):
#     # images = AddressSerializer(many=True,)
#     # reviews = ReviewSerializer(many=True,)
#     address = DriverAddressSerializer(many=True)
    
#     class Meta:
#         model = Driver
#         fields =['telephone', 'email', 'notes',]
#         read_only_fields = ['id']


#     def create(self, validated_data):
#         # images_data = self.context.get('view').request.FILES
#         address_data = validated_data.pop('address', [])
#         driver = Driver.objects.create(**validated_data)

        
#         # create new reviews
#         for address_datrum in address_data:
#             DriverAddress.objects.create(driver=driver, **address_datrum)

#         # create new image
#         # for image_data in images_data.values():
#         #     Images.objects.create(product=product, image=image_data)

#         return driver
 

# class DispatcherAddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DispatcherAddress
#         field = ['dispatcher', 'address', 'city', 'postal', 'state', 'country']
#         read_only_fields = ['id']


# class DispatcherSerializer(serializers.HyperlinkedModelSerializer):
#     # images = AddressSerializer(many=True,)
#     # reviews = ReviewSerializer(many=True,)
#     address = DispatcherAddressSerializer(many=True)
    
#     class Meta:
#         model = Dispatcher
#         fields =['telephone', 'email', 'notes', 'phone', 'rate']
#         read_only_fields = ['id']


#     def create(self, validated_data):
#         # images_data = self.context.get('view').request.FILES
#         address_data = validated_data.pop('address', [])
#         dispatcher = Dispatcher.objects.create(**validated_data)

        
#         # create new reviews
#         for address_datrum in address_data:
#             DispatcherAddress.objects.create(dispatcher=dispatcher, **address_datrum)

#         # create new image
#         # for image_data in images_data.values():
#         #     Images.objects.create(product=product, image=image_data)

#         return dispatcher
 

