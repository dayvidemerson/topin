from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('apps.core.routers')),
    path('api/', include('apps.route.routers'))
]
