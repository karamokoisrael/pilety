from django import forms
from .models import (LooseContainer, FullContainer, 
                     LooseCargo, FullCargo, 
                     LooseCargoInvoice, FullCargoInvoice
                     )

class LooseContainerForm(forms.ModelForm):
    class Meta:
        model = LooseContainer
        fields = ['depature',
                  'container_number', 'dispatcher'
                 ]
        
class FullContainerForm(forms.ModelForm):
    class Meta:
        model = FullContainer
        fields = ['delivery', 'depature', 'weight', 'cbm', 'status',
                  'ctns', 'amount', 'container_number', 'dispatcher'
                 ]
        
class LooseCargoForm(forms.ModelForm):
    class Meta:
        model = LooseCargo
        fields = ['item_mark', 'qty', 'total_pcs', 'total_price', 
                  'total_weight', 'receiver', 'loose_container', 
                  'container_number', 'checked_by'
                 ]
        
class FullCargoForm(forms.ModelForm):
    class Meta:
        model = FullCargo
        fields = ['item_mark', 'qty', 'total_pcs', 'total_price', 
                  'total_weight', 'receiver', 'full_container', 
                  'container_number', 'checked_by'
                 ]
        
class LooseCargoInvoiceForm(forms.ModelForm):
    class Meta:
        model = LooseCargoInvoice
        fields = ['cargo']
        
class FullCargoInvoiceForm(forms.ModelForm):
    class Meta:
        model = FullCargoInvoice
        fields = ['cargo']
