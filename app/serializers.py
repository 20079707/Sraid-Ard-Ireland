from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Product, Address, Shop, Category


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_line1', 'address_line2', 'town_city', 'county', 'eir_code']


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['shop_name', 'id', 'slogan', 'description', 'business_reg', 'logo', 'shop_image', 'address_line1',
                  'address_line2', 'town_city', 'county', 'eir_code']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_description', 'category_image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_code', 'name', 'price', 'quantity', 'weight', 'product_description', 'last_update',
                  'product_image', 'colour', 'stock', 'category', 'shipping_fee', 'shop']
