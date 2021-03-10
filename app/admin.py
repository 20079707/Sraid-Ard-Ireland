from django.contrib import admin

from app.models import Product, Address, Shop


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductCode', 'Name', 'Price']
    list_filter = ['LastUpdate']
    search_fields = ['Name']


@admin.register(Shop)
class Shop(admin.ModelAdmin):
    list_display = ['ShopName', 'Slogan', 'Description']
    search_fields = ['ShopName']


@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ['County']
    search_fields = ['County']
