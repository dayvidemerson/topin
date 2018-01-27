from rest_framework import serializers

from .models import Marker, PointLine, Line, Route


class MarkerSerializer(serializers.ModelSerializer):

    city = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Marker
        exclude = ['user', 'created_at', 'updated_at']


class PointLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointLine
        exclude = ['line', 'created_at', 'updated_at']


class LineSerializer(serializers.ModelSerializer):

    points = PointLineSerializer(source='pointline_set', many=True, read_only=True)
    markers = MarkerSerializer(many=True)

    class Meta:
        model = Line
        fields = ['id', 'name', 'slug', 'description', 'markers', 'points']


class RouteSerializer(serializers.ModelSerializer):

    city = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Route
        exclude = ['user', 'created_at', 'updated_at']
