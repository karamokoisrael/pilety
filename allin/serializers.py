from rest_framework import serializers
from allin.models import (LooseCargo, LooseContainer, FullCargo, 
                        FullContainer, Invoice, Expense, ExpenseCategory, Product,)



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