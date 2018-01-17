from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import StateSerializer, CitySerializer
from .filters import CityFilter
from .models import State, City


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = CityFilter
