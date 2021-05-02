from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from app.models import Product, Address, Shop, Category
from app.serializers import ProductSerializer, AddressSerializer, ShopSerializer, CategorySerializer
from drf_roles.mixins import RoleViewSetMixin



def Temp(request):
    return render(request, 'FYP_temp.html')


def FYP(request):
    return HttpResponse('First message')


class ProductViewSet(RoleViewSetMixin, ModelViewSet):   # product viewset
    serializer_class = ProductSerializer    # calls product serializer
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def post(self, request, *args, **kwargs):
        product_image = request.data['images']
        name = request.data['name']
        Product.objects.create(name=name, product_image=product_image)

        return HttpResponse({'message': 'Product Created'}, status=200)


class AddressViewSet(viewsets.ModelViewSet):    # address viewset
    serializer_class = AddressSerializer
    queryset = Address.objects.all()    # displays all address objects
    authentication_classes = (TokenAuthentication,) # requires a token to authenticate user


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)   # user has to be authenticate dor only allowed to read data


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
