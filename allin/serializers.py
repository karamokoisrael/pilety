from rest_framework import serializers
from allin.models import (LooseCargo, LooseContainer, FullCargo, 
                        FullContainer, Invoice, Expenses, Product,)



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
        
class ExpensesSerializer(serializers.Serializer):
    
    class Meta:
        model = Expenses
        

class ProductSerializer(serializers.Serializer):
    
    class Meta:
        model = Product