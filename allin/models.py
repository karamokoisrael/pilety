from django.db import models

from django.db.models import Sum
from users.models import Customer, Dispatcher, Supplier
# from shipping.models import LooseCargo, FullCargo
from choices import (CURRENCY_CHOICES, 
                     ORDERS_STATUS_CHOICES, 
                     PRODUCTS_TYPE_CHOICES, 
                     UNIT_PACKAGING_CHOICES,
                     EXPENSES_RECURRANCE_CHOICES,
                     CARGO_STATUS_CHOICES,
                     CARGO_TYPE_CHOICES,)
from decimal import Decimal


class BaseCargo(models.Model):
    
    mark = models.CharField(max_length = 150, blank=True, null=True)
    recieved = models.DateField(auto_now=False, auto_now_add=False,
                                        blank=True, null=True)
    depature = models.DateField(auto_now=False, auto_now_add=False,
                                        blank=True, null=True)
    arrived = models.DateField(auto_now=False, auto_now_add=False,
                                        blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3,
                                        blank=True, null=True)
    cbms = models.DecimalField(max_digits=10, decimal_places=3,
                                        blank=True, null=True)
    ctns = models.DecimalField(max_digits=10, decimal_places=3,
                                        blank=True, null=True)
       
    class Meta:
        abstract = True
  
    
class LooseCargo(BaseCargo):
    STATUS_CHOICES = CARGO_STATUS_CHOICES 
    
    
    status = models.CharField( max_length=3, choices=STATUS_CHOICES, 
                              default='RW')
    reciever = models.ForeignKey(Customer, 
                                related_name='loose_cargos_dispatched',
                                on_delete=models.CASCADE,
                                blank=True, null=True)    
    dispater = models.ForeignKey(Dispatcher, 
                                related_name='loose_cargos_dispatched',
                                on_delete=models.CASCADE,
                                blank=True, null=True)    
    
    def __str__(self):
        return self.product.name
    
    def save(self, *args, **kwargs):
        # self.total_pcs = self.qty * self.product.packaging
        # self.total_price = self.product.price * self.total_pcs
        # self.total_cbm()
        weight = self.product.aggregate(Sum('weight'))['weight__sum']
        self.weight = weight or 0  
        # cargo_cbm = 
        # total_price = self.product.aggregate(Sum('price'))['price__sum']
        # self.total_price = total_price or 0  

        total_qty = self.product.aggregate(Sum('qty'))['qty__sum']
        self.cbms = total_qty or 0  

        total_ctns = self.product.aggregate(Sum('ctns'))['ctns__sum']
        self.ctns = total_ctns or 0  


        super(LooseCargo, self).save(*args, **kwargs) # Call the real save() method


class FullCargo(BaseCargo):
    STATUS_CHOICES = CARGO_STATUS_CHOICES 
    status = models.CharField( max_length=3, choices=STATUS_CHOICES, 
                              default='RW')
    


class BaseContainer(models.Model):
    STATUS_CHOICES = CARGO_STATUS_CHOICES 
    depature = models.DateField(auto_now=False, auto_now_add=False,
                                blank=True, null=True)
    arrived = models.DateField(auto_now=False, auto_now_add=False,
                                blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3,
                                blank=True, null=True)
    cbms = models.DecimalField(max_digits=10, decimal_places=3,
                                blank=True, null=True)
    ctns = models.DecimalField(max_digits=10, decimal_places=3,
                                blank=True, null=True)
    # status = models.CharField( max_length=3, choices=, default='',
    #                           blank=True, null=True)
    status = models.CharField( max_length=3, choices=STATUS_CHOICES, 
                                default='RW')

class LooseContainer(BaseContainer):
    name = models.CharField(max_length = 150, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class FullContainer(BaseContainer):
    name = models.CharField(max_length = 150, blank=True, null=True)
    invoice = models.FileField(blank=True, null=True)
    reciever = models.ForeignKey(Customer, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'{self.name}'


class Invoice(models.Model):
    cargo = models.ForeignKey(LooseContainer, related_name='invoices', on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.cargo}'

    
class Expenses(models.Model):
    RECURRANCE_CHOICES = EXPENSES_RECURRANCE_CHOICES
    dispature = models.ForeignKey(Dispatcher, related_name='expenses',
                                  on_delete=models.CASCADE, 
                                  blank=True, null=True)
    name = models.CharField(verbose_name='Name of the expense' ,max_length = 150)
    amount = models.DecimalField(max_digits=10, decimal_places=2),
    is_reccuring = models.BooleanField()
    recurrance = models.CharField(max_length=4, choices=RECURRANCE_CHOICES, default='N')
    notes = models.TextField()

    def __str__(self):
        return self.name
    
    

class Product(models.Model):
    TYPE_CHOICES = PRODUCTS_TYPE_CHOICES
    CARGO_TYPE_CHOICES = CARGO_TYPE_CHOICES
    name = models.CharField(max_length = 150)
    # types = models.CharField(max_length = 150, default='', 
    #                          choices=TYPE_CHOICES, blank=True, null=True)
    cargo_types = models.CharField(max_length = 150, default='L', 
                             choices=CARGO_TYPE_CHOICES, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    packaging = models.IntegerField(blank=True, null=True)
    cbm = models.DecimalField(max_digits=10, decimal_places=3,
                              blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=3,
                              blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=3,
                                    blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=3,
                                    blank=True, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=3,
                                    blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=3,
                                    blank=True, null=True)
    owner = models.ForeignKey(Customer, related_name='products', 
                                    on_delete=models.CASCADE,
                                    blank=True, null=True)
    buyer = models.ForeignKey(Customer, related_name='products_bought', 
                                    on_delete=models.CASCADE,
                                    blank=True, null=True)
    Supplier = models.ForeignKey(Supplier, related_name='product', 
                                    on_delete=models.CASCADE,
                                    blank=True, null=True)
    stock = models.IntegerField()
    
    has_stock = models.BooleanField()
    
    
    l_cargo = models.ForeignKey(LooseCargo, related_name='products',
                                on_delete=models.CASCADE,
                                blank=True, null=True)

    f_cargo = models.ForeignKey(FullCargo, related_name='products',
                                on_delete=models.CASCADE,
                                   blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def update_stock(self):
        pass

    def calc_cbm(self):
        if not self.volume:
            if not (self.height and self.width and self.length):
                raise ValueError("Either 'cbm' must be provided or 'height', 'width', and 'length' must all be provided.")
            self.volume = Decimal(self.height * self.width * self.length) / Decimal(1000000)
            return f'{self.volume}'
        else:
            return self.volume
        
    def save(self, *args, **kwargs):
        self.calc_cbm()
        super().save(*args, **kwargs)

 