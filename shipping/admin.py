from django.contrib import admin
from shipping.models import Vehicle, Shipment
from shipping.models import (LooseContainer, FullContainer,
                             LooseCargo, FullCargo,
                             LooseCargoInvoice, FullCargoInvoice)


class LooseProductInline(admin.TabularInline):
    model = LooseCargo.product.through
    extra = 1


class FullProductInline(admin.TabularInline):
    model = FullCargo.product.through
    extra = 1


class FullCargoStack(admin.StackedInline):
    model = FullCargo


class LooseCargoStack(admin.StackedInline):
    model = LooseCargo


# @admin.register(Shipment)
# class ShipmentAdmin(admin.ModelAdmin):
#     '''Admin View for Shipment'''
#     list_display = ('driver', 'consignee', 'customer', 'delivery_date', 'pickup_date', 'total_rates')
#     list_filter = ('delivery_date', 'pickup_date')
#     search_fields = ('driver', 'consignee', 'customer', 'delivery_date', 'pickup_date', 'total_rates')

#     # inlines = [
#     #     ShipperAddressAdmin,
#     # ]


#     class Meta:
#         model = Shipment


# @admin.register(Vehicle)
# class VehicleAdmin(admin.ModelAdmin):
#     '''Admin View for Vehicle'''
#     list_display = ('id', 'driver', 'plate_number', 'make', 'mileage')
#     list_filter = ('mileage', 'weight', 'province')
#     search_fields = ('make', 'driver', 'plate_number', 'owner')

#     # inlines = [
#     #     ShipperAddressAdmin,
#     # ]


#     class Meta:
#         model = Vehicle


@admin.register(LooseContainer)
class LooseContainerAdmin(admin.ModelAdmin):
    list_display = ('container_number', 'status',
                    'dispatcher', 'delivery', 'depature', 'total_cargos', 'cbm','cbms')
    list_filter = ('status', 'dispatcher', 'delivery', 'depature')
    search_fields = ('container_number',)
    linked_models = {'receiver': 'users.Customer',
                     'checked_by': 'users.Dispatcher'}
    inlines = [
        LooseCargoStack,
    ]

    def total_cargos(self, obj):
        return sum(cargo.qty for cargo in obj.cargo.all())
    
    def cbms(self, obj):
        return sum(cargo.cargo_cbm for cargo in obj.cargo.all())

    total_cargos.short_description = 'Total Ctns'
    cbms.short_description = 'CBM'


@admin.register(FullContainer)
class FullContainerAdmin(admin.ModelAdmin):
    list_display = ('container_number', 'status',
                    'dispatcher', 'delivery', 'depature', 'total_cargos', 'cbm','cbms')
    list_filter = ('status', 'dispatcher', 'delivery', 'depature')
    search_fields = ('container_number',)
    linked_models = {'receiver': 'users.Customer',
                     'checked_by': 'users.Dispatcher'}
    inlines = [
        FullCargoStack,
    ]

    def total_cargos(self, obj):
        return sum(cargo.qty for cargo in obj.cargo.all())
    
    def cbms(self, obj):
        return sum(cargo.cargo_cbm for cargo in obj.cargo.all())

    total_cargos.short_description = 'Total Ctns'
    cbms.short_description = 'CBM'


@admin.register(LooseCargo)
class LooseCargoAdmin(admin.ModelAdmin):
    list_display = ('item_mark', 'receiver', 'loose_container', 'checked_by')
    list_filter = ('receiver', 'loose_container', 'checked_by')
    search_fields = ('item_mark',)
    linked_models = {'loose_container': 'LooseContainer',
                     'receiver': 'users.Customer', 'checked_by': 'users.Dispatcher'}
    # inlines = [LooseProductInline]
    filter_horizontal = ('product', )


@admin.register(FullCargo)
class FullCargoAdmin(admin.ModelAdmin):
    list_display = ('item_mark', 'receiver', 'full_container', 'checked_by',)
    list_filter = ('receiver', 'full_container', 'checked_by',)
    search_fields = ('item_mark',)
    linked_models = {'full_container': 'FullContainer',
                     'receiver': 'users.Customer', 'checked_by': 'users.Dispatcher'}
    # inlines = [FullProductInline]
    filter_horizontal = ('product',)

    


@admin.register(LooseCargoInvoice)
class LooseCargoInvoiceAdmin(admin.ModelAdmin):
    list_display = ('date',)
    list_filter = ('date',)
    search_fields = ()
    filter_horizontal = ('cargo',)


# @admin.register(LooseCargoInvoice)
# class LooseCargoInvoiceAdmin(admin.ModelAdmin):
#     list_display = ('date',)
#     list_filter = ('date',)
#     search_fields = ()


@admin.register(FullCargoInvoice)
class FullCargoInvoiceAdmin(admin.ModelAdmin):
    list_display = ('date',)
    list_filter = ('date',)
    search_fields = ()
