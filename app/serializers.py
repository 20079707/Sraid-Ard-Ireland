from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Product, Address, Shop, Category


class AddressSerializer(serializers.ModelSerializer):  # address model serializer
    class Meta:
        model = Address # calling address model
        fields = ['address_line1', 'address_line2', 'town_city', 'county', 'eir_code']  # fields sent as json


class ShopSerializer(serializers.ModelSerializer):  # shop model serializer
    class Meta:
        model = Shop
        fields = ['shop_name', 'id', 'slogan', 'description', 'business_reg', 'logo', 'shop_image', 'address_line1',
                  'address_line2', 'town_city', 'county', 'eir_code']


class CategorySerializer(serializers.ModelSerializer):  # category model serializer
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_description', 'category_image']


class ProductSerializer(serializers.ModelSerializer):   # product model serializer
    class Meta:
        model = Product
        fields = ['product_code', 'name', 'price', 'quantity', 'weight', 'product_description', 'last_update',
                  'product_image', 'colour', 'stock', 'category', 'shipping_fee', 'shop']
