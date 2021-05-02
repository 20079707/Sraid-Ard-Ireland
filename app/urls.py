from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Temp, ProductViewSet, AddressViewSet, ShopViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet)  # products route address
router.register('categories', CategoryViewSet)  # categories route address
router.register('address', AddressViewSet)  # address route address
router.register('shops', ShopViewSet)   # shops route address

urlpatterns = [
    path('', include(router.urls)), # if route is blank, use router routes
    #    path('another', Another.as_view()),

]
