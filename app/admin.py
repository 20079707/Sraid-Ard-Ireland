from django.contrib import admin

from app.models import Product, Address, Shop, Category

# All tables on admin page


@admin.register(Product)  # admin product view
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_code', 'name', 'category', 'product_image', 'product_description', 'shop']
    list_filter = ['last_update', 'shop', 'category']   # filter box
    search_fields = ['name', 'shop', 'category']


@admin.register(Shop)   # admin shop view
class ShopAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'slogan', 'description']  # fields show in list display
    search_fields = ['shop_name']


@admin.register(Category)   # admin category view
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category_description']
    search_fields = ['name']    # search field


@admin.register(Address)    # admin address view
class AddressAdmin(admin.ModelAdmin):
    list_display = ['county']
    search_fields = ['county']
