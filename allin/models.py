from django.db import models


from django.db import models
from users.models import Customer, Dispatcher, Supplier
# from shipping.models import LooseCargo, FullCargo
from choices import (CURRENCY_CHOICES, 
                     ORDERS_STATUS_CHOICES, 
                     PRODUCTS_TYPE_CHOICES, 
                     UNIT_PACKAGING_CHOICES)
from decimal import Decimal

class BaseProduct(models.Model):
    CURRENCY_CHOICES = CURRENCY_CHOICES
    TYPE_CHOICES = PRODUCTS_TYPE_CHOICES
    PACKAGING_TYPE_CHOICES = UNIT_PACKAGING_CHOICES

    name = models.CharField(max_length=100, blank=True, null=True
                            )
    item_number = models.CharField(verbose_name= 'Product/Item\'s number', 
                                   max_length=100, blank=True, null=True
                                   )
    description = models.CharField(max_length=200, blank=True, null=True
                                )  
    volume = models.DecimalField(verbose_name='CBM per carton', 
                                 decimal_places=5, max_digits=10, default=0, 
                                 blank=True, null=True
                                 )
    packaging_type = models.CharField(verbose_name=' Unit packaging type',
                                      choices=PACKAGING_TYPE_CHOICES, 
                                      default='PCS', max_length=15, 
                                      blank=True, null=True
                                      )
    packaging = models.IntegerField(verbose_name='No. of items in a carton',
                                    default=0, blank=True, null=True
                                    )
    height = models.DecimalField(verbose_name='Height in centimeters' ,
                                 decimal_places=3, max_digits=10, default=0, 
                                 blank=True, null=True
                                 )
    width = models.DecimalField(verbose_name='Width  in centimeters' ,
                                decimal_places=3, max_digits=10, 
                                default=0, blank=True, null=True
                                )
    length = models.DecimalField(verbose_name='Length  in centimeters' ,
                                 decimal_places=3, max_digits=10, default=0, 
                                 blank=True, null=True
                                 )
    weight = models.DecimalField(verbose_name='Weight per carton in KG' ,
                                 decimal_places=3, max_digits=10, default=0, 
                                 blank=True, null=True
                                 )
    pic = models.ImageField(upload_to='media/product_pic',
                            blank=True, null=True
                            )

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
        
    

class Product(BaseProduct):
    
    supplier = models.ForeignKey(Supplier, related_name='products', 
                                 on_delete=models.CASCADE,
                                 blank=True, null=True
                                 )
    stock = models.IntegerField(default=0, blank=True, null=True
                                )
    price = models.DecimalField(verbose_name='Unit price(price/pcs)',
                                decimal_places=3, max_digits=10, 
                                default=0, blank=True, null=True
                                )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, 
                                default='RMB', blank=True, null=True
                                )
    type = models.CharField(verbose_name='Product or Service' ,
                            max_length=7, choices=TYPE_CHOICES, 
                            default='PRODUCT', blank=True, null=True
                            )
    chinese_det = models.CharField(verbose_name='Chinese details',
                                   max_length=200, blank=True, null=True
                                )
   
   
      
    def get_price_per_ctn(self):
        return self.price * self.packaging
    
    def save(self, *args, **kwargs):
        self.calc_cbm()
        super().save(*args, **kwargs)
    # def save(self, *args, **kwargs):
       
    #    super(Product, self).save(*args, **kwargs) # Call the real save() method
                

class OtherProduct(models.Model):
    CURRENCY_CHOICES = CURRENCY_CHOICES
    TYPE_CHOICES = PRODUCTS_TYPE_CHOICES
    PACKAGING_TYPE_CHOICES = UNIT_PACKAGING_CHOICES

    name = models.CharField(max_length=100, blank=True, null=True
                            )
    item_number = models.CharField(verbose_name= 'Product/Item\'s number', 
                                   max_length=100, blank=True, null=True
                                   )
    supplier = models.ForeignKey(Supplier, related_name='products', 
                                 on_delete=models.CASCADE,
                                 blank=True, null=True
                                 )
    stock = models.IntegerField(default=0, blank=True, null=True
                                )
    price = models.DecimalField(verbose_name='Unit price(price/pcs)',
                                decimal_places=3, max_digits=10, 
                                default=0, blank=True, null=True
                                )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, 
                                default='RMB', blank=True, null=True
                                )
    type = models.CharField(verbose_name='Product or Service' ,
                            max_length=7, choices=TYPE_CHOICES, 
                            default='PRODUCT', blank=True, null=True
                            )
    chinese_det = models.CharField(verbose_name='Chinese details',
                                   max_length=200, blank=True, null=True
                                )
    description = models.CharField(max_length=200, blank=True, null=True
                                )  
    volume = models.DecimalField(verbose_name='CBM per carton', 
                                 decimal_places=5, max_digits=10, default=0, 
                                 blank=True, null=True
                                 )
    packaging_type = models.CharField(verbose_name=' Unit packaging type',
                                      choices=PACKAGING_TYPE_CHOICES, 
                                      default='PCS', max_length=15, 
                                      blank=True, null=True
                                      )
    packaging = models.IntegerField(verbose_name='No. of items in a carton',
                                    default=0, blank=True, null=True
                                    )
    height = models.DecimalField(verbose_name='Height in centimeters' ,
                                 decimal_places=3, max_digits=10, default=0, 
                                 blank=True, null=True
                                 )
    width = models.DecimalField(verbose_name='Width  in centimeters' ,
                                decimal_places=3, max_digits=10, 
                                default=0, blank=True, null=True
                                )
    length = models.DecimalField(verbose_name='Length  in centimeters' ,
                                 decimal_places=3, max_digits=10, default=0, 
                                 blank=True, null=True
                                 )
    weight = models.DecimalField(verbose_name='Weight per carton in KG' ,
                                 decimal_places=3, max_digits=10, default=0, 
                                 blank=True, null=True
                                 )
    pic = models.ImageField(upload_to='media/product_pic',
                            blank=True, null=True
                            )
    # loose_cargo = models.ForeignKey(LooseCargo, related_name='products', 
    #                                 on_delete=models.CASCADE, 
    #                                 blank=True, null=True)
    # full_cargo = models.ForeignKey(FullCargo, related_name='products', 
    #                                on_delete=models.CASCADE, 
    #                                blank=True, null=True)
    def __str__(self):
        return f'{self.name}' 

    def update_stock(self):
        pass


    def get_price_per_ctn(self):
        return self.price * self.packaging
    
    def save(self, *args, **kwargs):
        self.calc_cbm()
        super().save(*args, **kwargs)
    # def save(self, *args, **kwargs):
       
    #    super(Product, self).save(*args, **kwargs) # Call the real save() method
                

