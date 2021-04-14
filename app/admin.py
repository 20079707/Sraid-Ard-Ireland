from django.contrib import admin

from app.models import Product, Address, Shop


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_code', 'name', 'price', 'product_image', 'product_description', 'shop']
    list_filter = ['last_update']
    search_fields = ['name']


@admin.register(Shop)
class Shop(admin.ModelAdmin):
    list_display = ['shop_name', 'slogan', 'description']
    search_fields = ['shop_name']


@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ['county']
    search_fields = ['county']
