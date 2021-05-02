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
    path('admin/', admin.site.urls),    # admin page url
    path('app/', include('app.urls')),  # app route redirects to the app application
    path('user/', include('user.urls')),    # user route redirects to the user application
    path('auth/', obtain_auth_token),   # auth route listen authorizes user

]

# allows for photos to be viewed on browser
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

