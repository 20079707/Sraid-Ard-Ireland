from django.contrib import admin

from app.models import Product, Address, Shop, Category, Profile


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_code', 'name', 'category', 'product_image', 'product_description', 'shop']
    list_filter = ['last_update', 'shop', 'category']
    search_fields = ['name', 'shop', 'category']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'slogan', 'description']
    search_fields = ['shop_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_description']
    search_fields = ['name']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['county']
    search_fields = ['county']


admin.site.register(Profile)