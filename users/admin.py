from django.contrib import admin
from users.models import (Consignee, ConsigneeAddress,
                          Customer, CustomerAddress,
                          Driver, DriverAddress,
                          Dispatcher, DispatcherAddress,
                          Shipper, shipperAddress)

class CustomerAddressAdmin(admin.StackedInline):
    model = CustomerAddress

class ConsigneeAddressAdmin(admin.StackedInline):
    model = ConsigneeAddress

class DriverAddressAdmin(admin.StackedInline):
    model = DriverAddress

class DispatcherAddressAdmin(admin.StackedInline):
    model = DispatcherAddress

class ShipperAddressAdmin(admin.StackedInline):
    model = shipperAddress


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    '''Admin View for Customer'''
    list_display = ('id', 'username', 'email', 'telephone', 'mc_number')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'telephone', 'mc_number')
  
    inlines = [
        CustomerAddressAdmin,
    ]
   

    class Meta:
        model = Customer


@admin.register(Consignee)
class ConsigneeAdmin(admin.ModelAdmin):
    '''Admin View for Customer'''

    list_display = ('id', 'username', 'email', 'telephone', 'mc_number')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'telephone', 'mc_number')
 
    inlines = [
        ConsigneeAddressAdmin,
    ]
   

    class Meta:
        model = Consignee


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    '''Admin View for Driver'''
    list_display = ('id', 'username', 'email', 'telephone', 'status')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'telephone', 'status')
 
    inlines = [
        DriverAddressAdmin,
    ]
  

    class Meta:
        model = Driver


@admin.register(Dispatcher)
class DispatcherAdmin(admin.ModelAdmin):
    '''Admin View for Dispatcher'''
    list_display = ('id', 'username', 'email', 'telephone', 'rate')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'telephone', 'rate')
 
    inlines = [
        DispatcherAddressAdmin,
    ]
  

    class Meta:
        model = Dispatcher


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    '''Admin View for Shipper'''
    list_display = ('id', 'username', 'email', 'telephone', 'ext')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'telephone', 'ext')
 
    inlines = [
        ShipperAddressAdmin,
    ]
  

    class Meta:
        model = Shipper
