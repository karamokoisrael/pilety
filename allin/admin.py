from django.contrib import admin
from .models import (
    LooseCargo,
    FullCargo,
    LooseContainer,
    FullContainer,
    Invoice,
    Expenses,
    Product
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
    list_display = ('mark', 'recieved', 'depature', 'arrived', 'weight', 'cbms', 'ctns', 'status', 'reciever', 'dispature')
    search_fields = ('mark', 'status', 'reciever__name', 'dispature__name')
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
    list_display = ('name', 'depature', 'arrived', 'weight', 'cbms', 'ctns', 'status')
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


class ExpensesAdmin(admin.ModelAdmin):
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
admin.site.register(Expenses, ExpensesAdmin)
# admin.site.register(Product, ProductAdmin)



