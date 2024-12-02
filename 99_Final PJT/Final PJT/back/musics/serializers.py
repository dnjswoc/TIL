from rest_framework import serializers
from .models import Genre, Chart


class MusicGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MusicChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = '__all__'