from django.db import models


from django.db import models
from users.models import Customer, Dispatcher, Supplier
# from shipping.models import LooseCargo, FullCargo
from choices import (CURRENCY_CHOICES, 
                     ORDERS_STATUS_CHOICES, 
                     PRODUCTS_TYPE_CHOICES, 
                     UNIT_PACKAGING_CHOICES)
from decimal import Decimal


class Product(models.Model):
    TYPE_CHOICES = PRODUCTS_TYPE_CHOICES
    name = models.CharField(max_length = 150)
    types = models.CharField(max_length = 150, default='', 
                             choices=TYPE_CHOICES, blank=True, null=True)
    qty = models.IntegerField()
    packaging = models.IntegerField()
    cbm = models.DecimalField(max_digits=10, decimal_places=3)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    height = models.DecimalField(max_digits=10, decimal_places=3)
    length = models.DecimalField(max_digits=10, decimal_places=3)
    width = models.DecimalField(max_digits=10, decimal_places=3)
    owner = models.ForeignKey(Customer, related_name='products', on_delete=models.CASCADE)
    buyer = models.ForeignKey(Customer, related_name='products', on_delete=models.CASCADE)
    Supplier = models.ForeignKey(Supplier, related_name='product', on_delete=models.CASCADE)
    stock = models.IntegerField()
    has_stock = models.BooleanField()
    

    def __str__(self):
        return f'{self.name}'





class BaseCargo(models.Model):
    
    mark = models.CharField(max_length = 150, blank=True, null=True)
    recieved = models.DateField(auto_now=False, auto_now_add=False)
    depature = models.DateField(auto_now=False, auto_now_add=False)
    arrived = models.DateField(auto_now=False, auto_now_add=False)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    cbms = models.DecimalField(max_digits=10, decimal_places=3)
    ctns = models.DecimalField(max_digits=10, decimal_places=3)
       
    class Meta:
        abstract = True


    
class LooseCargo(BaseCargo):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                related_name='loose_cargo')
    status = models.CharField( max_length=3, choices=, default='')
    reciever = models.ForeignKey(Customer, related_name='loose_cargos_dispatched', on_delete=models.CASCADE)    
    dispater = models.ForeignKey(Dispatcher, related_name='loose_cargos_dispatched', on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.product.name


class BaseContainer(models.Model):

    depature = models.DateField(auto_now=False, auto_now_add=False)
    arrived = models.DateField(auto_now=False, auto_now_add=False)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    cbms = models.DecimalField(max_digits=10, decimal_places=3)
    ctns = models.DecimalField(max_digits=10, decimal_places=3)
    status = models.CharField( max_length=3, choices=, default='')


class LooseContainer(BaseContainer):
    name = models.CharField(max_length = 150, blank=True, null=True)
    
    

    def __str__(self):
        return f'{self.name}'

class Invoice(models.Model):
    cargo = models.ForeignKey(LooseContainer, related_name='invoices', on_delete=models.CASCADE)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
