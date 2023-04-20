from django.db import models
from users.models import (Consignee, Customer, Shipper, 
                          Driver, Supplier, Dispatcher
                          )
from finance.models import Product
from choices import LOAD_TYPE_CHOICES, CONTAINER_STATUS_CHOICES


class Shipment(models.Model):
    LOAD_TYPE_CHOICES = LOAD_TYPE_CHOICES
    customer = models.ForeignKey(Customer, related_name='shipments', 
                                 on_delete=models.CASCADE
                                 )
    driver = models.ForeignKey(Driver, related_name='shipments', 
                               on_delete=models.CASCADE
                               )
    shipper = models.ForeignKey(Shipper, related_name='shipments', 
                                on_delete=models.CASCADE
                                )
    consignee = models.ForeignKey(Consignee, related_name='shipments', 
                                  on_delete=models.CASCADE
                                  )
    load_number = models.CharField(max_length=10, blank=True, null=True
                                   )
    load_name = models.CharField(max_length=100,blank=True, null=True
                                 )
    load_type = models.CharField(max_length=3,choices=LOAD_TYPE_CHOICES, 
                                 default='LTL', blank=True, null=True
                                 )
    pickup_date = models.DateField(verbose_name='Pick up date', 
                                   blank=True, null=True
                                   )
    delivery_date = models.DateField(verbose_name='Delivery date', 
                                     blank=True, null=True
                                     )
    # dispatch = models.ForeignKey('TargetModel', related_name='shipment', on_delete=models.CASCADE)
    line_haul_rate = models.DecimalField(blank=True, null=True, max_digits=4, 
                                        max_length=6, decimal_places=3
                                        )
    unloading_fee = models.DecimalField(blank=True, null=True, max_digits=4, 
                                        max_length=6, decimal_places=3
                                        )
    detention_fee = models.DecimalField(blank=True, null=True, max_digits=4, 
                                        max_length=6, decimal_places=3
                                        )
    layovers_fee = models.DecimalField(blank=True, null=True, max_digits=4, 
                                        max_length=6, decimal_places=3
                                        )
    other_charges = models.DecimalField(blank=True, null=True, max_digits=4, 
                                        max_length=6, decimal_places=3
                                        )
    total_rates = models.DecimalField(blank=True, null=True, max_digits=4, 
                                        max_length=6, decimal_places=3
                                        )
    empty_M = models.CharField(max_length=100,blank=True, null=True
                                )
    loaded_M = models.CharField(max_length=100,blank=True, null=True
                                )
    per_mile = models.CharField(max_length=100,blank=True, null=True
                                )


    def __str__(self):
        return f'{self.customer} + {self.load_name}'


