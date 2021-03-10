from rest_framework import serializers
from .models import Product, Address, Shop


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['ProductCode', 'Name', 'Price', 'LastUpdate']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['AddressLine1', 'AddressLine2', 'TownCity', 'County', 'EirCode']


class ShopSerializer(serializers.ModelSerializer):
    Address = AddressSerializer(many=False)

    class Meta:
        model = Shop
        fields = ['ShopName', 'Slogan', 'Description', 'Address']
