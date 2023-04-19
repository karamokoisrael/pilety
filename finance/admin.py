
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'stock', 'price')
    search_fields = ('name', 'supplier__name')

admin.site.register(Product, ProductAdmin)
