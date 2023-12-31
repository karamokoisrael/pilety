import random
from django.db import models
from django.db.models import Sum
from users.models import User
# from shipping.models import LooseCargo, FullCargo
from choices import (CURRENCY_CHOICES, 
                     ORDERS_STATUS_CHOICES, 
                     PRODUCTS_TYPE_CHOICES, 
                     DELIVERY_STATUS,
                     EXPENSES_RECURRANCE_CHOICES,
                     CARGO_STATUS_CHOICES,
                     CARGO_TYPE_CHOICES,
                     QUOTE_STATUS,
                     UNIT_PACKAGING_CHOICES,
                     CATEGORY_CHOICES)
from decimal import Decimal


class DeliveryVehicle(models.Model):
    name = models.CharField(max_length = 150)
    car_model = models.CharField(max_length = 150)
    color = models.CharField(max_length = 150)
    plate_number = models.CharField(max_length = 150)
    status = models.CharField(max_length = 150)
    mileage = models.DecimalField(max_digits=6, decimal_places=3)
    last_checkup = models.DateField(auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name_plural = 'Delivery Vehicles'
        
    def __str__(self):
        return f'{self.name} - {self.plate_number}'

class Delivery(models.Model):
    DELIVERY_STATUS = DELIVERY_STATUS
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    vehicle = models.OneToOneField(DeliveryVehicle, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(auto_now=True, auto_now_add=False)
    status = models.CharField(max_length = 2, choices=DELIVERY_STATUS, default='WH')
    delivery_number = models.CharField(max_length=8, unique=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Deliveries'

    def __str__(self):
        return f'{self.date}\'s Delivery #  {self.delivery_number}'
    
    def generate_delivery_number(self):
        while True:
            delivery_number = str(random.randint(10000000, 99999999))
            if not Delivery.objects.filter(delivery_number=delivery_number).exists():
                return delivery_number
    
    def save(self, *args, **kwargs):
        if not self.delivery_number:
            self.delivery_number = self.generate_delivery_number()


        super(Delivery, self).save(*args, **kwargs) # Call the real save() method
    

class BaseContainer(models.Model):
    STATUS_CHOICES = CARGO_STATUS_CHOICES 
    number = models.CharField(max_length = 150, blank=True, null=True)
    
    depature = models.DateField(verbose_name='Loaded', auto_now=False, auto_now_add=False,
                                blank=True, null=True)
    arrived = models.DateField(auto_now=False, auto_now_add=False,
                                blank=True, null=True)
    weight = models.DecimalField(max_digits=15, decimal_places=7,
                                blank=True, null=True)
    cbms = models.DecimalField(max_digits=10, decimal_places=7,
                                blank=True, null=True)
    ctns = models.IntegerField(blank=True, null=True)
    # status = models.CharField( max_length=3, choices=, default='',
    #                           blank=True, null=True)
    status = models.CharField( max_length=3, choices=STATUS_CHOICES, 
                                default='RW')

class LooseContainer(BaseContainer):
    name = models.CharField(max_length = 150, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    
    
 
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.arrived
        super(LooseContainer, self).save(*args, **kwargs) # Call the real save() method
        weight = self.cargos.aggregate(Sum('weight'))['weight__sum']
        self.weight = weight or 0  
         

        total_cbms = self.cargos.aggregate(Sum('cbms'))['cbms__sum']
        self.cbms = total_cbms or 0  

        total_qty = self.cargos.aggregate(Sum('ctns'))['ctns__sum']
        self.ctns = total_qty or 0  


        super(LooseContainer, self).save(*args, **kwargs) # Call the real save() method


class FullContainer(BaseContainer):
    name = models.CharField(max_length = 150, blank=True, null=True)
    invoice = models.FileField(blank=True, null=True)
    reciever = models.ForeignKey(User, related_name='fullcontainers', 
                                 on_delete=models.SET_NULL, blank=True, null=True)
    


    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.arrived
        super(FullContainer, self).save(*args, **kwargs) # Call the real save() method
        weight = self.cargos.aggregate(Sum('weight'))['weight__sum']
        self.weight = weight or 0  
         

        total_cbms = self.cargos.aggregate(Sum('cbms'))['cbms__sum']
        self.cbms = total_cbms or 0  

        total_qty = self.cargos.aggregate(Sum('ctns'))['ctns__sum']
        self.ctns = total_qty or 0  
        super(FullContainer, self).save(*args, **kwargs) # Call the real save() method


class BaseCargo(models.Model):
    
    mark = models.CharField(max_length = 150, blank=True, null=True)
    recieved = models.DateField(auto_now=False, auto_now_add=False,
                                        blank=True, null=True)
    depature = models.DateField(auto_now=False, auto_now_add=False,
                                        blank=True, null=True)
    arrived = models.DateField(auto_now=False, auto_now_add=False,
                                        blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=5,
                                        blank=True, null=True)
    cbms = models.DecimalField(max_digits=10, decimal_places=7,
                                        blank=True, null=True)
    ctns = models.IntegerField(blank=True, null=True)
       
    class Meta:
        abstract = True


    
class LooseCargo(BaseCargo):
    STATUS_CHOICES = CARGO_STATUS_CHOICES 
    
    
    status = models.CharField( max_length=3, choices=STATUS_CHOICES, 
                              default='RW')
    invoice_number = models.CharField(max_length=8, unique=True, blank=True, null=True)
    cost = models.DecimalField(help_text='This is auto generated',
                                verbose_name='Total Cost',
                                max_digits=10, decimal_places=3,
                                blank=True, null=True)
    reciever = models.ForeignKey(User, 
                                related_name='loose_cargos_recieved',
                                on_delete=models.SET_NULL,
                                blank=True, null=True)    
    dispature = models.ForeignKey(User, 
                                related_name='loose_cargos_dispatched',
                                on_delete=models.SET_NULL,
                                blank=True, null=True)
    container = models.ForeignKey(LooseContainer, 
                                  on_delete=models.SET_NULL,
                                  related_name='cargos',
                                  blank=True, null=True) 
    delivery = models.ForeignKey(Delivery, 
                                  on_delete=models.SET_NULL,
                                  related_name='cargos',
                                  blank=True, null=True) 
                                  
    def __str__(self):
        return f'{self.mark}'

    def generate_invoice_number(self):
        while True:
            invoice_number = str(random.randint(10000000, 99999999))
            if not LooseCargo.objects.filter(invoice_number=invoice_number).exists():
                return invoice_number
    
  
    
    def save(self, *args, **kwargs):
        
        super(LooseCargo, self).save(*args, **kwargs)
        weight = self.products.aggregate(Sum('weight'))['weight__sum']
        self.weight = weight or 0  
         

        total_cbms = self.products.aggregate(Sum('cbms'))['cbms__sum']
        self.cbms = total_cbms or 0  

        total_qty = self.products.aggregate(Sum('qty'))['qty__sum']
        self.ctns = total_qty or 0  

        cost = self.products.aggregate(Sum('cbm_cost'))['cbm_cost__sum']
        self.cost = cost or 0  

        if not self.invoice_number:
            self.invoice_number = self.generate_invoice_number()


        super(LooseCargo, self).save(*args, **kwargs) # Call the real save() method
        super(LooseCargo, self).save(*args, **kwargs) # Call the real save() method


class FullCargo(BaseCargo):
    STATUS_CHOICES = CARGO_STATUS_CHOICES 
    status = models.CharField( max_length=3, choices=STATUS_CHOICES, 
                              default='RW')
    dispature = models.ForeignKey(User, 
                                related_name='full_cargos_dispatched',
                                on_delete=models.SET_NULL,
                                blank=True, null=True)   
    container = models.ForeignKey(FullContainer, 
                                  on_delete=models.SET_NULL,
                                  related_name='cargos',
                                  blank=True, null=True)
    # TODO when saving get the total cbm,weight and cartons and status change when saving

    def __str__(self):
        return f'{self.mark}'
      
    def save(self, *args, **kwargs):
        
        super(FullCargo, self).save(*args, **kwargs)
        weight = self.products.aggregate(Sum('weight'))['weight__sum']
        self.weight = weight or 0  
         

        total_cbms = self.products.aggregate(Sum('cbms'))['cbms__sum']
        self.cbms = total_cbms or 0  

        total_qty = self.products.aggregate(Sum('qty'))['qty__sum']
        self.ctns = total_qty or 0  


        super(FullCargo, self).save(*args, **kwargs) # Call the real save() method


class Invoice(models.Model):
    cargo = models.OneToOneField(LooseCargo, related_name='invoices', on_delete=models.SET_NULL, blank=True, null=True)
    invoice_no = models.CharField(verbose_name='Invoice number ', max_length=150, blank=True, null=True)
    
     # TODO add the file when saving

    def __str__(self):
        return f'{self.cargo}'

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
class Expense(models.Model):
    RECURRANCE_CHOICES = EXPENSES_RECURRANCE_CHOICES
    name = models.ForeignKey(ExpenseCategory, 
                                 on_delete=models.SET_NULL,
                                 verbose_name='Name of the expense',
                                 blank=True, null=True
                                 )

    dispature = models.ForeignKey(User, related_name='expenses',
                                  on_delete=models.SET_NULL, 
                                  blank=True, null=True)
    # name = models.CharField(,max_length = 150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_reccuring = models.BooleanField()
    recurrance = models.CharField(max_length=4, choices=RECURRANCE_CHOICES, default='N')
    notes = models.TextField()
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'{self.amount} ({self.name})'
    
  

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(verbose_name='Price/CBM', max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

# for category in categories:
# ProductCategoryChoices = tuple()

#     category_prices[category.name]=category.price
#     new_choice = ((category.name, category.name),)
#     ProductCategoryChoices += (new_choice)



cost_380=['TOYS',
'SUNGLASSES']

cost_400 = [
    'COSMETICS/PERFUME/TOOTHPASTE',
    'STATIONARY',
    'GYM EQUIPMENTS',
    'ORNAMENTS',
    'DECORATIONS',
    'PHONE ACCESSORIES'
    ]

cost_420 = [
    'Hardware - 1',
    'CLOTHES',
    'FURNITURE'
    ]

cost_450 = [
    'MOTORCYCLE SPAREPARTS',
    'SHOES',
    'CURTAINS',
    'CARPETS/ FLOOR MAT',
    'TV',
    'ELECTRONICS'
    ]

cost_500 = [
    'HARDWARE (wire mash, heavy hardware items)',
    'MABATI',
    'MACHINES',
    'CAR SPAREPARTS',
    'HOSPITAL',
    'Other'
    ]


class Product(models.Model):
    
    # categories = ProductCategory.objects.all()
    # ProductCategoryChoices = tuple((category.name, category.name) for category in categories)
    # category_prices = {category.name: category.price for category in categories}

    # ProductCategoryChoices=ProductCategoryChoices


    TYPE_CHOICES = PRODUCTS_TYPE_CHOICES
    CARGO_TYPE_CHOICES = CARGO_TYPE_CHOICES
    UNIT_PACKAGING_CHOICES = UNIT_PACKAGING_CHOICES
    CATEGORY_CHOICES = CATEGORY_CHOICES
    recieved = models.DateField(verbose_name='(Warehouse)recieved on',
                                blank=True, null=True,auto_now_add=True)
    name = models.CharField(max_length = 150,blank=True, null=True)
    chinese = models.CharField(verbose_name='chinese desc', 
                               max_length = 150, blank=True, null=True)
    qty = models.IntegerField(verbose_name='qty (ctn)',blank=True, null=True)
    packaging = models.IntegerField(verbose_name='units/ctn', 
                                    blank=True, null=True)
    units = models.CharField(max_length = 4, default='PCS', 
                             choices=UNIT_PACKAGING_CHOICES, blank=True, null=True)
    prod_type = models.CharField(verbose_name='Product Category',
                                 max_length = 150, 
                                 default='Other', 
                                 choices=CATEGORY_CHOICES)
    price = models.DecimalField(verbose_name='Unit Price',
                                max_digits=10, decimal_places=3,
                                blank=True, null=True)
    ttprice = models.DecimalField(verbose_name='T.T.Price',
                                max_digits=10, decimal_places=3,
                                blank=True, null=True)
    cbm = models.DecimalField(verbose_name='CBM/ctns',
                              max_digits=10, decimal_places=7,
                              blank=True, null=True)
    cbms = models.DecimalField(verbose_name='Total CBM',
                              max_digits=10, decimal_places=7,
                              blank=True, null=True)
    wght = models.DecimalField(verbose_name='weight/ctn', 
                               max_digits=10, decimal_places=3, null=True)
    weight = models.DecimalField(verbose_name='total weight', 
                                max_digits=10, decimal_places=3,
                                blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=3,
                                    blank=True, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=3,
                                    blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=3,
                                    blank=True, null=True)
    item_number = models.CharField(max_length=50, blank=True, null=True)
    cbm_cost = models.DecimalField(max_digits=15, decimal_places=4,blank=True, null=True )
    cargo_types = models.CharField(max_length = 150, default='L', 
                             choices=CARGO_TYPE_CHOICES, blank=True, null=True)
    stock = models.IntegerField(default=0,blank=True, null=True)
    has_stock = models.BooleanField(default=False)
       
    supplier = models.ForeignKey(User, related_name='product_supplied', 
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True)
    l_cargo = models.ForeignKey(LooseCargo, related_name='products',
                                on_delete=models.SET_NULL,
                                blank=True, null=True)
    f_cargo = models.ForeignKey(FullCargo, related_name='products',
                                on_delete=models.SET_NULL,
                                   blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def update_stock(self):
        if self.stock:
            self.has_stock = True

    def check_required_field(self):
        pass

    def fill_cbm_cost(self):


        if self.prod_type in cost_450:
            self.cbm_cost = Decimal(self.cbms * 450)
        
        elif self.prod_type in cost_400:
            self.cbm_cost = Decimal(self.cbms * 400)

        elif self.prod_type in cost_420:
            self.cbm_cost = Decimal(self.cbms * 420)

        elif self.prod_type in cost_380:
            self.cbm_cost = Decimal(self.cbms * 380)
        
        elif self.prod_type in cost_500:
            self.cbm_cost = Decimal(self.cbms * 500)
        
     
        
    def calculate(self):
        if not self.cbm:
            if not (self.height and self.width and self.length):
                raise ValueError("Either 'cbm' must be provided or 'height', 'width', and 'length' must all be provided.")
            self.cbm = Decimal(self.height * self.width * self.length) / Decimal(1000000)
            self.cbms = Decimal(self.cbm * self.qty)
        else:
            self.cbms = Decimal(self.cbm * self.qty)

        if not self.wght:
            if self.weight:
                self.wght = Decimal(self.weight/self.qty)
            else:
                raise ValueError("Please input the weight of one carton in kilograms")
        else:
            self.weight = Decimal(self.wght * self.qty)

        if self.price:
            self.ttprice = Decimal(self.price * self.qty)
        
        
    def save(self, *args, **kwargs):
        
        # self.cbm_cost = Decimal(self.cbms * category_prices[self.prod_type])
        self.calculate()
        self.fill_cbm_cost()
        # if self.prod_type:
        #     category = ProductCategory.objects.get(name=self.prod_type)
        #     self.cbm_cost = Decimal(self.cbms * category.price)
        super(Product, self).save(*args, **kwargs)
   


class ProductQuote(models.Model):
    QUOTE_STATUS = QUOTE_STATUS
    name = models.CharField(verbose_name= 'product name',max_length = 150)
    status = models.CharField(max_length=2, choices=QUOTE_STATUS, default='S')
    contact = models.CharField(max_length = 150,blank=True, null=True)
    description = models.TextField()
    qty = models.IntegerField()

    

    def __str__(self):
        return f'{self.name}'


class ProductQuoteImages(models.Model):
    product = models.ForeignKey(ProductQuote, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='frontend/src/media/', height_field=None, width_field=None, max_length=100)
    
    

    def __str__(self):
        return f'{self.product.name}'
    

class ShippingQuote(models.Model):
    mark = models.CharField(max_length = 150)
    contact = models.CharField(max_length = 150)
    cbms = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    ctns = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    


    def __str__(self):
        return f'{self.mark}'
    

    def save(self, *args, **kwargs):
       
        super(ShippingQuote, self).save(*args, **kwargs) # Call the real save() method
        weight = self.products.aggregate(Sum('weight'))['weight__sum']
        self.weight = weight or 0  
         

        total_cbms = self.products.aggregate(Sum('cbm'))['cbm__sum']
        self.cbms = total_cbms or 0  

        total_qty = self.products.aggregate(Sum('qty'))['qty__sum']
        self.ctns = total_qty or 0  

        super(ShippingQuote, self).save(*args, **kwargs) # Call the real save() method


class ProductShippingQuote(models.Model):
    '''creates products that are to be added in the shipping Quote model'''
    product = models.ForeignKey(ShippingQuote, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length = 150)
    cbm = models.DecimalField(max_digits=6, decimal_places=3)
    total_cbm = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3)
    total_weight = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    qty = models.IntegerField()

        
    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.total_cbm:
           self.total_cbm = Decimal(self.cbm * self.qty)

        if not self.total_weight:
           self.total_weight = Decimal(self.weight * self.qty)
        
        super(ProductShippingQuote, self).save(*args, **kwargs) # Call the real save() method
    
    
# TODO add quote status
# TODO add ref no for quote product that will be linked with the product model when it is sourced

# TODO add gthe tracking system