from django import forms
# from rest_framework import Forms
from allin.models import LooseCargo, LooseContainer, Invoice, Product
from allin.models import (LooseCargo, LooseContainer, FullCargo, 
                        FullContainer, Invoice, Expenses, Product,)


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

class ExpensesForm(forms.ModelForm):
    
    class Meta:
        model = Expenses
        fields = ('name', 'amount', 'is_reccuring',
                  'recurrance', 'notes',)
        
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = (
            'name', 'item_number', 'cargo_types', 'qty', 'packaging', 'cbm', 
            'price', 'weight', 'height', 'length', 'width',
            'owner', 'buyer', 'supplier', 'stock', 'has_stock',
            'l_cargo', 'f_cargo',
        )
  