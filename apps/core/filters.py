import django_filters

from .models import City


class CityFilter(django_filters.FilterSet):
    state = django_filters.CharFilter(name='state__slug')

    class Meta:
        model = City
        fields = ['state']
