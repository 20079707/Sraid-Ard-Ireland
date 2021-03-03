from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Another, Temp, ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('another', Another.as_view()),
    path('temp', views.Temp),
]