from django.db import models
from users.models import User
# from shipping.models import LooseCargo, FullCargo
from choices import (CURRENCY_CHOICES, 
                     ORDERS_STATUS_CHOICES, 
                     PRODUCTS_TYPE_CHOICES, 
                     UNIT_PACKAGING_CHOICES)
from decimal import Decimal
 
class Company(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True
                            )
    url = models.URLField(verbose_name='Company\'s Link', 
                          max_length=500, 
                          blank=True, null=True
                          )
    logo = models.ImageField(upload_to='media/company_logos', 
                             blank=True, null=True
                             )
        

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class CompanyAddress(models.Model):
    owner = models.ForeignKey(User, related_name='companies', 
                              on_delete=models.CASCADE
                              )
    company = models.ForeignKey(Company, related_name='address', 
                                on_delete=models.CASCADE
                                )
    address = models.CharField(max_length=100, blank=True, null=True
                                )
    city = models.CharField(max_length=100, blank=True, null=True
                            )
    postal = models.CharField(verbose_name='postal/ZIP code', 
                              max_length=100, blank=True, null=True
                              )
    state = models.CharField(max_length=100, blank=True, null=True
                            )
    country = models.CharField(max_length=100, blank=True, null=True
                             )
    phone = models.CharField(max_length=20, blank=True, null=True
                            )
    

    class Meta:
        verbose_name = "Company address"
        verbose_name_plural = "Company addresses"


class Account(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True
                            ) 
    description = models.CharField(max_length=300, blank=True, null=True
                                    )
    balance = models.DecimalField(decimal_places=3, max_digits=10, 
                                  blank=True, null=True, default=0.000)
    account_number = models.IntegerField(blank=True, null=True
                                        )
    holder = models.ForeignKey(User, related_name='account', 
                               on_delete=models.CASCADE
                               )
    bank_url = models.URLField(verbose_name=' Internet banking link', 
                               blank=True, null=True
                               )

    def __str__(self):
        return 

