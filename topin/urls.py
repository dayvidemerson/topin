from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext as _

admin.site.site_header = _('Topin')
admin.site.index_title = _('Gerenciamento da Empresa de Transporte Público')
admin.site.site_title = _('Topin')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('apps.core.routers')),
    path('api/', include('apps.route.routers'))
]
