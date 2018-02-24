import django_filters

from .models import Marker, Line, Schedule, Route


class MarkerFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(name='city__slug')

    class Meta:
        model = Marker
        fields = ['city']


class LineFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(name='city__slug')

    class Meta:
        model = Line
        fields = ['city']


class ScheduleFilter(django_filters.FilterSet):
    line = django_filters.CharFilter(name='line__slug')
    weekdays = django_filters.CharFilter(name='weekdays__in')

    class Meta:
        model = Schedule
        fields = ['line', 'weekdays']


class RouteFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(name='city__slug')

    class Meta:
        model = Route
        fields = ['city']
