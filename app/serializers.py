from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Product, Address, Shop


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_line1', 'address_line2', 'town_city', 'county', 'eir_code']


class ShopSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)

    class Meta:
        model = Shop
        fields = ['shop_name', 'slogan', 'description', 'address']


class ProductSerializer(serializers.ModelSerializer):
    shop = ShopSerializer(many=False)

    class Meta:
        model = Product
        fields = ['product_code', 'name', 'price', 'cover_image', 'product_description', 'last_update', 'product_image',
                  'shop']
