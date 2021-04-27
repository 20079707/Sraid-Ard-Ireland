from rest_framework import routers
from django.urls import path, include
from user.views import UserViewSet, registration_view


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', registration_view, name="register"),
]
