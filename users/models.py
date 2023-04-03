from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    telephone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    pass

class Customer(User):
    # user = models.OneToOneField('User', related_name='customer_profile', on_delete=models.CASCADE)
    mc_number = models.CharField(max_length=100, blank=True, null=True)

class CustomerAddress(models.Model):
    customer = models.ForeignKey('Customer', related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(verbose_name='postal/ZIP code', max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'{self.address} + {self.customer}'    

class Shipper(User):
    # user = models.OneToOneField('User', related_name='shipper_profile', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=100, blank=True, null=True)
    ext = models.CharField(max_length=100, blank=True, null=True)
 
class shipperAddress(models.Model):
    shipper = models.ForeignKey('Shipper', related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(verbose_name='postal/ZIP code', max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'{self.address} + {self.shipper}'    
    
class Consignee(User):
    # user = models.OneToOneField('User', related_name='consignee_profile', on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=50)
    type = models.CharField(max_length=100, blank=True, null=True)
    mc_number = models.CharField(max_length=100, blank=True, null=True)
  
   
class ConsigneeAddress(models.Model):
    consignee = models.ForeignKey('Consignee', related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(verbose_name='postal/ZIP code', max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'{self.address} + {self.consignee}'
       
class Driver(User):
    # user = models.OneToOneField('User', related_name='driver_profile', on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20)
    SSN = models.CharField(max_length=100, blank=True, null=True)
    insurance_liablity_cargo = models.CharField(verbose_name='Insurance(Liability&Cargo)' ,max_length=100, blank=True, null=True)
    insurance_truck_trailer = models.CharField(verbose_name='Insurance(Truck/Trailer)' ,max_length=100, blank=True, null=True)
    IFTA_service = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=100, blank=True, null=True)
    drug_test = models.CharField(max_length=100, blank=True, null=True)
    pay_type = models.CharField(max_length=100, blank=True, null=True)
    per_type = models.CharField(max_length=100, blank=True, null=True)
    empty_mile = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    prepass = models.CharField(max_length=100, blank=True, null=True)
    load_board = models.CharField(max_length=100, blank=True, null=True)
    trailer_rent = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(verbose_name='Date of birth' ,blank=True, null=True)
    license_expiry_date = models.DateField(verbose_name='License expiry date' ,blank=True, null=True)
    medical_date = models.DateField(verbose_name='Last medical date' ,blank=True, null=True)
    medical_expiry_date = models.DateField(verbose_name='medical expiry date' ,blank=True, null=True)
    percentage = models.DecimalField(blank=True, null=True, decimal_places=3, max_digits=5)

class DriverAddress(models.Model):
    driver = models.ForeignKey('Driver', related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(verbose_name='postal/ZIP code', max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'{self.address} +{self.driver}'


class Dispatcher(User): 
    phone = models.CharField(max_length=20, blank=True, null=True)
    rate = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=3,)
    

    def __str__(self):
        return self.firstname
   
class DispatcherAddress(models.Model):
    dispatcher = models.ForeignKey('Dispatcher', related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(verbose_name='postal/ZIP code', max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'{self.address} + {self.dispatcher}'


