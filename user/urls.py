from rest_framework import routers
from django.urls import path, include
from user.views import UserViewSet, registration_view

router = routers.DefaultRouter()
router.register('users', UserViewSet)  # users url displays user viewset

urlpatterns = [
    path('', include(router.urls)),  # redirects to router if blank
]
