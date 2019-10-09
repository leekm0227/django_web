from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('farm/', include('farm.urls')),
    path('', include('web.urls')),
]
