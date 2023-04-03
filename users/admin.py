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

    # list_display = ('',)
    # list_filter = ('',)
    inlines = [
        CustomerAddressAdmin,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

    class Meta:
        model = Customer


@admin.register(Consignee)
class ConsigneeAdmin(admin.ModelAdmin):
    '''Admin View for Customer'''

    # list_display = ('',)
    # list_filter = ('',)
    inlines = [
        ConsigneeAddressAdmin,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

    class Meta:
        model = Consignee


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    '''Admin View for Driver'''

    # list_display = ('',)
    # list_filter = ('',)
    inlines = [
        DriverAddressAdmin,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

    class Meta:
        model = Driver


@admin.register(Dispatcher)
class DispatcherAdmin(admin.ModelAdmin):
    '''Admin View for Dispatcher'''

    # list_display = ('',)
    # list_filter = ('',)
    inlines = [
        DispatcherAddressAdmin,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

    class Meta:
        model = Dispatcher


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    '''Admin View for Shipper'''

    # list_display = ('',)
    # list_filter = ('',)
    inlines = [
        ShipperAddressAdmin,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

    class Meta:
        model = Shipper

