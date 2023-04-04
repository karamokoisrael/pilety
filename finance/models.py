from django.db import models
from users.models import Customer
from choices import CURRENCY_CHOICES, ORDERS_STATUS_CHOICES, PRODUCTS_TYPE_CHOICES

class Company(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(verbose_name='Company\'s Link', max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to='media/company_logos', blank=True, null=True)
        

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

class CompanyAddress(models.Model):
    owner = models.ForeignKey(Customer, related_name='companies', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(verbose_name='postal/ZIP code', max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    

    class Meta:
        verbose_name = "Company address"
        verbose_name_plural = "Company addresses"

class Account(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True) 
    description = models.CharField(max_length=300, blank=True, null=True)
    balance = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True, default=0.000)
    account_number = models.IntegerField(blank=True, null=True)
    holder = models.ForeignKey(Customer, related_name='account', on_delete=models.CASCADE)
    bank_url = models.URLField(verbose_name=' Internet banking link', blank=True, null=True)

    def __str__(self):
        return 

class Deposit(models.Model):
    account = models.ForeignKey('Account', related_name='deposits', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='media/documents/deposits', blank=True, null=True)
    ammount = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)


    def __str__(self):
        return f'{self.account} deposited {self.ammount}' 

    def save(self, *args, **kwargs):
       self.account.balance = self.account.balance + self.ammount
       super(Deposit, self).save(*args, **kwargs) # Call the real save() method



class Expenses(models.Model):
    account = models.ForeignKey('Account', related_name='expenses', on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='media/documents/expenses', blank=True, null=True)
    ammount = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)


    def __str__(self):
        return f'{self.account} spent {self.ammount}' 

    def save(self, *args, **kwargs):
       self.account.balance = self.account.balance - self.ammount
       super(Expenses, self).save(*args, **kwargs) # Call the real save() method



class Transfer(models.Model):
    from_ac = models.ForeignKey('Account', related_name='transfer_to', on_delete=models.CASCADE)
    to_ac = models.ForeignKey('Account', related_name='recieved_from', on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    ammount = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)

    def __str__(self):
        return f'Transferred {self.ammount} from {self.from_ac} to {self.to_ac}'
    
    def save(self, *args, **kwargs):
       self.to_ac.balance = self.to_ac.balance + self.ammount
       self.from_ac.balance = self.from_ac.balance - self.ammount
       super(Transfer, self).save(*args, **kwargs) # Call the real save() method

class Product(models.Model):
    CURRENCY_CHOICES = CURRENCY_CHOICES
    TYPE_CHOICES = PRODUCTS_TYPE_CHOICES
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(decimal_places=3, max_digits=10, default=0, blank=True, null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RMB', blank=True, null=True)
    type = models.CharField(verbose_name='Product or Service' ,max_length=7, choices=TYPE_CHOICES, default='PRODUCT', blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return 



class Invoice(models.Model):
    CURRENCY_CHOICES = CURRENCY_CHOICES
    customer = models.ForeignKey(Customer, related_name='invoices', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', verbose_name='Product/Service', related_name='invoices', on_delete=models.CASCADE)
    qty = models.IntegerField(verbose_name='Quantity', default=0, blank=True, null=True)
    price = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)
    total = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)
    has_tax = models.BooleanField(default=True, blank=True, null=True)
    is_recurring = models.BooleanField(default=False, blank=True, null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RMB', blank=True, null=True)
    invoice_no = models.CharField(max_length=10, verbose_name='Invoice number', blank=True, null=True)
    date = models.DateField(verbose_name='Invoice date', blank=True, null=True)
    sales_tax = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)
    

    def __str__(self):
        return f'{self.customer}\'s'


