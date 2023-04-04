from django.db import models
from users.models import Consignee, Customer, Shipper, Driver
from choices import LOAD_TYPE_CHOICES


class Shipment(models.Model):
    LOAD_TYPE_CHOICES = LOAD_TYPE_CHOICES
    customer = models.ForeignKey(Customer, related_name='shipments', on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, related_name='shipments', on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, related_name='shipments', on_delete=models.CASCADE)
    consignee = models.ForeignKey(Consignee, related_name='shipments', on_delete=models.CASCADE)
    load_number = models.CharField(max_length=10, blank=True, null=True)
    load_name = models.CharField(max_length=100,blank=True, null=True)
    load_type = models.CharField(max_length=3,choices=LOAD_TYPE_CHOICES, default='LTL', blank=True, null=True)
    pickup_date = models.DateField(verbose_name='Pick up date', blank=True, null=True)
    delivery_date = models.DateField(verbose_name='Delivery date', blank=True, null=True)
    # dispatch = models.ForeignKey('TargetModel', related_name='shipment', on_delete=models.CASCADE)
    line_haul_rate = models.DecimalField(blank=True, null=True, max_digits=4, max_length=6, decimal_places=3)
    unloading_fee = models.DecimalField(blank=True, null=True, max_digits=4, max_length=6, decimal_places=3)
    detention_fee = models.DecimalField(blank=True, null=True, max_digits=4, max_length=6, decimal_places=3)
    layovers_fee = models.DecimalField(blank=True, null=True, max_digits=4, max_length=6, decimal_places=3)
    other_charges = models.DecimalField(blank=True, null=True, max_digits=4, max_length=6, decimal_places=3)
    total_rates = models.DecimalField(blank=True, null=True, max_digits=4, max_length=6, decimal_places=3)
    empty_M = models.CharField(max_length=100,blank=True, null=True)
    loaded_M = models.CharField(max_length=100,blank=True, null=True)
    per_mile = models.CharField(max_length=100,blank=True, null=True)


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

