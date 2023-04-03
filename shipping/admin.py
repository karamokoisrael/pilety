from django.contrib import admin
from shipping.models import Vehicle, Shipment


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    '''Admin View for Shipment'''
    list_display = ('driver', 'consignee', 'customer', 'delivery_date', 'pickup_date', 'total_rates')
    list_filter = ('delivery_date', 'pickup_date')
    search_fields = ('driver', 'consignee', 'customer', 'delivery_date', 'pickup_date', 'total_rates')
 
    # inlines = [
    #     ShipperAddressAdmin,
    # ]
  

    class Meta:
        model = Shipment


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    '''Admin View for Vehicle'''
    list_display = ('id', 'driver', 'plate_number', 'make', 'mileage')
    list_filter = ('mileage', 'weight', 'province')
    search_fields = ('make', 'driver', 'plate_number', 'owner')
 
    # inlines = [
    #     ShipperAddressAdmin,
    # ]
  

    class Meta:
        model = Vehicle



