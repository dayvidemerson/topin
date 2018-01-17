from rest_framework import serializers

from .models import Marker, Line, Route


class MarkerSerializer(serializers.ModelSerializer):

    city = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Marker
        exclude = ['user', 'created_at', 'updated_at']


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        exclude = ['user', 'created_at', 'updated_at']


class RouteSerializer(serializers.ModelSerializer):

    city = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Route
        exclude = ['user', 'created_at', 'updated_at']
