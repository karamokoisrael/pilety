from django.contrib import admin
from .models import (
    LooseCargo,
    FullCargo,
    LooseContainer,
    FullContainer,
    Invoice,
    Expense,
    ExpenseCategory,
    Product, 
    DeliveryVehicle,
    Delivery,
    ProductQuote,
    ProductQuoteImages,
    ShippingQuote,
    ProductShippingQuote

)



# class BaseCargoAdmin(admin.ModelAdmin):
#     list_display = ('mark', 'recieved', 'depature', 'arrived', 'weight', 'cbms', 'ctns')
#     search_fields = ('mark',)

class ProductStack(admin.TabularInline):
    model = Product

class FullCargoStack(admin.TabularInline):
    model = FullCargo
    inlines = [ProductStack]

class LooseCargoStack(admin.TabularInline):
    model = LooseCargo
    inlines = [ProductStack]


class LooseCargoAdmin(admin.ModelAdmin):
    list_display = ('mark', 'recieved', 'depature', 'container', 'weight', 'cbms', 'ctns', 'status', 'reciever', 'dispature')
    # search_fields = ('mark', 'status', 'container')
    list_filter = ('container', 'status', 'reciever', 'mark', 'dispature')
    inlines = [
        ProductStack,
    ]

class FullCargoAdmin(admin.ModelAdmin):
    list_display = ('mark', 'recieved', 'depature', 'arrived', 'weight', 'cbms', 'ctns', 'status')
    search_fields = ('mark', 'status')
    inlines = [
        ProductStack,
    ]

# class BaseContainerAdmin(admin.ModelAdmin):
#     list_display = ('depature', 'arrived', 'weight', 'cbms', 'ctns', 'status')
#     search_fields = ('status',)


class LooseContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'depature', 'arrived', 'weight', 'cbms', 'ctns',  'status')
    search_fields = ('name', 'status')
    inlines = [
        LooseCargoStack,
    ]

class FullContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'depature', 'arrived', 'weight', 'cbms', 'ctns', 'status', 'invoice', 'reciever')
    search_fields = ('name', 'status', 'invoice', 'reciever__name')
    inlines = [
        FullCargoStack,
    ]

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('cargo',)
    search_fields = ('cargo__name',)


class ExpenseCategoryAdmin(admin.ModelAdmin):
    pass

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'notes', 'recurrance', 'dispature', 'amount')
    search_fields = ('name', 'dispature__name', 'amount', 'date',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cargo_types', 'qty', 'packaging', 'cbm', 'price', 'weight', 'height')
    search_fields = ('name', 'cargo_types')



admin.site.register(LooseCargo, LooseCargoAdmin)
admin.site.register(FullCargo, FullCargoAdmin)
admin.site.register(LooseContainer, LooseContainerAdmin)
admin.site.register(FullContainer, FullContainerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
# admin.site.register(Product, ProductAdmin)
 
class ProductQuoteImagesInline(admin.TabularInline):
    model = ProductQuoteImages
    extra = 1

class DeliveryInline(admin.TabularInline):
    model = Delivery
    extra = 1

class ProductShippingQuoteInline(admin.TabularInline):
    model = ProductShippingQuote
    extra = 1

@admin.register(DeliveryVehicle)
class DeliveryVehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_model', 'color', 'plate_number', 'status', 'mileage', 'last_checkup']
    search_fields = ['name', 'car_model', 'plate_number']
    list_filter = ['status']

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['driver', 'vehicle', 'date', 'status']
    list_filter = ['status']
    search_fields = ['driver__name', 'vehicle__name']
    inlines = [LooseCargoStack]

@admin.register(ProductQuote)
class ProductQuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'status', 'contact', 'qty']
    search_fields = ['name']
    inlines = [ProductQuoteImagesInline]

@admin.register(ShippingQuote)
class ShippingQuoteAdmin(admin.ModelAdmin):
    list_display = ['mark', 'contact', 'cbms', 'weight']
    inlines = [ProductShippingQuoteInline]

@admin.register(ProductShippingQuote)
class ProductShippingQuoteAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'cbm', 'weight', 'qty']
    search_fields = ['product__name']




