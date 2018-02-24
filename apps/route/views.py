from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import MarkerSerializer, LineSerializer, ScheduleSerializer, RouteSerializer
from .filters import MarkerFilter, LineFilter, ScheduleFilter, RouteFilter
from .models import Marker, Line, Schedule, Route


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = MarkerFilter


class LineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = LineFilter


class ScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ScheduleFilter


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = RouteFilter
