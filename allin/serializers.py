from rest_framework import serializers
from allin.models import (LooseCargo, LooseContainer, FullCargo, 
                        FullContainer, Invoice, Expense, ExpenseCategory, Product,
                        ProductQuote, ProductQuoteImages, ShippingQuote, 
                        ProductShippingQuote, Delivery, DeliveryVehicle,)



class LooseCargoSerializer(serializers.Serializer):
    
    class Meta:
        model = LooseCargo

class LooseContainerSerializer(serializers.Serializer):
    
    class Meta:
        model = LooseContainer

class FullCargoSerializer(serializers.Serializer):
    
    class Meta:
        model = FullCargo

class FullContainerSerializer(serializers.Serializer):
    
    class Meta:
        model = FullContainer

class InvoiceSerializer(serializers.Serializer):
    
    class Meta:
        model = Invoice

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'

class ExpenseSerializer(serializers.Serializer):
    category = ExpenseCategorySerializer()
    class Meta:
        model = Expense
        fields = '__all__'

class ProductSerializer(serializers.Serializer):
    
    class Meta:
        model = Product


class DeliverySerializer(serializers.Serializer):
    
    class Meta:
        model = Delivery

class DeliveryVehicleSerializer(serializers.Serializer):
    
    class Meta:
        model = DeliveryVehicle

class ProductQuoteSerializer(serializers.Serializer):
    
    class Meta:
        model = ProductQuote

class ProductQuoteImagesSerializer(serializers.Serializer):
    
    class Meta:
        model = ProductQuoteImages

class ShippingQuoteSerializer(serializers.Serializer):
    
    class Meta:
        model = ShippingQuote

class ProductShippingQuoteSerializer(serializers.Serializer):
    
    class Meta:
        model = ProductShippingQuote

