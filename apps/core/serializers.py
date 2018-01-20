from rest_framework import serializers

from .models import State, City


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        exclude = ['id', 'created_at', 'updated_at']


class CitySerializer(serializers.ModelSerializer):

    state = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = City
        exclude = ['id', 'created_at', 'updated_at']
