from django import forms
# from rest_framework import Forms
from allin.models import LooseCargo, LooseContainer, Invoice, Product
from allin.models import (LooseCargo, LooseContainer, FullCargo, 
                         FullContainer, Invoice, ExpenseCategory, Expense, Product,
                         Delivery, DeliveryVehicle, ProductQuote, ProductQuoteImages,
                         ShippingQuote, ProductShippingQuote)



class DeliveryForm(forms.ModelForm):
    
    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryVehicleForm(forms.ModelForm):
    
    class Meta:
        model = DeliveryVehicle
        fields = '__all__'


class ProductQuoteForm(forms.ModelForm):
    
    class Meta:
        model = ProductQuote
        fields = '__all__'


class ShippingQuoteForm(forms.ModelForm):
    
    class Meta:
        model = ShippingQuote
        fields = '__all__'


class ProductShippingQuoteForm(forms.ModelForm):
    
    class Meta:
        model = ProductShippingQuote
        fields = '__all__'


class LooseCargoForm(forms.ModelForm):
    
    class Meta:
        model = LooseCargo
        fields = ('reciever', 'dispature', 'status',
                  'mark', 'recieved', 'depature', 'arrived',
                  'weight', 'cbms', 'ctns',)

class LooseContainerForm(forms.ModelForm):
    
    class Meta:
        model = LooseContainer
        fields = ('name', 'depature', 'arrived', 'weight',
                  'cbms', 'ctns', 'status',)

class FullCargoForm(forms.ModelForm):
    
    class Meta:
        model = FullCargo
        fields = ( 'dispature', 'mark', 'recieved', 
                  'depature', 'arrived', 'weight', 
                  'cbms', 'ctns', 'status',)

class FullContainerForm(forms.ModelForm):
    
    class Meta:
        model = FullContainer
        fields = ('name', 'depature', 'arrived', 'weight',
                  'cbms', 'ctns', 'status',
                  )

class InvoiceForm(forms.ModelForm):
    
    class Meta:
        model = Invoice
        fields = ('cargo',)

class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = ('name', 'amount', 'is_reccuring',
                  'recurrance', 'notes',)


class FilterForm(forms.Form):
    name = forms.ModelChoiceField(queryset=ExpenseCategory.objects.all(), required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = (
            'name', 'item_number', 'cargo_types', 'qty', 'packaging', 'cbm', 
            'price', 'weight', 'height', 'length', 'width',
            'owner', 'buyer', 'supplier', 'stock', 'has_stock',
            'l_cargo', 'f_cargo',
        )
  


