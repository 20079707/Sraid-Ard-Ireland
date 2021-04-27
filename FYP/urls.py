from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings
from user.views import (
    registration_view
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('user/', include('user.urls')),
    path('auth/', obtain_auth_token),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

