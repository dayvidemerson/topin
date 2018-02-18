from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import MarkerSerializer, LineSerializer, RouteSerializer
from .filters import MarkerFilter, LineFilter, RouteFilter
from .models import Marker, Line, Route


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


class RouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = RouteFilter
