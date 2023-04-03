from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, Group

class User(AbstractUser):
    pass

class Customer(User):
    # user = models.OneToOneField('User', related_name='customer_profile', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    

class Shipper(User):
    # user = models.OneToOneField('User', related_name='shipper_profile', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    
class Consignee(User):
    # user = models.OneToOneField('User', related_name='consignee_profile', on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    
class Driver(User):
    # user = models.OneToOneField('User', related_name='driver_profile', on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


class Dispatcher(User):
    phone = models.CharField(max_length=20, blank=True, null=True)
    rate = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=3,)
    

    def __str__(self):
        return self.firstname
   