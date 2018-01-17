import django_filters

from .models import Marker, Route


class MarkerFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(name='city__slug')

    class Meta:
        model = Marker
        fields = ['city']


class RouteFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(name='city__slug')

    class Meta:
        model = Route
        fields = ['city']
