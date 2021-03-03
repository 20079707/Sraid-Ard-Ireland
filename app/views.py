from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets

from app.models import Product
from app.serializers import ProductSerializer


def Temp(request):
    return render(request, 'FYP_temp.html')


class Another(View):
    products = Product.objects.exclude(Quantity=0)

    output = ''

    for product in products:
        output += f"We have {product.Name} in our DB priced at {product.Price}</br>"

    def get(self, request):
        return HttpResponse(self.output)


def FYP(request):
    return HttpResponse('First message')


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
