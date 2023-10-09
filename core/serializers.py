# shape_identifier/serializers.py

from rest_framework import serializers


class GridInputSerializer(serializers.Serializer):
    grid = serializers.ListField(child=serializers.ListField(child=serializers.CharField()))
