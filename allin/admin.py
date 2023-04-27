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


class LooseCargoAdmin(admin.ModelAdmin):
    list_display = ('mark', 'recieved', 'depature', 'arrived', 'weight', 'cbms', 'ctns', 'status', 'reciever', 'dispater')
    search_fields = ('mark', 'status', 'reciever__name', 'dispater__name')


class FullCargoAdmin(admin.ModelAdmin):
    list_display = ('mark', 'recieved', 'depature', 'arrived', 'weight', 'cbms', 'ctns', 'status')
    search_fields = ('mark', 'status')


# class BaseContainerAdmin(admin.ModelAdmin):
#     list_display = ('depature', 'arrived', 'weight', 'cbms', 'ctns', 'status')
#     search_fields = ('status',)


class LooseContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'depature', 'arrived', 'weight', 'cbms', 'ctns', 'status')
    search_fields = ('name', 'status')


class FullContainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'depature', 'arrived', 'weight', 'cbms', 'ctns', 'status', 'invoice', 'reciever')
    search_fields = ('name', 'status', 'invoice', 'reciever__name')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('cargo',)
    search_fields = ('cargo__name',)


class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'is_reccuring', 'recurrance', 'notes', 'dispature')
    search_fields = ('name', 'dispature__name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cargo_types', 'qty', 'packaging', 'cbm', 'price', 'weight', 'height')
    search_fields = ('name', 'cargo_types')



admin.site.register(LooseCargo, LooseCargoAdmin)
admin.site.register(FullCargo, FullCargoAdmin)
admin.site.register(LooseContainer, LooseContainerAdmin)
admin.site.register(FullContainer, FullContainerAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Product, ProductAdmin)



