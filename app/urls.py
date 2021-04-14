from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Temp, ProductViewSet, AddressViewSet, ShopViewSet, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('address', AddressViewSet)
router.register('shops', ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #    path('another', Another.as_view()),
    path('temp', views.Temp),
]