class Vehicle(models.Model):
    driver = models.ForeignKey(Driver, related_name='vehicle', on_delete=models.CASCADE)
    owner = models.CharField(max_length=100, blank=True, null=True)
    unit_number = models.CharField(max_length=100, blank=True, null=True)
    make = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    vin = models.CharField(max_length=100, blank=True, null=True)
    plate_number = models.CharField(max_length=100, blank=True, null=True)
    plate_expiry_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    deactivation_date = models.DateField(blank=True, null=True)
    DOT_inspection_date = models.DateField(blank=True, null=True)
    quaterly_inspection_date = models.DateField(verbose_name='90 days inspection date', blank=True, null=True)
    annual_inspection_date = models.DateField(blank=True, null=True)
    truck = models.CharField(max_length=100, blank=True, null=True)
    trailer = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    axels = models.CharField(max_length=100, blank=True, null=True)
    fuel_type = models.CharField(max_length=100, blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    IFTA_truck = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.driver

    def __unicode__(self):
        return self.driver


class LooseContainer(models.Model):
    STATUS_CHOICES = CONTAINER_STATUS_CHOICES

    # invoice = models.ForeignKey(CargoInvoice, 
    #                             related_name='loose_cargo_invoices', 
    #                             on_delete=models.CASCADE
    #                             )
    name = models.CharField(verbose_name='Holder Name', max_length=200,
                            blank=True, null=True
                            )
    delivery = models.DateField(verbose_name='Delivery date',
                                blank=True, null=True
                                )
    depature = models.DateField(verbose_name='Depature date',
                                blank=True, null=True
                                )
    weight = models.DecimalField(verbose_name='Overall weight',
                                 max_digits=15, decimal_places=3,
                                 blank=True, null=True
                                 )
    cbm = models.DecimalField(verbose_name='Overall CBM',
                                 max_digits=15, decimal_places=3,
                                 blank=True, null=True
                                 )
    status = models.CharField(max_length=5,choices=STATUS_CHOICES, 
                              default='NF', blank=True, null=True
                              )
    ctns = models.DecimalField(verbose_name='Number of cartons',
                                 max_digits=15, decimal_places=3,
                                 blank=True, null=True
                                 )
    amount = models.DecimalField(verbose_name='Overall amount',
                                 max_digits=15, decimal_places=3,
                                 blank=True, null=True
                                 )
    container_number = models.CharField(max_length=30,
                                        blank=True, null=True
                                        )
    dispatcher = models.ForeignKey(Dispatcher, 
                                   related_name='loose_container_dispatched',
                                   on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
       
       super(LooseContainer, self).save(*args, **kwargs) # Call the real save() method
    
    
class FullContainer(models.Model):
    STATUS_CHOICES = CONTAINER_STATUS_CHOICES
    name = models.CharField(verbose_name='Holder Name', max_length=200,
                            blank=True, null=True
                            )
    delivery = models.DateField(verbose_name='Delivery date',
                                blank=True, null=True
                                )
    depature = models.DateField(verbose_name='Depature date',
                                blank=True, null=True
                                )
    weight = models.DecimalField(verbose_name='Overall weight',
                                 max_digits=15, decimal_places=3,
                                 blank=True, null=True
                                 )
    cbm = models.DecimalField(verbose_name='Overall CBM',
                                 max_digits=15, decimal_places=3,
                                 blank=True, null=True
                                 )
    status = models.CharField(max_length=5,choices=STATUS_CHOICES, 
                              default='NF', blank=True, null=True
                              )
    ctns = models.DecimalField(verbose_name='Number of cartons',
                                 max_digits=15, decimal_places=3,
                                 blank=True, null=True
                                 )
    amount = models.DecimalField(verbose_name='Overall amount',
                                 max_digits=15, decimal_places=3,
                                 blank=True, null=True
                                 )
    container_number = models.CharField(max_length=30,
                                        blank=True, null=True
                                        )
    dispatcher = models.ForeignKey(Dispatcher, 
                                   related_name='full_container_dispatched',
                                   on_delete=models.CASCADE
                                   )
    # invoice = models.ForeignKey(CargoInvoice, 
    #                             related_name='cargo_invoices', 
    #                             on_delete=models.CASCADE
    #                             )   
    def __str__(self):
        return f'{self.name}'
    

class BaseCargo(models.Model):
    item_mark = models.CharField(max_length=100,blank=True, null=True
                                 )
    qty = models.IntegerField(verbose_name='Quantity in cartons',
                              blank=True, null=True
                              )
    total_pcs = models.IntegerField(verbose_name='Total Pieces',
                              blank=True, null=True
                              )
    total_price = models.DecimalField(max_digits=10, decimal_places=4,
                                      blank=True, null=True
                                      )
    total_weight = models.DecimalField(verbose_name='weight in KG',
                                       max_digits=10, decimal_places=4,
                                       blank=True, null=True
                                      )
    cargo_cbm = models.DecimalField(verbose_name='Cargo CBM', 
                                 decimal_places=5, max_digits=10, default=0, 
                                 blank=True, null=True
                                 )
    
    class Meta:
        abstract = True


class LooseCargo(BaseCargo):
    product = models.ManyToManyField(Product,
                                     verbose_name='cargo/product',
                                     related_name='loose_cargos',
                                     blank=True
                                    )
    receiver = models.ForeignKey(Customer, related_name='loose_cargos', 
                                 on_delete=models.CASCADE,
                                 blank=True, null=True
                                 )
    loose_container = models.ForeignKey(LooseContainer, 
                                        related_name='cargo', 
                                        on_delete=models.CASCADE,
                                        blank=True, null=True
                                        )
    container_number = models.CharField(max_length=30, 
                                        blank=True, null=True
                                        )
    checked_by = models.ForeignKey(Dispatcher, 
                                    related_name='loose_cargo_checked',
                                    on_delete=models.CASCADE,
                                    blank=True, null=True
                                    )
    def __str__(self):
        return f'{self.item_mark}'
    
    def total_cbm(self):
        self.cargo_cbm = self.product.volume * self.qty
        self.loose_container.cbm = self.loose_container.cbm + self.cargo_cbm
    
    def get_weight(self):
        self.weight = self.product.weight * self.qty

    def save(self, *args, **kwargs):
       self.total_pcs = self.qty * self.product.packaging
       self.total_price = self.product.price * self.total_pcs
       self.total_cbm()
       super(LooseCargo, self).save(*args, **kwargs) # Call the real save() method


class FullCargo(BaseCargo):
    product = models.ManyToManyField(Product,
                                     verbose_name='cargo/product',
                                     related_name='full_cargos',
                                     blank=True
                                    )
    receiver = models.ForeignKey(Customer, related_name='full_cargos', 
                                 on_delete=models.CASCADE,
                                 blank=True, null=True
                                 )
    full_container = models.ForeignKey(FullContainer, 
                                        related_name='cargo', 
                                        on_delete=models.CASCADE,
                                        blank=True, null=True
                                        )
    container_number = models.CharField(max_length=30, 
                                        blank=True, null=True
                                        )
    checked_by = models.ForeignKey(Dispatcher, 
                                    related_name='full_cargo_checked',
                                    on_delete=models.CASCADE,
                                    blank=True, null=True
                                    )
    
    def __str__(self):
        return f'{self.item_mark}'
    


class LooseCargoInvoice(models.Model):
    cargo = models.ManyToManyField(LooseContainer, related_name='invoices', 
                                   blank=True
                                   )
    date = models.DateField(auto_now_add=True,
                            blank=True, null=True
                            )

                           
class FullCargoInvoice(models.Model):
    cargo = models.ManyToManyField(FullContainer,related_name='invoice', 
                                   blank=True
                                   )
    date = models.DateField(auto_now_add=True,
                            blank=True, null=True
                            )
                            


