from django.db import models
from users.models import Customer


class Company(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(verbose_name='Company\'s Link', max_length=500, blank=True, null=True)

        

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

class CompanyAddress(models.Model):
    owner = models.ForeignKey('Customer', related_name='companies', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal = models.CharField(verbose_name='postal/ZIP code', max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    

    class Meta:
        verbose_name = "Company address"
        verbose_name_plural = "Company addresses"

