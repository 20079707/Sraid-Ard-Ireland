from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app.models import Product, Address, Shop
from app.serializers import ProductSerializer, AddressSerializer, ShopSerializer


def Temp(request):
    return render(request, 'FYP_temp.html')


# class Another(View):
#    products = Product.objects.exclude(Quantity=0)

#    output = ''

#    for product in products:
#        output += f"We have {product.Name} in our DB priced at {product.Price}</br>"

#    def get(self, request):
#        return HttpResponse(self.output)


def FYP(request):
    return HttpResponse('First message')


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    authentication_classes = (TokenAuthentication,)


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
