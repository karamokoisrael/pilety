from django import forms
from rest_framework import Forms
from allin.models import LooseCargo, LooseContainer, Invoice, Product



class LooseCargoForm(forms.ModelForm):
    
    class Meta:
        model = LooseCargo
        fields = ('product', 'reciever', 'dispature', 
                  'mark', 'recieved', 'depature', 'arrived',
                  'weight', 'cbms', 'ctns',)

class LooseContainerForm(forms.ModelForm):
    
    class Meta:
        model = LooseContainer
        fields = ('name', 'depature', 'arrived', 'eight',
                  'cbms', 'ctns',)

class InvoiceForm(forms.ModelForm):
    
    class Meta:
        model = Invoice
        fields = ('cargo',)
        

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = (
            'name', 'types', 'qty', 'packaging', 'cbm', 
            'price', 'weight', 'height', 'length', 'width',
            'owner', 'buyer', 'supplier', 'stock', 'has_stock',
        )
  