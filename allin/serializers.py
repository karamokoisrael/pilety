from rest_framework import serializers
from allin.models import LooseCargo, LooseContainer, Invoice, Product



class LooseCargoSerializer(serializers.Serializer):
    
    class Meta:
        model = LooseCargo

class LooseContainerSerializer(serializers.Serializer):
    
    class Meta:
        model = LooseContainer

class InvoiceSerializer(serializers.Serializer):
    
    class Meta:
        model = Invoice
        

class ProductSerializer(serializers.Serializer):
    
    class Meta:
        model = Product